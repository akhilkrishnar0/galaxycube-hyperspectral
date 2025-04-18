import matplotlib.pyplot as plt

def plot_cube_slices(cube, wavelengths):
    n_bands = len(wavelengths)
    fig, axs = plt.subplots(1, n_bands, figsize=(18, 3))
    for i in range(n_bands):
        axs[i].imshow(cube[i], origin='lower', cmap='magma')
        axs[i].set_title(f'{wavelengths[i]} nm')
        axs[i].axis('off')
    plt.suptitle("Simulated Hyperspectral Galaxy Slices", fontsize=16)
    plt.tight_layout()
    plt.show()

def plot_spectrum(cube, wavelengths, x, y):
    pixel_spectrum = cube[:, y, x]
    plt.figure(figsize=(6, 4))
    plt.plot(wavelengths, pixel_spectrum, marker='o', color='dodgerblue')
    plt.xlabel("Wavelength (nm)")
    plt.ylabel("Flux (a.u.)")
    plt.title(f"Spectrum at pixel ({x}, {y})")
    plt.grid(True)
    plt.show()

