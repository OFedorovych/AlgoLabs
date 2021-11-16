N = 0
start = 0
graph = []

def read_data():
    with open('graph.in.txt') as f:
        global N
        global start
        global graph
        for row in f:
            if (N == 0):
                data_str = row.split()
                N = int(data_str[0]) #number вершин
                start = int(data_str[1])
            else:
                data_str = row.split()
                u_v_w = [int(x) for x in data_str]
                graph.append(u_v_w)



def main():
    read_data()
#ініціалізація максимальними знавченнями
    dist = [float("Inf")] * N
    dist[start] = 0
#перебір всіх ребер для пошуку найкоротшого шляху
    for i in range(N-1):
        for u, v, w in graph:
            if dist[u] != float("Inf") and dist[v] > dist[u] + w:
                dist[v] = dist[u] + w


    for u, v, w in graph:
            if dist[u] != float("Inf") and dist[v] > dist[u] + w:
                print("Граф містить негативний цикл")
    
    sum = 0
    points = 0
    for i in range(0, N):
        if dist[i] != float("Inf"):
            sum += dist[i]
            points += 1
            print(i, dist[i])

    avg = sum / (points - 1)

    with open("graph.out.TXT", "w") as f_out:
        f_out.write(str(avg).format("{.:2f}"))
        f_out.close()



if __name__ == "__main__":
    main()