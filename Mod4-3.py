from collections import deque

graph = {
'0':set(['1','2']),
'2':set(['0']),
'1':set(['0','3','6']),
'3':set(['1','4','5']),
'4':set(['3']),
'5':set(['3','6']),
'6':set(['1','5'])
}

def bfs(graph, start, target=[]):
    visited= set()
    queue_list = [(start, [start])]

    while queue_list:
        (elem1, elem2) = queue_list.pop(0)
        if elem1 not in visited:
            visited.add(elem1)
            if elem1 == target:
                print('Целевая вершина', elem1)
                return elem2
            for neighbor in graph[elem1]:
                queue_list.append((neighbor, elem2 + [neighbor]))
    return None

start = '2'
target = '4'
elem = bfs(graph, start, target)

if elem:
    print(f"Путь от {start} к {target}: {elem}")
else:
    print(f"Путь от {start} к {target} не найден.")

