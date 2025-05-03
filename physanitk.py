"""
Yichen's Physics Animation Tool Kit! Modularized Physics Animation!
"""
from manim import *

class QuantAni():
    @staticmethod
    def getPhoton(scene, initialPos=0) -> VMobject:
        c = Circle(radius = 0.5, color=YELLOW, fill_color=YELLOW,
                   fill_opacity = 1).shift(initialPos).scale(0.1)
        scene.play(FadeIn(c, run_time=0.2))
        c.set_z_index(2)
        return c


    @staticmethod
    def getElectron(scene, initialPos=0) -> VMobject:
        c = Circle(radius=2, color=RED,
                   fill_color = "#e34639", fill_opacity=1).scale(0.1)
        c.set_stroke(color=RED, width=6)

        minus_sign = Text('-', color=WHITE)
        
        electron =  VGroup(c, minus_sign).shift(initialPos)
        electron.set_z_index(5)
        scene.play(FadeIn(electron, run_time=0.2))
        return electron
    
    @staticmethod
    def getEnergySpectrum(scene, initialPos=0) -> VMobject:
        lines = [
            Line(LEFT * 2 + UP * 1, RIGHT * 2 + UP * 1),
            Line(LEFT * 2 + UP * 0.5, RIGHT * 2 + UP * 0.5),
            Line(LEFT * 2, RIGHT * 2),
            Line(LEFT * 2 + DOWN * 0.5, RIGHT * 2 + DOWN * 0.5),
            Line(LEFT * 2 + DOWN * 1, RIGHT * 2 + DOWN * 1),
        ]

        for line in lines: 
            line.shift(initialPos)
            line.set_opacity(0.7)

        labels = [
            Text(f"n={5-i}", color=WHITE)
            .scale(0.6).next_to(line, LEFT, buff=0.2)
            for i, line in enumerate(lines)
        ]

        animations = [
            Succession(
                Create(line, run_time=0.3),
                FadeIn(label, run_time=0.2)
            )
            for line, label in zip(lines, labels)
        ]

        scene.play(AnimationGroup(*animations, lag_ratio=0.1))

        return VGroup(lines + labels)