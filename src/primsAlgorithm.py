from src.utilities import utilities
import sys

class primsAlgorithm():

	def __init__(self, N, M, startNodeNumber, townEdges):
		
		self.N = N
		self.M = M
		
		if startNodeNumber <= self.M + self.N:
			self.startNodeNumber = startNodeNumber
		else:
			sys.exit(f"\n***EXITING PROGRAM***\nError Message: startNodeNumber must be less than or equal to {self.N+self.M}")
		
		self.townEdges = townEdges

		self.edgesMST = self.getEdgesMST()
		self.totalLocalRoadLength = self.getTotalLocalRoadLength()
		self.totalExpressRoadLength = self.getTotalExpressRoadLength()
		self.totalCost = self.getTotalCost()

	# getEdgesMST is the function that implements the Prims algorithm and returns the edges that compose the minimum spanning tree
	def getEdgesMST(self):
		totalNumberOfNodes = self.N + self.M + 1
		totalNumberOfEdgesMST = totalNumberOfNodes -1
		edgeCount = 0
		# list that keeps track of which nodes have been visited
		nodesVisited = [True if i == self.startNodeNumber else False for i in range(totalNumberOfNodes)]
		edgesMST, priorityQueue = [], [] # MST edges, priority que

		# extract edges for specific node
		extractedEdges = utilities.extractEdges(self.startNodeNumber, self.townEdges, nodesVisited)
		# appending extracted edges for this specific node to priority que
		for edge in extractedEdges:
			priorityQueue.append(edge)
		
		# prims algorithm
		while len(priorityQueue) != 0 and edgeCount != totalNumberOfEdgesMST:
			# get the edge index of node with the minimum weight in priority queue
			index = utilities.getMinEdgeWeightIndex(priorityQueue)
			# get current node number
			currentNode = priorityQueue[index][0]
			# get which nodes this edge points to
			nextNode = priorityQueue[index][4] 

			# check if this node is visited, if yes then delete, if not, carry on
			if nodesVisited[nextNode]:
				priorityQueue.pop(index)
				continue

			# add the edges result to edgesMST list
			edgesMST.append(priorityQueue[index])
			# remove edge from priority que
			priorityQueue.pop(index)
			# update the edge count
			edgeCount += 1
			# update the fact that the next node is visited
			nodesVisited[nextNode] = True

			# extract edges for specific node
			extractedEdges = utilities.extractEdges(nextNode, self.townEdges, nodesVisited)
			# appending extracted edges for this specific node to priority que
			for edge in extractedEdges:
				priorityQueue.append(edge)

		return edgesMST

	# function that returns the total weighted cost of the road network (minimum spanning tree)
	def getTotalCost(self):
		totalCost = 0
		for edge in self.edgesMST:
			totalCost += edge[-2]
		return totalCost

	# function that returns the total length of all local roads
	def getTotalLocalRoadLength(self):
		totalLocalRoadLength = 0
		for edge in self.edgesMST:
			if edge[-1] == 'local':
				node1x, node1y, node2x, node2y = edge[2], edge[3], edge[6], edge[7]
				totalLocalRoadLength += utilities.getEuclidianDistance(node1x, node1y, node2x, node2y)
			else:
				pass
		return totalLocalRoadLength

	# function that retuns the total length of all express roads
	def getTotalExpressRoadLength(self):
		totalexpressRoadLength = 0
		for edge in self.edgesMST:
			if edge[-1] == 'express':
				node1x, node1y, node2x, node2y = edge[2], edge[3], edge[6], edge[7]
				totalexpressRoadLength += utilities.getEuclidianDistance(node1x, node1y, node2x, node2y)
			else:
				pass
		return totalexpressRoadLength
