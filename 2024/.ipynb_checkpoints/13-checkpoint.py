import numpy as np
import time
import re

class AdventOfCodeD13:
    def __init__(self, input_path):
        self._load_data(input_path)
        self.result = 0
    
    def _load_data(self, input_path):
        try:
            with open(input_path) as file:
                self.data = file.read().strip().split('\n\n')
        except (FileNotFoundError, ValueError, IndexError) as e:
            print(f'Error reading or parsing input file: {e}')
            raise

    def counting(self):
        for equation in self.data:
            equation = re.split(r"[+,\n=]", equation)
            A = np.array([[int(equation[1]), int(equation[5])],[int(equation[3]), int(equation[7])]])
            B = np.array([int(equation[9]), int(equation[11])])
            solution = np.linalg.solve(A, B)
            tolerance = 0.0001
            if abs(solution[0] - round(solution[0])) < tolerance and abs(solution[1] - round(solution[1])) < tolerance:
                self.result += (solution[0]*3 + solution[1])
                
    def counting_10000000000000(self):
        for equation in self.data:
            equation = re.split(r"[+,\n=]", equation)
            A = np.array([[int(equation[1]), int(equation[5])],[int(equation[3]), int(equation[7])]])
            B = np.array([int(equation[9]) + 10000000000000, int(equation[11]) + 10000000000000])
            solution = np.linalg.solve(A, B)
            tolerance = 0.0001
            if abs(solution[0] - round(solution[0])) < tolerance and abs(solution[1] - round(solution[1])) < tolerance:
                self.result += (solution[0]*3 + solution[1])
    
    def print_results(self):
        print(self.result)

if __name__ == '__main__':
    start_time = time.time()
    advent = AdventOfCodeD13('inputs/13.txt')
    advent.counting()
    advent.print_results()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f'Program ran for {elapsed_time:.4f} seconds')