import random
import copy
import json


class SchoolScheduleGeneticAlgorithm:
    def __init__(self, num_days, num_classes, num_lessons_per_day, lessons_per_day, other_lessons_per_day, teachers,
                 specialized_rooms):
        self.num_days = num_days
        self.num_classes = num_classes
        self.num_lessons_per_day = num_lessons_per_day
        self.lessons_per_day = lessons_per_day
        self.other_lessons_per_day = other_lessons_per_day
        self.teachers = teachers
        self.specialized_rooms = specialized_rooms
        self.population = []

    def initialize_population(self, population_size):
        for _ in range(population_size):
            classes_schedule = []
            for class_index in range(self.num_classes):
                class_schedule = []
                for _ in range(self.num_days):
                    day_schedule = []
                    if class_index == 0:
                        class_teacher = 'Вчитель1'
                        for _ in range(4):
                            lesson = random.choice(self.lessons_per_day)
                            while lesson in [day[0] for day in day_schedule]:
                                lesson = random.choice(self.lessons_per_day)
                            day_schedule.append((lesson, class_teacher))
                    else:
                        class_teacher = 'Вчитель2'
                        for _ in range(4):
                            lesson = random.choice(self.lessons_per_day)
                            while lesson in [day[0] for day in day_schedule]:
                                lesson = random.choice(self.lessons_per_day)
                            day_schedule.append((lesson, class_teacher))
                    for _ in range(self.num_lessons_per_day - 4):
                        lesson = random.choice(self.other_lessons_per_day)
                        while lesson[1] in [class_teacher] + self.teachers[:2] or lesson[0] in [day[0] for day in
                                                                                                day_schedule]:
                            lesson = random.choice(self.other_lessons_per_day)
                        day_schedule.append(lesson)
                    random.shuffle(day_schedule)
                    class_schedule.append(day_schedule)
                classes_schedule.append(class_schedule)
            self.population.append(classes_schedule)

    def mutate(self, schedule):
        mutated_schedule = copy.deepcopy(schedule)
        for day_schedule in mutated_schedule:
            for lesson_index in range(self.num_lessons_per_day):
                if random.random() < mutation_rate:
                    lesson = random.choice(self.other_lessons_per_day)
                    day_schedule[lesson_index] = lesson
        return mutated_schedule

    def crossover(self, schedule1, schedule2):
        crossover_point = random.randint(1, self.num_days - 1)
        crossed_schedule = []
        for day_index in range(len(schedule1)):
            if day_index < crossover_point:
                crossed_schedule.append(schedule1[day_index])
            else:
                crossed_schedule.append(schedule2[day_index])
        return crossed_schedule

    def evaluate_schedule(self, schedule):
        total_teacher_workload = {teacher: 0 for teacher in self.teachers}
        total_specialized_rooms_usage = {room: 0 for room in self.specialized_rooms}

        for class_schedule in schedule:
            for day_schedule in class_schedule:
                for lesson in day_schedule:
                    if lesson:
                        teacher = None
                        if len(lesson) == 2:
                            teacher = lesson[1]
                        if teacher:
                            total_teacher_workload[teacher] += 1

        return total_teacher_workload, total_specialized_rooms_usage

    def evolve(self, population_size, num_generations, mutation_rate, crossover_rate):
        self.initialize_population(population_size)
        best_schedule = None
        best_evaluation = float('-inf')
        for generation in range(num_generations):
            evaluations = []
            for schedule in self.population:
                total_teacher_workload, total_specialized_rooms_usage = self.evaluate_schedule(schedule)
                evaluation = sum(total_teacher_workload.values()) + sum(total_specialized_rooms_usage.values())
                evaluations.append((schedule, evaluation))
                if evaluation > best_evaluation:
                    best_evaluation = evaluation
                    best_schedule = schedule

            new_population = []
            while len(new_population) < population_size:
                if random.random() < crossover_rate:
                    parent1 = random.choice(self.population)
                    parent2 = random.choice(self.population)
                    child = self.crossover(parent1, parent2)
                    new_population.append(child)
                else:
                    parent = random.choice(self.population)
                    child = self.mutate(parent)
                    new_population.append(child)

            self.population = new_population

            print(f"Generation {generation + 1}, Best Schedule: {best_schedule}, Fitness: {best_evaluation}")
        return best_schedule


num_days = 5
num_classes = 2
num_lessons_per_day = 5
lessons_per_day = [
    ('Математика'),
    ('Українська мова'),
    ('Природознавство'),
    ('Історія'),
]
other_lessons_per_day = [
    ('Географія', 'Вчитель3'),
    ('Література', 'Вчитель4'),
    ('Англійська мова', 'Вчитель5')
]
teachers = ['Вчитель1', 'Вчитель2', 'Вчитель3', 'Вчитель4', 'Вчитель5']
specialized_rooms = ['Кабінет1', 'Кабінет2', 'Кабінет3']

mutation_rate = 0.1
crossover_rate = 0.8
population_size = 10
num_generations = 10

school_schedule_algorithm = SchoolScheduleGeneticAlgorithm(num_days, num_classes, num_lessons_per_day,
                                                           lessons_per_day, other_lessons_per_day, teachers,
                                                           specialized_rooms)

best_schedule = school_schedule_algorithm.evolve(population_size, num_generations, mutation_rate, crossover_rate)


def print_schedule(schedule):
    for class_index, class_schedule in enumerate(schedule):
        print(f'Class {class_index + 1}:')
        for day_index, day_schedule in enumerate(class_schedule):
            print(f'Day {day_index + 1}:')
            for lesson_index, (lesson, teacher) in enumerate(day_schedule):
                if lesson:
                    print(f'Lesson {lesson_index + 1}: {lesson}, Teacher: {teacher}')
                else:
                    print(f'Lesson {lesson_index + 1}: No lesson scheduled')
            print()


print_schedule(best_schedule)


def save_schedule_to_json(schedule, filename):
    with open(filename, 'w') as f:
        json.dump(schedule, f, indent=4)


save_schedule_to_json(best_schedule, 'best_schedule.json')
