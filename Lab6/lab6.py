def read_data(vertexes):
    words = []
    with open ('words_in.txt') as f:
        words.extend(f.read().split('\n'))
    for word in words:
        vertex = Vertex(word)
        w1 = {word :vertex}
        vertexes.update(w1)

class Vertex:
    def __init__ (self, name):
        self.name = name
        self.path_weight = 1
    
    def __repr__ (self):
        return repr(
            (
                self.name,
                self.path_weight
            )
        )

class Edge:
    def __init__ (self, start, stop):
        self.start = start
        self.stop = stop
        self.weight = 1

    def __repr__(self):
        return repr(
            (
                self.start,
                self.stop
            )
        )

def build_graph(vertexes, graph):
    for key_start, vert_start in vertexes.items():
        for key_stop, vert_stop in vertexes.items():
            if len(vert_start.name) - len(vert_stop.name) != 1:
                continue
            else:
                for i in range(0, len(vert_start.name) ):
                    vert_check = vert_start.name[0: i:] + vert_start.name[i + 1: :]
                    if vert_check == vert_stop.name:
                        edge = Edge(vert_start.name, vert_stop.name)
                        graph.append(edge)
                        break

def build_paths(vert, vertexes, graph):    # vert точка з якої починаємо шукати
    for edge in graph:
        if vert.name == edge.start:
            next_vert = vertexes.get(edge.stop)
            if next_vert.path_weight == 1:
                new_weight = build_paths(next_vert, vertexes, graph) + 1
            else:
                new_weight = next_vert.path_weight + 1
            
            if new_weight > vert.path_weight:
                vert.path_weight = new_weight
    
    return vert.path_weight



def main():
    vertexes = {}
    graph = []
    read_data(vertexes)
    build_graph(vertexes, graph)
    
    max_path = 0
    for key, vert in vertexes.items():
        build_paths(vert, vertexes, graph)

        if vert.path_weight > max_path:
            max_path = vert.path_weight

    print(vertexes)
    print(max_path)





if __name__ == "__main__":
    main()