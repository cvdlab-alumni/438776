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
from architectural import *

################################################ Exercise 1 code ################################################

def larStruct(item1, item2):
	V = item1[0] + item2[0]

	CV1 = item1[1]
	CV2 = [[j + len(item1[0]) for j in i]for i in item2[1]]
	CV = CV1 + CV2

	result = V, CV
	return result


DRAW = COMP([VIEW,STRUCT,MKPOLS])

master = assemblyDiagramInit([7,13,3])([[.3,4,.3,1.5,.3,5,.3],[.3,3,.3,1.5,.3,.5,.3,3,.3,2,.3,1,.3],[.3,2.7,.3]])
V,CV = master
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(CV)),CYAN,2)
#VIEW(hpc)

toRemove = [82,83,202,203,88,89,58,59,226,227,70,71,208,209,44,50,56,62,68,74,122,200,206,212,218,224,230,152,146,140,134,128,
			229,223,217,211,205,199,143,151,145,142,139,136,134,133,137,131,130,127,49,61,67,73,55,43,121]
master = V,[cell for k,cell in enumerate(CV) if not (k in toRemove)]
#DRAW(master)

hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)

#Bedroom window
toMerge = 206
diagram = assemblyDiagramInit([1,6,3])([[.3],[.5,.1,0.7,.1,.7,.1],[.1,2.5,.1]])
master = diagram2cell(diagram,master,toMerge)

#Bedroom window
toMerge = 200
diagram = assemblyDiagramInit([1,7,4])([[.3],[.5,.2,1.5,.2,1.5,.2,2.7],[1,.1,1.5,.1]])
master = diagram2cell(diagram,master,toMerge)

#Living room window
toMerge = 182
diagram = assemblyDiagramInit([1,7,3])([[.3],[.5,.15,1.2,.15,1.2,.15,2],[.1,2.5,.1]])
master = diagram2cell(diagram,master,toMerge)

#Bedroom door
toMerge = 146
diagram = assemblyDiagramInit([1,3,2])([[.3],[.1,0.5,.3],[2.5,.1]])
master = diagram2cell(diagram,master,toMerge)

#Bedroom door
toMerge = 140
diagram = assemblyDiagramInit([1,3,2])([[.3],[.1,0.3,.3],[2.5,.1]])
master = diagram2cell(diagram,master,toMerge)

#Living room door
toMerge = 128
diagram = assemblyDiagramInit([1,3,2])([[.3],[.7,2.5,.01],[2.5,.1]])
master = diagram2cell(diagram,master,toMerge)

#Toilet door
toMerge = 112
diagram = assemblyDiagramInit([4,1,2])([[.1,.1,1,.1],[.3],[2.5,.1]])
master = diagram2cell(diagram,master,toMerge)

#Bedroom door
toMerge = 86
diagram = assemblyDiagramInit([1,3,2])([[.3],[.1,0.5,.3],[2.5,.1]])
master = diagram2cell(diagram,master,toMerge)

#Bathroom door
toMerge = 80
diagram = assemblyDiagramInit([1,3,2])([[.3],[.1,0.45,.6],[2.5,.1]])
master = diagram2cell(diagram,master,toMerge)

#Bedroom window
toMerge = 60
diagram = assemblyDiagramInit([7,1,3])([[0.2,.1,0.7,0.1,0.7,.1,2.3],[.3],[.1,2.5,.1]])
master = diagram2cell(diagram,master,toMerge)

#Kitchen door
toMerge = 44
diagram = assemblyDiagramInit([3,1,2])([[.1,0.15,.3],[.3],[2.5,.1]])
master = diagram2cell(diagram,master,toMerge)

#Kitchen window
toMerge = 40
diagram = assemblyDiagramInit([6,1,3])([[2.5,.15,0.8,.15,.8,.15],[.3],[.1,2.5,.1]])
master = diagram2cell(diagram,master,toMerge)

#Door
toMerge = 10
diagram = assemblyDiagramInit([1,3,2])([[.3],[.1,1.2,.3],[2.5,.1]])
master = diagram2cell(diagram,master,toMerge)

hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,1)
#VIEW(hpc)


toRemove = [339,340,341,342,343,344,348,349,350,351,352,353,253,254,255,256,257,258,262,263,264,265,266,
			267,227,228,229,231,232,233,239,240,241,243,244,245,207,208,209,210,211,212,216,217,218,219,
			220,221,356,332,285,279,305,273,299,293, 312,313,314,315,316,317,321,322,323,324,325,326]
rooms = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]

#Y-axis balcony model
yBalcony = assemblyDiagramInit([2,3,2])([[1.5,.3],[.3,3.5,.3],[.1,1]])
V,CV = yBalcony

hpc = SKEL_1(STRUCT(MKPOLS(yBalcony)))
hpc = cellNumbering (yBalcony,hpc)(range(len(CV)),CYAN,2)
#VIEW(hpc)

toRemove = [3]
yBalcony = V,[cell for k,cell in enumerate(CV) if not (k in toRemove)]

#Living room balcony
V,CV = yBalcony
V1 = larTranslate([11.7,0.0,0.0])(V)
livingRoomBalcony = V1, CV

apartment = larStruct(rooms, livingRoomBalcony)

#Bedroom balcony
V,CV = livingRoomBalcony
V1 = larTranslate([0.0,9.2,0.0])(larScale([1,0.952,1])(V))
bedroomBalcony = V1, CV

apartment = larStruct(apartment, bedroomBalcony)

#X-axis balcony model
xBalcony = assemblyDiagramInit([3,2,2])([[.3,3.5,.3],[1.5,.3],[.1,1]])
V,CV = xBalcony
hpc = SKEL_1(STRUCT(MKPOLS(xBalcony)))
hpc = cellNumbering (xBalcony,hpc)(range(len(CV)),CYAN,2)
#VIEW(hpc)

toRemove = [5]
xBalcony = V,[cell for k,cell in enumerate(CV) if not (k in toRemove)]

#Bedroom balcony
V,CV = xBalcony
V1 = larTranslate([0.0,13.1,0.0])(V)
bedroomTwoBalcony = V1, CV

apartment = larStruct(apartment, bedroomTwoBalcony)

#Kitchen balcony
V,CV = xBalcony
V1 = larTranslate([1.5,0.0,0.0])(larScale([1,-1,1])(V))
kitchenBalcony = V1, CV



apartment = larStruct(apartment, kitchenBalcony)

#DRAW(apartment)

################################################ Exercise 1 code end ################################################

######################## FIRST FLOOR ########################

#First block of apartments, left-below
V, CV = apartment
V1 = larTranslate([0.0,0.0,3.3])(V)

apartment = V, CV
apartment2 = V1, CV

apartmentsLeft = larStruct(apartment, apartment2)

#Second block of apartments, right-below
V, CV = apartmentsLeft
V1 = larScale([-1.0,1.0,1.0])(V)

apartmentsRight = V1, CV

#First block of apartments, left-below (traslated)
V, CV = apartmentsLeft
V1 = larTranslate([3.0,0.0,0.0])(V)

apartmentsLeft = V1, CV

#All below apartments
apartments = STRUCT(MKPOLS(apartmentsRight) + MKPOLS(apartmentsLeft))

#Landing (pianerottolo)
landing = T(1)(-3)(PROD([CUBOID([3,13.1]), Q(0.3)]))

#Ceiling
ceiling = T(1)(-11.9)(PROD([CUBOID([26.8,13.1]), Q(0.3)]))


condominiumBelow = STRUCT([apartments, T([1,3])([3,3.3])(landing), ceiling, T([3])([6.6])(ceiling)])



######################## SECOND FLOOR ########################

#Third block of apartments, right-above
V, CV = apartmentsRight
V1 = larTranslate([0,0,6.6])(V)

apartmentsTop = V1, CV
apartmentsTop = STRUCT(MKPOLS(apartmentsTop))

#External wall
externalWall = T([3])([6.9])(PROD([CUBOID([0.3,13.1]), Q(6.3)]))


condominiumTop = STRUCT([apartmentsTop, S(1)(0.58)(T([1,3])([-8.7,12.9])(ceiling)), T([1,3])([3,9.9])(landing), T(1)(3)(externalWall)])



######################## GROUND FLOOR ########################

#Pavement
pavement = COLOR([0.47,0.46,0.45])(T([1,2,3])([-2,-2,-3.3])(PROD([CUBOID([30.5,17.5]), Q(0.3)])))

stair = STRUCT(MKPOLS(spiralStair(width=0.3,R=1.3,r=0.3,riser=0.1,pitch=3.5,nturns=7.5,steps=36)))


condominiumApartments = STRUCT([condominiumBelow, condominiumTop])

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

archRow = STRUCT([archElement, T(1)(3.25)] * 8)


#archRow, T(2)(11.3)(archRow)
condominium = STRUCT([T([1,3])([11.7,3])(condominiumApartments), T(2)(0.8)(archRow), T(2)(10.5)(archRow), T([3])([3])(pavement), T([1,2,3])([13.3,14.6,-.15])(stair)])

VIEW(condominium)