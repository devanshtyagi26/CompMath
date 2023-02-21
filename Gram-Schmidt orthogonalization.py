import numpy as np

# Define the vectors that form the basis of the vector space
v1 = np.array([1, 1, 0])
v2 = np.array([1, 0, 1])
v3 = np.array([0, 1, 1])

# Define a function to perform the Gram-Schmidt orthogonalization process
def gram_schmidt(vectors):
    # Normalize the first vector
    basis = [vectors[0] / np.linalg.norm(vectors[0])]
    
    # Loop over the remaining vectors and orthogonalize them with respect to the
    # previous ones in the basis
    for v in vectors[1:]:
        # Compute the projection of v onto each vector in the basis
        projections = [np.dot(v, b) * b for b in basis]
        
        # Subtract the projections from v to orthogonalize it with respect to the basis
        v_orthogonal = v - np.sum(projections, axis=0)
        
        # Normalize the resulting orthogonal vector and add it to the basis
        basis.append(v_orthogonal / np.linalg.norm(v_orthogonal))
        
    return basis

# Use the gram_schmidt function to find the orthonormal basis of the vector space
basis = gram_schmidt([v1, v2, v3])

# Print the orthonormal basis vectors
for b in basis:
    print(b)