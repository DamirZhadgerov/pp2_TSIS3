import math

def sphere_volume(radius):
    volume = (4/3) * math.pi * radius**3
    return volume

# Read the radius of the sphere from the user
radius = float(input("Enter the radius of the sphere: "))

# Calculate the volume of the sphere
volume = sphere_volume(radius)

# Display the volume of the sphere
print(f"The volume of the sphere with radius {radius} is {volume:.2f} cubic units.")
