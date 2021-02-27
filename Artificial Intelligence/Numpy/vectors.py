import numpy as np

vec_a = np.array([3, 2])
vec_b = np.array([-6, 0])

scalar = 3

vec_3d = np.array([5, 5, 5])
vec_4d = np.array([3, 0, 9, 1])
vec42d = np.linspace(-1.0, 1.0, num=42)  # vector size 1x42


# Vector Subtract
vec_sub = vec_a - vec_b  # [9, 2]

# Vector Addition
vec_sum = vec_a + vec_b  # [-3, 2]

# Vector DorProduct
vec_dot = np.dot(vec_a, vec_b)  # [-18]

# Vector Divide
vec_div = np.dot(vec_a, np.divide(1, 3))  # [1, 0.6]
