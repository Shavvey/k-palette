import kpalette.kmeans as k
import pathlib as p

from manim import *
import numpy as np
from PIL import Image

K_VAL = 3


def main():
    pass


class Plot3DPoints(ThreeDScene):
    def construct(self):
        img = Image.open("images/image_resized.png")
        img.thumbnail((50, 50))  # Resize for performance
        pixels = np.array(img)
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
        centroids = VGroup()
        self.play(Write(text))
        self.wait(2)
        self.play(Unwrite(text))
        self.add(axes)
        self.play(Create(points), run_time=3)
        text = Paragraph("Then init the centroids...", t2c={"centroid": YELLOW})
        text.scale_to_fit_width(config.frame_width)
        self.play(Write(text))
        self.wait(5)

        # Then plot figure out the centroids and plot them
        rng = np.random.default_rng()
        centroids = VGroup()
        for _ in range(K_VAL):
            dot = Dot(
                point=axes.c2p(rng.random(), rng.random(), rng.random()),
                color=YELLOW,
            )
            centroids.add(dot)
        self.play(Create(centroids), run_time=3)


if __name__ == "__main__":
    main()
