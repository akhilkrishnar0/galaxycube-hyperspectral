import numpy as np

def generate_hyperspectral_cube(height=100, width=100, wavelengths=None, noise_level=0.1):
    if wavelengths is None:
        wavelengths = np.array([150, 230, 355, 475, 622, 763, 905])  # nm
    n_bands = len(wavelengths)

    x = np.linspace(-1, 1, width)
    y = np.linspace(-1, 1, height)
    X, Y = np.meshgrid(x, y)
    galaxy_core = np.exp(-(X**2 + Y**2) / (2 * 0.2**2))

    spectrum = np.exp(-(wavelengths - 700)**2 / (2 * 200**2))

    cube = np.zeros((n_bands, height, width))
    for i in range(n_bands):
        cube[i] = galaxy_core * spectrum[i] + noise_level * np.random.rand(height, width)

    return cube, wavelengths

