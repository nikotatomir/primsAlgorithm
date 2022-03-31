from src.townData import townData
from src.visualization import visualization
from src.primsAlgorithm import primsAlgorithm

# USER DEFINED PROPERTIES
N = 8 # 8 number of houses
M = 5 # 5 number of malls
alpha = 0.5 # weight for edges
mapXYmin = 0 # lower bounding of town, used for random node generation and for axis limits in plots
mapXYmax = 10 # upper bounding of town, used for random node generation and for axis limits in plots
nodeGenerationMethod = 'manual' # 'random' or 'manual'
getEdgesForSingleNode = 10 # choose node for which all possible edges are shown in plot
startNodeNumber = 1 # from which node to start constructing MST

# initialize townData class, gather data on all possible roads (edges)
town = townData(N, M, alpha, mapXYmin, mapXYmax, nodeGenerationMethod)

# initilize the visualization class
visualize = visualization(town, getEdgesForSingleNode)
# plot initial town map without road network
visualize.plotInitialTownMap()
# plot all possible edges for a given node (specified by variable getEdgesForSingleNode) 
visualize.plotEdgesForNode()

# initialize the primsAlgorithm get edges composing the road network (minimum spanning tree)
solution = primsAlgorithm(N,M,startNodeNumber, town.edges)

# print total cost to screen
print('Cost =', round(solution.totalCost,2))
# print total local road length to screen
print('Total Local Road Length =', round(solution.totalLocalRoadLength,2))
# print total express road length to screen
print('Total Express Road Length =', round(solution.totalExpressRoadLength,2))
# plot final town map with optimized road network
visualize.plotFinalTownMap(solution, startNodeNumber, alpha)