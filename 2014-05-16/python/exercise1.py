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

from sysml import *

DRAW = COMP([VIEW,STRUCT,MKPOLS])

master = assemblyDiagramInit([7,13,3])([[.3,4,.3,1.5,.3,5,.3],[.3,3,.3,1.5,.3,.5,.3,3,.3,2,.3,1,.3],[.3,2.7,.3]])
V,CV = master
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(CV)),CYAN,2)
#VIEW(hpc)

toRemove = [82,83,202,203,88,89,58,59,226,227,70,71,208,209,44,50,56,62,68,74,122,200,206,212,218,224,230,152,146,140,134,128,229,223,217,211,205,199,143,151,145,142,139,136,134,133,137,131,130,127,49,61,67,73,55,43,121]
master = V,[cell for k,cell in enumerate(CV) if not (k in toRemove)]
DRAW(master)

hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)

#Bedroom window
toMerge = 206
diagram = assemblyDiagramInit([1,4,3])([[.3],[.5,0.7,.1,.7],[.1,2.5,.1]])
master = diagram2cell(diagram,master,toMerge)

hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)

#Living room windows
toMerge = 182
master = diagram2cell(diagram,master,toMerge)

hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)

#Kitchen window
toMerge = 40
diagram = assemblyDiagramInit([4,1,3])([[2.5,0.7,.1,.7],[.3],[.1,2.5,.1]])
master = diagram2cell(diagram,master,toMerge)

hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)

#Bedroom window
toMerge = 198
diagram = assemblyDiagramInit([1,5,3])([[.3],[.5,0.7,.1,0.7,2.7],[1.1,1.5,.1]])
master = diagram2cell(diagram,master,toMerge)

hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)

#Bedroom window
toMerge = 59
diagram = assemblyDiagramInit([5,1,3])([[0.2,0.7,0.1,0.7,2.3],[.3],[.1,2.5,.1]])
master = diagram2cell(diagram,master,toMerge)

hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)

#Bedroom door
toMerge = 144
diagram = assemblyDiagramInit([1,3,3])([[.3],[.1,0.7,.4],[0,2.5,.1]])
master = diagram2cell(diagram,master,toMerge)

hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)

#Bedroom door
toMerge = 138
diagram = assemblyDiagramInit([1,3,3])([[.3],[.1,0.5,.6],[0,2.5,.1]])
master = diagram2cell(diagram,master,toMerge)

hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)

#Living room door
toMerge = 126
diagram = assemblyDiagramInit([1,3,3])([[.3],[.1,0.1,0.8],[0,2.5,.1]])
master = diagram2cell(diagram,master,toMerge)

hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)

#Bedroom door
toMerge = 84
diagram = assemblyDiagramInit([1,3,3])([[.3],[.1,0.3,.1],[0,2.5,.1]])
master = diagram2cell(diagram,master,toMerge)

hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)

#Bathroom door
toMerge = 78
diagram = assemblyDiagramInit([1,3,3])([[.3],[.1,0.5,.6],[0,2.5,.1]])
master = diagram2cell(diagram,master,toMerge)

hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)

#Kitchen door
toMerge = 43
diagram = assemblyDiagramInit([3,1,3])([[.5,0.3,.8],[.3],[0,2.5,.1]])
master = diagram2cell(diagram,master,toMerge)

hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)

#Door
toMerge = 10
diagram = assemblyDiagramInit([1,3,3])([[.3],[.1,0.8,.3],[0,2.5,.1]])
master = diagram2cell(diagram,master,toMerge)

hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)

#Toilet door
toMerge = 106
diagram = assemblyDiagramInit([4,1,3])([[.1,.1,1,.1],[.3],[0,2.5,.1]])
master = diagram2cell(diagram,master,toMerge)

hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,1)
VIEW(hpc)

toRemove = [220,226,244,250,208,214,265,259,328,232,238,274,283,295,322,310,301,340]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
DRAW(master)