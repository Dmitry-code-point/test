from collections import deque

graph = {'0':set(['1','2']),
'2':set(['0']),
'1':set(['0','3','6']),
'3':set(['1','4','5']),
'4':set(['3']),
'5':set(['3','6']),
'6':set(['1','5'])
}

def bfs(graph, start, target=[]):
    visited= set()
    queue = deque([(start, [start])])
    while queue:
        top = queue.popleft()
        way = queue.popleft()
        if top == target:
            return top
        if top not in visited:
            visited.add(top)
            for neighbor in graph[top]:
                queue.append((neighbor, way + [neighbor]))
    return None

start = '2'
target = '7'
way = bfs(graph, start, target)

if way:
    print(f"Путь от {start} к {target}: {way}")
else:
    print(f"Путь от {start} к {target} не найден.")

