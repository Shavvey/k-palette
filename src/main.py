import kpalette.kmeans as k
import pathlib as p

import manim as mn
import numpy as np


def main():
    arr = k.get_pixel_data(p.Path("images/image.png"))
    print(arr.shape)
    arr_shape = arr.shape
    print(np.array(arr.reshape(arr_shape[0] * arr_shape[1], 3)))


class Plot3DPoints(mn.ThreeDScene):
    def construct(self):
        # 1. Set up 3D Axes
        axes = mn.ThreeDAxes(
            x_range=[0, 255, 1],
            y_range=[0, 255, 1],
            z_range=[0, 255, 1],
            x_length=256,
            y_length=256,
            z_length=256,
        )
        arr = k.get_pixel_data(p.Path("images/image.png"))
        print(arr.shape)
        arr_shape = arr.shape

        # 2. Define Points (Example: A Helix)
        # Each point is a numpy array [x, y, z]
        num_points = arr_shape[0] * arr_shape[1]
        points = np.array(arr.reshape(arr_shape[0] * arr_shape[1], 3))

        # 3. Create Dots for each point
        dots = mn.VGroup(
            *[mn.Dot3D(point=axes.c2p(p[0], p[1], p[2]), radius=0.05) for p in points]
        )

        # 4. Set Camera
        self.set_camera_orientation(phi=75 * mn.DEGREES, theta=30 * mn.DEGREES)
        self.add(axes)

        # 5. Animate
        self.play(mn.Create(dots))
        self.begin_3dillusion_camera_rotation(rate=0.2)
        self.wait(2)
        self.stop_3dillusion_camera_rotation()


if __name__ == "__main__":
    main()
