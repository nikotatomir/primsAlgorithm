import random
import numpy as np
import sys

from src.utilities import utilities

class townData():

	def __init__(self, N, M, alpha, mapXYmin, mapXYmax, nodeGenerationMethod):
		self.N = N # number of houses
		self.M = M # number of malls
		self.alpha = alpha # variable for weighted edges
		self.mapXYmin = mapXYmin
		self.mapXYmax = mapXYmax
		self.nodeGenerationMethod = nodeGenerationMethod
		
		self.nodes = self.getNodes()
		self.edges = self.getEdges()

	# function generates a node with random coordinates
	@staticmethod
	def generateRandomNode(nodeNumber, nodeType, mapXYmin, mapXYmax,  roundingLimit = 2):
		x = random.uniform(mapXYmin, mapXYmax)
		y = random.uniform(mapXYmin, mapXYmax)
		newNode = (nodeNumber, nodeType, round(x,roundingLimit), round(y,roundingLimit))
		return newNode

	# function generates a node with speficied coordinates
	@staticmethod
	def generateManualNode(nodeNumber, nodeType, xCoordinate, yCoordinate):
		newNode = (nodeNumber, nodeType, xCoordinate, yCoordinate)
		return newNode

	# function checks edge (road) type - 'local' or 'express' between 2 nodes
	@staticmethod
	def getEdgeType(node1type, node2type):
		nodeTypes = [node1type, node2type]
		if ('house' in nodeTypes) and ('center' not in nodeTypes): # any connection with a house must be a local road
			edgeType = 'local'
		elif 'mall' in nodeTypes: # any connection with a mall (given that house is checked), must be a express road
			edgeType = 'express'
		else:
			sys.exit("\n***EXITING PROGRAM***\nError Message: No road connection exist")

		return edgeType # road type

	# function that gets the edge weight depending on the type of road ('local' of 'express' - i.e. alpha coefficient)
	@staticmethod
	def getEdgeWeight(node1type, node1x, node1y, node2type, node2x, node2y, alpha):
		euclidianDistance = utilities.getEuclidianDistance(node1x, node1y, node2x, node2y)
		if townData.getEdgeType(node1type, node2type) == 'local':
			edgeWeight = alpha*euclidianDistance
		elif townData.getEdgeType(node1type, node2type) == 'express':
			edgeWeight = (1-alpha)*euclidianDistance
		else:
			sys.exit("\n***EXITING PROGRAM***\nError Message: getEdgeWeight() function must return 'local' or 'express' (road)")
		return edgeWeight # cost

	# function that create a list of nodes stored in tuples
	def getNodes(self):
		nodes = []
		if self.nodeGenerationMethod == 'random':
			
			for i in range(self.N+self.M):
				if i < self.N: # generate RANDOM coordinates for houses
					newNode = townData.generateRandomNode(i, 'house', self.mapXYmin, self.mapXYmax)
				else: # generate RANDOM coordinates for malls
					newNode = townData.generateRandomNode(i, 'mall', self.mapXYmin, self.mapXYmax)
				nodes.append(newNode)
			
			# generate RANDOM coordinate for center
			newNode = townData.generateRandomNode(self.N+self.M, 'center', self.mapXYmin, self.mapXYmax)
			nodes.append(newNode)

		elif self.nodeGenerationMethod == 'manual':
			coordinates = np.loadtxt('manualCoordinates.txt', delimiter=',', skiprows = 4)
			if self.N+self.M+1 != len(coordinates[:,0]):
				sys.exit("\n***EXITING PROGRAM***\nError Message: Total Number of Nodes Imported Does Not Equal The Number Of Nodes Specified (N+M+1)")
			else:
				for i in range(self.N+self.M):
					if i < self.N: # generate MANUAL coordinates for houses
						newNode = townData.generateManualNode(i, 'house', coordinates[i,0], coordinates[i,1])
					else: # generate MANUAL coordinates for malls
						newNode = townData.generateManualNode(i, 'mall', coordinates[i,0], coordinates[i,1])	
					nodes.append(newNode)

				# generate MANUAL coordinates for center
				newNode = townData.generateManualNode(self.N+self.M, 'center', coordinates[self.N+self.M,0], coordinates[self.N+self.M,1])
				nodes.append(newNode)

		else:
			sys.exit("\n***EXITING PROGRAM***\nError Message: nodeGenerationMethod must be 'random' or 'manual'")

		return nodes

	# function that returns a list of edges stored in tuples
	def getEdges(self):
		edges = []
		counter = 0
		for i in range(self.N+self.M+1): # looping over all houses
			startNodeNumber, startNodeType, startNodeX, startNodeY = [self.nodes[i][k] for k in range(4)]

			#print(f'node {startNodeNumber} ({startNodeType})')
			
			for j in range(self.N+self.M+1): # looping over all houses, but the i-th house is excluded
				if (j == i) or (i<self.N and j == self.N+self.M) or (i == self.M+self.N and j < self.N): 
					# 1st - checks if same node
					# 2nd - checks if house connected to center
					# 3rd - check if center connected to house
					continue
				else:
					endNodeNumber, endNodeType, endNodeX, endNodeY = [self.nodes[j][k] for k in range(4)]

					cost = townData.getEdgeWeight(startNodeType, startNodeX, startNodeY,
										 		  endNodeType, endNodeX, endNodeY,
										 		  self.alpha)

					road = townData.getEdgeType(startNodeType, endNodeType)
					
					newEdge = (startNodeNumber, startNodeType, startNodeX, startNodeY, 
							   endNodeNumber, endNodeType, endNodeX, endNodeY, 
							   cost, road)
					edges.append(newEdge)

					#print(f'\tnode {endNodeNumber} ({endNodeType})')
					
					counter += 1

		return edges




