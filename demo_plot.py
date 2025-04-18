from hypersim import generate_hyperspectral_cube, plot_cube_slices, plot_spectrum

cube, wavelengths = generate_hyperspectral_cube()
plot_cube_slices(cube, wavelengths)
plot_spectrum(cube, wavelengths, 50, 50)

