class graphs:
    
    def init(self):
        self.graph= {}
        self.directed = False
 #Adding Vertex
    def addVertex(self,vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
    
 #Adding Edges   
    def addEdges(self,src,dst):
        self.addVertex(src)
        self.addVertex(dst)

        #if graph is directed
        self.graph[src].append(dst)

        #if graph is undirected
        if not self.directed:
            self.graph[dst].append(src)
    
    
    def display(self):
        for vertex in self.graph:
            print(f"{vertex} -> {self.graph[vertex]}")
    
    #Breadth First Search

def bfs(self,startVertex):
        queue = [startVertex]
        visited = [startVertex]
        next=self.graph[startVertex]
        while queue:
            currentVertex = queue.pop()
            print(currentVertex , end = " ")
 
            for neighbour in self.graph[currentVertex]:
                if neighbour not in visited:
                    queue.append(neighbour)
                    visited.append(neighbour)


#Deadth First Search

def dfs(self,vertex,visited):
        if vertex not in visited:
            print(vertex,end= " ")
            visited.append(vertex)
            for neigh in self.graph[vertex]:
                self.dfs(neigh,visited)


G = graph()
G.addEdges('A','B')
G.addEdges('C','B')
G.addEdges('A','D')
G.addEdges('C','E')
G.addEdges('D','E')
G.addEdges('A','E')
G.addVertex('F')

#display graph

G.display()

#Breadth first search
G.bfs('A')

#Deapth first search
G.dfs('A',[])



