
# Hypersim

**Hypersim** is a Python package designed to simulate and visualize hyperspectral imaging of galaxies. The package allows you to generate synthetic 3D data cubes representing galaxy observations across different wavelengths, and visualize the data in both image slices and spectral form.
![hc](https://github.com/user-attachments/assets/8d7a7760-50a2-4423-9c60-15b4c7c92ba9)

## Features

- Generate synthetic 3D data cubes of galaxy hyperspectral data.
- Visualize wavelength-dependent image slices.
- Extract and plot spectra from specific pixels within the galaxy.

## Installation

To install the package locally, clone the repository and run the following command in your terminal:

```bash
pip install .
```

Or directly install via `pip` if hosted on GitHub:

```bash
pip install git+https://github.com/yourusername/hypersim.git
```

## Usage

To generate a hyperspectral cube and visualize it, use the following example code:

```python
from hypersim import generate_hyperspectral_cube, plot_cube_slices, plot_spectrum

# Generate the synthetic hyperspectral cube
cube, wavelengths = generate_hyperspectral_cube()

# Plot the 2D slices for each wavelength
plot_cube_slices(cube, wavelengths)

# Plot the spectrum for a pixel at coordinates (50, 50)
plot_spectrum(cube, wavelengths, 50, 50)
```

### Example Output

Running the above example code generates the following outputs:

1. **Hyperspectral Slices (Generated at different wavelengths)**  
   The plot below shows the 2D images of the galaxy at seven different wavelengths. The central galaxy core is visible, and each slice corresponds to a different wavelength band.

   ![Hyperspectral Slices](images/hyperspectral_slices.png)

2. **Pixel Spectrum at (50, 50)**  
   The plot below shows the spectrum of the galaxy at a specific pixel in the center of the galaxy. The x-axis represents the wavelength, and the y-axis shows the flux in arbitrary units.

   ![Pixel Spectrum](images/pixel_spectrum.png)

## How It Works

### `generate_hyperspectral_cube(height=100, width=100, wavelengths=None, noise_level=0.1)`
This function generates a synthetic hyperspectral data cube where each pixel represents the brightness at a given wavelength. The brightness profile is modeled as a Gaussian distribution, and each wavelength has a specific spectral energy distribution (SED).

- **Parameters:**
  - `height` (int): The height of the galaxy image.
  - `width` (int): The width of the galaxy image.
  - `wavelengths` (array-like): List of wavelengths in nm (default is `[150, 230, 355, 475, 622, 763, 905]`).
  - `noise_level` (float): The level of random noise added to the cube (default is `0.1`).

- **Returns:**
  - `cube` (3D numpy array): A `n_bands x height x width` array representing the hyperspectral cube.
  - `wavelengths` (array): The list of wavelengths used.

### `plot_cube_slices(cube, wavelengths)`
This function visualizes the hyperspectral cube by displaying each 2D slice for every wavelength in the cube.

- **Parameters:**
  - `cube` (3D numpy array): The hyperspectral data cube.
  - `wavelengths` (array): List of wavelengths corresponding to the cube slices.

### `plot_spectrum(cube, wavelengths, x, y)`
This function extracts and visualizes the spectral flux at a specific pixel in the hyperspectral cube.

- **Parameters:**
  - `cube` (3D numpy array): The hyperspectral data cube.
  - `wavelengths` (array): List of wavelengths corresponding to the cube slices.
  - `x`, `y` (int): The coordinates of the pixel from which the spectrum is to be extracted.

## License

Distributed under the MIT License. See `LICENSE` for more information.

```

---

