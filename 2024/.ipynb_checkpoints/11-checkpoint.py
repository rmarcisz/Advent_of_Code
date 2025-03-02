import time

class AdventOfCodeD11:
    def __init__(self, input_path):
        self._load_data(input_path)
        self._dict_preload()
    
    def _load_data(self, input_path):
        try:
            with open(input_path) as file:
                self.data = file.readline().split(' ')
                self.data = [int(x) for x in self.data]
        except (FileNotFoundError, ValueError, IndexError) as e:
            print(f'Error reading or parsing input file: {e}')
            raise

    def part1(self):
        new_list = []
        for elem in self.data:
            if elem == 0:
                new_list.append(1)
            elif len(str(elem)) % 2 == 0:
                digits_num = len(str(elem))
                first = int(str(elem)[:int(digits_num/2)])
                second = int(str(elem)[int(digits_num/2):])
                new_list.append(first)
                new_list.append(second)
            else:
                new_list.append(elem*2024)
        self.data = new_list.copy()

    def _dict_preload(self):
        self.dictionary = {}
        for elem in self.data:
            if elem in self.dictionary:
                self.dictionary[elem] += 1
            else:
                self.dictionary[elem] = 1
    
    def part2(self):
        new_dict = {}
        for key, value in self.dictionary.items():
            if key == 0:
                if 1 in new_dict:
                    new_dict[1] += value
                else:
                    new_dict[1] = value
            elif len(str(key)) % 2 == 0:
                digits_num = len(str(key))
                first = int(str(key)[:int(digits_num/2)])
                second = int(str(key)[int(digits_num/2):])
                if first in new_dict:
                    new_dict[first] += value
                else:
                    new_dict[first] = value
                if second in new_dict:
                    new_dict[second] += value
                else:
                    new_dict[second] = value
            else:
                if key*2024 in new_dict:
                    new_dict[key*2024] += value
                else:
                    new_dict[key*2024] = value
        self.dictionary = new_dict.copy()
            
    def print_results(self):
        print(sum(self.dictionary.values()))

if __name__ == '__main__':
    start_time = time.time()
    advent = AdventOfCodeD11('inputs/11.txt')
    for i in range(75):
        advent.part2()
    advent.print_results()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f'Program ran for {elapsed_time:.4f} seconds')