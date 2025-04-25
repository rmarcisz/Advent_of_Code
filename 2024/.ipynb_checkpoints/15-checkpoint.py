import time
import re
import numpy as np

class AdventOfCodeD15:
    def __init__(self, input_path):
        self._load_data(input_path)
        self.result = 0
        self.maze = []
        self.instructions = []
        self.robot_pos = (0,0)
        self.directions = {'<': (0, -1), '>': (0, 1), '^': (-1, 0), 'v': (1, 0)}
        for row in self.data:
            if '#' in row:
                self.maze.append(list(row))
            else:
                self.instructions.append(row)
        self.instructions = ''.join(self.instructions)
            
    
    def _load_data(self, input_path):
        try:
            with open(input_path) as file:
                self.data = file.read().strip().split('\n')
        except (FileNotFoundError, ValueError, IndexError) as e:
            print(f'Error reading or parsing input file: {e}')
            raise
    
    def _find_robot(self):
        for i, row in enumerate(self.maze):
            for j, char in enumerate(row):
                if char == '@':
                    self.robot_pos = (i, j)
                    return
    
    def _move_robot(self, direction):
        result = tuple(np.sum([self.robot_pos, self.directions[direction]], axis=0))
        first_move = tuple(np.sum([self.robot_pos, self.directions[direction]], axis=0))
        while self.maze[result[0]][result[1]] == 'O':
            result = tuple(np.sum([result, self.directions[direction]], axis=0))
        if self.maze[result[0]][result[1]] == '#':
            return
        self.maze[result[0]][result[1]] = 'O'
        self.maze[self.robot_pos[0]][self.robot_pos[1]] = '.'
        self.maze[first_move[0]][first_move[1]] = '@'
        self.robot_pos = first_move

    def print_maze(self):
        for row in self.p2_maze:
            print(''.join(row))
        
    def _print_results(self):
        for i, row in enumerate(self.maze):
            for j, char in enumerate(row):
                if char == 'O':
                    self.result += (100*i + j)
        print(self.result)
                    
    def part1(self):
        self._find_robot()
        for char in self.instructions:
            self._move_robot(char)
        self._print_results()

    def part2(self):
        self._part2_converter()
        self._part2_finder()

    def _part2_converter(self):
        conversion = {'O': '[]', '#': '##', '.': '..', '@': '@.'}
        self.p2_maze = []
        for row in self.maze:
            new_row = []
            for char in row:
                new_row.append(conversion[char][0])
                new_row.append(conversion[char][1])
            self.p2_maze.append(new_row)

    def _part2_finder(self):
        self.maze_map = {'#': [], '[': [], ']': [], '@': []}
        for i, row in enumerate(self.p2_maze):
            for j, char in enumerate(row):
                if char == '#':
                    self.maze_map['#'].append((i,j))
                if char == '@':
                    self.maze_map['@'] = (i,j)
                if char == '[':
                    self.maze_map['['].append((i,j))
                if char == ']':
                    self.maze_map[']'].append((i,j))

    def _move_robot_2(self, direction):
        result = tuple(np.sum([self.maze_map['@'], self.directions[direction]], axis=0))
        print(result)

if __name__ == '__main__':
    start_time = time.time()
    advent = AdventOfCodeD15('inputs/15.txt')
    #advent.part1()
    advent.part2()
    advent._move_robot_2('v')
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f'Program ran for {elapsed_time:.4f} seconds')