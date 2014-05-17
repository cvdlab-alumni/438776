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

def mapBlocks(diagram,cellsToRemove):
	#"diagram" is the 3-array of blocks to map 
	def mapBlocks0(master,blocks,diagram=diagram):
		#"blocks" is the list of master's blocks where to map diagram
		sortedBlocks = sorted(blocks, reverse=True)
		#reverse sort is used to avoid the renumbering of destination blocks, in fact, when
		#a diagram is mapped into a block, numbers for all subsequent blocks change

		V,CV = diagram
		diagram = V,[cell for k,cell in enumerate(CV) if not (k in cellsToRemove)]

		for block in sortedBlocks:
			master = diagram2cell(diagram,master,block)

		return master
	return mapBlocks0

###################################### Test ######################################

master = assemblyDiagramInit([5,5,2])([[.3,3.2,.1,5,.3],[.3,4,.1,2.9,.3],[.3,2.7]])
V,CV = master
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(CV)),CYAN,2)
VIEW(hpc)

diagram = assemblyDiagramInit([3,1,2])([[2,1,2],[.3],[2.2,.5]])
V,CV = diagram
hpc = SKEL_1(STRUCT(MKPOLS(diagram)))
hpc = cellNumbering (diagram,hpc)(range(len(CV)),CYAN,2)
VIEW(hpc)

master = mapBlocks(diagram,[2])(master,[31,39])

hpc = STRUCT(MKPOLS(master))
VIEW(hpc)