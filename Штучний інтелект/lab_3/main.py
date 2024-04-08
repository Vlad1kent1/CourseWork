import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans, AgglomerativeClustering
import time

# 2. Згенерувати тестову послідовність з N значень (для визначеності, можна
# покласти N≥1000), що є парами дійсних чисел на одиничному квадраті.
def generate_data(N):
    data = np.random.rand(N, 2)
    return data

# 3. Реалізувати допоміжну функцію для обчислення міри віддалі.
def distance(x1, x2):
    return np.linalg.norm(x1 - x2)

# 4. Реалізувати допоміжну функцію для виконання алгоритму кластеризації
# за методом К-середніх (англ. K-means).
def kmeans_clustering(data, n_clusters):
    model = KMeans(n_clusters=n_clusters)
    model.fit(data)
    centroids = model.cluster_centers_
    clusters = model.predict(data)
    return centroids, clusters

# 5. Реалізація методу ієрархічного кластеризації
def hierarchical_clustering(data, n_clusters):
    model = AgglomerativeClustering(n_clusters=n_clusters)
    clusters = model.fit_predict(data)
    return clusters

# Функція для обчислення середньо-зваженої оцінки розміру кластера згідно з заданою мірою відстані
def evaluate_clustering_quality(clusters, data, distance_measure):
    cluster_sizes = {}
    weighted_cluster_sizes = {}
    for cluster_id in np.unique(clusters):
        cluster_points = data[clusters == cluster_id]
        cluster_sizes[cluster_id] = len(cluster_points)
        weighted_cluster_sizes[cluster_id] = len(cluster_points) * np.mean(distance_measure(cluster_points, np.mean(cluster_points, axis=0)))
    total_weighted_size = sum(weighted_cluster_sizes.values())
    average_weighted_size = total_weighted_size / len(data)
    return average_weighted_size

# 6. Безпосередньо реалізувати кластеризацію даних двома методами та
# порівняти результати кластеризації.
def compare_clustering_methods(data, k):
    start_time = time.time()

    centroids_kmeans, clusters_kmeans = kmeans_clustering(data, k)
    time_kmeans = time.time() - start_time
    quality_kmeans = evaluate_clustering_quality(clusters_kmeans, data, distance)

    start_time = time.time()
    clusters_hierarchical = hierarchical_clustering(data, k)
    time_hierarchical = time.time() - start_time
    quality_hierarchical = evaluate_clustering_quality(clusters_hierarchical, data, distance)

    return centroids_kmeans, clusters_kmeans, clusters_hierarchical, time_kmeans, time_hierarchical, quality_kmeans, quality_hierarchical

# 7. Порівняйте кількість кластерів та якість кластеризації.
def main():
    # Генеруємо дані
    N = 1000
    data = generate_data(N)
    k = 3

    # Виконуємо кластеризацію
    centroids_kmeans, clusters_kmeans, clusters_hierarchical, time_kmeans, time_hierarchical, quality_kmeans, quality_hierarchical = compare_clustering_methods(data, k)

    # Виводимо результати
    print("K-means Clustering:")
    print("Number of clusters:", len(centroids_kmeans))
    print("Centroids:", centroids_kmeans)
    print("Time:", time_kmeans)
    print("Quality:", quality_kmeans)

    print("\nHierarchical Clustering:")
    print("Number of clusters:", len(np.unique(clusters_hierarchical)))
    print("Time:", time_hierarchical)
    print("Quality:", quality_hierarchical)

    # Візуалізація кластерів
    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.scatter(data[:, 0], data[:, 1], c=clusters_kmeans, cmap='viridis', s=20, alpha=0.5)
    plt.scatter(centroids_kmeans[:, 0], centroids_kmeans[:, 1], c='red', marker='s', label='K-means Centroids')
    plt.title('K-means Clustering')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.scatter(data[:, 0], data[:, 1], c=clusters_hierarchical, cmap='viridis', s=20, alpha=0.5)
    plt.title('Hierarchical Clustering')
    plt.xlabel('X')
    plt.ylabel('Y')

    plt.show()

if __name__ == "__main__":
    main()
