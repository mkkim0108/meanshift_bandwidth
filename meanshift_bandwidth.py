# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1cJAoBbDVb_pwFem2JIN_rX43s3wQOval
"""

# Reimporting necessary libraries and recreating the code due to environment reset

from sklearn.cluster import MeanShift, estimate_bandwidth
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
import numpy as np

# Create data (create 2D datasets that can be clustered well)
centers = [[1, 1], [5, 5], [9, 9]]  # Specify three center points
X, _ = make_blobs(n_samples=300, centers=centers, cluster_std=0.6)

# Wide bandwidth case (quantile value set large)
bandwidth_wide = estimate_bandwidth(X, quantile=0.8)
ms_wide = MeanShift(bandwidth=bandwidth_wide)
ms_wide.fit(X)
labels_wide = ms_wide.labels_
cluster_centers_wide = ms_wide.cluster_centers_

# Properly set bandwidth case (set the quantile value appropriately)
bandwidth_optimal = estimate_bandwidth(X, quantile=0.2)
ms_optimal = MeanShift(bandwidth=bandwidth_optimal)
ms_optimal.fit(X)
labels_optimal = ms_optimal.labels_
cluster_centers_optimal = ms_optimal.cluster_centers_

# Automatically bandwidth-set cases (automatic bandwidth estimation of MeanShift itself)
ms_auto = MeanShift()
ms_auto.fit(X)
labels_auto = ms_auto.labels_
cluster_centers_auto = ms_auto.cluster_centers_

# Visualization of results (if bandwidth is wide, if appropriate, auto-set)

plt.figure(figsize=(18, 5))

# If the bandwidth is wide
plt.subplot(1, 3, 1)
plt.scatter(X[:, 0], X[:, 1], c=labels_wide, cmap='viridis', marker='o', s=30, label="Data Points")
plt.scatter(cluster_centers_wide[:, 0], cluster_centers_wide[:, 1], c='red', marker='x', s=100, label="cluster center")
plt.title('bandwidth : 0.8 Mean Shift')
plt.xlabel('X ')
plt.ylabel('Y ')
plt.legend()

# Bandwidth is appropriate
plt.subplot(1, 3, 2)
plt.scatter(X[:, 0], X[:, 1], c=labels_optimal, cmap='viridis', marker='o', s=30, label="Data Points")
plt.scatter(cluster_centers_optimal[:, 0], cluster_centers_optimal[:, 1], c='red', marker='x', s=100, label="cluster center")
plt.title('bandwidth : 0.2 Mean Shift')
plt.xlabel('X ')
plt.ylabel('Y ')
plt.legend()

#Automatic bandwidth estimation
plt.subplot(1, 3, 3)
plt.scatter(X[:, 0], X[:, 1], c=labels_auto, cmap='viridis', marker='o', s=30, label="Data Points")
plt.scatter(cluster_centers_auto[:, 0], cluster_centers_auto[:, 1], c='red', marker='x', s=100, label="cluster center")
plt.title('bandwidth : auto Mean Shift')
plt.xlabel('X ')
plt.ylabel('Y ')
plt.legend()


plt.show()