import sys

start = 1
stop = 6
graph = []

def read_data():
    edge = Edge(1,2,16, False)
    graph.append(edge)
    edge = Edge(2,4,12, False)
    graph.append(edge)
    edge = Edge(4,6,20, False)
    graph.append(edge)
    edge = Edge(1,3,13, False)
    graph.append(edge)
    edge = Edge(3,2,4, False)
    graph.append(edge)
    edge = Edge(3,5,14, False)
    graph.append(edge)
    edge = Edge(5,6,4, False)
    graph.append(edge)
    edge = Edge(4,3,9, False)
    graph.append(edge)
    edge = Edge(5,4,7, False)
    graph.append(edge)


class Edge:
    def __init__ (self, start, stop, weight, visited):
        self.start = start
        self.stop = stop
        self.weight = weight
        self.visited = visited
        

class Path:
    def __init__ (self, min_weight, found):
        self.min_weight = min_weight
        self.found = found


def dfs (l_start, l_stop, l_graph, path):
    if l_start == l_stop:
        path.found = True
    else:
        for edge in l_graph:
            if l_start == edge.start and not edge.visited:
                edge.visited = True 
                curr_weight = path.min_weight
                path.min_weight = min(path.min_weight, edge.weight)
                dfs(edge.stop, l_stop, l_graph, path)
                if path.found :
                    edge.weight -= path.min_weight
                    if edge.weight <= 0:
                        l_graph.remove(edge)
                    return
                else :
                    path.min_weight = curr_weight

        path = Path(sys.maxsize, False)



def main():
    read_data()

    max_capacity = 0
    while True:
        path = Path(sys.maxsize, False)
        for edge in graph:
            edge.visited = False

        dfs(start, stop, graph, path)
        if path.found :
            max_capacity += path.min_weight
            print(path.min_weight)
        else:
            break
    
    print(max_capacity)


if __name__ == "__main__":
    main()