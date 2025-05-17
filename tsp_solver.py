from itertools import combinations

def greedy_tsp_solver(places, dist, start_index):
    n = len(places)
    unvisited = set(range(n))
    path = [start_index]
    unvisited.remove(start_index)
    while unvisited:
        last = path[-1]
        next_city = min(unvisited, key=lambda i: dist[last][i])
        path.append(next_city)
        unvisited.remove(next_city)
    return path

def path_distance(path, dist):
    return sum(dist[path[i]][path[i + 1]] for i in range(len(path) - 1))

def two_opt(path, dist):
    improved = True
    while improved:
        improved = False
        for i, j in combinations(range(1, len(path) - 1), 2):
            if j - i == 1:
                continue
            new_path = path[:i] + path[i:j][::-1] + path[j:]
            if path_distance(new_path, dist) < path_distance(path, dist):
                path = new_path
                improved = True
    return path