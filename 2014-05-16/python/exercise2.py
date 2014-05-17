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

################################################ Exercise 1 code ################################################

DRAW = COMP([VIEW,STRUCT,MKPOLS])

master = assemblyDiagramInit([7,13,3])([[.3,4,.3,1.5,.3,5,.3],[.3,3,.3,1.5,.3,.5,.3,3,.3,2,.3,1,.3],[.3,2.7,.3]])
V,CV = master
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(CV)),CYAN,2)
#VIEW(hpc)

toRemove = [82,83,202,203,88,89,58,59,226,227,70,71,208,209,44,50,56,62,68,74,122,200,206,212,218,224,230,152,146,140,134,128,229,223,217,211,205,199,143,151,145,142,139,136,134,133,137,131,130,127,49,61,67,73,55,43,121]
master = V,[cell for k,cell in enumerate(CV) if not (k in toRemove)]
#DRAW(master)

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
#VIEW(hpc)

toRemove = [220,226,244,250,208,214,265,259,328,232,238,274,283,295,322,310,301,340]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
#DRAW(master)

################################################ Exercise 1 code end ################################################

apartment = STRUCT(MKPOLS(master))

#Landing (pianerottolo)
landingVerts = [[0,0],[3,0],[3,13.1],[0,13.1]]
landingCells = [[1,2,3,4]]
pols = None
landing = MKPOL([landingVerts, landingCells, pols])
landing = PROD([landing,Q(0.3)])
landing = T(1)(-3)(landing)

#Ceiling
ceilingVerts = [[0,0],[26.6,0],[26.6,13.1],[0,13.1]]
ceilingCells = [[1,2,3,4]]
ceiling = MKPOL([ceilingVerts, ceilingCells, pols])
ceiling = PROD([ceiling,Q(0.3)])
ceiling = T(1)(-14.8)(ceiling)

apartmentsPart = STRUCT([apartment, T(3)(3.3)(apartment)])
apartments = STRUCT([apartmentsPart, T(3)(3.15)(landing), T(1)(-14.7)(apartmentsPart), ceiling, T(3)(6.6)(ceiling)])

#Basement
domain = larDomain([12,12,12])
controlPoints1 = [[0,0,0],[3,0,3],[6,0,0]]
controlPoints2 = [[0,4,0],[3,4,3],[6,4,0]]

controlPoints3 = [[0,0,2.5],[3,0,2.5],[6,0,2.5]]
controlPoints4 = [[0,4,2.5],[3,4,2.5],[6,4,2.5]]

b1 = BEZIER(S1)(controlPoints1)
b2 = BEZIER(S1)(controlPoints2)

b3 = BEZIER(S1)(controlPoints3)
b4 = BEZIER(S1)(controlPoints4)

surface = BEZIER(S2)([b1,b2])

surface2 = BEZIER(S2)([b3,b4])

mapping = BEZIER(S3)([surface,surface2])
arch = larMap(mapping)(domain)
arch = STRUCT(MKPOLS(arch))

archWall = PROD([CUBOID([0.5,4]), Q(6.7)])

archWalls = STRUCT([archWall, T(1)(6.5)] * 2)

archElement = STRUCT([T([1,3])([0.5,4.2])(arch), archWalls])

archElement = S([1,2,3])([0.52,0.45,0.45])(archElement)

#VIEW(archElement)
archRow = STRUCT([archElement, T(1)(3.25)] * 8)

#External wall
externalWall = T([1,3])([14.7,9.6])(PROD([CUBOID([0.3,13.1]), Q(6.6)]))

#Pavement
pavement = COLOR([0.47,0.46,0.45])(T([1,2,3])([-2,-2,-0.3])(PROD([CUBOID([30.5,17.5]), Q(0.3)])))

#Spiral stair
def spiralStair(thickness=0.3,R=1.5,r=0.5,riser=0.1,pitch=3.5,nturns=7.5,steps=18):
	V,CV = larSolidHelicoid(thickness,R,r,pitch,nturns,steps)()
	W = CAT([[V[k],V[k+1],V[k+2],V[k+3]]+[SUM([V[k+1],[0,0,-riser]]),SUM([V[k+3],[0,0,-riser]])]
	for k,v in enumerate(V[:-4]) if k%4==0])
	for k,w in enumerate(W[:-12]):
		if k%6==0: W[k+1][2]=W[k+10][2]; W[k+3][2]=W[k+11][2]
	nsteps = len(W)/12
	CW =[SUM([[0,1,2,3,6,8,10,11],[6*k]*8])
	for k in range(nsteps)]
	return W,CW

stair = STRUCT(MKPOLS(spiralStair()))

condominium = STRUCT([T([1,3])([14.7,3])(apartments), archRow, T(2)(11.3)(archRow), T([1,3])([0,9.6])(apartmentsPart), S(1)(0.58)(T([1,3])([14.5,15.9])(ceiling)), T([1,3])([14.7,13.05])(landing), externalWall, pavement, T([1,2])([13,14.5])(stair)])

VIEW(condominium)