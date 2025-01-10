'''--- Day 7: Bridge Repair ---
The Historians take you to a familiar rope bridge over a river in the middle of a jungle. The Chief isn't on this side of the bridge, though; maybe he's on the other side?

When you go to cross the bridge, you notice a group of engineers trying to repair it. (Apparently, it breaks pretty frequently.) You won't be able to cross until it's fixed.

You ask how long it'll take; the engineers tell you that it only needs final calibrations, but some young elephants were playing nearby and stole all the operators from their calibration equations! They could finish the calibrations if only someone could determine which test values could possibly be produced by placing any combination of operators into their calibration equations (your puzzle input).'''

import time

class AdventOfCodeD7:
    def __init__(self):
        with open('inputs/7.txt') as data:
            self.data_l = [row.strip().split() for row in data]
        for i, row in enumerate(self.data_l):
            self.data_l[i][0] = row[0].replace(':', '')
            for j, elem in enumerate(row):
                self.data_l[i][j] = int(self.data_l[i][j])
        self.result = 0

    def obliczeniator(self):
        for i, row in enumerate(self.data_l):
            tree = []
            for number in row[1:]:
                if not tree:
                    tree.append(number)
                else:
                    new_tree = []
                    for elem in tree:
                        new_tree.append(elem + number)
                        new_tree.append(elem * number)
                        new_tree.append(int(str(elem) + str(number))) #thats the whole part 2 lol
                    tree = new_tree
            if self.data_l[i][0] in tree:
                self.result += self.data_l[i][0]
    
    def print_results(self):
        print(self.result)

if __name__ == '__main__':
    start_time = time.time()
    advent = AdventOfCodeD7()
    advent.obliczeniator()
    advent.print_results()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Program ran for {elapsed_time:.4f} seconds")