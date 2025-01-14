'''--- Day 8: Resonant Collinearity ---
You find yourselves on the roof of a top-secret Easter Bunny installation.

While The Historians do their thing, you take a look at the familiar huge antenna. Much to your surprise, it seems to have been reconfigured to emit a signal that makes people 0.1% more likely to buy Easter Bunny brand Imitation Mediocre Chocolate as a Christmas gift! Unthinkable!

Scanning across the city, you find that there are actually many such antennas. Each antenna is tuned to a specific frequency indicated by a single lowercase letter, uppercase letter, or digit. You create a map (your puzzle input) of these antennas.

The signal only applies its nefarious effect at specific antinodes based on the resonant frequencies of the antennas. In particular, an antinode occurs at any point that is perfectly in line with two antennas of the same frequency - but only when one of the antennas is twice as far away as the other. This means that for any pair of antennas with the same frequency, there are two antinodes, one on either side of them.

Calculate the impact of the signal. How many unique locations within the bounds of the map contain an antinode?'''

import time
import numpy

class AdventOfCodeD8:
    def __init__(self):
        with open('inputs/8.txt') as data:
            self.data_l = [row.strip() for row in data]
        self.map_w = len(self.data_l[0])
        self.map_h = len(self.data_l)
        self.freq = []
        self.letters = []
        for row in self.data_l:
            for char in row:
                if char not in self.freq and char != '.':
                    self.freq.append(char)
        self.clean_row = '.' * self.map_w
        self.clean_map = [self.clean_row for i in range(self.map_h)]

    def find_antenna(self):
        self.locations = []
        for char in self.freq:
            self.letters.append(char)
            char_locs = []
            for h, row in enumerate(self.data_l):
                for w, letter in enumerate(row):
                    if letter == char:
                        char_locs.append((h,w))
            self.locations.append(char_locs)

    def find_antinodes(self):
        self.antinodes = []
        for letter in self.locations:
            for loc in letter:
                for i in range(len(letter)):
                    antinode_d = tuple(numpy.subtract(loc, letter[i]))
                    antinode = tuple(numpy.add(loc, antinode_d))
                    if antinode != loc and 0 <= antinode[0] < self.map_w and 0 <= antinode[1] < self.map_h and antinode not in self.antinodes:
                        self.antinodes.append(antinode)

    def find_resonating_antinodes(self):
        self.antinodes = []
        for l, letter in enumerate(self.locations):
            print(f'working for letter {self.letters[l]}. It has {len(letter)}')
            for loc in letter:
                for i in range(len(letter)):
                    antinode_d = tuple(numpy.subtract(loc, letter[i]))
                    antinode = tuple(numpy.add(loc, antinode_d))
                    while True:
                        if antinode_d == (0,0):
                            break
                        if 0 <= antinode[1] < self.map_w and 0 <= antinode[0] < self.map_h:
                            self.antinodes.append(antinode)
                        antinode = tuple(numpy.add(antinode, antinode_d))
                        if self.map_w <= antinode[1] or antinode[0] < 0 or self.map_h <= antinode[0] or antinode[1] < 0:
                            self.antinodes.append(loc)
                            break
                        
    def apply_anti(self):
        for anti in self.antinodes:
            new_row = (self.clean_map[anti[0]][:anti[1]] + '#' + (self.clean_map[anti[0]][anti[1]+1:]))
            self.clean_map[anti[0]] = new_row
 
    def print_map(self):
        for row in self.clean_map:
            print(row)
    
    def print_results(self):
        #print(self.freq)
        #print(self.locations)
        print(len(list(set(self.antinodes))))
        #print(self.map_w)
        return

if __name__ == '__main__':
    start_time = time.time()
    advent = AdventOfCodeD8()
    #advent.print_map()
    advent.find_antenna()
    #advent.find_antinodes()
    advent.find_resonating_antinodes()
    advent.apply_anti()
    advent.print_map()
    advent.print_results()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Program ran for {elapsed_time:.4f} seconds")