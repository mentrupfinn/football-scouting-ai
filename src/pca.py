import numpy as np

def pca(X, n_components=2):

    X = np.asarray(X, dtype=float)

    # 1. Zentrieren
    X_centered = X - np.mean(X, axis=0)

    # 2. Kovarianzmatrix
    cov_matrix = np.cov(X_centered, rowvar=False)

    # 3. Eigenwerte/-vektoren
    eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)

    # 4. Sortieren
    sorted_idx = np.argsort(eigenvalues)[::-1]

    eigenvalues = eigenvalues[sorted_idx]
    eigenvectors = eigenvectors[:, sorted_idx]

    # 5. Komponenten wählen
    components = eigenvectors[:, :n_components]

    # 6. Projektion
    X_pca = X_centered @ components

    return X_pca, eigenvalues, eigenvectors