import board
import collections

class Queue:
    def __init__(self):
        self.elements = collections.deque()
    
    def empty(self):
        return len(self.elements) == 0
    
    def put(self, x):
        self.elements.append(x)
    
    def get(self):
        return self.elements.popleft()

def breadth_first_search(graph, start, goal):
    frontier = Queue()
    frontier.put(start)
    came_from = {}
    came_from[start] = None
    
    while not frontier.empty():
        current = frontier.get()
        
        if current == goal: #if see the goal then stop to run Dijkstra
            break
        

        for nextOne in board.neighbours(graph, current):
            if nextOne not in came_from:
                frontier.put(nextOne) # put in the list we gonna look at next
                came_from[nextOne] = current # this is the path
    
    return came_from