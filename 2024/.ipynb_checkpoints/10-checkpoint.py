import time
import numpy as np

class AdventOfCodeD10:
    def __init__(self, input_path):
        self.starting_points = []
        self.movements = []
        self.paths = []
        self.visited_9 = 0
        self.ways_to_9 = 0
        self.dir = [(0,1), (0,-1), (1,0), (-1,0)]
        self._load_data(input_path)
        self.w = len(self.data[0])
        self.h = len(self.data)
    
    def _load_data(self, input_path):
        try:
            with open(input_path) as file:
                self.data = [[int(char) for char in row.strip()] for row in file]
        except (FileNotFoundError, ValueError, IndexError) as e:
            print(f'Error reading or parsing input file: {e}')
            raise

    def _find_starters(self):
        self.starting_points.extend((i, j) for i in range(len(self.data)) for j in range(len(self.data[i])) if self.data[i][j] == 0)

    def _find_movements(self, starter):
        if self.data[starter[0]][starter[1]] == 9:
            self.visited_9 += 1
            self.movements.remove(starter)
            return
        for direction in self.dir:
            new_pos = tuple(np.subtract(starter, direction))
            if 0 <= new_pos[0] <= (self.h - 1) and 0 <= new_pos[1] <= (self.w - 1):
                if (self.data[starter[0]][starter[1]] - self.data[new_pos[0]][new_pos[1]]) == -1 and new_pos not in self.movements:
                    self.movements.append(new_pos)
        self.movements.remove(starter)

    def _part1(self):
        self._find_starters()
        while len(self.starting_points) >= 1:
            self.movements.append(self.starting_points[0])
            while len(self.movements) >= 1:
                starter = self.movements[0]
                self._find_movements(starter)
            self.starting_points.remove(self.starting_points[0])

    def _find_paths(self, starter):
        for direction in self.dir:
            #print(f'we are working for starter: {starter}')
            new_path = starter.copy()
            new_pos = tuple(np.subtract(new_path[-1], direction))
            if 0 <= new_pos[0] <= (self.h - 1) and 0 <= new_pos[1] <= (self.w - 1):
                if (self.data[starter[-1][0]][starter[-1][1]] - self.data[new_pos[0]][new_pos[1]]) == -1:
                    new_path.append(new_pos)
                    self.paths.append(new_path)
                    new_path = starter
                    if self.data[new_pos[0]][new_pos[1]] == 9:
                        self.ways_to_9 += 1
        self.paths.remove(starter)
        

    def _part2(self):
        self._find_starters()
        while len(self.starting_points) >= 1:
            self.paths.append([self.starting_points[0]])
            while len(self.paths) >= 1:
                starter = self.paths[0]
                self._find_paths(starter)
            self.starting_points.remove(self.starting_points[0])
    
    def print_results(self):
        print(self.ways_to_9)

if __name__ == '__main__':
    start_time = time.time()
    advent = AdventOfCodeD10('inputs/10.txt')
    advent._part2()
    advent.print_results()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f'Program ran for {elapsed_time:.4f} seconds')