# -*- coding: utf-8 -*-
"""
Spyder Editor

"""
import networkx as nx 
import numpy as np
import collections as cs
import matplotlib.pyplot as plt 

 

#get all the connected components in a graph and form subgraphs from them
def connected_component_subgraphs(G):
      for c in nx.connected_components(G):
          yield G.subgraph(c)
          
          
          
          
#plot degree distribution          
def degree_Distribution(graph, dir_name, sub_dir, file_name):
   #list of degree frequencies of a graph
   degree_frequencies = nx.degree_histogram(graph)	
   plt.ylabel("Frequency")
   plt.xlabel("Node degree")
   plt.plot(degree_frequencies)
   plt.tight_layout()
   plt.savefig(dir_name + "/" + sub_dir + "/" + file_name + ".pdf")
   plt.show()			
   

	
         

#get the distribution of the local clustering coefficient of the nodes of the graph
def cluster_Distribution(graph, dir_name, sub_dir, file_name):
   clusters_of_graph = nx.clustering(graph)
   plt.ylabel("Clustering Coefficient")
   plt.xlabel("Node Number")
   x_label_data = list(clusters_of_graph.keys())
   y_label_data = list(clusters_of_graph.values())
   x_label_data = np.arange(len(x_label_data))
   plt.bar(x_label_data, y_label_data, align="center", alpha=0.6)
   plt.tight_layout()
   plt.savefig(dir_name + "/" + sub_dir + "/" + file_name + ".pdf")
   plt.show()
   
          
          
   
            
#get the distribution of the shortest path lengths of the graph    
def short_path_Distribution(graph, dir_name, sub_dir, file_name):
   short_path_lengths = []
   counter = {}
   #get the lengths of all shortest paths and store them in dictionary "counter". The key is the path length and the value is the number of paths in the graph 
   for T in nx.shortest_path_length(graph):
	   for w in T[1].values():
	    short_path_lengths.append(w)
   counter = cs.Counter(short_path_lengths)  
   length_dist = counter
   plt.xlabel('Shortest Path Length')
   plt.ylabel('Number of shortest paths')
   x_label_data = list(length_dist.keys())
   y_label_data = list(length_dist.values())
   x_label_data_arr = np.arange(len(x_label_data))
   plt.bar(x_label_data_arr, y_label_data, align="center", alpha=0.6)
   plt.xticks(x_label_data_arr, x_label_data)    
   plt.tight_layout()
   plt.savefig(dir_name + "/" + sub_dir + "/" + file_name + ".pdf")
   plt.show()
   
    
   
    
   
    
#get  global clustering coefficient, average shortest path length and the diameter of the graph     
def compute_graph(graph, dir_name, sub_dir, file_name):
	file = open(dir_name + "/" + sub_dir + "/" + file_name + "_data.txt", "w+")
	#get the global clustering coefficient 
	file.write("Global clustering coefficient: %s\n" % nx.average_clustering(graph))
	#get the average shortest path length 
	file.write("Average shortest path length: %s\n" % nx.average_shortest_path_length(graph))
	#get the diameter
	file.write("Diameter of the graph: %s\n" % nx.diameter(graph))
	file.close()    
    
   
    
   
    
   

#generate three erdos random graphs
def erdos_renyi_graphs():
   n = 1000 # number of nodes (size of graph)
   p = 0.19   
   random_graph_one = nx.erdos_renyi_graph(n,p)
   

   n = 1000 # number of nodes (size of graph)
   p = 0.14   
   random_graph_two = nx.erdos_renyi_graph(n,p)


   n = 1000 # number of nodes (size of graph)
   p = 0.25
   random_graph_three = nx.erdos_renyi_graph(n,p)
   
   
   #get the largest CCG for each random graph
   Gcc1 = sorted(nx.connected_components(random_graph_one), key=len, reverse=True)
   giant_one = random_graph_one.subgraph(Gcc1[0]) 
   Gcc2 = sorted(nx.connected_components(random_graph_two), key=len, reverse=True)
   giant_two = random_graph_two.subgraph(Gcc2[0])  
   Gcc3 = sorted(nx.connected_components(random_graph_three), key=len, reverse=True)
   giant_three = random_graph_three.subgraph(Gcc3[0])   
    
   
   
   #get the number of nodes for CCG for each random graph
   number_of_nodes_CCG_one = giant_one.number_of_nodes()
   number_of_nodes_CCG_two = giant_two.number_of_nodes()
   number_of_nodes_CCG_three = giant_three.number_of_nodes()
   
   
   #get the number of edges for CCG for each random graph
   number_of_edges_CCG_one = giant_one.number_of_edges()
   number_of_edges_CCG_two = giant_two.number_of_edges()
   number_of_edges_CCG_three = giant_three.number_of_edges()
   
   
   #table for the GCC for each random graph
   CCG_table_data = [[number_of_nodes_CCG_one, number_of_edges_CCG_one],
                     [number_of_nodes_CCG_two, number_of_edges_CCG_two],
                     [number_of_nodes_CCG_three, number_of_edges_CCG_three]]
   CCG_table_column = ("Number of Nodes", "Number of Edges")
   CCG_table_row = ("CCG for random graph one", "CCG for random graph two","CCG for random graph three")
   plt.table(cellText=CCG_table_data, rowLabels=CCG_table_row, rowColours=None, rowLoc='right', colColours=None, colLabels=CCG_table_column, loc='center')
   plt.axis("off")
   plt.tight_layout()
   plt.savefig("erdos" + "/" + "table_GCC_random_graphs.pdf")
   print("Table for the different CCG of the three random graphs ")
   plt.show()
   
   #degree distribution
   print("degree distribution of random graph one")
   degree_Distribution(giant_one, "erdos", "er1", "giant_one_erdos_degree_dis")
   print("degree distribution of random graph two")
   degree_Distribution(giant_two, "erdos", "er2", "giant_two_erdos_degree_dis")
   print("degree distribution of random graph three")
   degree_Distribution(giant_three, "erdos", "er3", "giant_three_erdos_degree_dis")


   #the local clustering coefficient of the nodes of the graph 
   print("cluster distribution of random graph one")
   cluster_Distribution(giant_one, "erdos", "er1", "giant_one_erdos_clus_dis")
   print("cluster distribution of random graph two")
   cluster_Distribution(giant_two, "erdos", "er2", "giant_two_erdos_clus_dis")
   print("cluster distribution of random graph three")
   cluster_Distribution(giant_three, "erdos", "er3", "giant_three_erdos_clus_dis")
   
   
   #get the distribution of the shortest path lengths of the graph 
   print("shortest path lengths distribution of random graph one")
   short_path_Distribution(giant_one, "erdos", "er1", "giant_one_erdos_pl_dis")
   print("shortest path lengths distribution of random graph two")
   short_path_Distribution(giant_two, "erdos", "er2", "giant_two_erdos_pl_dis")
   print("shortest path lengths distribution of random graph three")
   short_path_Distribution(giant_three, "erdos", "er3", "giant_three_erdos_pl_dis")
   
   
   #get  global clustering coefficient, average shortest path length and the diameter of the graph     
   print("global clustering coefficient, average shortest path length and the diameter of the graph one")
   compute_graph(giant_one, "erdos", "er1", "giant_one_erdos_measurement")
   print("global clustering coefficient, average shortest path length and the diameter of the graph two")
   compute_graph(giant_two, "erdos", "er2", "giant_two_erdos_measurement")
   print("global clustering coefficient, average shortest path length and the diameter of the graph three")
   compute_graph(giant_three, "erdos", "er3", "giant_three_erdos_measurement")




#generate three Watts Strogatz small world graphs
def watts_Strogatz_graphs(): 
   n = 1000 # number of nodes (size of graph)
   k = 200
   p = 0.2   
   small_world_graph_one = nx.watts_strogatz_graph(n, k, p)
   
   n = 1000 # number of nodes (size of graph)
   k = 175
   p = 0.3 
   small_world_graph_two = nx.watts_strogatz_graph(n, k, p)
   
   n = 1000 # number of nodes (size of graph)
   k = 225
   p = 0.4
   small_world_graph_three = nx.watts_strogatz_graph(n, k, p)
   
   #get the largest CCG for each random graph
   Gcc1 = sorted(nx.connected_components(small_world_graph_one), key=len, reverse=True)
   giant_one = small_world_graph_one.subgraph(Gcc1[0]) 
   Gcc2 = sorted(nx.connected_components(small_world_graph_two), key=len, reverse=True)
   giant_two = small_world_graph_two.subgraph(Gcc2[0])  
   Gcc3 = sorted(nx.connected_components(small_world_graph_three), key=len, reverse=True)
   giant_three = small_world_graph_three.subgraph(Gcc3[0])  
   
   
   #get the number of nodes for CCG for each small world graph
   number_of_nodes_CCG_one = giant_one.number_of_nodes()
   number_of_nodes_CCG_two = giant_two.number_of_nodes()
   number_of_nodes_CCG_three = giant_three.number_of_nodes()
   
   
   #get the number of edges for CCG for each small world graph
   number_of_edges_CCG_one = giant_one.number_of_edges()
   number_of_edges_CCG_two = giant_two.number_of_edges()
   number_of_edges_CCG_three = giant_three.number_of_edges()
   
   
   #table for the GCC for each small world graph
   CCG_table_data = [[number_of_nodes_CCG_one, number_of_edges_CCG_one],
                     [number_of_nodes_CCG_two, number_of_edges_CCG_two],
                     [number_of_nodes_CCG_three, number_of_edges_CCG_three]]
   CCG_table_column = ("Number of Nodes", "Number of Edges")
   CCG_table_row = ("CCG for small world graph one", "CCG for small world two","CCG for small world three")
   plt.table(cellText=CCG_table_data, rowLabels=CCG_table_row, rowColours=None, rowLoc='right', colColours=None, colLabels=CCG_table_column, loc='center')
   plt.axis("off")
   plt.tight_layout()
   plt.savefig("watts" + "/" + "table_GCC_small_world_graphs.pdf")
   plt.show()
   
   
   
   #degree distribution
   print("degree distribution of watts graph one")
   degree_Distribution(giant_one, "watts", "ws1", "giant_one_watts_degree_dis")
   print("degree distribution of watts graph two")
   degree_Distribution(giant_two, "watts", "ws2", "giant_two_watts_degree_dis")
   print("degree distribution of watts graph three")
   degree_Distribution(giant_three, "watts", "ws3", "giant_three_watts_degree_dis")


   #the local clustering coefficient of the nodes of the graph 
   print("cluster distribution of watts graph one")
   cluster_Distribution(giant_one, "watts", "ws1", "giant_one_watts_clus_dis")
   print("cluster distribution of watts graph two")
   cluster_Distribution(giant_two, "watts", "ws2", "giant_two_watts_clus_dis")
   print("cluster distribution of watts graph three")
   cluster_Distribution(giant_three, "watts", "ws3", "giant_three_watts_clus_dis")
   
   
   #get the distribution of the shortest path lengths of the graph 
   print("shortest path lengths distribution of watts graph one")
   short_path_Distribution(giant_one, "watts", "ws1", "giant_one_watts_pl_dis")
   print("shortest path lengths distribution of watts graph two")
   short_path_Distribution(giant_two, "watts", "ws2", "giant_two_watts_pl_dis")
   print("shortest path lengths distribution of watts graph three")
   short_path_Distribution(giant_three, "watts", "ws3", "giant_three_watts_pl_dis")
   
   
   #get  global clustering coefficient, average shortest path length and the diameter of the graph     
   print("global clustering coefficient, average shortest path length and the diameter of the graph one")
   compute_graph(giant_one, "watts", "ws1", "giant_one_watts_measurement")
   print("global clustering coefficient, average shortest path length and the diameter of the graph two")
   compute_graph(giant_two, "watts", "ws2", "giant_two_watts_measurement")
   print("global clustering coefficient, average shortest path length and the diameter of the graph three")
   compute_graph(giant_three, "watts", "ws3", "giant_three_watts_measurement")   
   


#generate three barabasi albert scale free graphs
def barabasi_albert_graphs(): 
   n = 1000 # number of nodes (size of graph)
   m = 90   
   scale_free_graph_one = nx.barabasi_albert_graph(n, m) 
   
   n = 1000 # number of nodes (size of graph)
   m = 117
   scale_free_graph_two = nx.barabasi_albert_graph(n, m)
   
   n = 1000 # number of nodes (size of graph)
   m = 130
   scale_free_graph_three = nx.barabasi_albert_graph(n, m)
 
   
 
   #get the largest CCG for each random graph
   Gcc1 = sorted(nx.connected_components(scale_free_graph_one), key=len, reverse=True)
   giant_one = scale_free_graph_one.subgraph(Gcc1[0]) 
   Gcc2 = sorted(nx.connected_components(scale_free_graph_two), key=len, reverse=True)
   giant_two = scale_free_graph_two.subgraph(Gcc2[0])  
   Gcc3 = sorted(nx.connected_components(scale_free_graph_three), key=len, reverse=True)
   giant_three = scale_free_graph_three.subgraph(Gcc3[0])  
   
   
   #get the number of nodes for CCG for each scale free graph
   number_of_nodes_CCG_one = giant_one.number_of_nodes()
   number_of_nodes_CCG_two = giant_two.number_of_nodes()
   number_of_nodes_CCG_three = giant_three.number_of_nodes()
   
   
   #get the number of edges for CCG for each scale free graph
   number_of_edges_CCG_one = giant_one.number_of_edges()
   number_of_edges_CCG_two = giant_two.number_of_edges()
   number_of_edges_CCG_three = giant_three.number_of_edges()
   
   
   #table for the GCC for each scale free graph
   CCG_table_data = [[number_of_nodes_CCG_one, number_of_edges_CCG_one],
                     [number_of_nodes_CCG_two, number_of_edges_CCG_two],
                     [number_of_nodes_CCG_three, number_of_edges_CCG_three]]
   CCG_table_column = ("Number of Nodes", "Number of Edges")
   CCG_table_row = ("CCG for scale free graph one", "CCG for scale free two","CCG for scale free three")
   plt.table(cellText=CCG_table_data, rowLabels=CCG_table_row, rowColours=None, rowLoc='right', colColours=None, colLabels=CCG_table_column, loc='center')
   plt.axis("off")
   plt.tight_layout()
   plt.savefig("barabasi" + "/" + "table_GCC_scale_free_graphs.pdf")
   plt.show()


   #degree distribution
   print("degree distribution of barabasi graph one")
   degree_Distribution(giant_one, "barabasi", "ba1", "giant_one_barabasi_degree_dis")
   print("degree distribution of barabasi graph two")
   degree_Distribution(giant_two, "barabasi", "ba2", "giant_two_barabasi_degree_dis")
   print("degree distribution of barabasi graph three")
   degree_Distribution(giant_three, "barabasi", "ba3", "giant_three_barabasi_degree_dis")


   #the local clustering coefficient of the nodes of the graph 
   print("cluster distribution of barabasi graph one")
   cluster_Distribution(giant_one, "barabasi", "ba1", "giant_one_barabasi_clus_dis")
   print("cluster distribution of barabasi graph two")
   cluster_Distribution(giant_two, "barabasi", "ba2", "giant_two_barabasi_clus_dis")
   print("cluster distribution of barabasi graph three")
   cluster_Distribution(giant_three, "barabasi", "ba3", "giant_three_barabasi_clus_dis")
   
   
   #get the distribution of the shortest path lengths of the graph 
   print("shortest path lengths distribution of barabasi graph one")
   short_path_Distribution(giant_one, "barabasi", "ba1", "giant_one_barabasi_pl_dis")
   print("shortest path lengths distribution of barabasi graph two")
   short_path_Distribution(giant_two, "barabasi", "ba2", "giant_two_barabasi_pl_dis")
   print("shortest path lengths distribution of barabasi graph three")
   short_path_Distribution(giant_three, "barabasi", "ba3", "giant_three_barabasi_pl_dis")
   
   
   #get  global clustering coefficient, average shortest path length and the diameter of the graph     
   print("global clustering coefficient, average shortest path length and the diameter of the graph one")
   compute_graph(giant_one, "barabasi", "ba1", "giant_one_barabasi_measurement")
   print("global clustering coefficient, average shortest path length and the diameter of the graph two")
   compute_graph(giant_two, "barabasi", "ba2", "giant_two_barabasi_measurement")
   print("global clustering coefficient, average shortest path length and the diameter of the graph three")
   compute_graph(giant_three, "barabasi", "ba3", "giant_three_barabasi_measurement") 



  
erdos_renyi_graphs()  
watts_Strogatz_graphs()
barabasi_albert_graphs()   
