from pyplasm import *

######################################### NORD #########################################
#first level (garden)
gardenNORDVerts = [[0,0,0],[65.4,0,0],[65.4,0,3.75],[0,0,3.75]]
gardenNORDCells = [[1,2,3,4]]
pols = None
gardenNORD = MKPOL([gardenNORDVerts, gardenNORDCells, pols])
coloredgardenNORD = COLOR(WHITE)(gardenNORD)

#second level (first stair)
firstStairNORDVerts = [[6.1,0,3.75],[59.3,0,3.75],[59.3,0,4.75],[6.1,0,4.75]]
firstStairNORDCells = [[1,2,3,4]]
firstStairNORD = MKPOL([firstStairNORDVerts, firstStairNORDCells, pols])
coloredfirstStairNORD = COLOR([0.816,0.804,0.804])(firstStairNORD)

#third level (second stair)
secondStairVerts = [[7.1,0,4.75],[58.3,0,4.75],[58.3,0,5.05],[7.1,0,5.05]]
secondStairCells = [[1,2,3,4]]
secondStair = MKPOL([secondStairVerts, secondStairCells, pols])
coloredsecondStair = COLOR([0.859,0.859,0.859])(secondStair)

#fourth level (columns basement)
columnBasementVerts = [[8.1,0,5.05],[57.3,0,5.05],[57.3,0,6.05],[8.1,0,6.05]]
columnBasementCells = [[1,2,3,4]]
columnBasement = MKPOL([columnBasementVerts, columnBasementCells, pols])
columnBasement = COLOR([0.922,0.922,0.922])(columnBasement)

#capitello top
topCapitelloNORDVerts = [[8.3,0,19.25],[10.4,0,19.25],[10.4,0,19.45],[8.3,0,19.45]]
topCapitelloNORDCells = [[1,2,3,4]]
topCapitelloNORD = MKPOL([topCapitelloNORDVerts, topCapitelloNORDCells, pols])
topCapitelloNORD = COLOR([0.350,0.350,0.350])(topCapitelloNORD)
topCapitelloNORD = STRUCT([topCapitelloNORD, T(1)(4.2)] * 12)

#capitello bottom
bottomCapitelloNORDVerts = [[8.4,0,19.05],[10.3,0,19.05],[10.3,0,19.25],[8.4,0,19.25]]
bottomCapitelloNORDCells = [[1,2,3,4]]
bottomCapitelloNORD = MKPOL([bottomCapitelloNORDVerts, bottomCapitelloNORDCells, pols])
bottomCapitelloNORD = COLOR([0.816,0.804,0.804])(bottomCapitelloNORD)
bottomCapitelloNORD = STRUCT([bottomCapitelloNORD, T(1)(4.2)] * 12)

#columns
columnsVerts = [[8.4,0,6.05],[10.3,0,6.05],[10.3,0,19.05],[8.4,0,19.05]]
columnsCells = [[1,2,3,4]]
columns = MKPOL([columnsVerts, columnsCells, pols])
columns = COLOR(WHITE)(columns)
columns = STRUCT([columns, T(1)(4.2)] * 12)

#internal wall
wallNORDVerts = [[12.7,0,6.05],[52.6,0,6.05],[52.6,0,19.45],[12.7,0,19.45]]
wallNORDCells = [[1,2,3,4]]
wallNORD = MKPOL([wallNORDVerts, wallNORDCells, pols])
wallNORD = COLOR([0.550,0.550,0.550])(wallNORD)

#floor1 basement
basementNORDVerts = [[8.1,0,19.45],[57.3,0,19.45],[57.3,0,22.35],[8.1,0,22.35]]
basementNORDCells = [[1,2,3,4]]
basementNORD = MKPOL([basementNORDVerts, basementNORDCells, pols])
basementNORD = COLOR([0.859,0.859,0.859])(basementNORD)

#floor1 basement top
basementTopNORDVerts = [[7.1,0,22.35],[58.3,0,22.35],[58.3,0,23.95],[7.1,0,23.95]]
basementTopNORDCells = [[1,2,3,4]]
basementTopNORD = MKPOL([basementTopNORDVerts, basementTopNORDCells, pols])
basementTopNORD = COLOR([0.750,0.750,0.750])(basementTopNORD)

#roof
roofNORDVerts = [[12.55,0,23.95],[52.85,0,23.95],[52.85,0,28.95],[12.55,0,28.95]]
roofNORDCells = [[1,2,3,4]]
roofNORD = MKPOL([roofNORDVerts, roofNORDCells, pols])
roofNORD = COLOR([0.600,0.600,0.600])(roofNORD)

#roof top
roofTopNORDVerts = [[11.55,0,28.95],[53.85,0,28.95],[53.85,0,30.65],[11.55,0,30.65]]
roofTopNORDCells = [[1,2,3,4]]
roofTopNORD = MKPOL([roofTopNORDVerts, roofTopNORDCells, pols])
roofTopNORD = COLOR(WHITE)(roofTopNORD)


NORD = INSR(STRUCT)([coloredgardenNORD,coloredfirstStairNORD,coloredsecondStair,columnBasement,topCapitelloNORD,bottomCapitelloNORD,columns,wallNORD,basementNORD,basementTopNORD,roofNORD,roofTopNORD])


######################################### OVEST #########################################
#first level (garden)
gardenOVESTVerts = [[65.4,0,0],[65.4,0,3.75],[65.4,47.7,0],[65.4,47.7,3.75]]
gardenOVESTCells = [[1,2,3,4]]
gardenOVEST = MKPOL([gardenOVESTVerts, gardenOVESTCells, pols])
gardenOVEST = COLOR(WHITE)(gardenOVEST)

#second level (first stair)
firstStairOVESTVerts = [[65.4,6.1,3.75],[65.4,6.1,4.75],[65.4,41.6,3.75],[65.4,41.6,4.75]]
firstStairOVESTCells = [[1,2,3,4]]
firstStairOVEST = MKPOL([firstStairOVESTVerts, firstStairOVESTCells, pols])
firstStairOVEST = COLOR([0.816,0.804,0.804])(firstStairOVEST)

#third level (second stair)
secondStairOVESTVerts = [[65.4,7.1,4.75],[65.4,7.1,5.05],[65.4,40.6,4.75],[65.4,40.6,5.05]]
secondStairOVESTCells = [[1,2,3,4]]
secondStairOVEST = MKPOL([secondStairOVESTVerts, secondStairOVESTCells, pols])
secondStairOVEST = COLOR([0.859,0.859,0.859])(secondStairOVEST)

#fourth level (columns basement)
columnBasementOVESTVerts = [[65.4,8.1,5.05],[65.4,8.1,6.05],[65.4,39.6,5.05],[65.4,39.6,6.05]]
columnBasementOVESTCells = [[1,2,3,4]]
columnBasementOVEST = MKPOL([columnBasementOVESTVerts, columnBasementOVESTCells, pols])
columnBasementOVEST = COLOR([0.922,0.922,0.922])(columnBasementOVEST)

#capitello top
topCapitelloOVESTVerts = [[65.4,8.3,19.25],[65.4,10.4,19.25],[65.4,10.4,19.45],[65.4,8.3,19.45]]
topCapitelloOVESTCells = [[1,2,3,4]]
topCapitelloOVEST = MKPOL([topCapitelloOVESTVerts, topCapitelloOVESTCells, pols])
topCapitelloOVEST = COLOR([0.350,0.350,0.350])(topCapitelloOVEST)
topCapitelloOVEST = STRUCT([topCapitelloOVEST, T(2)(4.2)] * 8)

#capitello bottom
bottomCapitelloOVESTVerts = [[65.4,8.4,19.05],[65.4,10.3,19.05],[65.4,10.3,19.25],[65.4,8.4,19.25]]
bottomCapitelloOVESTCells = [[1,2,3,4]]
bottomCapitelloOVEST = MKPOL([bottomCapitelloOVESTVerts, bottomCapitelloOVESTCells, pols])
bottomCapitelloOVEST = COLOR([0.816,0.804,0.804])(bottomCapitelloOVEST)
bottomCapitelloOVEST = STRUCT([bottomCapitelloOVEST, T(2)(4.2)] * 8)

#columns
columnsOVESTVerts = [[65.4,8.4,6.05],[65.4,10.3,6.05],[65.4,10.3,19.05],[65.4,8.4,19.05]]
columnsOVESTCells = [[1,2,3,4]]
columnsOVEST = MKPOL([columnsOVESTVerts, columnsOVESTCells, pols])
columnsOVEST = COLOR(WHITE)(columnsOVEST)
columnsOVEST = STRUCT([columnsOVEST, T(2)(4.2)] * 8)

#internal wall
wallOVESTVerts = [[65.4,12.3,6.05],[65.4,35.4,6.05],[65.4,35.4,19.45],[65.4,12.3,19.45]]
wallOVESTCells = [[1,2,3,4]]
wallOVEST = MKPOL([wallOVESTVerts, wallOVESTCells, pols])
wallOVEST = COLOR([0.550,0.550,0.550])(wallOVEST)

#floor1 basement
basementOVESTVerts = [[65.4,8.1,19.45],[65.4,40.5,19.45],[65.4,40.5,22.35],[65.4,8.1,22.35]]
basementOVESTCells = [[1,2,3,4]]
basementOVEST = MKPOL([basementOVESTVerts, basementOVESTCells, pols])
basementOVEST = COLOR([0.859,0.859,0.859])(basementOVEST)

#floor1 basement top
basementTopOVESTVerts = [[65.4,7.1,22.35],[65.4,41.5,22.35],[65.4,41.5,23.95],[65.4,7.1,23.95]]
basementTopOVESTCells = [[1,2,3,4]]
basementTopOVEST = MKPOL([basementTopOVESTVerts, basementTopOVESTCells, pols])
basementTopOVEST = COLOR([0.750,0.750,0.750])(basementTopOVEST)

#roof
roofOVESTVerts = [[65.4,12.55,23.95],[65.4,36.05,23.95],[65.4,36.05,28.95],[65.4,12.55,28.95]]
roofOVESTCells = [[1,2,3,4]]
roofOVEST = MKPOL([roofOVESTVerts, roofOVESTCells, pols])
roofOVEST = COLOR([0.600,0.600,0.600])(roofOVEST)

#roof top
roofOVESTTopVerts = [[65.4,11.5,28.95],[65.4,37.05,28.95],[65.4,37.05,30.65],[65.4,11.55,30.65]]
roofOVESTTopCells = [[1,2,3,4]]
roofOVESTTop = MKPOL([roofOVESTTopVerts, roofOVESTTopCells, pols])
roofOVESTTop = COLOR(WHITE)(roofOVESTTop)

OVEST = INSR(STRUCT)([gardenOVEST,firstStairOVEST,secondStairOVEST,columnBasementOVEST,topCapitelloOVEST,bottomCapitelloOVEST,columnsOVEST,wallOVEST,basementOVEST,basementTopOVEST,roofOVEST,roofOVESTTop])


######################################### EST #########################################

EST = T([1,2])([-65.4,-47.7])(OVEST)
EST = ROTATE([1,2])(PI)(EST)


######################################### SUD #########################################

SUD = INSR(STRUCT)([coloredgardenNORD,coloredfirstStairNORD,coloredsecondStair,columnBasement,topCapitelloNORD,bottomCapitelloNORD,columns,basementNORD,basementTopNORD,roofNORD,roofTopNORD])
SUD = ROTATE([1,2])(PI)(SUD)
SUD = T([1,2])([65.4,47.7])(SUD)

#internal wall
wallLeftVerts = [[52.6,47.7,6.05],[52.6,47.7,19.45],[37.9,47.7,6.05],[37.9,47.7,19.45]]
wallLeftCells = [[1,2,3,4]]
wallLeft = MKPOL([wallLeftVerts, wallLeftCells, pols])
wallLeft = COLOR([0.550,0.550,0.550])(wallLeft)

wallRightVerts = [[27.3,47.7,6.05],[27.3,47.7,19.45],[12.7,47.7,6.05],[12.7,47.7,19.45]]
wallRightCells = [[1,2,3,4]]
wallRight = MKPOL([wallRightVerts, wallRightCells, pols])
wallRight = COLOR([0.550,0.550,0.550])(wallRight)

#statue basement
statueBasamentVerts = [[28.5,47.7,6.05],[37,47.7,6.05],[37,47.7,9.05],[28.5,47.7,9.05]]
statueBasamentCells = [[1,2,3,4]]
statueBasament = MKPOL([statueBasamentVerts, statueBasamentCells, pols])
statueBasament = COLOR([0.922,0.922,0.922])(statueBasament)

#walls near the stairs
stairsRightWallVerts = [[22.8,47.7,0],[22.8,47.7,6.05],[21.3,47.7,0],[21.3,47.7,6.05]]
stairsRightWallCells = [[1,2,3,4]]
stairsRightWall = MKPOL([stairsRightWallVerts, stairsRightWallCells, pols])
stairsRightWall = COLOR([0.650,0.650,0.650])(stairsRightWall)

stairsLeftWallVerts = [[44,47.7,0],[44,47.7,6.05],[42.5,47.7,0],[42.5,47.7,6.05]]
stairsLeftWallCells = [[1,2,3,4]]
stairsLeftWall = MKPOL([stairsLeftWallVerts, stairsLeftWallCells, pols])
stairsLeftWall = COLOR([0.650,0.650,0.650])(stairsLeftWall)

stairsWall = STRUCT([stairsRightWall,stairsLeftWall])


SUD = INSR(STRUCT)([SUD,wallLeft,wallRight,statueBasament,stairsRightWall,stairsLeftWall])




####################### CODICE DELL'ESERCIZIO 1 ############################

#from pyplasm import *

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

#roof top
roofTopVerts = [[11.55,11.55],[53.85,11.55],[53.85,36.15],[11.55,36.15]]
roofTopCells = [[1,2,3,4]]
roofTop = MKPOL([roofTopVerts, roofTopCells, pols])
roofTop = COLOR(WHITE)(roofTop)


floor1 = INSR(STRUCT)([basementTop,roof,basement,roofTop])

floor1 = INSR(STRUCT)([basementTop, roof,basement])
floor1 = T(3)(18.6)(floor1)

two_and_half_model = STRUCT([floor0,floor1])
#VIEW(two_and_half_model)


######################### FINE CODICE ESERCIZIO 1 #########################################

two_and_half_model = T(3)(3.75)(two_and_half_model)
mock_up_3D = INSR(STRUCT)([NORD,OVEST,EST,SUD,two_and_half_model])
VIEW(mock_up_3D)