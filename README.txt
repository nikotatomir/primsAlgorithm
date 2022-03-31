This python code implements Prims Algorithm to optimize town road networks (minimum spanning tree problem).

The town consists of a single city center, houses and malls with no road network.
The aim is to build a road network that connects all the houses, malls & city center while minimizing the total road network costs.

There are two types of roads:
	1. 'local' roads connect houses to houses & houses to malls
	2. 'express' roads connect malls to malls & the single city center to malls

The road network cost is given by the following equation:
	cost = alpha*total_length_local + (1-alpha)*total_length_express, where alpha is a coefficient between 0 and 1. 
	
	Notice that when alpha=0.5, the cost of the local and express roads are equal and the algorithm will favour the roads that are the shortest. 
	When alpha=0, the local roads are free and the algorithm will favour the local roads. 
	When alpha=1, the express roads are free and the algorithm will favour the express roads. 
	
The sampleResults/ folder gives the optimized road network (minimum spanning tree) for
alpha in range [0, 0.25, 0.5, 0.75, 1]. The images are titled:

	1. finalTownMap_alpha0.png
	2. finalTownMap_alpha0.25.png
	3. finalTownMap_alpha0.5.png
	4. finalTownMap_alpha0.75.png
	5. finalTownMap_alpha1.png

Note that to obtain these images, you need to change the alpha in the run.py file and run the code for each case. 
In addition, when running the run.py file, the following two images will be generated as well:
	
	1. initialTownMap.png (shows the locations of the houses, malls and city center without any road network)
	2. initialTownMapEdges.png (shows the possible roads, i.e. edges, considered during optimization for a chosen house/mall/city center)

Note that if you only change the alpha coefficient, these two files will remain unchanged and hence only a single instance of these images is 
given in the sampleResults/ folder.
	