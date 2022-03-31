import sys
import numpy as np
import matplotlib.pyplot as plt
from src.townData import townData
from src.utilities import utilities

class visualization():

	# class variables
	houseAndLocal = '#a6a6a6'
	mallAndExpress = '#7a0a0a'
	center = 'k'

	def __init__(self, town, getEdgesForSingleNode):
		self.town = town

		if getEdgesForSingleNode <= self.town.M + self.town.N:
			self.getEdgesForSingleNode = getEdgesForSingleNode
		else:
			sys.exit(f"\n***EXITING PROGRAM***\nError Message: getEdgesForSingleNode must be less than or equal to {self.town.N+self.town.M}")

	@staticmethod
	def gridlines():
	    plt.minorticks_on()
	    plt.grid(zorder = 0, which='major', axis='x', linewidth=0.75, linestyle='-', color='0.75')
	    plt.grid(zorder = 0, which='minor', axis='x', linewidth=0.25, linestyle='-', color='0.75')
	    plt.grid(zorder = 0, which='major', axis='y', linewidth=0.75, linestyle='-', color='0.75')
	    plt.grid(zorder = 0, which='minor', axis='y', linewidth=0.25, linestyle='-', color='0.75')

	# function that creates a list of x and y coordinates for the houses, malls and city center
	def getNodesForPlot(self):
		nodesForPlotX = []
		nodesForPlotY = []
		for i in range(self.town.N+self.town.M+1):
			nodesForPlotX.append(self.town.nodes[i][2])
			nodesForPlotY.append(self.town.nodes[i][3])

		return nodesForPlotX, nodesForPlotY

	# function that plots the coordinates of the house, malls and city center
	def plotNodes(self):

		nodesX, nodesY = self.getNodesForPlot()
		# Plotting Houses
		plt.plot(nodesX[0:self.town.N], nodesY[0:self.town.N], 
				 color= visualization.houseAndLocal, linestyle = '', marker = '.', markersize = 5, label='House', zorder = 3)
		# Plotting Malls
		plt.plot(nodesX[self.town.N:self.town.N+self.town.M], nodesY[self.town.N:self.town.N+self.town.M], 
				 color= visualization.mallAndExpress, linestyle = '', marker = '.', markersize = 10, label='Mall', zorder = 3)
		# Plotting Center
		plt.plot(nodesX[self.town.N+self.town.M], nodesY[self.town.N+self.town.M], 
				 color= visualization.center, linestyle = '', marker = '.', markersize = 7.5, label='Center', zorder=3)

		# Numbering The Nodes
		for i in range(self.town.N+self.town.M+1):
			plt.text(nodesX[i] + 0.05, nodesY[i] + 0.05, i)

	# function that returns a list of all the possible edges (roads) for a specific node given by the self.getEdgesForSingleNode variable
	def getEdgesForPlot(self):
		edgesForPlot = []
		indices = utilities.getEdgeIndices(self.getEdgesForSingleNode, self.town.edges)
		for index in indices:
			edgesForPlot.append(self.town.edges[index])
		return edgesForPlot

	# function that plots either (1. or 2.)
	# 1. all edges (roads) for single node specificed by the self.getEdgesForSingleNode variable
	# 2. all edges (roads) that compose the road network (i.e. the minimum spanning tree)
	def plotEdges(self, edgesMST = []):
		if edgesMST:
			edgesForPlot = edgesMST
		else:
			edgesForPlot = self.getEdgesForPlot()

		localCounter = 0
		expressCounter = 0
		for i in range(len(edgesForPlot)):
			x1, y1, x2, y2 = edgesForPlot[i][2], edgesForPlot[i][3], edgesForPlot[i][6], edgesForPlot[i][7]
			cost = edgesForPlot[i][-2]
			plt.text(x1+0.75*(x2-x1), y1+0.75*(y2-y1), round(cost,2), fontsize=5)
			if 'local' in edgesForPlot[i]:
				if localCounter == 0:
					plt.plot([x1, x2], [y1, y2], color= visualization.houseAndLocal, linestyle = '-', linewidth=0.75, zorder = 2, label = 'Local Road')
				else:
					plt.plot([x1, x2], [y1, y2], color= visualization.houseAndLocal, linestyle = '-', linewidth=0.75, zorder = 2)
				localCounter += 1
			elif 'express' in edgesForPlot[i]:
				if expressCounter == 0:
					plt.plot([x1, x2], [y1, y2], color= visualization.mallAndExpress, linestyle = '-', linewidth=0.75, zorder = 2, label = 'Express Road')
				else:
					plt.plot([x1, x2], [y1, y2], color= visualization.mallAndExpress, linestyle = '-', linewidth=0.75, zorder = 2)
				expressCounter += 1
			else:
				pass

	# function that creates the initial town map image using self.plotNodes()
	def plotInitialTownMap(self):
		plt.figure(1, figsize=(6.0,6.0))
		
		# Add 2D grid
		visualization.gridlines()
		# Plot Nodes (House, Malls, Center)
		self.plotNodes()

		plt.xlabel('X')
		plt.ylabel('Y')
		plt.title(f'Town Map ({self.town.nodeGenerationMethod.capitalize()} Input)')
		plt.xlim([0,self.town.mapXYmax+int(0.25*self.town.mapXYmax)])
		plt.ylim([0,self.town.mapXYmax+int(0.25*self.town.mapXYmax)])
		plt.legend(loc = 'upper center', ncol=3)
		plt.savefig('initialTownMap.png', bbox_inches='tight', dpi=250)

	# function that creates the image where all the edges for a single node are visualized
	def plotEdgesForNode(self):
		plt.figure(2, figsize=(6.0,6.0))
		# Add 2D grid
		visualization.gridlines()
		# Plot Nodes (House, Malls, Center)
		self.plotNodes()
		# Plot Edges For Single Node
		self.plotEdges()

		plt.xlabel('X')
		plt.ylabel('Y')
		plt.title(f'Town Map Edges For Node {self.getEdgesForSingleNode}')
		plt.xlim([0,self.town.mapXYmax+int(0.25*self.town.mapXYmax)])
		plt.ylim([0,self.town.mapXYmax+int(0.25*self.town.mapXYmax)])
		plt.legend(loc = 'upper center', ncol=2)
		plt.savefig('initialTownMapEdges.png', bbox_inches='tight', dpi=250)

	# function that create the final town map image with the complete road network (i.e. minimum spanning tree)
	def plotFinalTownMap(self, solution, startNodeNumber, alpha):
		plt.figure(3, figsize=(6.0,6.0))
		
		# Add 2D grid
		visualization.gridlines()
		# Plot Nodes (House, Malls, Center)
		self.plotNodes()
		self.plotEdges(solution.edgesMST)

		plt.xlabel('X')
		plt.ylabel('Y')
		plt.title(f'Final Town Map ({self.town.nodeGenerationMethod.capitalize()} Input) $\\rightarrow$ Total Cost = {round(solution.totalCost,2)}')
		plt.xlim([0,self.town.mapXYmax+int(0.25*self.town.mapXYmax)])
		plt.ylim([0,self.town.mapXYmax+int(0.25*self.town.mapXYmax)])
		plt.legend(loc = 'upper center', ncol=2)
		plt.savefig(f'finalTownMap_alpha{alpha}.png', bbox_inches='tight', dpi=250)
