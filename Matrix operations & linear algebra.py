
import numpy as np

# Create matrix A and vector b
A = np.array([[2.0, 1.0],
              [1.0, 3.0]])

b = np.array([1.0, 2.0])

# Display matrix A
print("Matrix A:\n", A)

# Find transpose
print("\nTranspose A^T:\n", A.T)

# Find inverse
print("\nInverse A^-1:\n", np.linalg.inv(A))

# Find eigenvalues and eigenvectors
eigvals, eigvecs = np.linalg.eig(A)
print("\nEigenvalues:", np.round(eigvals, 4))
print("\nEigenvectors:\n", np.round(eigvecs, 4))

# Solve the equation Ax = b
x = np.linalg.solve(A, b)
print("\nSolve A x = b --> x:", np.round(x, 4))
