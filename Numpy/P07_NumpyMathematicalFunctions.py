import numpy as np

angles = np.array([0, 30, 45, 60, 90, 180, 360])

# Convert to radians and compute sine, cosine, and tangent
radians = np.radians(angles)
sine = np.sin(radians)
cosine = np.cos(radians)
tangent = np.tan(radians)

print("Sine:", sine)
print("Cosine:", cosine)
print("Tangent:", tangent)

# Compute inverse sine and convert to degrees
sineinv = np.arcsin(sine)
degrees = np.degrees(sineinv)

print("Inverse Sine (radians):", sineinv)
print("Inverse Sine (degrees):", degrees)

# Round the sine values to 4 decimal places
rounded_sine = np.round(sine, 4)

print("Rounded Sine:", rounded_sine)

# Round to the previous integer using floor
rounded_floor = np.floor(sine)

print("Rounded to Previous Integer:", rounded_floor)

# Round to the next integer using ceil
rounded_ceil = np.ceil(sine)

print("Rounded to Next Integer:", rounded_ceil)

