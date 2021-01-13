# This project is a python project on graphs , the main idea of this project was to "translate" an exist project we have from java to python and comparing some graph algorithims between them and between networkx . let's subscribe our classes and methods   

EX_3:
# class NodeData 
This class represents a node_data which is a vertex in a weighted-directed graph that contains few fields: key, info ,geo location, weight and tag. Each node can have vertices “neighbors” which means there are weighted edges(a unergative weight) that connect it to each one of these vertices . The fields of this class are:

Key : Represents the key of the node.

gl (geo location): represent the geo location of the node - tuple (x,y,x)=the location of the node on the graph

weight : represent the weight of the node

Info (String): Represent the info (meta data) of the node- will help us with some algorithims

Tag (int): A variable which can help for marking 

# Methods:
-get (for all the fields)

-set(for all the fields)





# class DiGraph :
This class represents a directed, weighted graph, which is a collection of nodes/vertex, the nodes can be connected to each other, but not necessarily.each edge has source dest and weight

The fields of this class are:

MyNodes  A Dictionary of data nodes which represent our graph, in form of node_key -> node_data.
Dictionary[key,Dictionary[neighboor key,weight of the edge]] 
InEdges: represent us the inner edges in the graph(from which node it arrived).
In the inner dictionary the key is the neighbor and value is the weight of the edge
Dictionary[key,Dictionary[neighboor key,the weight of the edge]] 
OutEdges: represent us the external edges in the graph(to which node it goes).in the inner dictionary the key is the neighbor and value is the weight of the edge
NumOfEdge (int): Represents the number of edges that the graph contains.
MC : Represents the number of operations that were made on the graph. Each update on the graph, will raise MC by one. Initial value is zero.
# Methods:
Adding/removing a node to/from the graph, connecting between nodes (by weighted edge and by source-dest ) in the graph. Get size (num of nodes), specific node, MC, list of graph’s nodes and list of neighbors. Also, getEdge which give us information about the edge between nodes. removing a edge from the graph. The function equals chek if tow graph are equals by they struct and there information..

# Class Graph_Algo :
This class represents some algorithms on the graph that will help us to get some information. The fields of this class are: -g (graph): Represents our actual graph.

# Methods and algorithms:
load_from_json:
The method Loads a graph from a json file.

save_to_json
The method: Saves the graph in JSON format to a file and returns True if the save was successful, False o.w.

shortestPath :
The method retrieves a list of vertices which represents a path in the graph from a given source and destination, if exists. The method will first check some basic cases, such as same source and destination node, or if one of these doesn’t exists in the graph. And then using the dijakstra algorithm  will return us the shortest path cost and the nodes we passed through . about the algorithim you can find information in https://en.wikipedia.org/wiki/Dijkstra's_algorithm 


connected_component:
This method finds the Strongly Connected Component(SCC) that node id1 is a part of. 
* helping functions:
BFS , bfsReverse- both methods runs on the graph in the bfs algorithim which yo can find information in : https://en.wikipedia.org/wiki/Breadth-first_search
bfs wiil run on the nodes that sending a arrow (all_out_edges_of_node) and the bfsReverse will run on the nodes who gets arrows ( all_in_edges_of_node).
then the main function will compare between the two lists we got from the functions and will take the common nodes from the lists which will be a part of the compnonent of the node. 


connected_components:
This method finds all the Strongly Connected Component(SCC) in the graph using the previous method. 
in the function we wull run through all the nodes and will ask for the connected_component of each node . then we will add it to a list and then in the list will appear al the connected_components

 


plot_graph: 
This method Plots the graph.
        If the nodes have a position, the nodes will be placed there.
        Otherwise, they will be placed in a random but elegant manner.

# The second part of the project:
about the second part of the project which contains the comperation you can find in the wiki page


