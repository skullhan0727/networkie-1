import networkx as nx
from networkie.gen import Custom
lff = Custom.LoadFromFile()
g = lff.from_in_class_network()
def compute_num_triangles():  # This is Prob. 3-e.
    '''
    Write your code documentation here.  # This is Prob. 4-a.
        Write a function that parses the In-class network.txt file to a networkx Graph object.
        
        Write a function that calculates the total number of triangles in the network n∆.
        
        Parameters
        ----------

        Returns
        -------
        sum_tri : 'float'
             the total number of triangles in the network n∆.
        
    '''
    tri = nx.triangles(g)
    sum_tri = sum(nx.triangles(g).values())/3
    return sum_tri


class Node(object):
    def __init__(self):
        pass

    def betweenness(self):
        pass

    def degree_dist(self):  # This is Prob. 3-d.
        '''
        Write your code documentation here.  # This is Prob. 4-a.
        
        Write a function which outputs the vector k, as a Python list, whose elements are the degrees ki of vertex i. Use the ‘ID’ key in           the file as the index i of the list.
        
        Parameters
        ----------

        Returns
        -------
        l : 'list'
            a Python list, whose elements are the degrees ki of vertex i. Use the ‘ID’ key in the file as the index i of the list.
            
        '''

        l=[]
        for i in range(len(g.nodes)):
            l.append(g.degree(i))

        return l

