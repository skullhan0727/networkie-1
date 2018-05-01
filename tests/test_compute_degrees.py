from networkie.gen import Custom
from networkie.utils import Measures
lff = Custom.LoadFromFile()
g = lff.from_in_class_network()
Node= Measures.Node()
l=Node.degree_dist()

class Testdegree:
    def test_degree(self):
        expected=g.size()
        result=sum(Node.degree_dist())/2
        
        assert expected==result
   




