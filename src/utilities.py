import numpy as np

class utilities():

	def __init__(self):
		pass

	# function that calculates the euclidian distance between two points
	@staticmethod
	def getEuclidianDistance(x1, y1, x2, y2):
		deltaX = x1 - x2
		deltaY = y1 - y2
		vector = np.array([deltaX,deltaY])
		euclidianDistance = np.linalg.norm(vector)
		return euclidianDistance

	# function that gets all the edges in a list (by index) that connect to a specific node
	@staticmethod
	def getEdgeIndices(nodeNumber, edges):
		edgeIndices = []
		for i in range(len(edges)):
			currentNode = edges[i][0]
			if currentNode == nodeNumber:
				edgeIndices.append(i) 
			else:
				pass
		return edgeIndices

	# function that gets the index of the minimum edge weight of a list of edges (use for priority queue)
	@staticmethod
	def getMinEdgeWeightIndex(edges):
		edgeWeights = [edges[i][-2] for i in range(len(edges))] 
		minEdgeWeightValue = min(edgeWeights)
		minEdgeWeightIndex = edgeWeights.index(minEdgeWeightValue)
		return minEdgeWeightIndex

	# function that extracts all the edges connected to the current node (does not take into account already visited nodes) for priority que
	@staticmethod
	def extractEdges(nodeNumber, edges, nodesVisited):
		extractedEdges = []
		edgeIndices = utilities.getEdgeIndices(nodeNumber, edges)
		for edgeIndex in edgeIndices:
			nextNode = edges[edgeIndex][4]
			# check if next node is already visited
			if nodesVisited[nextNode] != True:
				extractedEdges.append(edges[edgeIndex])
			else:
				pass
		return extractedEdges