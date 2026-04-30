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
        text = Paragraph("First plot the pixels...")
        self.play(Write(text))
        self.wait(1)
        self.play(Unwrite(text))

        self.add(axes)
        self.play(Create(points), run_time=3)
        self.wait(1)

        self.play(FadeOut(axes, points))
        text = Tex(r"Then init the k centroids at random points $C_1$, $C_2$, $C_3$")
        self.play(Write(text))
        self.wait(1)
        self.play(Unwrite(text))
        self.wait(1)
        color_arr = [RED, BLUE, GREEN]
        # Then plot figure out the centroids and plot them
        rng = np.random.default_rng()
        centroids: list[VGroup] = [VGroup() for _ in range(K_VAL)]
        centroid_labels = VGroup()
        for k in range(K_VAL):
            x = rng.random
            y = rng.random
            z = rng.random
            dot = Dot(
                point=axes.c2p(rng.random(), rng.random(), rng.random()),
                color=color_arr[k],
                radius=0.05,
            )
            label = Text(f"C{k+1}", color=color_arr[k]).next_to(dot, UR, buff=0.001)
            centroids[k].add(dot)
            centroids[k].append_points(np.array([x, y, z]))
            centroid_labels.add(label)

        self.play(FadeIn(axes, points))
        for k in range(K_VAL):
            self.play(Create(centroids[k]), run_time=1)
        self.play(Create(centroid_labels), run_time=1)

        self.wait(2)

        for k in range(K_VAL):
            self.play(FadeOut(centroids[k]))
        self.play(FadeOut(axes, points))

        text = Paragraph("Assign points to these centroids based on minimum distance")
        for p in points.points:
            min: float = MIN_SENTINEL
            centroid_idx = 0
            for k in range(K_VAL):
                c = centroids[k]
                d = distance(c.points, p)
                if d < min:
                    min = d
                    # Record centroid with the mimimum distance
                    c.add(Dot(p, radius=0.01))
                    print(f"Assigned centroid idx: {centroid_idx}")
                centroid_idx += 1

        self.play(FadeIn(axes))
        for k in range(K_VAL):
            self.play(FadeIn(centroids[k]))

        self.wait(2)

        for k in range(K_VAL):
            self.play(FadeOut(centroids[k]))

        self.play(FadeOut(axes))


def get_centroid_index(centroids: VGroup, centroid: mtyp.Point3D_Array) -> int:
    for i, c in enumerate(centroids):
        if c.points.all() == centroid.all():
            return i
    return -1


if __name__ == "__main__":
    main()
