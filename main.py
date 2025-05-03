from manim import *

class Vid(Scene):
    def construct(self):
        #self.quoteAnimation()
        #self.intro()
        es = self.getElectronSpectrum()

        self.play(es.animate.shift(RIGHT))
        self.wait(5)
    
    def getElectronSpectrum(self):
        lines = [
            Line(LEFT * 2 + UP * 1, RIGHT * 2 + UP * 1),
            Line(LEFT * 2 + UP * 0.5, RIGHT * 2 + UP * 0.5),
            Line(LEFT * 2, RIGHT * 2),
            Line(LEFT * 2 + DOWN * 0.5, RIGHT * 2 + DOWN * 0.5),
            Line(LEFT * 2 + DOWN * 1, RIGHT * 2 + DOWN * 1),
        ]

        labels = [
            Text(f"n={5-i}", color=WHITE)
            .scale(0.6).next_to(line, LEFT, buff=0.2)
            for i, line in enumerate(lines)
        ]

        # Pair each line and label animation
        animations = [
            Succession(
                Create(line, run_time=0.3),
                FadeIn(label, run_time=0.2)
            )
            for line, label in zip(lines, labels)
        ]

        self.play(AnimationGroup(*animations, lag_ratio=0.1))

        return VGroup(lines + labels)

    def getElectron(self):
        c = Circle(radius=2, color=RED, fill_opacity=0.5).scale(0.1)
        c.set_stroke(color=RED, width=6)

        minus_sign = Text('-', color=WHITE).move_to(ORIGIN)
        
        electron =  VGroup(c, minus_sign)
        self.play(FadeIn(electron, run_time=0.2))
        return electron

    def intro(self):
        eV13_6 = MathTex(r"-13.6\; \text{eV}")
        e_level_eq = MathTex(
            r"\Delta E = -13.6eV \left( \frac{1}{n^2_{f}}-\frac{1}{n_{i}^2} \right)"
            ).shift(DOWN * 0.6)
        self.play(Create(eV13_6))
        self.wait(0.5)
        self.play(eV13_6.animate.shift(UP * 0.6))
        self.play(Create(e_level_eq))

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