from pyplasm import *

######################################### FIRST FLOOR #########################################
#first level (garden)
gardenVerts = [[0,0],[65.4,0],[65.4,47.7],[0,47.7]]
gardenCells = [[1,2,3,4]]
pols = None
garden = MKPOL([gardenVerts, gardenCells, pols])
coloredGarden = COLOR([0.133,0.384,0.055])(garden)

#second level (first stair)
firstStairVerts = [[6.1,6.1],[59.3,6.1],[59.3,41.6],[6.1,41.6]]
firstStairCells = [[1,2,3,4]]
firstStair = MKPOL([firstStairVerts, firstStairCells, pols])
coloredfirstStair = COLOR([0.816,0.804,0.804])(firstStair)

#third level (second stair)
secondStairVerts = [[7.1,7.1],[58.3,7.1],[58.3,40.6],[7.1,40.6]]
secondStairCells = [[1,2,3,4]]
secondStair = MKPOL([secondStairVerts, secondStairCells, pols])
coloredsecondStair = COLOR([0.859,0.859,0.859])(secondStair)

#fourth level (columns basement)
columnBasementVerts = [[8.1,8.1],[57.3,8.1],[57.3,39.6],[8.1,39.6]]
columnBasementCells = [[1,2,3,4]]
columnBasement = MKPOL([columnBasementVerts, columnBasementCells, pols])
columnBasement = COLOR([0.922,0.922,0.922])(columnBasement)

#capitello top
x_topCapitelloRow = QUOTE([2.1,-2.1] * 12)
Y_topCapitelloRow = QUOTE([2.1,-27.3] * 2)
topCapitelloRow = INSR(PROD)([x_topCapitelloRow,Y_topCapitelloRow])
topCapitelloRow = COLOR([0.450,0.450,0.450])(topCapitelloRow)

x_topCapitelloColumn = QUOTE([2.1, -44.1] * 2)
Y_topCapitelloColumn = QUOTE([2.1,-2.1] * 8)
topCapitelloColumn = INSR(PROD)([x_topCapitelloColumn,Y_topCapitelloColumn])
topCapitelloColumn = COLOR([0.450,0.450,0.450])(topCapitelloColumn)

x_topCapitelloCouple = QUOTE([-21,2.1,-2.1,2.1])
Y_topCapitelloCouple = QUOTE([-25.2,2.1])
topCapitelloCouple = INSR(PROD)([x_topCapitelloCouple,Y_topCapitelloCouple])
topCapitelloCouple = COLOR([0.450,0.450,0.450])(topCapitelloCouple)

topCapitello = INSR(STRUCT)([topCapitelloRow,topCapitelloColumn,topCapitelloCouple])

topCapitello = STRUCT([topCapitello,topCapitelloCouple])
topCapitello = T([1,2])([8.5,8.1])(topCapitello)

#capitello bottom
x_bottomCapitelloRow = QUOTE([1.9,-2.3] * 12)
Y_bottomCapitelloRow = QUOTE([1.9,-27.5] * 2)
bottomCapitelloRow = INSR(PROD)([x_bottomCapitelloRow,Y_bottomCapitelloRow])
bottomCapitelloRow = COLOR([0.816,0.804,0.804])(bottomCapitelloRow)

x_bottomCapitelloColumn = QUOTE([1.9, -44.3] * 2)
Y_bottomCapitelloColumn = QUOTE([1.9,-2.3] * 8)
bottomCapitelloColumn = INSR(PROD)([x_bottomCapitelloColumn,Y_bottomCapitelloColumn])
bottomCapitelloColumn = COLOR([0.816,0.804,0.804])(bottomCapitelloColumn)

x_bottomCapitelloCouple = QUOTE([-21,1.9,-2.3,1.9])
Y_bottomCapitelloCouple = QUOTE([-25.2,1.9])
bottomCapitelloCouple = INSR(PROD)([x_bottomCapitelloCouple,Y_bottomCapitelloCouple])
bottomCapitelloCouple = COLOR([0.816,0.804,0.804])(bottomCapitelloCouple)

bottomCapitello = INSR(STRUCT)([bottomCapitelloRow,bottomCapitelloColumn,bottomCapitelloCouple])
bottomCapitello = T([1,2])([8.6,8.2])(bottomCapitello)

#columns
def sphere(p): return [0.95*COS(p[0]), 0.95*SIN(p[0])]
def domain(n): return INTERVALS(2*PI)(n)
column = MAP(sphere)(domain(16))
column = JOIN(column)

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

wallRightVerts = [[12.7,33.3],[27.3,33.3],[27.3,35.4],[12.7,35.4]]
wallRightCells = [[1,2,3,4]]
wallRight = MKPOL([wallRightVerts, wallRightCells, pols])

wallBackVerts = [[12.7,12.3],[52.6,12.3],[52.6,14.4],[12.7,14.4]]
wallBackCells = [[1,2,3,4]]
wallBack = MKPOL([wallBackVerts, wallBackCells, pols])

wallLateralLeftVerts = [[50.5,12.3],[52.6,12.3],[52.6,35.4],[50.5,35.4]]
wallLateralLeftCells = [[1,2,3,4]]
wallLateralLeft = MKPOL([wallLateralLeftVerts, wallLateralLeftCells, pols])

wallLateralRight = T([1])([-37.8])(wallLateralLeft)

internalWall = INSR(STRUCT)([wallLeft,wallRight,wallBack,wallLateralLeft,wallLateralRight])

#statue basement
statueBasamentVerts = [[28.1,14.4],[36.5,14.4],[36.5,22.8],[28.1,22.8]]
statueBasamentCells = [[1,2,3,4]]
statueBasament = MKPOL([statueBasamentVerts, statueBasamentCells, pols])
statueBasament = COLOR([0.922,0.922,0.922])(statueBasament)

#walls near the stairs
stairsRightWallVerts = [[21.3,39.6],[22.8,39.6],[22.8,44.6],[21.3,44.6]]
stairsRightWallCells = [[1,2,3,4]]
stairsRightWall = MKPOL([stairsRightWallVerts, stairsRightWallCells, pols])
stairsRightWall = COLOR([0.650,0.650,0.650])(stairsRightWall)

stairsLeftWallVerts = [[42.5,39.6],[44,39.6],[44,44.6],[42.5,44.6]]
stairsLeftWallCells = [[1,2,3,4]]
stairsLeftWall = MKPOL([stairsLeftWallVerts, stairsLeftWallCells, pols])
stairsLeftWall = COLOR([0.650,0.650,0.650])(stairsLeftWall)

stairsWall = STRUCT([stairsRightWall,stairsLeftWall])



floor0 = INSR(STRUCT)([coloredGarden,coloredfirstStair,coloredsecondStair,columnBasement,topCapitello,bottomCapitello,columns,internalWall,statueBasament,stairsWall])


######################################### SECOND FLOOR #########################################
#basement
basementVerts = [[8.1,8.1],[57.3,8.1],[57.3,39.6],[8.1,39.6]]
basementCells = [[1,2,3,4]]
basement = MKPOL([basementVerts, basementCells, pols])
basement = COLOR([0.922,0.922,0.922])(basement)

#basement top
basementTopVerts = [[7.1,7.1],[58.3,7.1],[58.3,40.6],[7.1,40.6]]
basementTopCells = [[1,2,3,4]]
basementTop = MKPOL([basementTopVerts, basementTopCells, pols])
basementTop = COLOR([0.800,0.800,0.800])(basementTop)

#roof
roofVerts = [[12.55,12.55],[52.85,12.55],[52.85,35.15],[12.55,35.15]]
roofCells = [[1,2,3,4]]
roof = MKPOL([roofVerts, roofCells, pols])
roof = COLOR(WHITE)(roof)



floor1 = INSR(STRUCT)([basementTop, roof,basement])
floor1 = T(3)(18.6)(floor1)

two_and_half_model = STRUCT([floor0,floor1])
VIEW(two_and_half_model)