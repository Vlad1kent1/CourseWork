import random
import math
import matplotlib.pyplot as plt
import numpy as np


class AntColony:
    def __init__(self, distances, n_ants, evaporation_rate, alpha, beta):
        self.distances = distances
        self.n_ants = n_ants
        self.evaporation_rate = evaporation_rate
        self.alpha = alpha
        self.beta = beta
        self.n_cities = len(distances)
        self.pheromone = [[1 / (self.n_cities * self.n_cities) for _ in range(self.n_cities)] for _ in
                          range(self.n_cities)]

    def update_pheromone(self, paths, distances):
        for i in range(self.n_cities):
            for j in range(self.n_cities):
                self.pheromone[i][j] *= (1 - self.evaporation_rate)
        for path, distance in zip(paths, distances):
            for i in range(len(path) - 1):
                self.pheromone[path[i]][path[i + 1]] += 1.0 / distance

    def ant_path(self):
        paths = []
        distances = []
        for ant in range(self.n_ants):
            visited = set()
            current_city = random.randint(0, self.n_cities - 1)
            path = [current_city]
            total_distance = 0.0
            visited.add(current_city)
            while len(visited) < self.n_cities:
                probabilities = self.calculate_probabilities(path, visited)
                next_city = self.choose_next_city(probabilities, visited)
                path.append(next_city)
                visited.add(next_city)
                total_distance += self.distances[current_city][next_city]
                current_city = next_city
            total_distance += self.distances[path[-1]][path[0]]
            paths.append(path)
            distances.append(total_distance)
        return paths, distances

    def calculate_probabilities(self, path, visited):
        current_city = path[-1]
        unvisited = [city for city in range(self.n_cities) if city not in visited or city == path[0]]
        probabilities = []
        total = 0
        for city in unvisited:
            distance = self.distances[current_city][city]
            if distance != 0:  # Додана перевірка на нуль
                total += math.pow(self.pheromone[current_city][city], self.alpha) * math.pow(1.0 / distance, self.beta)
        for city in unvisited:
            distance = self.distances[current_city][city]
            if distance != 0:  # Додана перевірка на нуль
                probability = math.pow(self.pheromone[current_city][city], self.alpha) * math.pow(1.0 / distance,
                                                                                                  self.beta) / total
                probabilities.append((city, probability))
        return probabilities

    def choose_next_city(self, probabilities, visited):
        probabilities.sort(key=lambda x: x[1], reverse=True)
        for city, probability in probabilities:
            if city not in visited:
                return city
        return None


def generate_distances(n_cities):
    distances = [[random.randint(10, 100) for _ in range(n_cities)] for _ in range(n_cities)]
    for i in range(n_cities):
        distances[i][i] = 0
    return distances


def plot_map(best_path, cities_amount):
    best_x = []
    best_y = []
    fig, ax = plt.subplots(figsize=(8, 8))

    # Coordinates of center point
    cx, cy = 0.5, 0.5

    # Radius of the circle
    r = 0.4

    # Calculate the angles of the vertices in the polygon
    angles = np.linspace(0, 2 * np.pi, cities_amount, endpoint=False)

    # Calculate the x, y coordinates of the vertices
    x = r * np.cos(angles) + cx
    y = r * np.sin(angles) + cy

    for i in range(cities_amount):
        for j in range(cities_amount):
            if i < j:
                ax.plot([x[i], x[j]], [y[i], y[j]], 'k-', linewidth=0.3, alpha=0.4)

    for i in range(cities_amount):
        if i == best_path[0]:
            circle = plt.Circle((x[i], y[i]), 0.018, color='#D2691E', zorder=10)
        else:
            circle = plt.Circle((x[i], y[i]), 0.018, color='#000080', zorder=10)

        ax.add_artist(circle)
        ax.text(x[i], y[i], str(i), fontsize=11, color='white', fontweight='bold', zorder=10, ha='center', va='center')
        best_x = [x[i] for i in best_path]
        best_y = [y[i] for i in best_path]

    ax.quiver(best_x[:-1], best_y[:-1], np.diff(best_x), np.diff(best_y),
              angles='xy', scale_units='xy', scale=1, color='red', alpha=0.7, width=0.0055,
              headlength=7, headwidth=4, headaxislength=5, )

    ax.plot(best_x + [best_x[0]], best_y + [best_y[0]], 'o-', color='red', linewidth=0.7, alpha=0.7,
            label='Optimal Path')
    ax.scatter(x, y, zorder=6, s=30, color='red', label='Cities')
    ax.legend(loc='best', fontsize=12)
    ax.set_xlabel('X', fontsize=12)
    ax.set_ylabel('Y', fontsize=12)
    ax.set_title('Traveling Salesman Problem', fontsize=16)
    plt.tight_layout()
    plt.show()


def main():
    n_cities = random.randint(25, 35)
    distances = generate_distances(n_cities)
    n_ants = random.randint(10, 100)
    evaporation_rate = 0.1
    alpha = 1
    beta = 2
    colony = AntColony(distances, n_ants, evaporation_rate, alpha, beta)

    best_paths = []
    best_distances = []
    for i in range(n_ants):
        paths, distances = colony.ant_path()
        colony.update_pheromone(paths, distances)
        best_path_index = distances.index(min(distances))
        best_path = paths[best_path_index]
        best_distance = distances[best_path_index]
        best_paths.append(best_path)
        best_distances.append(best_distance)
        print(f"Iteration {i + 1}: Best Path: {best_path}, Distance: {best_distance}")

    best_path_index = best_distances.index(min(best_distances))
    best_path = best_paths[best_path_index]
    print(f"\nBest Path Overall: {best_path}, Distance: {min(best_distances)}")
    plot_map(best_path, n_cities)

if __name__ == "__main__":
    main()
