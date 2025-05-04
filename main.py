from manim import *
import physanitk as tk


"""
Each method is a scene manually generated and brought to edit.
manim -pqk main.py Vid -o outputName
"""
class Vid(Scene):
    def construct(self):
        #self.quoteAnimation()
        #self.energyLevel()
        #self.preReqAni()
        
        self.overView()

    
    def overView(self):
        t = Tex("In this video:")
        g1 = Tex("What")


    def preReqAni(self):
        border457 = RoundedRectangle(
                        corner_radius=0.2,
                        width=3,
                        height=1.5,
                        color=RED
                    )

        name457 = MathTex(r"\text{PHYS 457}", font_size=36)
        desc457 = Tex("Quantum Physics II", font_size=24)
        qcStudentText = Text("McGill Student Lern this in:").move_to(UP * 2)
        label457 = VGroup(name457, desc457).arrange(DOWN, buff=0.15).move_to(border457.get_center())
        prereqText = Tex("Prerequiste (QC) for:").move_to(LEFT * 3.5 + UP * 3)
        phys457Course = VGroup(border457, label457)
        self.play(
            Succession(
                AnimationGroup(
                    Write(qcStudentText),
                    Write(phys457Course),
                    run_time=0.7
                ),
                Wait(),
                FadeOut(qcStudentText),
                AnimationGroup(
                    Write(prereqText),
                    phys457Course.animate.shift(LEFT * 3.5 + UP * 1.65)
                )
            )
        )

        # Left table: 3 rows × 2 cols
        left_courses = [
            r"\text{Calculus I}", r"\text{Mechanics}",
            r"\text{Calculus II}", r"\text{Waves \& Optics}",
            r"\text{Linear Algebra}", r"\text{E\&M}",
        ]

        # Right table: 4 rows × 2 cols with descriptions
        right_courses = [
            (r"\text{MATH 222}", "Calculus III"),
            (r"\text{MATH 248}", "Vector Calculus"),
            (r"\text{MATH 247}", "Applied Linear Algebra"),
            (r"\text{MATH 249}", "Complex Variables"),
            (r"\text{MATH 325}", "ODEs"),
            (r"\text{PHYS 251}", "Classical Mechanics"),
            (r"\text{PHYS 350}", "E\&M"),
            (r"\text{PHYS 357}", "Quantum Physics I"),
        ]

        def create_table(course_list, rows, cols, border_color=BLUE, with_description=False):
            box_width = 3
            box_height = 1.5 if with_description else 1
            spacing_x = 0.2
            spacing_y = 0.2

            boxes = VGroup()
            for i in range(rows):
                for j in range(cols):
                    index = i * cols + j
                    if index >= len(course_list):
                        continue

                    if with_description:
                        course_name, desc = course_list[index]
                    else:
                        course_name = course_list[index]

                    box = RoundedRectangle(
                        corner_radius=0.2,
                        width=box_width,
                        height=box_height,
                        color=border_color
                    )

                    # Course name (MathTex) on top
                    name_tex = MathTex(course_name, font_size=36)
                    if with_description:
                        # Description (plain text) below
                        desc_tex = Tex(desc, font_size=24)
                        label = VGroup(name_tex, desc_tex).arrange(DOWN, buff=0.15).move_to(box.get_center())
                    else:
                        label = name_tex.move_to(box.get_center())

                    course_box = VGroup(box, label)

                    x = (j - (cols - 1) / 2) * (box_width + spacing_x)
                    y = ((rows - 1) / 2 - i) * (box_height + spacing_y)
                    course_box.move_to([x, y, 0])

                    boxes.add(course_box)

            # Background box for the table
            padding_x = 0.5
            padding_y = 0.5
            table_width = (cols - 1) * (box_width + spacing_x) + box_width
            table_height = (rows - 1) * (box_height + spacing_y) + box_height

            background = RoundedRectangle(
                corner_radius=0.3,
                width=table_width + padding_x,
                height=table_height + padding_y,
                fill_color=border_color,
                fill_opacity=0.3,
                stroke_opacity=0
            ).move_to(boxes.get_center())

            return VGroup(background, boxes)

        # Build tables
        left_table = create_table(left_courses, 3, 2, border_color=BLUE, with_description=False)
        right_table = create_table(right_courses, 4, 2, border_color=GREEN, with_description=True)

        # Position with gap
        gap = 0.1
        left_table.shift(LEFT * (right_table.width / 2 + gap) + DOWN * 1.6)
        right_table.shift(RIGHT * (left_table.width / 2 + gap))

        
        # Render
        self.play(Write(left_table), Write(right_table), run_time = 3)
        self.wait()

    def energyLevel(self):
        eV13_6 = MathTex(r"-13.6\; \text{eV}")
        e_level_eq = MathTex(
            r"\Delta E = -13.6eV \left( \frac{1}{n^2_{f}}-\frac{1}{n_{i}^2} \right)"
            ).shift(DOWN * 0.6)
        
        eq_border = SurroundingRectangle(e_level_eq, color=WHITE, buff=0.3)
        self.play(Create(eV13_6))
        self.wait(0.5)
        self.play(eV13_6.animate.shift(UP * 0.6))
        self.play(Write(e_level_eq))

        self.wait()
        self.play(FadeOut(eV13_6), run_time=0.5)
        self.play(e_level_eq.animate.shift(DOWN * 0.75))
        
        self.play(Create(eq_border.shift(DOWN * 0.75)))

        transition_energy = lambda n1, n2: 13.6 * (1 / n1**2 - 1 / n2**2)
        sp = UP * 2

        electron = tk.QuantAni.getElectron(self, sp)
        eLevel = tk.QuantAni.getEnergySpectrum(self, sp)
        p1 = tk.QuantAni.getPhoton(self,sp)
        p2 = tk.QuantAni.getPhoton(self,sp + UP * 5 + LEFT * 3)
        p3 = tk.QuantAni.getPhoton(self,sp + DOWN * 10 + LEFT * 3)

        delta_E_eq = MathTex(r"\Delta E = ").shift(sp + DOWN * 1.75 + LEFT * 0.75)
        delta_E_val = ValueTracker(0)
        delta_E_num = DecimalNumber().add_updater(
             lambda d: d.set_value(delta_E_val.get_value())).shift(
                 sp + DOWN * 1.75 + RIGHT * 0.5)
        
        self.play(Create(delta_E_eq), Create(delta_E_num), run_time = 0.3)
        self.wait(1)
        s = Succession(
            AnimationGroup(
                electron.animate.shift(DOWN),
                p1.animate.shift(UP * 3 + RIGHT * 4),
                delta_E_val.animate.set_value(transition_energy(3, 1)), 
                run_time=0.5
            ),
            Wait(1.2), 
            ApplyMethod(p2.shift, DOWN * 6 + RIGHT * 3, run_time=0.4),
            AnimationGroup(
                electron.animate.shift(UP*0.5), 
                p2.animate.shift(DOWN * 4.5 + RIGHT * 3),
                delta_E_val.animate.set_value(transition_energy(1, 4)),
                run_time=0.5
            ),
            Wait(1.2),
            ApplyMethod(p3.shift, UP * 10.5 + RIGHT * 3, run_time=0.4),
            AnimationGroup(
                electron.animate.shift(UP*1), 
                p3.animate.move_to(UP * 1000),
                p2.animate.shift(DOWN * 4 + RIGHT * 3),
                delta_E_val.animate.set_value(transition_energy(4, 5)),
                run_time=0.5
            ),
            Wait(1.2),
            AnimationGroup(
                electron.animate.shift(0), 
                p2.animate.shift(DOWN * 25 + RIGHT * 7),
                delta_E_val.animate.set_value(transition_energy(5, 3)),
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

        self.wait()



        
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