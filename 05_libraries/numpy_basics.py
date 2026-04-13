# ============================================================
#  NumPy Basics — python-everything-you-need-to-know
# ============================================================

import numpy as np

print("=" * 50)
print("  NumPy Basics")
print("=" * 50)

# ------ 1. Array Creation ------
print("\n[1] Array Creation")
arr1D = np.array([10, 20, 30, 40, 50])
arr2D = np.array([[1, 2, 3], [4, 5, 6]])
zeros  = np.zeros((3, 3))
ones   = np.ones((2, 4))
eye    = np.eye(3)
rand   = np.random.randint(0, 100, (4, 4))

print("1D Array:", arr1D)
print("2D Array:\n", arr2D)
print("Zeros:\n", zeros)
print("Identity:\n", eye)
print("Random 4x4:\n", rand)

# ------ 2. Array Properties ------
print("\n[2] Array Properties")
print("Shape:", rand.shape)
print("Dtype:", rand.dtype)
print("Dimensions:", rand.ndim)
print("Size:", rand.size)

# ------ 3. Indexing & Slicing ------
print("\n[3] Indexing & Slicing")
print("Element [1][2]:", arr2D[1][2])
print("Slice rand[0:2, 1:3]:\n", rand[0:2, 1:3])
print("Last row:", rand[-1])

# ------ 4. Math Operations ------
print("\n[4] Math Operations")
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print("a + b:", a + b)
print("a * b:", a * b)
print("Dot product:", np.dot(a, b))
print("Sum:", np.sum(rand))
print("Mean:", np.mean(rand))
print("Std Dev:", np.std(rand))
print("Max:", np.max(rand))
print("Min:", np.min(rand))

# ------ 5. Reshape & Transpose ------
print("\n[5] Reshape & Transpose")
r = np.arange(1, 13)           # [1, 2, ..., 12]
reshaped = r.reshape(3, 4)
print("Original:", r)
print("Reshaped (3x4):\n", reshaped)
print("Transposed:\n", reshaped.T)

# ------ 6. Boolean Masking ------
print("\n[6] Boolean Masking")
data = np.array([15, 42, 7, 88, 23, 61])
mask = data > 30
print("Data:", data)
print("Mask (> 30):", mask)
print("Filtered:", data[mask])

# ------ 7. Linear Space ------
print("\n[7] linspace & arange")
print("linspace(0, 1, 6):", np.linspace(0, 1, 6))
print("arange(0, 20, 4):", np.arange(0, 20, 4))

# ------ 8. Matrix Multiplication ------
print("\n[8] Matrix Multiplication")
m1 = np.random.randint(1, 5, (2, 3))
m2 = np.random.randint(1, 5, (3, 2))
print("M1:\n", m1)
print("M2:\n", m2)
print("M1 @ M2:\n", m1 @ m2)

print("\n✅ NumPy tutorial complete!")
