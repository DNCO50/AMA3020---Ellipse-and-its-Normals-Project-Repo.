import numpy as np
import matplotlib.pyplot as plt

#a and b for the ellipse
a = 7
b = 4

#Parametrisation for the ellipse
t = np.linspace(0, 2*np.pi, 800)
x_ellipse = a * np.cos(t)
y_ellipse = b * np.sin(t)

#Starting to plot
plt.figure(figsize=(8, 6))
plt.plot(x_ellipse, y_ellipse, label=r'Ellipse: $\frac{x^2}{a^2}+\frac{y^2}{b^2}=1$', color='blue', linewidth=2)

# Compute the evolute
x_evolute = (a**2 - b**2)/a * np.cos(t)**3
y_evolute = (a**2 - b**2)/b * np.sin(t)**3
plt.plot(x_evolute, y_evolute, label='Evolute of the Ellipse', color='magenta', linewidth=2)

#Choose a single point on the evolute
t0 = np.pi / 4
x0 = (a**2 - b**2)/a * np.cos(t0)**3
y0 = (a**2 - b**2)/b * np.sin(t0)**3

#Mark the point on the evolute
plt.scatter(x0, y0, color='red', edgecolors='black', s=80, zorder=5, label=f'Evolute Point: ({x0:.2f}, {y0:.2f})')

#Set up a grid for plotting the hyperbola
x_range = np.linspace(-a * 3, a * 3, 800)
y_range = np.linspace(-b * 3, b * 3, 800)
X, Y = np.meshgrid(x_range, y_range)

#Define the hyperbola using its implicit equation
F = X * Y * (a**2 - b**2) - a**2 * x0 * Y + b**2 * y0 * X

#hyperbola plot 
contour = plt.contour(X, Y, F, levels=[0], colors='green', linewidths=2, linestyles='--')
plt.clabel(contour, inline=True, fontsize=10)


plt.xlabel('x')
plt.ylabel('y')
plt.title('Ellipse, Evolute, and Hyperbola for a Point on the Evolute')
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.show()
