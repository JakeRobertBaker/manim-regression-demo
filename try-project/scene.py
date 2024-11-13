from manim import *  # noqa: F403


class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen


class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set color and transparency

        square = Square()  # create a square
        square.rotate(PI / 4)  # rotate a certain amount

        self.play(Create(square))  # animate the creation of the square
        self.play(Transform(square, circle))  # interpolate the square into the circle
        self.play(FadeOut(square))  # fade out animation


class SquareAndCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency

        square = Square()  # create a square
        square.set_fill(BLUE, opacity=0.5)  # set the color and transparency

        square.next_to(circle, UP, buff=0.5)  # set the position
        self.play(Create(circle), Create(square))  # show the shapes on screen


class AnimatedSquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        square = Square()  # create a square

        self.play(Create(square))  # show the square on screen
        self.play(square.animate.flip())
        self.play(square.animate.rotate(PI / 4))  # rotate the square
        self.play(Transform(square, circle))  # transform the square into a circle
        self.play(square.animate.set_fill(PINK, opacity=0.5))  # color the circle on screen
        self.play(square.animate.flip())
        self.play(square.animate.shift(2 * DOWN))
        # if you apply flip to circle it then appears!
        # self.play(circle.animate.flip())


class DifferentRotations(Scene):
    def construct(self):
        left_square = Square(color=BLUE, fill_opacity=0.7).shift(2 * LEFT)
        right_square = Square(color=GREEN, fill_opacity=0.7).shift(2 * RIGHT)
        self.play(left_square.animate.rotate(PI), Rotate(right_square, angle=PI), run_time=2)
        self.wait()


class TwoTransforms(Scene):
    def transform(self):
        a = Circle()
        b = Square()
        c = Triangle()
        self.play(Transform(a, b))
        self.play(Transform(a, c))
        self.play(FadeOut(a))

    def replacement_transform(self):
        a = Circle()
        b = Square()
        c = Triangle()
        self.play(ReplacementTransform(a, b))
        self.play(ReplacementTransform(b, c))
        self.play(FadeOut(c))

    def construct(self):
        self.transform()
        self.wait(0.5)  # wait for 0.5 seconds
        self.replacement_transform()


class TransformCycle(Scene):
    def construct(self):
        a = Circle()
        t1 = Square()
        t2 = Triangle()
        self.add(a)
        self.wait()
        for t in [t1, t2]:
            self.play(Transform(a, t))


class PlaneLinePointAnimation(ThreeDScene):
    def construct(self):
        # Set up the 3D axes
        axes = ThreeDAxes()

        labels = axes.get_axis_labels(MathTex(r"U_0"), MathTex(r"U_1"), MathTex(r"U_p"))

        # Create a line passing through the plane
        line = Line(start=axes.c2p(-2, 0, 0), end=axes.c2p(2, 0, 0), color=YELLOW)
        line_that_becomes_plane = Line(start=axes.c2p(-2, 0, 0), end=axes.c2p(2, 0, 0), color=YELLOW)
        line_length = line.get_length()

        # Create a 2D plane in the xy-plane
        plane = Rectangle(width=line_length, height=line_length, color=BLUE, fill_opacity=0.5)

        # Create a point above the plane
        point = Dot3D(axes.c2p(1, 1, 1), color=RED)

        # Set the initial camera position
        self.set_camera_orientation(phi=50 * DEGREES, theta=-60 * DEGREES)

        # add the axes and labels to the scene
        self.add(axes, labels)

        self.play(Create(line))
        self.add(line_that_becomes_plane)
        self.wait(1)

        # Show the plane and point above the plane
        # self.play(Create(plane), Create(point))

        self.play(FadeTransform(line_that_becomes_plane, plane))

        # Optional: Rotate the camera for a dynamic effect
        self.begin_ambient_camera_rotation(rate=0.01)
        self.wait(5)
        self.stop_ambient_camera_rotation()
