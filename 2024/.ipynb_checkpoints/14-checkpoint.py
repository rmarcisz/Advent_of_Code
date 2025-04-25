import time
import re

class AdventOfCodeD14:
    def __init__(self, input_path):
        self._load_data(input_path)
        self.result = 0
        self.robots = []
        self.columns = 101
        self.rows = 103
        for robot in self.data:
            robot = re.split('[, =\n]', robot)
            self.robots.append(robot)
    
    def _load_data(self, input_path):
        try:
            with open(input_path) as file:
                self.data = file.read().strip().split('\n')
        except (FileNotFoundError, ValueError, IndexError) as e:
            print(f'Error reading or parsing input file: {e}')
            raise

    def move_robot(self, steps):
        final_pos = []
        for robot in self.robots:
            col = ((int(robot[1]) + (steps * int(robot[4]))) % self.columns)
            row = ((int(robot[2]) + (steps * int(robot[5]))) % self.rows)
            final_pos.append((row, col))
        return final_pos

    def count_factor(self):
        leftup = 0
        leftdown = 0
        rightup = 0
        rightdown = 0
        for pos in self.final_pos:
            if pos[0] < (self.rows-1)/2 and pos[1] < (self.columns-1)/2:
                leftup += 1
            elif pos[0] < (self.rows-1)/2 and pos[1] > (self.columns-1)/2:
                leftdown += 1
            elif pos[0] > (self.rows-1)/2 and pos[1] < (self.columns-1)/2:
                rightup += 1
            elif pos[0] > (self.rows-1)/2 and pos[1] > (self.columns-1)/2:
                rightdown += 1
            else:
                pass
        self.result = leftup * leftdown * rightup * rightdown

    def print_da_bathroom(self):
        for num in range(10000):
            canvas = []
            canvas_row = []
            for col in range(self.columns):
                canvas_row = [' '] * (self.rows)
                canvas.append(canvas_row)
            current_pos = self.move_robot(num)
            for pos in current_pos:
                canvas[pos[1]][pos[0]] = '#'
            for row in canvas:
                x = re.search('########', ''.join(row))
                if x != None:
                    print(num)
            if num == 6446:
                for row in canvas:
                    print(''.join(row))
    
    def print_results(self):
        print(self.result)

if __name__ == '__main__':
    start_time = time.time()
    advent = AdventOfCodeD14('inputs/14.txt')
    advent.print_da_bathroom()
    advent.print_results()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f'Program ran for {elapsed_time:.4f} seconds')