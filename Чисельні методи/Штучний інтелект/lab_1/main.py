import random
from copy import deepcopy
from datetime import datetime
from math import exp
import matplotlib.pyplot as plt

random.seed(datetime.now().timestamp())
START_TEMPERATURE = 30
FINAL_TEMPERATURE = 0.5
ALPHA = 0.98
STEPS_PER_CHANGE = 100


class Solution:
    conflicts: int
    decision: list

    def __init__(self,n):
        self.generate_start_placement(n)
        self.evaluation_of_the_decision()
        print(f"start solution is{self.decision}\nwith {self.conflicts} conflicts")
        print(f"start temperature is {START_TEMPERATURE}")
        self.print_solution()

    def evaluation_of_the_decision(self):
        self.conflicts = 0
        for i in range(len(self.decision)):
            j = i + 1
            while j < len(self.decision):
                if i + self.decision[i] == j + self.decision[j] or i - self.decision[i] == j - self.decision[j]:
                    self.conflicts += 1
                j += 1

    def print_solution(self):
        for i in range(len(self.decision)):
            line = ['0' for _ in range(len(self.decision))]
            line[self.decision[i] - 1] = 'Q'
            print(line)

    def change_solution(self):
        i = random.randint(0, len(self.decision) - 1)
        j = random.randint(0, len(self.decision) - 1)
        while j == i:
            j = random.randint(0, len(self.decision) - 1)
        self.decision[i], self.decision[j] = self.decision[j], self.decision[i]
        self.evaluation_of_the_decision()

    def generate_start_placement(self, n):
        placement = [i + 1 for i in range(n)]
        random_array = [random.randint(0, n - 1) for _ in range(n)]
        for i in range(n):
            placement[i], placement[random_array[i]] = placement[random_array[i]], placement[i]
        self.decision = placement

def algorithm(init_solution):
    # plt data
    temperature_array = []
    conflicts_array = []

    current_solution = deepcopy(init_solution)
    current_most_solution = deepcopy(init_solution)
    temperature = START_TEMPERATURE
    while temperature > FINAL_TEMPERATURE and current_most_solution.conflicts != 0:

        work_solution = deepcopy(current_solution)
        for i in range(STEPS_PER_CHANGE):

            work_solution.change_solution()


            if work_solution.conflicts < current_most_solution.conflicts:
                current_solution = deepcopy(work_solution)
                current_most_solution = deepcopy(work_solution)

                # plt data
                temperature_array.append(temperature)
                conflicts_array.append(work_solution.conflicts)
                continue
            if work_solution.conflicts < current_solution.conflicts or random.uniform(0, 1) <= exp(
                    -(work_solution.conflicts - current_solution.conflicts) / temperature):
                current_solution = work_solution

                # plt data
                temperature_array.append(temperature)
                conflicts_array.append(work_solution.conflicts)
        temperature *= ALPHA

    plt.title('Графік зміни температури')
    plt.xlabel('час')
    plt.plot(range(len(temperature_array)), temperature_array, label='Температура')
    plt.plot(range(len(conflicts_array)), conflicts_array, label='Кількість конфліктів')
    plt.legend()
    plt.grid(True)
    plt.show()
    return current_most_solution, temperature


N = 8
init_solution = Solution(N)
most_solution, final_temperature = algorithm(init_solution)
print(f"most solution is{most_solution.decision}\nwith {most_solution.conflicts} conflicts")
print(f"final temperature is {final_temperature}")
most_solution.print_solution()
