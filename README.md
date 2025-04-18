# Hyperspectral cube

A Python package to simulate hyperspectral imaging of galaxies for educational and prototyping purposes.

## Features

- Generate 3D data cubes with galaxy spectral signatures
- Visualize wavelength slices
- Plot pixel-level spectra

## Installation

```bash
pip install .


##Usag
from hypersim import generate_hyperspectral_cube, plot_cube_slices, plot_spectrum

cube, wavelengths = generate_hyperspectral_cube()
plot_cube_slices(cube, wavelengths)
plot_spectrum(cube, wavelengths, 50, 50)
