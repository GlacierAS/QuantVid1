from manim import *
import physanitk as tk

class Vid(Scene):
    def construct(self):
        #self.quoteAnimation()
        #self.hook()
        
        sp = UR * 2 + RIGHT * 2

        electron = tk.QuantAni.getElectron(self, sp)
        eLevel = tk.QuantAni.getEnergySpectrum(self, sp)
        p1 = tk.QuantAni.getPhoton(self,sp)
        p2 = tk.QuantAni.getPhoton(self,sp + UP * 5 + LEFT * 3)
        p3 = tk.QuantAni.getPhoton(self,sp + DOWN * 10 + LEFT * 3)

        #delta_E = MathTex(r"\Delta E = 0").shift(sp)
        
        s = Succession(
            AnimationGroup(
                electron.animate.shift(DOWN),
                p1.animate.shift(UP * 3 + RIGHT * 4), 
                run_time=0.5
            ),
            Wait(1.2), 
            ApplyMethod(p2.shift, DOWN * 6 + RIGHT * 3, run_time=0.4),
            AnimationGroup(
                electron.animate.shift(UP*0.5), 
                p2.animate.shift(DOWN * 4.5 + RIGHT * 3),
                run_time=0.5
            ),
            Wait(1.2),
            ApplyMethod(p3.shift, UP * 10.5 + RIGHT * 3, run_time=0.4),
            AnimationGroup(
                electron.animate.shift(UP*1), 
                p3.animate.move_to(UP * 1000),
                p2.animate.shift(DOWN * 4 + RIGHT * 3),
                run_time=0.5
            ),
            Wait(1.2),
            AnimationGroup(
                electron.animate.shift(0), 
                p2.animate.shift(DOWN * 25 + RIGHT * 7),
                run_time=0.5
            ),
            Wait(1.2),
        )
        
        for i in range(5):
            self.play(s)
            electron.move_to(sp)
            p1.move_to(sp)
            p2.move_to(sp + UP * 5 + LEFT * 3)
            p3.move_to(sp + DOWN * 10 + LEFT * 3)

        self.wait(5)


    def hook(self):
        eV13_6 = MathTex(r"-13.6\; \text{eV}")
        e_level_eq = MathTex(
            r"\Delta E = -13.6eV \left( \frac{1}{n^2_{f}}-\frac{1}{n_{i}^2} \right)"
            ).shift(DOWN * 0.6)
        self.play(Create(eV13_6))
        self.wait(0.5)
        self.play(eV13_6.animate.shift(UP * 0.6))
        self.play(Create(e_level_eq))



        
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