class Graph:
    def __init__ (self):
        self.vertices = 0 #number of vertices initialized to zero
        self.edges = 0; #number of edges
        self.adjacent = {} #this is a dict: key:str="Node name", val:list="set of adjacent nodes --> to avoid duplicates"
    def addVertex (self, name):
        self.adjacent[name] = set()
        self.vertices += 1
        
    def addEdge (self, src, dest):
        self.adjacent[src].add(dest)
        self.edges += 1
    def printer (self):
        pass
    
myg = Graph()
myg.addVertex("State Street")
myg.addVertex("Avenel Street")
myg.addVertex("Elm Street")
myg.addVertex("William Ave")
myg.addVertex("Pocono Pl")

myg.addEdge ("State Street", "Elm Street")
myg.addEdge ("State Street", "Avenel Street")

myg.addEdge ("Avenel Street", "Pocono Pl")

myg.addEdge ("Elm Street", "Avenel Street")
myg.addEdge ("Elm Street", "William Ave")

myg.addEdge ("William Ave", "State Street")
myg.addEdge ("William Ave", "Pocono Pl")

myg.addEdge ("Pocono Pl", "Elm Street")

print(myg.adjacent)
