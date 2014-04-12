from pyplasm import *
import sys
""" import modules from lar-cc/lib """
sys.path.insert(0, 'C:/Users/Damian/lar-cc/lib/py/')
from simplexn import *
from larcc import *
from lar2psm import *
from largrid import *
from mapper import *

######################################### BASEMENT #########################################
#garden
gardenVerts = [[0,0],[65.4,0],[65.4,47.7],[0,47.7]]
gardenCells = [[1,2,3,4]]
pols = None
garden = MKPOL([gardenVerts, gardenCells, pols])
garden = PROD([garden,Q(3.75)])

coloredGarden = COLOR([0.133,0.384,0.055])(garden)

#garden border
gardenBorderVerts = [[-1,-1],[66.4,-1],[66.4,48.7],[-1,48.7]]
gardenBorderCells = [[1,2,3,4]]
pols = None
gardenBorder = MKPOL([gardenBorderVerts, gardenBorderCells, pols])
gardenBorder = PROD([gardenBorder,Q(3.75)])

gardenBorder = DIFFERENCE([gardenBorder, garden])

#first stair
firstStairVerts = [[6.1,6.1],[59.3,6.1],[59.3,41.6],[6.1,41.6]]
firstStairCells = [[1,2,3,4]]
firstStair = MKPOL([firstStairVerts, firstStairCells, pols])
coloredfirstStair = COLOR([0.816,0.804,0.804])(firstStair)
coloredfirstStair = T(3)(3.75)(PROD([coloredfirstStair,Q(1)]))

#second stair
secondStairVerts = [[7.1,7.1],[58.3,7.1],[58.3,40.6],[7.1,40.6]]
secondStairCells = [[1,2,3,4]]
secondStair = MKPOL([secondStairVerts, secondStairCells, pols])
coloredsecondStair = COLOR([0.859,0.859,0.859])(secondStair)
coloredsecondStair = T(3)(4.75)(PROD([coloredsecondStair,Q(0.3)]))

#columns basement
columnBasementVerts = [[8.1,8.1],[57.3,8.1],[57.3,39.6],[8.1,39.6]]
columnBasementCells = [[1,2,3,4]]
columnBasement = MKPOL([columnBasementVerts, columnBasementCells, pols])
columnBasement = COLOR([0.922,0.922,0.922])(columnBasement)
columnBasement = T(3)(5.05)(PROD([columnBasement,Q(1)]))


basementStruct = INSR(STRUCT)([gardenBorder,coloredGarden,coloredfirstStair,coloredsecondStair,columnBasement])


######################################### COLUMNS AND WALL #########################################
#capitello top
x_topCapitelloRow = QUOTE([2.1,-2.1] * 12)
Y_topCapitelloRow = QUOTE([2.1,-27.3] * 2)
topCapitelloRow = INSR(PROD)([x_topCapitelloRow,Y_topCapitelloRow])
topCapitelloRow = COLOR([0.450,0.450,0.450])(topCapitelloRow)
topCapitelloRow = T(3)(19.25)(PROD([topCapitelloRow,Q(0.2)]))

x_topCapitelloColumn = QUOTE([2.1, -44.1] * 2)
Y_topCapitelloColumn = QUOTE([2.1,-2.1] * 8)
topCapitelloColumn = INSR(PROD)([x_topCapitelloColumn,Y_topCapitelloColumn])
topCapitelloColumn = COLOR([0.450,0.450,0.450])(topCapitelloColumn)
topCapitelloColumn = T(3)(19.25)(PROD([topCapitelloColumn,Q(0.2)]))

x_topCapitelloCouple = QUOTE([-21,2.1,-2.1,2.1])
Y_topCapitelloCouple = QUOTE([-25.2,2.1])
topCapitelloCouple = INSR(PROD)([x_topCapitelloCouple,Y_topCapitelloCouple])
topCapitelloCouple = COLOR([0.450,0.450,0.450])(topCapitelloCouple)
topCapitelloCouple = T(3)(19.25)(PROD([topCapitelloCouple,Q(0.2)]))

topCapitello = INSR(STRUCT)([topCapitelloRow,topCapitelloColumn,topCapitelloCouple])

topCapitello = STRUCT([topCapitello,topCapitelloCouple])
topCapitello = T([1,2])([8.5,8.1])(topCapitello)

#capitello bottom
x_bottomCapitelloRow = QUOTE([1.9,-2.3] * 12)
Y_bottomCapitelloRow = QUOTE([1.9,-27.5] * 2)
bottomCapitelloRow = INSR(PROD)([x_bottomCapitelloRow,Y_bottomCapitelloRow])
bottomCapitelloRow = COLOR([0.816,0.804,0.804])(bottomCapitelloRow)
bottomCapitelloRow = T(3)(19.05)(PROD([bottomCapitelloRow,Q(0.2)]))

x_bottomCapitelloColumn = QUOTE([1.9, -44.3] * 2)
Y_bottomCapitelloColumn = QUOTE([1.9,-2.3] * 8)
bottomCapitelloColumn = INSR(PROD)([x_bottomCapitelloColumn,Y_bottomCapitelloColumn])
bottomCapitelloColumn = COLOR([0.816,0.804,0.804])(bottomCapitelloColumn)
bottomCapitelloColumn = T(3)(19.05)(PROD([bottomCapitelloColumn,Q(0.2)]))

x_bottomCapitelloCouple = QUOTE([-21,1.9,-2.3,1.9])
Y_bottomCapitelloCouple = QUOTE([-25.2,1.9])
bottomCapitelloCouple = INSR(PROD)([x_bottomCapitelloCouple,Y_bottomCapitelloCouple])
bottomCapitelloCouple = COLOR([0.816,0.804,0.804])(bottomCapitelloCouple)
bottomCapitelloCouple = T(3)(19.05)(PROD([bottomCapitelloCouple,Q(0.2)]))

bottomCapitello = INSR(STRUCT)([bottomCapitelloRow,bottomCapitelloColumn,bottomCapitelloCouple])
bottomCapitello = T([1,2])([8.6,8.2])(bottomCapitello)

#columns
def sphere(p): return [0.95*COS(p[0]), 0.95*SIN(p[0])]
def domain(n): return INTERVALS(2*PI)(n)
column = MAP(sphere)(domain(16))
column = JOIN(column)
column = T(3)(6.05)(PROD([column,Q(13)]))

firstColumnsRow = STRUCT([column, T(1)(4.2)] * 12)
firstColumnsRow = T([1,2])([9.55,9.15])(firstColumnsRow)

secondColumnsRow = STRUCT([column, T(1)(4.2)] * 12)
secondColumnsRow = T([1,2])([0,29.40])(firstColumnsRow)

firstColumnsColumn = STRUCT([column, T(2)(4.2)] * 8)
firstColumnsColumn = T([1,2])([9.55,9.15])(firstColumnsColumn)

secondColumnsColumn = STRUCT([column, T(2)(4.2)] * 8)
secondColumnsColumn = T([1,2])([46.2,0])(firstColumnsColumn)

coupleColumn = STRUCT([column, T(1)(4.2)] * 2)
coupleColumn = T([1,2])([30.55, 34.35])(coupleColumn)

columns = INSR(STRUCT)([firstColumnsRow,secondColumnsRow,firstColumnsColumn,secondColumnsColumn,coupleColumn])


#internal wall
wallLeftVerts = [[37.9,33.3],[52.6,33.3],[52.6,35.4],[37.9,35.4]]
wallLeftCells = [[1,2,3,4]]
wallLeft = MKPOL([wallLeftVerts, wallLeftCells, pols])
wallLeft = T(3)(6.05)(PROD([wallLeft,Q(13.04)]))

wallRightVerts = [[12.7,33.3],[27.3,33.3],[27.3,35.4],[12.7,35.4]]
wallRightCells = [[1,2,3,4]]
wallRight = MKPOL([wallRightVerts, wallRightCells, pols])
wallRight = T(3)(6.05)(PROD([wallRight,Q(13.04)]))

wallBackVerts = [[12.7,12.3],[52.6,12.3],[52.6,14.4],[12.7,14.4]]
wallBackCells = [[1,2,3,4]]
wallBack = MKPOL([wallBackVerts, wallBackCells, pols])
wallBack = T(3)(6.05)(PROD([wallBack,Q(13.04)]))

wallLateralLeftVerts = [[50.5,12.3],[52.6,12.3],[52.6,35.4],[50.5,35.4]]
wallLateralLeftCells = [[1,2,3,4]]
wallLateralLeft = MKPOL([wallLateralLeftVerts, wallLateralLeftCells, pols])
wallLateralLeft = T(3)(6.05)(PROD([wallLateralLeft,Q(13.04)]))

wallLateralRight = T([1])([-37.8])(wallLateralLeft)

internalWall = INSR(STRUCT)([wallLeft,wallRight,wallBack,wallLateralLeft,wallLateralRight])

#statue basement
statueBasamentVerts = [[28.1,14.4],[36.5,14.4],[36.5,22.8],[28.1,22.8]]
statueBasamentCells = [[1,2,3,4]]
statueBasament = MKPOL([statueBasamentVerts, statueBasamentCells, pols])
statueBasament = COLOR([0.922,0.922,0.922])(statueBasament)
statueBasament = T(3)(6.05)(PROD([statueBasament,Q(3)]))

#walls near the stairs
stairsRightWallVerts = [[21.3,39.6],[22.8,39.6],[22.8,44.6],[21.3,44.6]]
stairsRightWallCells = [[1,2,3,4]]
stairsRightWall = MKPOL([stairsRightWallVerts, stairsRightWallCells, pols])
stairsRightWall = COLOR([0.650,0.650,0.650])(stairsRightWall)
stairsRightWall = T(3)(3.75)(PROD([stairsRightWall,Q(2.3)]))

stairsLeftWallVerts = [[42.5,39.6],[44,39.6],[44,44.6],[42.5,44.6]]
stairsLeftWallCells = [[1,2,3,4]]
stairsLeftWall = MKPOL([stairsLeftWallVerts, stairsLeftWallCells, pols])
stairsLeftWall = COLOR([0.650,0.650,0.650])(stairsLeftWall)
stairsLeftWall = T(3)(3.75)(PROD([stairsLeftWall,Q(2.3)]))

stairsWall = STRUCT([stairsRightWall,stairsLeftWall])

#stairs
stair1WallVerts = [[21.3,39.6],[44,39.6],[44,40.6],[21.3,40.6]]
stair1WallCells = [[1,2,3,4]]
stair1Wall = MKPOL([stair1WallVerts, stair1WallCells, pols])
stair1Wall = COLOR([0.650,0.650,0.650])(stair1Wall)
stair1Wall = T(3)(3.75)(PROD([stair1Wall,Q(2.3)]))
stair2WallVerts = [[21.3,40.6],[44,40.6],[44,41.6],[21.3,41.6]]
stair2WallCells = [[1,2,3,4]]
stair2Wall = MKPOL([stair2WallVerts, stair2WallCells, pols])
stair2Wall = COLOR([0.650,0.650,0.650])(stair2Wall)
stair2Wall = T(3)(3.75)(PROD([stair2Wall,Q(2)]))
stair3WallVerts = [[21.3,41.6],[44,41.6],[44,42.6],[21.3,42.6]]
stair3WallCells = [[1,2,3,4]]
stair3Wall = MKPOL([stair3WallVerts, stair3WallCells, pols])
stair3Wall = COLOR([0.650,0.650,0.650])(stair3Wall)
stair3Wall = T(3)(3.75)(PROD([stair3Wall,Q(1.7)]))
stair4WallVerts = [[21.3,42.6],[44,42.6],[44,43.6],[21.3,43.6]]
stair4WallCells = [[1,2,3,4]]
stair4Wall = MKPOL([stair4WallVerts, stair4WallCells, pols])
stair4Wall = COLOR([0.650,0.650,0.650])(stair4Wall)
stair4Wall = T(3)(3.75)(PROD([stair4Wall,Q(1.4)]))
stair5WallVerts = [[21.3,43.6],[44,43.6],[44,44.6],[21.3,44.6]]
stair5WallCells = [[1,2,3,4]]
stair5Wall = MKPOL([stair5WallVerts, stair5WallCells, pols])
stair5Wall = COLOR([0.650,0.650,0.650])(stair5Wall)
stair5Wall = T(3)(3.75)(PROD([stair5Wall,Q(1.1)]))
stair6WallVerts = [[21.3,44.6],[44,44.6],[44,45.6],[21.3,45.6]]
stair6WallCells = [[1,2,3,4]]
stair6Wall = MKPOL([stair6WallVerts, stair6WallCells, pols])
stair6Wall = COLOR([0.650,0.650,0.650])(stair6Wall)
stair6Wall = T(3)(3.75)(PROD([stair6Wall,Q(0.8)]))
stair7WallVerts = [[21.3,45.6],[44,45.6],[44,46.6],[21.3,46.6]]
stair7WallCells = [[1,2,3,4]]
stair7Wall = MKPOL([stair7WallVerts, stair7WallCells, pols])
stair7Wall = COLOR([0.650,0.650,0.650])(stair7Wall)
stair7Wall = T(3)(3.75)(PROD([stair7Wall,Q(0.5)]))
stair8WallVerts = [[21.3,46.6],[44,46.6],[44,47.7],[21.3,47.7]]
stair8WallCells = [[1,2,3,4]]
stair8Wall = MKPOL([stair8WallVerts, stair8WallCells, pols])
stair8Wall = COLOR([0.650,0.650,0.650])(stair8Wall)
stair8Wall = T(3)(3.75)(PROD([stair8Wall,Q(0.2)]))

stairs = INSR(STRUCT)([stair1Wall,stair2Wall,stair3Wall,stair4Wall,stair5Wall,stair6Wall,stair7Wall,stair8Wall])

#stairs front
stairsDown = T([2,3])([8.1,-2.3])(stairs)
stairsDown = COLOR([0.780,0.780,0.722])(stairsDown)
stairsBottomVerts = [[21.3,47.7],[44,47.7],[44,55.8],[21.3,55.8]]
stairsBottomCells = [[1,2,3,4]]
stairsBottom = MKPOL([stairsBottomVerts, stairsBottomCells, pols])
stairsBottom = PROD([stairsBottom,Q(1.45)])
stairsBottom = COLOR([0.780,0.780,0.722])(stairsBottom)

stairsDown1Verts = [[21.3,49.7],[44,49.7],[44,58.7],[21.3,58.7]]
stairsDown1Cells = [[1,2,3,4]]
stairsDown1 = MKPOL([stairsDown1Verts, stairsDown1Cells, pols])
stairsDown1 = PROD([stairsDown1,Q(0.6)])
stairsDown1 = COLOR([0.780,0.780,0.722])(stairsDown1)

stairsDown2Verts = [[21.3,49.7],[44,49.7],[44,57.3],[21.3,57.3]]
stairsDown2Cells = [[1,2,3,4]]
stairsDown2 = MKPOL([stairsDown2Verts, stairsDown2Cells, pols])
stairsDown2 = PROD([stairsDown2,Q(1.2)])
stairsDown2 = COLOR([0.780,0.780,0.722])(stairsDown2)



columnsAndWall = INSR(STRUCT)([topCapitello,bottomCapitello,columns,internalWall,stairs,stairsWall,stairsDown,stairsBottom,stairsDown1,stairsDown2])


######################################### INTERIOR FURNITURE #########################################
#statue basement
statueBasamentVerts = [[28.1,14.4],[36.5,14.4],[36.5,22.8],[28.1,22.8]]
statueBasamentCells = [[1,2,3,4]]
statueBasament = MKPOL([statueBasamentVerts, statueBasamentCells, pols])
statueBasament = COLOR([0.922,0.922,0.922])(statueBasament)
statueBasament = T(3)(6.05)(PROD([statueBasament,Q(3)]))


######################################### COVERAGE #########################################
#basement
basementVerts = [[8.1,8.1],[57.3,8.1],[57.3,39.6],[8.1,39.6]]
basementCells = [[1,2,3,4]]
basement = MKPOL([basementVerts, basementCells, pols])
basement = COLOR([0.922,0.922,0.922])(basement)
basement = T(3)(0)(PROD([basement,Q(2.9)]))

#basement top
basementTopVerts = [[7.1,7.1],[58.3,7.1],[58.3,40.6],[7.1,40.6]]
basementTopCells = [[1,2,3,4]]
basementTop = MKPOL([basementTopVerts, basementTopCells, pols])
basementTop = COLOR([0.800,0.800,0.800])(basementTop)
basementTop = T(3)(2.9)(PROD([basementTop,Q(1.6)]))

#roof
roofVerts = [[12.55,12.55],[52.85,12.55],[52.85,35.15],[12.55,35.15]]
roofCells = [[1,2,3,4]]
roof = MKPOL([roofVerts, roofCells, pols])
roof = COLOR(WHITE)(roof)
roof = T(3)(4.5)(PROD([roof,Q(5)]))

#roof top
roofTopVerts = [[11.55,11.55],[53.85,11.55],[53.85,36.15],[11.55,36.15]]
roofTopCells = [[1,2,3,4]]
roofTop = MKPOL([roofTopVerts, roofTopCells, pols])
roofTop = COLOR(WHITE)(roofTop)
roofTop = T(3)(9.5)(PROD([roofTop,Q(1.7)]))


coverage = INSR(STRUCT)([basementTop,roof,basement,roofTop])
coverage = T(3)(15.7)(coverage)


solid_model_3D = INSR(STRUCT)([basementStruct, statueBasament, columnsAndWall, coverage])


######################################### NEIGHBOURING BUILDINGS #########################################
#There are no buildings near the monument that I chose, so I invented someone

#first building
floor1Structure = T(3)(0.25)(PROD([CUBOID([25,15]), Q(3.75)]))
floor1Structure = COLOR([0.51,0.51,0.51])(floor1Structure)
floor1Border = COLOR(BLACK)(PROD([CUBOID([25,15]), Q(0.25)]))
floor1 = STRUCT([floor1Border, floor1Structure])
building1 = STRUCT([floor1, T(3)(4)] * 10)
building1 = T([1,2])([130,0])(building1)
building1 = ROTATE([1,2])(PI/15)(building1)

#second building
floor2Structure = T(3)(0.25)(PROD([CUBOID([10,15]), Q(3.75)]))
floor2Structure = COLOR([0.48,0.3,0.15])(floor2Structure)
floor2Border = COLOR(BLACK)(PROD([CUBOID([10,15]), Q(0.25)]))
floor2 = STRUCT([floor2Border, floor2Structure])
building2 = STRUCT([floor2, T(3)(4)] * 5)
building2 = T([1,2])([160,0])(building2)
building2 = ROTATE([1,2])(PI/15)(building2)

#third building
floor3Structure = T(3)(0.25)(PROD([CUBOID([10,15]), Q(3.75)]))
floor3Structure = COLOR([0.84,0.65,0.49])(floor3Structure)
floor3Border = COLOR(BLACK)(PROD([CUBOID([10,15]), Q(0.25)]))
floor3 = STRUCT([floor3Border, floor3Structure])
building3 = STRUCT([floor3, T(3)(4)] * 8)
building3 = T([1,2])([-100,0])(building3)
building3 = ROTATE([1,2])(PI/2)(building3)


buildings = INSR(STRUCT)([building1, building2, building3])


######################################### URBAN FITTINGS #########################################
#Round garden under the monument
def disk2D(p):
	u,v = p
	return [65*v*COS(u), 65*v*SIN(u)]
domain2D = PROD([INTERVALS(2*PI)(60), INTERVALS(1)(3)])
roundGarden = T([1,2])([32.7, 23.85])(COLOR([0.17,0.41,0.17])(MAP(disk2D)(domain2D)))

#Sidewalk
sidewalk = T([1,2])([30.7, 21.85])(MAP(disk2D)(domain2D))
sidewalk = S([1,2])([1.08,1.08])(sidewalk)
sidewalk = DIFFERENCE([sidewalk,roundGarden])

#Street
firstRoadway = T([1,2])([29, 20.5])(MAP(disk2D)(domain2D))
firstRoadway = S([1,2])([1.16,1.16])(firstRoadway)
firstRoadway = COLOR([0.47,0.46,0.45])(DIFFERENCE([firstRoadway,sidewalk,roundGarden]))
firstRoadwayBorder = S([1,2])([1.01,1.01])(firstRoadway)
firstRoadwayBorder =DIFFERENCE([firstRoadwayBorder,firstRoadway,sidewalk,roundGarden])
firstRoadway = STRUCT([firstRoadway,firstRoadwayBorder])

secondRoadway = T([1,2])([27.5, 19])(MAP(disk2D)(domain2D))
secondRoadway = S([1,2])([1.24,1.24])(secondRoadway)
secondRoadway = COLOR([0.47,0.46,0.45])(DIFFERENCE([secondRoadway,firstRoadway,roundGarden,sidewalk]))
secondRoadwayBorder = S([1,2])([1.25,1.25])(T([1,2])([27.5, 18.9])(MAP(disk2D)(domain2D)))
secondRoadwayBorder = DIFFERENCE([secondRoadwayBorder,secondRoadway,roundGarden,firstRoadway,sidewalk])
secondRoadway = STRUCT([secondRoadway,secondRoadwayBorder])

thirdRoadway = T([1,2])([26, 17.5])(MAP(disk2D)(domain2D))
thirdRoadway = S([1,2])([1.32,1.32])(thirdRoadway)
thirdRoadway = COLOR([0.47,0.46,0.45])(DIFFERENCE([thirdRoadway,secondRoadwayBorder,secondRoadway,firstRoadway,roundGarden,sidewalk]))
thirdRoadwayBorder = S([1,2])([1.33,1.33])(T([1,2])([25.9, 17.5])(MAP(disk2D)(domain2D)))
thirdRoadwayBorder = DIFFERENCE([thirdRoadwayBorder,thirdRoadway,secondRoadwayBorder,secondRoadway,roundGarden,firstRoadway,sidewalk])
thirdRoadway = STRUCT([thirdRoadway,thirdRoadwayBorder])


street = INSR(STRUCT)([firstRoadway, secondRoadway, thirdRoadway])

#Trees
cylinder = checkModel(larCylinder([1.5,3])([32,1]))
sphere = checkModel(larSphere(4.5)())
cylinder = COLOR([0.44,0.32,0.05])(STRUCT(MKPOLS(cylinder)))
sphere = COLOR([0.13,0.29,0.09])(T(3)(6.5)(STRUCT(MKPOLS(sphere))))

tree = T(1)(-5)(STRUCT([cylinder,sphere]))

tree2 = T(1)(75)(tree)

tree3 = T([1,2])([6,3])(tree2)

tree4 = T(2)(45)(tree2)
tree5 = T([1,2])([4,10])(tree4)
tree6 = T([1,2])([0,14])(tree4)
tree7 = T([1,2])([-6,18])(tree4)

tree8 = T([1,2])([-73,10])(tree4)
tree9 = T([1,2])([-67,14])(tree4)
tree10 = T([1,2])([-63,18])(tree4)

tree11 = T([1,2])([-5,10])(tree)
tree12 = T([1,2])([-2,15])(tree)
tree13 = T([1,2])([-10,20])(tree)

tree14 = T([1,2])([10,10])(tree2)
tree15 = T([1,2])([1,15])(tree2)
tree16 = T([1,2])([3,20])(tree2)

cylinder = checkModel(larCylinder([2,4])([32,1]))
sphere = checkModel(larSphere(6)())
cylinder = COLOR([0.44,0.32,0.05])(STRUCT(MKPOLS(cylinder)))
sphere = COLOR([0.13,0.29,0.09])(T(3)(8.5)(STRUCT(MKPOLS(sphere))))

tree17 = T([1,2])([75,30])(STRUCT([cylinder,sphere]))

tree18 = T([1,2])([-85,10])(tree17)

tree19 = T([1,2])([-82,-2])(tree17)


trees = INSR(STRUCT)([tree,tree2,tree3,tree4,tree5,tree6,tree7,tree8,tree9,tree10,tree11,tree12,tree13,tree14,tree15,tree16,tree17,tree18,tree19])

#Flower containers
containerTerrain = CUBOID([10,5])
containerTerrain = PROD([containerTerrain,Q(1.75)])
containerTerrain = COLOR([0.35,0.25,0.04])(containerTerrain)

containerBorder = T([1,2])([-1,-1])(CUBOID([12,7]))
containerBorder = PROD([containerBorder,Q(1.75)])
containerBorder = COLOR(WHITE)(containerBorder)
containerBorder = DIFFERENCE([containerBorder, containerTerrain])

flower = checkModel(larSphere(0.7)())
flower = COLOR(RED)(T([1,2,3])([8,3,2])(STRUCT(MKPOLS(flower))))

flower2 = T(1)(-3)(flower)
flower3 = T(1)(-6)(flower)

container = T([1,2])([50,49.7])(STRUCT([containerBorder,containerTerrain,flower,flower2,flower3]))

containers = STRUCT([container, T(1)(-45)(container)])

#Street lamps
pole = MAP(disk2D)(domain2D)
pole = S([1,2])([0.005,0.005])(pole)
pole = COLOR([0.47,0.46,0.45])(PROD([pole,Q(19)]))

light = checkModel(larSphere(2)())
light = COLOR(YELLOW)(T(3)(21)(STRUCT(MKPOLS(light))))

lamp = STRUCT([pole, light])

lamps = INSR(STRUCT)([T([1,2])([-20,-10])(lamp), T([1,2])([62,80])(lamp), T([1,2])([85,-10])(lamp)])

#Benches
back = PROD([CUBOID([3,0.3]), Q(1.2)])
sit = PROD([CUBOID([3,1.2]), Q(0.3)])
leg = PROD([CUBOID([0.3,0.3]), Q(0.5)])

bench = INSR(STRUCT)([leg, T(1)(2.7)(leg), T(2)(0.9)(leg), T([1,2])([2.7,0.9])(leg), T(3)(0.5)(sit), T(3)(0.5)(back)])
bench = T([1,2])([45,65])(bench)
bench = COLOR([0.79,0.64,0.3])(bench)
bench = ROTATE([1,2])(PI/6)(bench)

benches = INSR(STRUCT)([bench, T([1,2])([18,-10])(ROTATE([1,2])(PI/6)(bench))])

#Bus shelters
backShelter = PROD([CUBOID([7,0.3]), Q(3)])
top = PROD([CUBOID([7,2]), Q(0.5)])

busShelter = INSR(STRUCT)([backShelter, T(3)(3)(top)])
busShelter = T([1,2])([43,64])(busShelter)
busShelter = COLOR([0.69,0.1,0.2])(busShelter)
busShelter = ROTATE([1,2])(PI/6)(busShelter)

poleBus = MAP(disk2D)(domain2D)
poleBus = S([1,2])([0.005,0.005])(poleBus)
poleBus = COLOR([0.47,0.46,0.45])(PROD([poleBus,Q(7)]))
poleBusSignal = T([1,2,3])([-0.3,-0.3,7])(PROD([CUBOID([0.5,2]), Q(2)]))


busShelters = INSR(STRUCT)([T([1,2])([15,90])(STRUCT([poleBus, poleBusSignal])), busShelter, T([1,2])([18,-10])(ROTATE([1,2])(PI/6)(busShelter))])



urbanFittings = INSR(STRUCT)([roundGarden,sidewalk,street,trees,containers,lamps,benches,busShelters])



smallAreaPlan = INSR(STRUCT)([solid_model_3D, buildings, urbanFittings])
VIEW(smallAreaPlan)