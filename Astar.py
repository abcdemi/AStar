from pyamaze import maze, agent, textLabel
from queue import PriorityQueue

def manhattan(cell1, cell2):
    x1, y1 = cell1
    x2, y2 = cell2
    return abs(x1 - x2) + abs(y1 - y2)

def aStar(m):
    start = (m.rows, m.cols)
    g_score = {cell: float('inf') for cell in m.grid}
    g_score[start] = 0
    f_score = {cell: float('inf') for cell in m.grid}
    f_score[start] = 0
    
    open = PriorityQueue()
    open.put((manhattan(start, (1,1)), manhattan(start, (1,1)), start))
    aPath = {}
    
    while not open.empty():
        currCell = open.get()[2]
        if currCell==(1,1):
            break
        for direction in 'ESNW':
            if m.maze_map[currCell][direction] == True:
                if direction == 'E':
                    childCell = (currCell[0], currCell[1] + 1)
                if direction == 'W':
                    childCell = (currCell[0], currCell[1] - 1)
                if direction == 'N':
                    childCell = (currCell[0] - 1, currCell[1])
                if direction == 'S':
                    childCell = (currCell[0] + 1, currCell[1])
        
                temp_g_score = g_score[currCell] + 1
                temp_f_score = temp_g_score + manhattan(childCell, (1,1))
                
                if temp_f_score < f_score[childCell]:
                    g_score[childCell] = temp_g_score
                    f_score[childCell] = temp_f_score
                    open.put((temp_f_score, manhattan(childCell,(1,1)), childCell))
                    aPath[childCell] = currCell
    fwdPath={}
    cell = (1,1)
    while cell != start:
        fwdPath[aPath[cell]] = cell
        cell = aPath[cell]
    return fwdPath

if __name__ == '__main__':
    m = maze(5, 5)
    m.CreateMaze()
    path = aStar(m)
    
    a = agent(m, footprints = True)
    m.tracePath({a:path})
    l = textLabel(m, 'aStar path length', len(path) + 1)
    
    m.run()