import numpy as np
import matplotlib.pyplot as plt

def baker_map(x, y):
    if x < 0.5:
        return 2 * x, y / 2
    else:
        return 2 * (1 - x), 1 - (y / 2)

np.random.seed(0) 
points = np.random.rand(1000, 2)

mapped_points = np.array([baker_map(x, y) for x, y in points])

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.scatter(points[:, 0], points[:, 1], color='blue', s=1)
plt.title('Original Points')
plt.xlim(0, 1)
plt.ylim(0, 1)

plt.subplot(1, 2, 2)
plt.scatter(mapped_points[:, 0], mapped_points[:, 1], color='red', s=1)
plt.title('Mapped Points by Baker Map')
plt.xlim(0, 1)
plt.ylim(0, 1)

plt.tight_layout()
plt.show()
