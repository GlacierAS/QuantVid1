from manim import *

class AnimatedSquareToCircle(Scene):
    def construct(self):
        #self.quoteAnimation()
        self.intro()


        self.wait(5)

    def getElectron(self):
        c = Circle(radius=2, color=RED, fill_opacity=0.5)
        c.set_stroke(color=RED, width=6)

        minus_sign = Text('-', color=WHITE).scale(2).move_to(ORIGIN)
        electron = VGroup(c, minus_sign)

        self.play(electron.animate.fade(0))
    def intro(self):
        eV13_6 = MathTex(r"-13.6\; \text{eV}")
        e_level_eq = MathTex(
            r"\Delta E = -13.6eV \left( \frac{1}{n^2_{f}}-\frac{1}{n_{i}^2} \right)"
            ).shift(DOWN * 0.8)
        self.play(Create(eV13_6))
        self.wait(0.5)
        self.play(eV13_6.animate.shift(UP * 0.8))
        self.play(Create(e_level_eq))
        self.wait(5)

        self.getElectron()

        

    

    def quoteAnimation(self):
        quote = Tex(r"I think I can safely say that nobody \\ understands quantum mechanics")
        au = Tex(r"\textit{-Richard P. Feynman}").shift(0.5 * DOWN)
        self.play(Create(quote))
        self.wait(1)
        self.play(quote.animate.shift(UP * 0.5))
        self.play(Create(au))
        self.wait(0.5)

        self.play(
            quote.animate.fade(1).shift(0.5 * UP),
            au.animate.fade(1).shift(0.5 * DOWN)
        )