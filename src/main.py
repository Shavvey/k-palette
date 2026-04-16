import manim as mn


class MakeCircle(mn.Scene):
    def construct(self):
        circle = mn.Circle()  # create a circle
        circle.set_fill(mn.BLUE, opacity=1)  # set color and transparency

        square = mn.Square()  # create a square
        square.flip(mn.RIGHT)  # flip horizontally
        square.rotate(-3 * mn.TAU / 8)  # rotate a certain amount

        self.play(mn.Create(square))  # animate the creation of the square
        self.play(
            mn.Transform(square, circle)
        )  # interpolate the square into the circle
        self.play(mn.FadeOut(square))  # fade out animation
