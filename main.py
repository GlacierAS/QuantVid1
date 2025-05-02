from manim import *

class AnimatedSquareToCircle(Scene):
    def construct(self):
        quote = Tex(r"I think I can safely say that \\ nobody understands quantum mechanics")
        self.play(Create(quote))
        self.wait(0.5)
        