import kpalette.kmeans as k
import pathlib as p
import math as m

from manim import *
import manim.typing as mtyp
import numpy as np
from PIL import Image

K_VAL = 3
DEF_INSTITIAL_WAIT = 1
MIN_SENTINEL = 1 << 32


def main():
    pass


def distance(p1: mtyp.Point3DLike, p2: mtyp.Point3DLike) -> float:
    return m.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2)


class Plot3DPoints(ThreeDScene):
    def construct(self):
        img = Image.open("images/image_resized.png")
        img.thumbnail((50, 50))  # Resize for performance
        pixels = np.array(img)
        # determine image shape (given internal numpy format of HxWxC, where C should be 3)
        h, w, c = pixels.shape

        # 2. Reshape and normalize pixels for plotting
        pixels = pixels.reshape(-1, 3) / 255.0

        # 3. Create 3D Axes
        axes = ThreeDAxes(
            y_range=[0, 1, 0.2],
            x_range=[0, 1, 0.2],
            z_range=[0, 1, 0.2],
            x_length=6,
            y_length=6,
            z_length=6,
            axis_config={"include_tip": True},
        )
        text = Paragraph("First plot the image's pixels in colorspace")
        axes.add_coordinates()
        points = VGroup()
        # Populate pixels onto 3D axes
        for pixel in pixels:
            # RGB color mapping to 3D position
            dot = Dot(
                point=axes.c2p(pixel[0], pixel[1], pixel[2]),
                color=rgb_to_color(pixel),
                radius=0.05,
            )
            points.add(dot)
            points = points.append_points(dot.points)
        text = Paragraph("First plot the pixels...")
        self.play(Write(text))
        self.wait(1)
        self.play(Unwrite(text))
        self.add(axes)
        self.play(Create(points), run_time=3)
        self.wait(1)
        self.play(FadeOut(axes, points))
        text = Paragraph("Then init the centroids...", t2c={"centroids": YELLOW})
        self.play(Write(text))
        self.play(Unwrite(text))
        self.wait(1)

        # Then plot figure out the centroids and plot them
        rng = np.random.default_rng()
        centroids = VGroup()
        for _ in range(K_VAL):
            dot = Dot(
                point=axes.c2p(rng.random(), rng.random(), rng.random()),
                color=YELLOW,
                radius=0.05,
            )
            centroids.add(dot)
            centroids = centroids.append_points(dot.points)
        self.play(FadeIn(axes, points))
        self.play(Create(centroids), run_time=3)
        self.wait(2)
        self.play(FadeOut(axes, points, centroids))

        point_assignments: list[VGroup] = [VGroup() for _ in range(K_VAL)]
        # FIX: object cannot serve as key because it is not hashable
        centroid_to_vgroup_dict = {centroids.points[i]: i for i in range(K_VAL)}

        text = Paragraph("Assign points to these centroids based on minimum distance")
        for p in points.points:
            min: float = MIN_SENTINEL
            centroid = None
            for c in centroids.points:
                d = distance(c, p)
                if d < min:
                    min = d
                    # Record centroid with the mimimum distance
                    centroid = c
            point_assignments[centroid_to_vgroup_dict[centroid]].add(p)


if __name__ == "__main__":
    main()
