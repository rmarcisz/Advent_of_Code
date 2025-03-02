import time
import numpy as np

class AdventOfCodeD12:
    def __init__(self, input_path):
        self._load_data(input_path)
        self.visited = []
        self.areas = []
        self.directions = [(-1,0), (1,0), (0,1), (0,-1)]
        self.directions_directed = [(-1,0, 'A'), (1,0, 'B'), (0,1, 'C'), (0,-1, 'D')]
        self.results = 0
    
    def _load_data(self, input_path):
        try:
            with open(input_path) as file:
                self.data = file.read()
                self.data = self.data.splitlines()
        except (FileNotFoundError, ValueError, IndexError) as e:
            print(f'Error reading or parsing input file: {e}')
            raise

    def _check_area(self, point):
        area_letter = self.data[point[0]][point[1]]
        area = []
        area.append(point)
        points = []
        points.append(point)
        while len(points) > 0:
            for direction in self.directions:
                check_point = tuple(np.sum([direction, points[0]], axis=0))
                if 0 <= check_point[0] <= (len(self.data[0]) -1) and 0 <= check_point[1] <= (len(self.data) - 1) and check_point not in self.visited:
                    if self.data[check_point[0]][check_point[1]] == area_letter:
                        self.visited.append(check_point)
                        area.append(check_point)
                        points.append(check_point)
            points.remove(points[0])
        self.areas.append(area)
        
    def scan(self):
        for r, row in enumerate(self.data):
            for c, letter in enumerate(row):
                if (r, c) not in self.visited:
                    self.visited.append((r,c))
                    self._check_area((r,c))

    def count_perimeter(self):
        for area in self.areas:
            area_letter = self.data[area[0][0]][area[0][1]]
            border = []
            for point in area:
                for direction in self.directions:
                    check_point = tuple(np.sum([direction, point], axis=0))
                    if 0 > check_point[0] or check_point[0] > (len(self.data[0]) -1) or 0 > check_point[1] or check_point[1] > (len(self.data) - 1) or self.data[check_point[0]][check_point[1]] != area_letter:
                        border.append(check_point)
            self.results += (len(area) * len(border))

    def count_perimeter_discounted(self):
        for area in self.areas:
            area_letter = self.data[area[0][0]][area[0][1]]
            border = []
            area = sorted(area)
            border_dupes = []
            for point in area:
                for direction in self.directions_directed:
                    check_point = (point[0] + direction[0], point[1] + direction[1], direction[2])
                    if 0 > check_point[0] or check_point[0] > (len(self.data[0]) -1) or 0 > check_point[1] or check_point[1] > (len(self.data) - 1) or self.data[check_point[0]][check_point[1]] != area_letter:
                        border.append(check_point)
                        if ((check_point[0] -1, check_point[1], check_point[2])) in border or ((check_point[0], check_point[1] -1, check_point[2])) in border:
                            border_dupes.append(check_point)
            self.results += (len(area) * (len(border) - len(border_dupes)))
                               
    def print_results(self):
        print(self.results)

if __name__ == '__main__':
    start_time = time.time()
    advent = AdventOfCodeD12('inputs/12.txt')
    advent.scan()
    advent.count_perimeter_discounted()
    advent.print_results()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f'Program ran for {elapsed_time:.4f} seconds')