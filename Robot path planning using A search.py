def heuristic(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)
def reconstruct_path(cameFrom, current):
    
    total_path = [current]
    while current in cameFrom:
        current = cameFrom[current]
        total_path.append(current)
    return total_path
    
def Findneighbor(graph,m):
    nodes = []
    s = m
    if s[0]>=0 and s[1]+1>=0 and s[0]<len(graph) and s[1]+1 <len(graph[0]):
        if graph[s[0]][s[1]+1] != 1:
            nodes.append((s[0],s[1]+1))
      
    if s[0]>=0 and s[1]-1>=0 and s[0]<len(graph) and s[1]-1 <len(graph[0]):
       if graph[s[0]][s[1]-1] != 1:
           nodes.append((s[0],s[1]-1))
    
    if s[0]+1>=0 and s[1]>=0 and s[0]+1<len(graph) and s[1] <len(graph[0]):
       if graph[s[0]+1][s[1]] != 1:
           nodes.append((s[0]+1,s[1]))
      
    if s[0]-1>=0 and s[1]>=0 and s[0]-1<len(graph) and s[1] <len(graph[0]):
        if graph[s[0]-1][s[1]] != 1:
            nodes.append((s[0]-1,s[1]))
      
    return nodes

def cost(current,i):
    g = current
    if (g[0]+1,g[1]) == i or (g[0]-1,g[1]) == i:
        return 1
    elif (g[0],g[1]+1) == i or (g[0],g[1]-1) == i:
        return 2


def astar(start, end, graph):
    open_list = []
    closed_list = []
    G={}
    F={}
    cameFrom={}
    G[start]=0
    F[start]=heuristic(start, end)
    path = []
    open_list.append(start)
    while len(open_list) >= 0:
        current = open_list[0]
        current_index = current
        if current == end:
            return reconstruct_path(cameFrom, current)
#        
        open_list.remove(current_index)
        closed_list.append(current)
#      
        neighbor = Findneighbor(graph,current)
   
        for i in neighbor:
#       
            if i in closed_list:
                continue
          
            G[i] = cost(current,i)
            tentative_gScore = G[current] + G[i]
            
            if i not in open_list:
                open_list.append(i)
            elif tentative_gScore >= G[i]:
                continue 
                
            cameFrom[i] = current
          
            G[i] = tentative_gScore
            F[i] = G[i] + heuristic(i, end)
           
      

def main():

    graph = [
            [0, 0, 0, 0, 0, 0],
            [0, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0],
            [0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0],
            ]
    start = (3, 1)
    end = (3, 4)
   
    path = astar(start, end,graph)
    
    print("the path is --",path)  


if __name__ == '__main__':
    main()
    