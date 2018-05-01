import networkx as nx
import numpy as np


class LoadFromFile(object):
    def __init__(self):
        """
        Initiate variables for the class.
        """
        self.g = nx.Graph()

        pass

    def from_edgelist(self, path):
        '''
        Read graph in edgelist txt format from `path`.

        Parameters
        ----------
        path: `str`
            The path to the edgelist text file. Note that the node index must start from 0.

        Returns
        -------
        G: `NetworkX graph`
            The parsed graph.

        '''

        edgelist = []
        with open(path, 'r') as f:
            for line in f:
                node_pair = line.replace('\n', '').split(' ')
                edgelist += [node_pair]
        self.g.add_edges_from(edgelist)
        print(nx.info(self.g))
        print('Edgelist txt data successfully loaded into a networkx Graph!')
        return self.g

    def from_in_class_network(self):  # This is Prob. 3-a.
        '''
        
        Write your code documentation here.  # This is Prob. 4-a.
        
        Write a function that parses the In-class network.txt file to a networkx Graph object.
        
        Parameters
        ----------

        Returns
        -------
        g : `NetworkX graph`
            The parsed graph.

        '''
        linelist=[]
        with open('dataset/In-class_network.txt', 'r') as f:
            for line in f:
                linelist.append(line.strip().split('\t'))
                
        for i in range(1,len(linelist)):
            linelist[i][1]=linelist[i][1].split(',')

        nodelist=[]
        for i in range(1,len(linelist)):
            nodelist.append(int(linelist[i][0]))

        edgelist=[]
        for i in range(1,len(linelist)):
            for  j in range(len(linelist[i][1])):
                if linelist[i][1][j]!=' ':
                    edgelist.append([int(linelist[i][0]),int(linelist[i][1][j])])
        
        self.g=nx.Graph()
        self.g.add_nodes_from(nodelist)
        self.g.add_edges_from(edgelist)
        

        return self.g