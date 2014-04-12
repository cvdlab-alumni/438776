from pyplasm import *

######################################### BASEMENT #########################################
#first stair
firstStairVerts = [[6.1,6.1],[59.3,6.1],[59.3,41.6],[6.1,41.6]]
firstStairCells = [[1,2,3,4]]
pols = None
firstStair = MKPOL([firstStairVerts, firstStairCells, pols])
coloredfirstStair = COLOR([0.816,0.804,0.804])(firstStair)
coloredfirstStair = PROD([coloredfirstStair,Q(1)])

#second stair
secondStairVerts = [[7.1,7.1],[58.3,7.1],[58.3,40.6],[7.1,40.6]]
secondStairCells = [[1,2,3,4]]
secondStair = MKPOL([secondStairVerts, secondStairCells, pols])
coloredsecondStair = COLOR([0.859,0.859,0.859])(secondStair)
coloredsecondStair = T(3)(1)(PROD([coloredsecondStair,Q(0.3)]))

#columns basement
columnBasementVerts = [[8.1,8.1],[57.3,8.1],[57.3,39.6],[8.1,39.6]]
columnBasementCells = [[1,2,3,4]]
columnBasement = MKPOL([columnBasementVerts, columnBasementCells, pols])
columnBasement = COLOR([0.922,0.922,0.922])(columnBasement)
columnBasement = T(3)(1.3)(PROD([columnBasement,Q(1)]))

#walls near the stairs
stairsRightWallVerts = [[21.3,39.6],[22.8,39.6],[22.8,44.6],[21.3,44.6]]
stairsRightWallCells = [[1,2,3,4]]
stairsRightWall = MKPOL([stairsRightWallVerts, stairsRightWallCells, pols])
stairsRightWall = COLOR([0.650,0.650,0.650])(stairsRightWall)
stairsRightWall = PROD([stairsRightWall,Q(2.3)])

stairsLeftWallVerts = [[42.5,39.6],[44,39.6],[44,44.6],[42.5,44.6]]
stairsLeftWallCells = [[1,2,3,4]]
stairsLeftWall = MKPOL([stairsLeftWallVerts, stairsLeftWallCells, pols])
stairsLeftWall = COLOR([0.650,0.650,0.650])(stairsLeftWall)
stairsLeftWall = PROD([stairsLeftWall,Q(2.3)])

stairsWall = STRUCT([stairsRightWall,stairsLeftWall])

#stairs
stair1WallVerts = [[21.3,39.6],[44,39.6],[44,40.6],[21.3,40.6]]
stair1WallCells = [[1,2,3,4]]
stair1Wall = MKPOL([stair1WallVerts, stair1WallCells, pols])
stair1Wall = COLOR([0.650,0.650,0.650])(stair1Wall)
stair1Wall = PROD([stair1Wall,Q(2.3)])
stair2WallVerts = [[21.3,40.6],[44,40.6],[44,41.6],[21.3,41.6]]
stair2WallCells = [[1,2,3,4]]
stair2Wall = MKPOL([stair2WallVerts, stair2WallCells, pols])
stair2Wall = COLOR([0.650,0.650,0.650])(stair2Wall)
stair2Wall = PROD([stair2Wall,Q(2)])
stair3WallVerts = [[21.3,41.6],[44,41.6],[44,42.6],[21.3,42.6]]
stair3WallCells = [[1,2,3,4]]
stair3Wall = MKPOL([stair3WallVerts, stair3WallCells, pols])
stair3Wall = COLOR([0.650,0.650,0.650])(stair3Wall)
stair3Wall = PROD([stair3Wall,Q(1.7)])
stair4WallVerts = [[21.3,42.6],[44,42.6],[44,43.6],[21.3,43.6]]
stair4WallCells = [[1,2,3,4]]
stair4Wall = MKPOL([stair4WallVerts, stair4WallCells, pols])
stair4Wall = COLOR([0.650,0.650,0.650])(stair4Wall)
stair4Wall = PROD([stair4Wall,Q(1.4)])
stair5WallVerts = [[21.3,43.6],[44,43.6],[44,44.6],[21.3,44.6]]
stair5WallCells = [[1,2,3,4]]
stair5Wall = MKPOL([stair5WallVerts, stair5WallCells, pols])
stair5Wall = COLOR([0.650,0.650,0.650])(stair5Wall)
stair5Wall = PROD([stair5Wall,Q(1.1)])
stair6WallVerts = [[21.3,44.6],[44,44.6],[44,45.6],[21.3,45.6]]
stair6WallCells = [[1,2,3,4]]
stair6Wall = MKPOL([stair6WallVerts, stair6WallCells, pols])
stair6Wall = COLOR([0.650,0.650,0.650])(stair6Wall)
stair6Wall = PROD([stair6Wall,Q(0.8)])
stair7WallVerts = [[21.3,45.6],[44,45.6],[44,46.6],[21.3,46.6]]
stair7WallCells = [[1,2,3,4]]
stair7Wall = MKPOL([stair7WallVerts, stair7WallCells, pols])
stair7Wall = COLOR([0.650,0.650,0.650])(stair7Wall)
stair7Wall = PROD([stair7Wall,Q(0.5)])
stair8WallVerts = [[21.3,46.6],[44,46.6],[44,47.7],[21.3,47.7]]
stair8WallCells = [[1,2,3,4]]
stair8Wall = MKPOL([stair8WallVerts, stair8WallCells, pols])
stair8Wall = COLOR([0.650,0.650,0.650])(stair8Wall)
stair8Wall = PROD([stair8Wall,Q(0.2)])

stairs = INSR(STRUCT)([stair1Wall,stair2Wall,stair3Wall,stair4Wall,stair5Wall,stair6Wall,stair7Wall,stair8Wall])


basementStruct = INSR(STRUCT)([coloredfirstStair,coloredsecondStair,columnBasement]) 


######################################### COLUMNS AND WALL #########################################
#capitello top
x_topCapitelloRow = QUOTE([2.1,-2.1] * 12)
Y_topCapitelloRow = QUOTE([2.1,-27.3] * 2)
topCapitelloRow = INSR(PROD)([x_topCapitelloRow,Y_topCapitelloRow])
topCapitelloRow = COLOR([0.450,0.450,0.450])(topCapitelloRow)
topCapitelloRow = T(3)(15.5)(PROD([topCapitelloRow,Q(0.2)]))

x_topCapitelloColumn = QUOTE([2.1, -44.1] * 2)
Y_topCapitelloColumn = QUOTE([2.1,-2.1] * 8)
topCapitelloColumn = INSR(PROD)([x_topCapitelloColumn,Y_topCapitelloColumn])
topCapitelloColumn = COLOR([0.450,0.450,0.450])(topCapitelloColumn)
topCapitelloColumn = T(3)(15.5)(PROD([topCapitelloColumn,Q(0.2)]))

x_topCapitelloCouple = QUOTE([-21,2.1,-2.1,2.1])
Y_topCapitelloCouple = QUOTE([-25.2,2.1])
topCapitelloCouple = INSR(PROD)([x_topCapitelloCouple,Y_topCapitelloCouple])
topCapitelloCouple = COLOR([0.450,0.450,0.450])(topCapitelloCouple)
topCapitelloCouple = T(3)(15.5)(PROD([topCapitelloCouple,Q(0.2)]))

topCapitello = INSR(STRUCT)([topCapitelloRow,topCapitelloColumn,topCapitelloCouple])

topCapitello = STRUCT([topCapitello,topCapitelloCouple])
topCapitello = T([1,2])([8.5,8.1])(topCapitello)

#capitello bottom
x_bottomCapitelloRow = QUOTE([1.9,-2.3] * 12)
Y_bottomCapitelloRow = QUOTE([1.9,-27.5] * 2)
bottomCapitelloRow = INSR(PROD)([x_bottomCapitelloRow,Y_bottomCapitelloRow])
bottomCapitelloRow = COLOR([0.816,0.804,0.804])(bottomCapitelloRow)
bottomCapitelloRow = T(3)(15.3)(PROD([bottomCapitelloRow,Q(0.2)]))

x_bottomCapitelloColumn = QUOTE([1.9, -44.3] * 2)
Y_bottomCapitelloColumn = QUOTE([1.9,-2.3] * 8)
bottomCapitelloColumn = INSR(PROD)([x_bottomCapitelloColumn,Y_bottomCapitelloColumn])
bottomCapitelloColumn = COLOR([0.816,0.804,0.804])(bottomCapitelloColumn)
bottomCapitelloColumn = T(3)(15.3)(PROD([bottomCapitelloColumn,Q(0.2)]))

x_bottomCapitelloCouple = QUOTE([-21,1.9,-2.3,1.9])
Y_bottomCapitelloCouple = QUOTE([-25.2,1.9])
bottomCapitelloCouple = INSR(PROD)([x_bottomCapitelloCouple,Y_bottomCapitelloCouple])
bottomCapitelloCouple = COLOR([0.816,0.804,0.804])(bottomCapitelloCouple)
bottomCapitelloCouple = T(3)(15.3)(PROD([bottomCapitelloCouple,Q(0.2)]))

bottomCapitello = INSR(STRUCT)([bottomCapitelloRow,bottomCapitelloColumn,bottomCapitelloCouple])
bottomCapitello = T([1,2])([8.6,8.2])(bottomCapitello)

#columns
def sphere(p): return [0.95*COS(p[0]), 0.95*SIN(p[0])]
def domain(n): return INTERVALS(2*PI)(n)
column = MAP(sphere)(domain(16))
column = JOIN(column)
column = T(3)(2.3)(PROD([column,Q(13)]))

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
wallLeft = T(3)(2.3)(PROD([wallLeft,Q(13.55)]))

wallRightVerts = [[12.7,33.3],[27.3,33.3],[27.3,35.4],[12.7,35.4]]
wallRightCells = [[1,2,3,4]]
wallRight = MKPOL([wallRightVerts, wallRightCells, pols])
wallRight = T(3)(2.3)(PROD([wallRight,Q(13.55)]))

wallBackVerts = [[12.7,12.3],[52.6,12.3],[52.6,14.4],[12.7,14.4]]
wallBackCells = [[1,2,3,4]]
wallBack = MKPOL([wallBackVerts, wallBackCells, pols])
wallBack = T(3)(2.3)(PROD([wallBack,Q(13.55)]))

wallLateralLeftVerts = [[50.5,12.3],[52.6,12.3],[52.6,35.4],[50.5,35.4]]
wallLateralLeftCells = [[1,2,3,4]]
wallLateralLeft = MKPOL([wallLateralLeftVerts, wallLateralLeftCells, pols])
wallLateralLeft = T(3)(2.3)(PROD([wallLateralLeft,Q(13.55)]))

wallLateralRight = T([1])([-37.8])(wallLateralLeft)

internalWall = INSR(STRUCT)([wallLeft,wallRight,wallBack,wallLateralLeft,wallLateralRight])


columnsAndWall = INSR(STRUCT)([topCapitello,bottomCapitello,columns,internalWall,stairs,stairsWall])



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

solid_model_3D = INSR(STRUCT)([basementStruct, columnsAndWall, coverage])
VIEW(solid_model_3D)