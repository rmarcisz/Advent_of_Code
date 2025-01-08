'''--- Day 5: Print Queue ---
Satisfied with their search on Ceres, the squadron of scholars suggests subsequently scanning the stationery stacks of sub-basement 17.

The North Pole printing department is busier than ever this close to Christmas, and while The Historians continue their search of this historically significant facility, an Elf operating a very familiar printer beckons you over.

The Elf must recognize you, because they waste no time explaining that the new sleigh launch safety manual updates won't print correctly. Failure to update the safety manuals would be dire indeed, so you offer your services.

Safety protocols clearly indicate that new pages for the safety manuals must be printed in a very specific order. The notation X|Y means that if both page number X and page number Y are to be produced as part of an update, page number X must be printed at some point before page number Y.

The Elf has for you both the page ordering rules and the pages to produce in each update (your puzzle input), but can't figure out whether each update has the pages in the right order.'''

class AdventOfCodeD5:
    def __init__(self):
        with open('inputs/5.txt') as data:
            self.data_l = [row.strip() for row in data]
        self.rules = [elem for elem in self.data_l if '|' in elem]
        self.updates_raw = [elem.split(',') for elem in self.data_l if ',' in elem]
        self.updates = [[int(e) for e in elem] for elem in self.updates_raw]
        self.result = 0
        self.inresult = 0
        self.ruleset = {}
        for elem in self.rules:
            key = int(elem[0:2])
            value = int(elem[3:5])
            if key not in self.ruleset:
                self.ruleset[key] = []
            self.ruleset[key].append(value)
        self.correct_updates = []
        self.incorrect_updates = []

    def check_validity(self, update):
        for i, elem in enumerate(update):
            for j in range(i):
                if update[j] in self.ruleset.get(elem, []):
                    return False
        return True
    
    def check_updates(self):
        for update in self.updates:
            if self.check_validity(update):
                self.correct_updates.append(update)
            else:
                self.incorrect_updates.append(update)
                
    def fix_incorrect(self):
        for update in self.incorrect_updates:
            while not self.check_validity(update):
                for i, elem in enumerate(update):
                    for j in range(i):
                        if update[j] in self.ruleset.get(elem, []):
                            update[i], update[j] = update[j], update[i]
                            break
                            
    def get_numbers(self):
        for update in self.correct_updates:
            self.result += update[len(update) // 2]

    def get_innumbers(self):
        for update in self.incorrect_updates:
            self.inresult += update[len(update) // 2]

    def print_results(self):
        print("Correct result:", self.result)
        print("After fixing incorrects result:", self.inresult)

if __name__ == '__main__':
    advent = AdventOfCodeD5()
    advent.check_updates()
    advent.get_numbers()
    advent.fix_incorrect()
    advent.get_innumbers()
    advent.print_results()