from pyplasm import *
from scipy import *
import os,sys
""" import modules from larcc/lib """
sys.path.insert(0, 'C:/Users/Damian/lar-cc/lib/py/')
from lar2psm import *
from simplexn import *
from larcc import *
from largrid import *
from mapper import *
from boolean import *

def boundaryOfChain(cells,facets):
   csrBoundaryMat = boundary(cells,facets)
   csrChain = zeros((len(cells),1))
   def boundaryOfChain0(chain):
      for cell in chain:  csrChain[cell,0]=1.0
      csrBoundaryChain = matrixProduct(csrBoundaryMat, csrChain)
      boundaryCells = [k for k,val in enumerate(csrBoundaryChain.tolist()) 
                     if val == [1.0]]
      return boundaryCells
   return boundaryOfChain0

""" Diagram initialization """
def assemblyDiagramInit (shape):
   def assemblyDiagram (quoteList):
      print "\n shape =",shape
      # shape and quoteList must be 3D, i.e. a python array with 3 indices
      assert (len(shape) == 3) and (len(quoteList) == 3)
      coordList = [list(cumsum([0]+pattern)) for pattern in quoteList]
      verts = CART(coordList)
      _,CV = larCuboids(shape)
      return verts,CV
   return assemblyDiagram

def lar2boundaryFaces(CV,FV):
   """ Boundary cells computation """
   return boundaryCells(CV,FV)

def lar2InteriorFaces(CV,FV):
   """ Boundary cells computation """
   boundarychain2D = boundaryCells(CV,FV)
   totalChain2D = range(len(FV))
   interiorCells = set(totalChain2D).difference(boundarychain2D)
   return interiorCells

""" Diagram scaling to given size """
def unitDiagram(diagram, size=[1,1,1]):
   V,CV = diagram
   print "\n shape =",shape
   # size must be a python array with 3 numbers
   assert (len(size) == 3) and (AND(AA(ISNUM)(size)) == True)
   V_ = array(V) / AA(float)(max(V))
   V = (V_ * size).tolist()
   diagram = V,CV
   return diagram

from myfont import *
""" Drawing numbers of cells """
def cellNumbering (larModel,hpcModel):
   V,CV = larModel
   def cellNumbering0 (cellSubset,color=WHITE,scalingFactor=1):
      text = TEXTWITHATTRIBUTES (TEXTALIGNMENT='centre', TEXTANGLE=0, 
                     TEXTWIDTH=0.1*scalingFactor, 
                     TEXTHEIGHT=0.2*scalingFactor, 
                     TEXTSPACING=0.025*scalingFactor)
      hpcList = [hpcModel]
      for cell in cellSubset:
         point = CCOMB([V[v] for v in CV[cell]])
         hpcList.append(T([1,2,3])(point)(COLOR(color)(text(str(cell)))))
      return STRUCT(hpcList)
   return cellNumbering0


""" 3D window to viewport transformation """
def diagram2cellMatrix(diagram):
   def diagramToCellMatrix0(master,cell):
      wdw = min(diagram[0]) + max(diagram[0])         # window3D
      cV = [master[0][v] for v in master[1][cell]]
      vpt = min(cV) + max(cV)                      # viewport3D
      print "\n window3D =",wdw
      print "\n viewport3D =",vpt
      
      mat = zeros((4,4))
      mat[0,0] = (vpt[3]-vpt[0])/(wdw[3]-wdw[0])
      mat[0,3] = vpt[0] - mat[0,0]*wdw[0]
      mat[1,1] = (vpt[4]-vpt[1])/(wdw[4]-wdw[1])
      mat[1,3] = vpt[1] - mat[1,1]*wdw[1]
      mat[2,2] = (vpt[5]-vpt[2])/(wdw[5]-wdw[2])
      mat[2,3] = vpt[2] - mat[2,2]*wdw[2]
      mat[3,3] = 1
      print "\n mat =",mat
      return mat
   return diagramToCellMatrix0


##############################################################################################
# Before professor's lecture, I did the exercise in this way, by defining a new function to 
# remove duplicated vertices ...

def removeDuplicates(V,CV):
   import itertools
   import copy
   
   Vcopy = copy.copy(V)
   V.sort()
   V = list(k for k,_ in itertools.groupby(V))

   map = {}

   i = 0

   for v in V:
      map[str(v)] = i,
      i += 1

   j = 0
   k = 0

   CVcopy = copy.copy(CV)

   for c in CV:
      k = 0
      for v in c:
         CVcopy[j][k] = map[str(Vcopy[v])][0]
         k += 1
      j += 1

   return V,CVcopy

def diagram2cell(diagram,master,cell):
   mat = diagram2cellMatrix(diagram)(master,cell)
   diagram =larApply(mat)(diagram)  
   
   """
   # yet to finish coding
   V, CV1, CV2, n12 = vertexSieve(master,diagram)
   masterBoundaryFaces = boundaryOfChain(CV,FV)([cell])
   diagramBoundaryFaces = lar2boundaryFaces(CV,FV)
   """
   V = master[0] + diagram[0]
   
   offset = len(master[0])
   CV = [c for k,c in enumerate(master[1]) if k != cell] + [
         [v+offset for v in c] for c in diagram[1]]
   
   #This function removes duplicated vertices
   master = removeDuplicates(V, CV)

   return master


##############################################################################################
# After professor's lecture, I did the exercise also using the code shown in classroom

# addition of incident vertices into the adjacents of theCell
def checkInclusion(V,theCell,newRange):
   theVerts = [V[v] for v in theCell]
   theMin, theMax = min(theVerts), max(theVerts)
   
   theCell += [v for v in newRange if (
      theMin[0] <= V[v][0] and theMin[1] <= V[v][1] and theMin[2] <= V[v][2] 
      and 
      V[v][0] <= theMax[0] and V[v][1] <= theMax[1] and V[v][2] <= theMax[2] 
      )]
   
   return theCell

def diagram2cell(diagram,master,cell):
   mat = diagram2cellMatrix(diagram)(master,cell)
   diagram =larApply(mat)(diagram)  
   (V1,CV1),(V2,CV2) = master,diagram
   n1,n2 = len(V1), len(V2)
   
   # identification of common vertices
   V, CV1, CV2, n12 = vertexSieve(master,diagram)
   commonRange = range(n1-n12, n1)
   newRange = range(n1,n1-n12+n2)
   
   # addition of new vertices into the adjacents of cell c
   CV1 = [checkInclusion(V,c,newRange) 
         if set(c).intersection(commonRange) != set() else c
          for c in CV1]
   
   CV = [c for k,c in enumerate(CV1) if k != cell] + CV2
   
   master = V, CV
   return master


########################################## Test ##########################################

master = assemblyDiagramInit([5,5,2])([[.3,3.2,.1,5,.3],[.3,4,.1,2.9,.3],[.3,2.7]])
V,CV = master
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(CV)),CYAN,2)
VIEW(hpc)

toMerge = 39

diagram = assemblyDiagramInit([3,1,2])([[2,1,2],[.3],[2.2,.5]])
master = diagram2cell(diagram,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
VIEW(hpc)