from collections import deque
from queue import PriorityQueue

# to keep track of the blocks of maze
class Grid_Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# each block will have its own position and cost of steps taken
class Node:
    def __init__(self, pos: Grid_Position, cost):
        self.pos = pos
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost

def manhattan_distance(start: Grid_Position, destination: Grid_Position):
    return abs(destination.x - start.x) + abs(destination.y - start.y)


# Algoritmo A*
def a_star(Grid, dest: Grid_Position, start: Grid_Position):
    # to get neighbours of current node
    adj_cell_x = [-1, 0, 0, 1]
    adj_cell_y = [0, -1, 1, 0]

    m, n = (len(Grid), len(Grid))
    visited_blocks = [[False for i in range(m)] for j in range(n)]

    queue = PriorityQueue()
    sol = Node(start, 0)
    queue.put((manhattan_distance(dest, start), sol))
    cells = 4
    cost = 0

    while queue:
        current_block = queue.get()[1]  # Dequeue the front cell
        current_pos = current_block.pos
        print('[', current_pos.x, ', ', current_pos.y, ']')


        if current_block not in visited_blocks:
            visited_blocks[current_pos.x][current_pos.y] = True
            cost = cost + 1
        else:
            continue

        if current_pos.x == dest.x and current_pos.y == dest.y:
            print('Meta encontrada')
            print('Nodos expandidos:', cost - 1)
            return current_block.cost
        else:
            x_pos = current_pos.x
            y_pos = current_pos.y
            for i in range(cells):
                if x_pos == len(Grid) - 1 and adj_cell_x[i] == 1:
                    x_pos = current_pos.x
                    y_pos = current_pos.y + adj_cell_y[i]
                if y_pos == 0 and adj_cell_y[i] == -1:
                    x_pos = current_pos.x + adj_cell_x[i]
                    y_pos = current_pos.y
                else:
                    x_pos = current_pos.x + adj_cell_x[i]
                    y_pos = current_pos.y + adj_cell_y[i]
                if x_pos < 12 and y_pos < 12 and x_pos >= 0 and y_pos >= 0:
                    if Grid[x_pos][y_pos] == 1:
                        if not visited_blocks[x_pos][y_pos]:
                            next_cell = Node(Grid_Position(x_pos, y_pos), current_block.cost + 1)
                            # print(next_cell.cost)
                            visited_blocks[x_pos][y_pos] = True
                            queue.put((manhattan_distance(Grid_Position(x_pos, y_pos), dest) + next_cell.cost, next_cell))
    return -1


if __name__ == '__main__':
    maze = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0],
            [0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1],
            [0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0],
            [0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
            [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
            [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    starting_position = Grid_Position(4, 11)
    destination = Grid_Position(10, 0)

    limit = 1


    print('\n----- A* -----')
    res = a_star(maze, destination, starting_position)
    if res != -1:
        print('Nodos expandidos:', res)
    else:
        print('No pudo encontrarse un camino')

    