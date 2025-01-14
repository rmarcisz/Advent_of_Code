'''--- Day 9: Disk Fragmenter ---
Another push of the button leaves you in the familiar hallways of some friendly amphipods! Good thing you each somehow got your own personal mini submarine. The Historians jet away in search of the Chief, mostly by driving directly into walls.

While The Historians quickly figure out how to pilot these things, you notice an amphipod in the corner struggling with his computer. He's trying to make more contiguous free space by compacting all of the files, but his program isn't working; you offer to help.'''

import time

class AdventOfCodeD9:
    def __init__(self):
        self.files = []
        self.spaces = []
        self.data_s = ''
        self.result = 0
        self._load_data()
        self.defragmented = ''
        self.dots = ''

    def _load_data(self):
        try:
            with open('inputs/9.txt') as file:
                data = file.readline().strip()
            for i, char in enumerate(data):
                if i % 2 == 0:
                    self.files.append(int(char))
                else:
                    self.spaces.append(int(char))
            self._generate_data_string()
        except (FileNotFoundError, ValueError, IndexError) as e:
            print(f"Error reading or parsing input file: {e}")
            raise

    def _generate_data_string(self):
        for pos, (file_count, space_count) in enumerate(zip(self.files, self.spaces)):
            self.data_s += str(pos) * file_count + '.' * space_count
    
    def defragment(self):
        while len(self.data_s) >= 1:
            if self.data_s[0] != '.':
                self.defragmented += self.data_s[0]
                self.data_s = self.data_s[1:]
            else:
                if self.data_s[-1] != '.':
                    self.defragmented += self.data_s[-1]
                    self.data_s = self.data_s[:-1]
                else:
                    self.dots += '.'
                    self.data_s = self.data_s[:-1]
        self.defragmented = self.defragmented + self.dots
                    
    def checksum(self):
        self.result = sum(i * int(val) for i, val in enumerate(self.defragmented) if val != '.')

    def print_results(self):
        print(f"Checksum: {self.result}")

if __name__ == '__main__':
    start_time = time.time()
    advent = AdventOfCodeD9()
    advent.defragment()
    advent.checksum()
    advent.print_results()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Program ran for {elapsed_time:.4f} seconds")