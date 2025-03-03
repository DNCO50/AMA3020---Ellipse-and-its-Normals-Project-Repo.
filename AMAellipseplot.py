import numpy as np
import matplotlib.pyplot as pl
import matplotlib.cm as cm

# a and b for the ellipse
a = 7
b = 4

#Arrays for x0 and y0 ya bich
x0_values = np.linspace(-2, 2, 2)  
y0_values = np.linspace(-2, 2, 2)  

#Parametrising for the ellipse
t = np.linspace(0, 2*np.pi, 800)
x_ellipse = a * np.cos(t)
y_ellipse = b * np.sin(t)

#set up a grid to plot the hyperbola - this was AI magic I am not gonna lie
x_range = np.linspace(-a * 3, a * 3, 800)
y_range = np.linspace(-b * 3, b * 3, 800)
X, Y = np.meshgrid(x_range, y_range)




#Starting to plot


#Plot the ellipse
pl.figure(figsize=(8, 6))
pl.plot(x_ellipse, y_ellipse, label=r'Ellipse: $\frac{x^2}{a^2}+\frac{y^2}{b^2}=1$', color='blue', linewidth=2)

#Evolute of the ellipse:  This shit can be change, in fact it must be changed at some point, because this is fucked
denominator = np.sqrt(a**2 * np.sin(t)**2 + b**2 * np.cos(t)**2)
x_evolute = a * np.cos(t) - ((a**2 - b**2) * (np.sin(t)**2 * np.cos(t))) / denominator
y_evolute = b * np.sin(t) - ((a**2 - b**2) * (np.sin(t) * np.cos(t)**2)) / denominator
pl.plot(x_evolute, y_evolute, label='Evolute of the Ellipse', color='magenta', linewidth=2)


#For the colours of dem hyperbola dere
num_curves = len(x0_values) * len(y0_values)
colours = cm.viridis(np.linspace(0, 1, num_curves))  # Use the 'viridis' colormap

#  plot the hyperbola for each x0, y0 pairing
curve_index = 0
for x0 in x0_values:
    for y0 in y0_values:
        # implicit equation function value computinggg
        F = X * Y * (a**2 - b**2) - a**2 * x0 * Y + b**2 * y0 * X
        
        # Plot the implicit curve using contour with a unique color
        contour = pl.contour(X, Y, F, levels=[0], colors=[colours[curve_index]])

        # Plot the (x0, y0) point with the same color
        pl.scatter(x0, y0, color=colours[curve_index], edgecolors='black', s=50, label=f'({x0:.1f}, {y0:.1f})')

        curve_index += 1  # Move to the next color




pl.xlabel('x')
pl.ylabel('y')
pl.title('Ellipse, Evolute, and Multiple Hyperbolas with Corresponding (x0, y0) Points')
pl.legend()
pl.grid(True)
pl.axis('equal')
pl.show()



