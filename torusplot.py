import numpy as np
import matplotlib.pyplot as plt


def torus_plot(r1=2, r2=1, resolution=40, color='#808080'):
    def immerse_torus(u, v):
        alpha = r1 + r2*np.cos(v)
        return \
            alpha * np.cos(u), \
            alpha * np.sin(u), \
            r2 * np.sin(v)

    f = plt.figure()
    ax3 = f.add_subplot(projection='3d')

    u, v = np.meshgrid(
        np.linspace(-np.pi, np.pi, resolution),
        np.linspace(-np.pi, np.pi, resolution),
    )

    torus = immerse_torus(u, v)
    ax3.plot_wireframe(*torus, lw=.5, color=color)

    size = r1 + r2
    for lim in [ax3.set_xlim, ax3.set_ylim, ax3.set_zlim]:
        lim(-size, size)

    ax3.axis('off')

    def plot_curve(curve, *args, **kwargs):
        c = np.atleast_2d(curve)
        x, y, z = immerse_torus(c[:, 0], c[:, 1])
        ax3.plot(x, y, z, *args, **kwargs)

    return plot_curve


if __name__ == "__main__":
    tp = torus_plot(
        r1=2,  # larger radius
        r2=1,  # smaller radius
        resolution=50,  # number of mesh points is resolution^2
    )

    # The function tp accepts an array of shape n x 2
    example_path = np.load("example.npy")
    tp(example_path, color='blue')

    zero = np.zeros(2)
    tp(zero, 'o', color='black')

    r = 0.5
    phi = np.linspace(-np.pi, np.pi, 100)
    a_circle = r*np.array([np.cos(phi), np.sin(phi)]).T
    tp(a_circle, '--', color='orange', lw=3)
    plt.show()
