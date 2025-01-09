'''--- Day 6: Guard Gallivant ---
The Historians use their fancy device again, this time to whisk you all away to the North Pole prototype suit manufacturing lab... in the year 1518! It turns out that having direct access to history is very convenient for a group of historians.

You still have to be careful of time paradoxes, and so it will be important to avoid anyone from 1518 while The Historians search for the Chief. Unfortunately, a single guard is patrolling this part of the lab.

Maybe you can work out where the guard will go ahead of time so that The Historians can search safely?'''

class AdventOfCodeD6:
    def __init__(self):
        with open('inputs/6.txt') as data:
            self.data_l = [row.strip() for row in data]
        self.robot_pos = [0, 0, '>']
        self.robot_dir = {'^': [-1, 0], '>': [0, 1], 'v': [1, 0], '<': [0, -1]}
        self.dir_order = list(self.robot_dir)
        self.result = 0
        self.move_robo = True
        self.mw = len(self.data_l[0])
        self.ml = len(self.data_l)
        self.starting_pos = []
        self.skips = 0
        self.result_path = 0
        self.paths = {}
        self.number_of_loops = 0
        self.activations = 0

    def find_robot(self):
        for r, row in enumerate(self.data_l):
            for c, char in enumerate(row):
                if char in self.robot_dir:
                    self.robot_pos = [r, c, char]
                    self.starting_pos = self.robot_pos.copy()
                    return
                    
    def move_robot(self):
        while self.move_robo:
            new_pos = [a + b for a, b in zip(self.robot_pos, self.robot_dir.get(self.robot_pos[2]))]
            if new_pos[1] < 0 or new_pos[1] > self.mw - 1 or new_pos[0] < 0 or new_pos[0] > self.ml - 1:
                self.move_robo = False
                new_row = (self.data_l[self.robot_pos[0]][:self.robot_pos[1]]) + "X" + (self.data_l[self.robot_pos[0]][self.robot_pos[1]+1:])
                self.data_l[self.robot_pos[0]] = new_row
            elif (self.data_l[new_pos[0]][new_pos[1]]) == '#':
                self.robot_pos[2] = self.dir_order[(self.dir_order.index(self.robot_pos[2]) + 1) % len(self.dir_order)]
            else:
                new_row = (self.data_l[self.robot_pos[0]][:self.robot_pos[1]]) + "X" + (self.data_l[self.robot_pos[0]][self.robot_pos[1]+1:])
                self.data_l[self.robot_pos[0]] = new_row
                self.robot_pos[0], self.robot_pos[1] = new_pos[0], new_pos[1]
                

    def add_wall_on_path(self, i):
        self.robot_pos = self.starting_pos.copy()
        self.data_path = [row for row in self.data_l]
        self.data_path = [row.replace('X', '.') for row in self.data_l]
        self.skips = 0
        for n, row in enumerate(self.data_l):
            for m, char in enumerate(row):
                if char == 'X':
                    if self.skips == i:
                        new_row = (self.data_path[n][:m]) + '#' + (self.data_path[n][m+1:])
                        self.data_path[n] = new_row
                        return
                    else:
                        new_row = (self.data_path[n][:m]) + '.' + (self.data_path[n][m+1:])
                        self.data_path[n] = new_row
                        self.skips += 1
                    
    def move_robot_on_path(self):
        self.activations += 1
        self.movements = []
        self.move_robo = True
        while self.move_robo:
            new_pos = [a + b for a, b in zip(self.robot_pos, self.robot_dir.get(self.robot_pos[2]))]
            if new_pos[1] < 0 or new_pos[1] > self.mw - 1 or new_pos[0] < 0 or new_pos[0] > self.ml - 1:
                self.move_robo = False
                new_row = (self.data_path[self.robot_pos[0]][:self.robot_pos[1]]) + "X" + (self.data_path[self.robot_pos[0]][self.robot_pos[1]+1:])
                self.data_path[self.robot_pos[0]] = new_row
            elif (self.data_path[new_pos[0]][new_pos[1]]) == '#':
                self.robot_pos[2] = self.dir_order[(self.dir_order.index(self.robot_pos[2]) + 1) % len(self.dir_order)]
            else:
                new_row = (self.data_path[self.robot_pos[0]][:self.robot_pos[1]]) + "X" + (self.data_path[self.robot_pos[0]][self.robot_pos[1]+1:])
                self.data_path[self.robot_pos[0]] = new_row
                self.robot_pos[0], self.robot_pos[1] = new_pos[0], new_pos[1]
                if str(self.robot_pos) in self.movements:
                    self.number_of_loops += 1
                    return
                self.movements.append(str(self.robot_pos) + '')
        
                    
    def count_x(self):
        for row in self.data_l:
            for char in row:
                self.result += char == 'X'

    def get_x(self):
        return self.result
    
    def print_results(self):
        print(self.result)
        print(self.number_of_loops)
        
    def print_maze(self):
        for row in self.data_l:
            print(row)
            
    def print_path(self):
        for row in self.data_path:
            print(row)

if __name__ == '__main__':
    advent = AdventOfCodeD6()
    advent.find_robot()
    advent.move_robot()
    #advent.print_maze()
    advent.count_x()
    amount = advent.get_x()
    for a in range(amount):
        advent.add_wall_on_path(a)
        advent.move_robot_on_path()
    #advent.print_path()
    advent.print_results()

    
    