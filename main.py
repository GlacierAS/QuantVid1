from manim import *
import physanitk as tk
from mrStarfruit import MRSF
from enumcfg import * 
from scipy.stats import norm # for probabilistic calculations

"""
Each method is a scene manually generated and brought to edit.
manim -pqk main.py Vid -o outputName
"""
class Vid(Scene):
    def construct(self):
        self.qtex = TexTemplate()
        self.qtex.add_to_preamble(r"\usepackage{braket}")
        self.qtex.add_to_preamble(r"\usepackage{amssymb}")
        
        # PREFACE
        #self.quoteAnimation()
        #self.energyLevel()
        #self.preReqAni()
        #self.overView()
        # PART I
        self.howPhycistDescribeNormalObject()
        #self.propertyValue()
        #self.take_a_break()
        # PART 2
        #self.qcoord()
        #self.qcoord2_heisenburg()
        # TODO: Take a break2 
        # PART 3
        #self.measurements()
        #self.measurements2()
        # TODO: Take a break3
        #self.measurements3()
    def measurements3(self):
        qs3 = Tex("Step 3: Making measurements").to_edge(UP)
        self.add(qs3)

        sigma = 1
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[0, 0.5, 0.1],
            x_length=10,
            y_length=3,
            axis_config={"include_numbers": False},
            tips=False
        ).shift(UP * 0.5)

        x_label = axes.get_x_axis_label("x", edge=RIGHT, direction=DOWN)
        y_label = axes.get_y_axis_label(r"|\psi(x)|^2", edge=UP, direction=LEFT)
        
        self.play(Create(VGroup(axes, x_label, y_label)), run_time = 2)

        # Gaussian probability density function
        def psi_squared(x):
            return (1 / (np.sqrt(2 * np.pi) * sigma)) * np.exp(-x**2 / (2 * sigma**2))

        graph = axes.plot(psi_squared, color=BLUE)
        self.play(Create(graph))

        qapple_ls = []
        opacity_ls = [0.2, 0.4, 0.6, 0.8, 0.8, 0.6, 0.4, 0.2]
        t = ValueTracker(0)
        for i, tick in enumerate(axes.x_axis.ticks):
            pos = tick.get_center() + DOWN * 0.7
            # maxinum is 4
            opacity = opacity_ls[i]

            print(opacity, psi_squared(i - 4)/4.0)
            qa = self.getApple(size = SSize.S, t=t, sp=pos, o=opacity)
            qa.set_opacity(opacity)
            self.play(FadeIn(qa), run_time = 0.2)
            qapple_ls.append(qa)

            if i == 3: # for center since no tick
                qc = self.getApple(size = SSize.S, t=t, sp=pos + RIGHT * 1.25)
                self.play(FadeIn(qc), run_time = 0.2)
                qapple_ls.append(qc)

        superposition = Tex(r"Exist in ALL state! ", "Superposition!").next_to(qapple_ls[4], DOWN).shift(DOWN * 0.5)
        self.play(
            t.animate.increment_value(20 * PI),
            
            Succession(
                Wait(10),
                Create(superposition[0]),
                Wait(),
                Create(superposition[1]),
                Wait(7)
            ),
            run_time = 20)

        eig_apple = self.getApple(size = SSize.S, t=t, sp=axes.coords_to_point(1.2, 0) + DOWN * 0.7)
        
        # direc delta function
        dd = Arrow(start=axes.coords_to_point(1.2, 0), end=axes.coords_to_point(1.2, 0) + UP * 2.5, color=BLUE, buff=0)
        apples = VGroup(qapple_ls)
        collapse = Tex(r"Collapse!", color=YELLOW).next_to(qapple_ls[4], DOWN).shift(DOWN * 0.5)
        self.play(
            Transform(graph, dd),
            Succession(
                FadeIn(apples, run_time=0.1),
                FadeOut(apples, run_time=0.1),
                FadeIn(apples, run_time=0.1),
                FadeOut(apples, run_time=0.1),
                FadeIn(apples, run_time=0.1),
                FadeOut(apples, run_time=0.1),
                FadeIn(apples, run_time=0.1),
                FadeOut(apples, run_time=0.1),
                FadeIn(apples, run_time=0.1),
                FadeOut(apples, run_time=0.1),
            ),
            Transform(superposition, collapse)
        )
        self.add(eig_apple)
        self.wait()

        self.play(Create(Tex(r'Maximum \\ Momentum \\ Uncertainty!', color=YELLOW ).next_to(dd, RIGHT)))
        self.wait()
        #TODO: ADD Prof Starfruit idea on left simultaneous for max momentum uncertainty text
    def measurements2(self):
        qs3 = Tex("Step 3: Making measurements").to_edge(UP)
        self.add(qs3)

        op = MathTex(r"\hat{x}\ket{\psi}  \text{ or }\hat{x}\psi(x)\text{ or }\hat{x}\psi(p_x)", tex_template=self.qtex)
        mes = Tex(r"Give position according to \\ probability distribution \\ in their coordinate system", color=YELLOW).shift(RIGHT * 3)
        
        self.play(Create(op))
        self.play(op.animate.shift(LEFT * 3.5))

        arr = Arrow(start = mes.get_edge_center(LEFT), end=op.get_edge_center(RIGHT), color=YELLOW)
    
        self.play(Create(arr), Create(mes))

        l1 = VGroup(arr, mes, op)
        self.play(l1.animate.shift(UP * 2))
        xhat_pos = MathTex(r"\hat{x}=x \leftarrow \text{Position Coordinate}").next_to(l1, DOWN)
        xhat_mom = MathTex(r"\hat{x}=i\hbar \frac{ \partial }{ \partial p } \leftarrow \text{Momentum Coordinate}").next_to(xhat_pos, DOWN)

        self.play(Create(xhat_pos), Create(xhat_mom))
        # Expectation value of position (QM)
        exp_val_eq = MathTex(
            r"\langle x \rangle = \int_{-\infty}^{\infty} \psi(x)^* \hat{x} \psi(x) dx", 
            font_size=42
        )

        # Standard error (uncertainty) in position
        uncertainty_eq = MathTex(
            r"\Delta x = \sqrt{\langle x^2 \rangle - \langle x \rangle^2}", 
            font_size=42
        )

        # Center-aligned group
        equations = VGroup(exp_val_eq, uncertainty_eq).arrange(DOWN, center=True, buff=0.6).shift(DOWN * 2.3)

        # Animate
        self.wait(1)
        self.play(Write(equations))
        self.play(equations.animate.shift(LEFT * 3))
        not_focus = Tex(r"You can do these \\ to report value! \\ (Not our focus today...)", color=RED).next_to(equations, RIGHT).shift(RIGHT)
        arr1 = Arrow(start = not_focus.get_edge_center(LEFT), end=equations.get_edge_center(RIGHT), color=RED)
        self.play(Create(not_focus), Create(arr1))
        self.wait()
        self.play(FadeOut(arr, arr1, not_focus, equations, xhat_mom, xhat_pos, l1))
        self.wait()

        # Create the big circle (pool of states)
        circle = Circle(radius=2.5, color=BLUE).shift(LEFT * 3 + DOWN * 0.5)
        title = Tex("Position eigenstates").next_to(circle, UP)
        self.play(Create(circle))
        self.play(Write(title))

        # Eigenstate labels
        eigenstates = [r"\ket{1}", r"\ket{1.13}", r"\ket{2.2}", r"\ket{0.5}", r"\ket{3.14}", r"\ket{-1.2}", r"\ket{0}"]
        placed_labels = [] # (state, eigval)

        for state in eigenstates:
            while True:  
                x = np.random.uniform(-2.4, 2.4)
                y = np.random.uniform(-2.4, 2.4)
                pos = np.array([x, y, 0]) + circle.get_center()

                # Check within the circle
                if np.linalg.norm(pos - circle.get_center()) >= 1.8:
                    continue

                # Check spacing to previous labels
                if all(np.linalg.norm(pos - lbl.get_center()) > 0.9 for (lbl, _) in placed_labels):
                    label = MathTex(state, tex_template=self.qtex).move_to(pos)
                    placed_labels.append((label, state[5:-1]))
                    self.play(Write(label), run_time=0.3)
                    break  # Success, move to next state

        self.wait(2)

        for (eigstate, eigval) in placed_labels:
            eigstate = eigstate.copy()
            eigeqn = MathTex(r'\hat{x}\ket{' + f'{eigval}' + r'}', f'={eigval}' + r'\ket{' +f'{eigval}' + r'}', tex_template=self.qtex).shift(RIGHT * 3)
            self.add(eigstate)
            self.play(eigstate.animate.move_to(RIGHT * 2))
            measure = Tex(r'Measure!', color=YELLOW).next_to(eigeqn, DOWN)
            self.wait()
            self.add(measure)
            self.play(Transform(eigstate, eigeqn[0]))
            
            self.wait(0.5)
            self.play(Write(eigeqn[1]), FadeOut(measure))
            self.wait()
            self.play(FadeOut(eigstate, eigeqn[1]))

        pool = VGroup([t[0] for t in placed_labels], circle)

        gen_eig_eqn = MathTex(r'\hat{x}\ket{x_{0}}=x_{0}', '?', tex_template=self.qtex).shift(RIGHT * 3)
        ketx0 = MathTex(r'\ket{x_{0}}', tex_template=self.qtex).next_to(gen_eig_eqn, RIGHT).shift(LEFT * 0.3)
        eig_val_eqn_text = Tex('Eigenvalue Equation:').next_to(gen_eig_eqn, UP)
        self.play(Create(gen_eig_eqn))
        self.wait(0.5)
        self.play(FadeOut(gen_eig_eqn[1]), Create(ketx0), Create(eig_val_eqn_text))
        self.wait()
        gen_eig_fun = MathTex(r'\hat{x}\psi(x)=x_{0} \psi(x)', tex_template=self.qtex).shift(RIGHT * 3)
        self.play(Transform(gen_eig_eqn, gen_eig_fun), FadeOut(ketx0))
        self.wait()
        pos_sol = MathTex(r'\text{Solve} \implies \psi(x)=\delta(x-x_{0})').next_to(gen_eig_eqn, DOWN)
        self.play(Create(pos_sol))
        self.wait()
        self.play(FadeOut(VGroup(pos_sol, gen_eig_eqn, eig_val_eqn_text, pool, title)))


    def measurements(self):
        qs3 = Tex("Step 3: Making measurements")
        self.play(FadeIn(qs3), qs3.animate.to_edge(UP))


        # ValueTrackers for bounds
        a = ValueTracker(-0.5)
        b = ValueTracker(1.5)
        sigma = 1

        # Axes
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[0, 0.5, 0.1],
            x_length=10,
            y_length=3,
            axis_config={"include_numbers": False},
            tips=False
        ).shift(DOWN)

        x_label = axes.get_x_axis_label("x", edge=RIGHT, direction=DOWN)
        y_label = axes.get_y_axis_label(r"|\psi(x)|^2", edge=UP, direction=LEFT)
        p_label = axes.get_x_axis_label("p_x", edge=RIGHT, direction=DOWN)
        y_p_label = axes.get_y_axis_label(r"|\psi(p_x)|^2", edge=UP, direction=LEFT)

        self.play(Create(VGroup(axes, x_label, y_label)), run_time = 2)

        # Gaussian probability density function
        def psi_squared(x):
            return (1 / (np.sqrt(2 * np.pi) * sigma)) * np.exp(-x**2 / (2 * sigma**2))

        graph = axes.plot(psi_squared, color=BLUE)

        # Area between a and b
        def get_area():
            return axes.get_area(
                graph,
                x_range=(a.get_value(), b.get_value()),
                color=BLUE,
                opacity=0.4
            )

        area = always_redraw(get_area)

        # Probability text
        def get_prob_text():
            prob = norm.cdf(b.get_value(), scale=sigma) - norm.cdf(a.get_value(), scale=sigma)
            return MathTex(r"\text{Area = Probability}" + f"= {prob:.3f}").next_to(axes, DOWN).scale(1)

        eqn = MathTex(r"\int_{a}^b|\psi(x)|^2dx=\text{Probability of measuring } x \text{ in range }[a,b]")
        eqn_p = MathTex(r"\int_{a}^b|\psi(p_x)|^2dp_x=\text{Probability of measuring } p_x \text{ in range }[a,b]").shift(UP * 1.8)

        
        prob_text = always_redraw(get_prob_text)
        self.play(Write(eqn.shift(UP * 1.8)))

        self.play(Create(VGroup(graph, area)), run_time=4)
        self.play(Create(prob_text))

        # Animate values
        self.wait(1)
        self.play(a.animate.set_value(-2), b.animate.set_value(1), run_time=2)
        self.wait(1)
        self.play(a.animate.set_value(-0.5), b.animate.set_value(0.5), run_time=2)
        self.wait(1)
        self.play(a.animate.set_value(-1), b.animate.set_value(2.3), run_time=2)
        self.wait(1)

        x_label.save_state()
        y_label.save_state()
        eqn.save_state()
        self.play(
            Transform(x_label, p_label),
            Transform(y_label, y_p_label),
            Transform(eqn, eqn_p)
        )
        self.wait()
        self.play(Restore(x_label), Restore(y_label), Restore(eqn))

        rmk1 = MathTex(r"\int_{-\infty}^\infty|\psi(x)|^2dx=1").shift(UP * 1.8)
        self.wait()
        self.play(Transform(eqn, rmk1), a.animate.set_value(-4), b.animate.set_value(4))
        self.wait()
        self.play(FadeOut(VGroup(x_label, y_label, axes, area, graph, prob_text)))
        rmk2 = MathTex(r"\psi(x) \text{ can be complex!}").shift(UP * 1.5)
        self.play(Transform(eqn, rmk2))
        i_def = MathTex(r"i=\sqrt{-1}")
        self.wait()
        self.play(Create(i_def))
        self.wait()
        its_ok = Tex("It's ok! Just a mathmatical tool!").shift(DOWN * 1.5)
        self.play(Create(its_ok))

    def qcoord2_heisenburg(self):
        qs2 = Tex("Step 2: Attach Coordinate System to the Object").to_edge(UP)
        self.add(qs2)

        heis = MathTex(r"\Delta x\Delta p_{x} \ge \frac{\hbar}{2}").next_to(qs2, DOWN).shift(DOWN * 0.5)
        self.play(Write(heis))
        self.wait()
        # Constants
        hbar = 1

        # Trackers
        x0 = ValueTracker(1)
        delta_x = ValueTracker(2)

        def get_delta_p():
            return hbar / (2 * delta_x.get_value())

        axis_x = NumberLine(
            x_range=[-5, 5, 1],
            length=10,  
            include_tip=True,
            include_numbers=False
        ).shift(UP * 0.5)

        axis_p = NumberLine(
            x_range=[-5, 5, 1],
            length=10,
            include_tip=True,
            include_numbers=False
        ).next_to(axis_x, DOWN * 8)

        # Axis labels
        x_label = MathTex(r"\text{Position }  x").next_to(axis_x, DOWN)
        p_label = MathTex(r"\text{Momentum }  p").next_to(axis_p, DOWN)

        self.play(Create(VGroup(axis_x, axis_p, x_label, p_label)), run_time=3)

        ## -- X Axis Visuals -- ##
        arrow_x = always_redraw(lambda: Arrow(
            start=axis_x.number_to_point(x0.get_value()) + DOWN * 1.2,
            end=axis_x.number_to_point(x0.get_value()),
            buff=0.1,
            stroke_width=4,
            color=YELLOW
        ))

        label_x = always_redraw(lambda: MathTex(r"68 \% \; x \text{ certainty}")
                                .next_to(arrow_x.get_start(), DOWN).shift(UP * 0.2))

        tick_left_x = always_redraw(lambda: Line(
            axis_x.number_to_point(x0.get_value() - delta_x.get_value()) + DOWN * 0.2,
            axis_x.number_to_point(x0.get_value() - delta_x.get_value()) + UP * 0.2,
            color=BLUE
        ))

        tick_right_x = always_redraw(lambda: Line(
            axis_x.number_to_point(x0.get_value() + delta_x.get_value()) + DOWN * 0.2,
            axis_x.number_to_point(x0.get_value() + delta_x.get_value()) + UP * 0.2,
            color=BLUE
        ))

        highlight_x = always_redraw(lambda: Rectangle(
            height=0.4,
            width=axis_x.number_to_point(x0.get_value() + delta_x.get_value())[0] -
                  axis_x.number_to_point(x0.get_value() - delta_x.get_value())[0],
            color=BLUE,
            fill_opacity=0.3,
            stroke_width=0
        ).move_to(
            (axis_x.number_to_point(x0.get_value() + delta_x.get_value())[0] +
             axis_x.number_to_point(x0.get_value() - delta_x.get_value())[0]) / 2 * RIGHT +
            axis_x.get_center()[1] * UP
        ))

        ## -- P Axis Visuals -- ##
        arrow_p = always_redraw(lambda: Arrow(
            start=axis_p.number_to_point(0) + DOWN * 1.2,
            end=axis_p.number_to_point(0),
            buff=0.1,
            stroke_width=4,
            color=YELLOW
        ))

        label_p = always_redraw(lambda: MathTex(r"68 \% \; p \text{ certainty}")
                                .next_to(arrow_p.get_start(), DOWN).shift(UP * 0.2))

        tick_left_p = always_redraw(lambda: Line(
            axis_p.number_to_point(-get_delta_p()) + DOWN * 0.2,
            axis_p.number_to_point(-get_delta_p()) + UP * 0.2,
            color=GREEN
        ))

        tick_right_p = always_redraw(lambda: Line(
            axis_p.number_to_point(get_delta_p()) + DOWN * 0.2,
            axis_p.number_to_point(get_delta_p()) + UP * 0.2,
            color=GREEN
        ))

        highlight_p = always_redraw(lambda: Rectangle(
            height=0.4,
            width=axis_p.number_to_point(get_delta_p())[0] -
                  axis_p.number_to_point(-get_delta_p())[0],
            color=GREEN,
            fill_opacity=0.3,
            stroke_width=0
        ).move_to(
            (axis_p.number_to_point(get_delta_p())[0] +
             axis_p.number_to_point(-get_delta_p())[0]) / 2 * RIGHT +
            axis_p.get_center()[1] * UP
        ))

        # Add all elements
        self.play(FadeIn(VGroup(
                arrow_x, label_x, tick_left_x, tick_right_x, highlight_x,
                arrow_p, label_p, tick_left_p, tick_right_p, highlight_p)
            )
        )

        # Animate to show changes
        self.wait(1)
        self.play(x0.animate.set_value(-2), delta_x.animate.set_value(1))
        self.wait(1)
        self.play(delta_x.animate.set_value(3))
        self.wait(1)
        self.play(delta_x.animate.set_value(0.2), x0.animate.set_value(2))
        self.wait(1)
        self.play(delta_x.animate.set_value(0.01))
        
    def qcoord(self):
        qs2 = Tex("Step 2: Attach Coordinate System to the Object")
        self.play(FadeIn(qs2), qs2.animate.to_edge(UP))
        
        kpsi = MathTex(r"\ket{\psi}", tex_template = self.qtex).shift(UP * 0.7)
        xkpsi = MathTex(r"\braket{x |\psi}", tex_template = self.qtex).shift(UP * 0.7)
        pkpsi = MathTex(r"\braket{p_x |\psi}", tex_template = self.qtex).shift(UP * 0.7)
        wf = MathTex(r"=", r"\psi(x)").shift(UP * 0.7 + RIGHT)

        self.play(Write(kpsi))
        self.wait()
        self.play(Transform(kpsi, xkpsi))
        self.wait()
        self.play(Succession(Transform(kpsi, pkpsi), Wait(), Transform(kpsi, xkpsi)))
        self.play(AnimationGroup(kpsi.animate.shift(LEFT * 0.5), Create(wf), lag_ratio=0.3))
        self.wait()

        what = Tex("What???").shift(RIGHT + DOWN * 0.7)
        arr = Arrow(start=what.get_top(), end=wf.get_bottom(), buff=0.1)
        self.play(Create(what), Create(arr))
        self.wait(3)
        qcoord = VGroup(kpsi, wf, what, arr)
        self.play(qcoord.animate.shift(LEFT * 4))
        

        inCM = Tex("In classical mechanics:", color=YELLOW).shift(RIGHT * 3 + UP * 2)
        CMline = NumberLine(
            x_range=[0, 4, 1],  # Start, end, step
            length=4,            # Short length in units
            include_numbers=True,
        ).next_to(inCM, DOWN * 2)
        
        x_col = MathTex(r"x:").next_to(CMline, LEFT).shift(UP * 0.2)
        self.play(
            Create(inCM), Create(CMline), 
            Create(x_col)
        )

        value_tracker = ValueTracker(2)

        arrow = always_redraw(lambda: Arrow(
            start=CMline.number_to_point(value_tracker.get_value()) + DOWN * 1.5,
            end=CMline.number_to_point(value_tracker.get_value()) + DOWN * 0.5,
            buff=0.05,
            stroke_width=4
        ))

        # Label showing the current value at the start of the arrow
        label = always_redraw(lambda: DecimalNumber(
            value_tracker.get_value(),
            num_decimal_places=2,
        ).next_to(arrow.get_start(), DOWN))
        CMapple = self.getApple(size = SSize.S).next_to(arrow, UP)
        self.add(arrow, label)

        self.play(Create(CMapple), Create(arrow), Write(label))

        # Animate the value tracker changing, which moves the arrow and updates the label
        self.play(value_tracker.animate.set_value(1), CMapple.animate.shift(LEFT), run_time=1)
        self.play(value_tracker.animate.set_value(4), CMapple.animate.shift(RIGHT * 3), run_time=2)
        self.play(value_tracker.animate.set_value(2.24), CMapple.animate.shift(LEFT * 1.76), run_time=1)
        self.wait()

        x_is_num = MathTex(r"x \to 2.24 \text{ is a number!}").next_to(label, DOWN)
        yellow_rec = SurroundingRectangle(label, color=YELLOW, buff=0.1)
        self.play(Create(yellow_rec), run_time=0.5)
        self.play(Create(x_is_num))

        self.wait()
        x_rep = MathTex(r"\text{PositionRep(Apple)}", r"=", r"x").next_to(x_is_num, DOWN)
        self.play(Create(x_rep))
        self.wait()

        x_pos = Tex("Position(Apple)").next_to(x_rep, DOWN * 2)
        x_pos_vec = Arrow(start=x_pos.get_edge_center(RIGHT), end=x_rep[2].get_center())
        
        self.wait()
        self.play(Create(x_pos), Create(x_pos_vec))
        kpsi_bg = BackgroundRectangle(
            kpsi,
            color=BLUE,
            fill_opacity=0.3,
            buff=0.1
        )
        wf_bg = BackgroundRectangle(
            wf[1],
            color=YELLOW,
            fill_opacity=0.3,
            buff=0.1
        )
        x_rep_bg_0 = BackgroundRectangle(
            x_rep[0],
            color=BLUE,
            fill_opacity=0.3,
            buff=0.1
        )
        x_rep_bg_1 = BackgroundRectangle(
            x_rep[2],
            color=YELLOW,
            fill_opacity=0.3,
            buff=0.1
        )
        self.play(Create(kpsi_bg), Create(x_rep_bg_0))
        self.wait()
        self.play(Create(wf_bg), Create(x_rep_bg_1))
        self.wait()
        wf_text = Tex("Wavefunction?").next_to(arr, DOWN)
        self.play(Transform(what, wf_text))
        self.wait()
        complicated = MathTex(r"x \overset{\text{wtf???}}{\to}\left(  \frac{m\omega}{\pi\hbar} \right)^{1/4} \exp\left( -\frac{m\omega x^2}{2\hbar} \right)=\psi(x)",
                              tex_template = self.qtex).next_to(wf_text, DOWN)
        self.play(Create(complicated.scale(0.7)))
        self.wait()

        start = complicated.get_corner(DL)
        end = complicated.get_corner(UR)

        strike = Line(start, end, color=RED)

        self.play(Create(strike))
        self.wait()

        # Second part of QCoord
        everything_so_far = VGroup(
            kpsi, wf, what, arr,
            inCM, CMline,
            arrow, label,
            x_is_num, x_rep, x_pos, x_pos_vec,
            kpsi_bg, wf_bg, x_rep_bg_0, x_rep_bg_1,
            wf_text, complicated, strike, yellow_rec, CMapple, x_col
        )
        self.play(FadeOut(everything_so_far))
        
        cm_fact = MathTex(r"\text{CM: Position}(\;\;\;\;\;)=\text{PositionRep}(\;\;\;\;\;)").shift(UP)
        f_ma = MathTex(r"\vec{F}=m \vec{a}=\frac{d\vec{p}}{dt}").shift(DOWN * 0.5)
        regular_apple1 = self.getApple(size = SSize.S).shift(UP + LEFT * 0.73)
        regular_apple2 = self.getApple(size = SSize.S).shift(UP + RIGHT * 3.66)
        
        self.play(Write(cm_fact), Create(regular_apple1), Create(regular_apple2))
        self.play(FadeIn(f_ma))
        self.play(f_ma.animate.shift(LEFT * 2))
        
        changes_motion = Tex(r"Changes postion", color=YELLOW).next_to(f_ma, RIGHT).shift(RIGHT)
        changes_motion_arrow = Arrow(start=changes_motion.get_edge_center(LEFT), end=f_ma.get_edge_center(RIGHT), color = YELLOW)
        
        
        self.play(Write(changes_motion), Write(changes_motion_arrow))
        f_ma_group = VGroup(f_ma, changes_motion, changes_motion_arrow)
        cm_fact_group = VGroup(cm_fact, regular_apple1, regular_apple2)
        self.play(
            AnimationGroup(
                cm_fact_group.animate.next_to(qs2, DOWN),
                f_ma_group.animate.shift(UP * 2),
                lag_ratio=0.1
            )
        )

        t = ValueTracker(0)
        qa = self.getApple(size = SSize.S, t=t, sp=RIGHT * 0.1)
        qa2 = self.getApple(size = SSize.S, t=t, sp=LEFT * 2.1 + DOWN * 3)
        qm_fact = MathTex(r"\text{QM: Position}(\;\;\;\;\;)=\text{Random?}")
        
        schord_eq = MathTex(r"i \hbar \frac{\partial}{\partial t} \ket{\psi(t)} = \hat{H} \ket{\psi(t)}", tex_template=self.qtex).shift(DOWN + LEFT * 1.8)
        changes_motion_q = Tex(r"Changes state", color=BLUE).next_to(schord_eq, RIGHT).shift(RIGHT)
        changes_motion_arrow_q = Arrow(start=changes_motion_q.get_edge_center(LEFT), end=schord_eq.get_edge_center(RIGHT), color = BLUE)
        q_schord_group = VGroup(schord_eq, changes_motion_q, changes_motion_arrow_q)

        xp_incompatibility = MathTex(r"x\text{ and } p \text{ incompatible?}", color=GREEN).shift(DOWN*2)
        measure_position = Tex(r"\text{Measure(Position}(\;\;\;\;\;)\text{) changes momentum and vice versa!}").shift(DOWN * 3)



        self.play(FadeIn(qa), Write(qm_fact))
        self.play(
            t.animate.increment_value(20 * PI),
            Succession(
                Wait(15),
                Create(q_schord_group),
                Wait(15),
                Create(xp_incompatibility),
                Wait(15),
                Create(VGroup(measure_position, qa2)),
                Wait(15), run_time=63
            ), run_time=63
        )

        
        everything_so_far2 = VGroup(f_ma_group, cm_fact_group, q_schord_group, xp_incompatibility, measure_position, qa, qa2, qm_fact)
        self.play(FadeOut(everything_so_far2))
        self.wait()
        

    def take_a_break(self):
        msg = """
            A more formal discussion of the limitations of physical properties 
        involves recognizing that every property has a representation as a
        subspace of some extended Hilbert space, with either a finite or
        uncountably infinite set of basis vectors called eigenvectors, each
        associated with an eigenvalue. 
        
            Each eigenvalue represents a physically measurable quantity.

            I will get to the eigenvectors later, but I will avoid mentioning
        the Hilbert space...
        """
        takeBreak = Tex("Take a break!").to_edge(UP)
        self.wait()
        self.play(Create(takeBreak))
        do_you_know = Text(msg, width=11).shift(UP * 0.5)
        self.play(Write(do_you_know), run_time = 7)
        box = SurroundingRectangle(do_you_know, color=RED, buff=0.2)
        self.play(Write(box))

        # TODO: Insert sleeping prof starfruit
    
    def propertyValue(self):
        qs1 = Tex("Step 1: Representing the Object by Assigning Properties")
        kpsi = MathTex(r"\text{Quantum State:} \ket{\psi}", "=", tex_template=self.qtex).shift(UP * 0.7)
        posTex = Tex(r"Position", color = YELLOW)
        momTex = Tex(r"Momentum", color = BLUE).shift(DOWN*0.7)


        self.play(FadeIn(qs1), qs1.animate.to_edge(UP))
        self.play(
            Succession(
                Create(kpsi[0]),
                Wait(),
                kpsi[0].animate.shift(LEFT * 0.5),
                Create(kpsi[1].shift(LEFT * 0.5)),
            )
        )


        t = ValueTracker(0)
        qa = self.getApple(size = SSize.S, t=t, sp=RIGHT * 2.4 + UP * 0.7)
        self.play(FadeIn(qa))
        
        self.play(
            t.animate.increment_value(20 * PI),
            Succession(
                AnimationGroup(
                    Create(posTex),
                    Create(momTex),
                    lag_ratio=0.3
                ),
                Wait(14) #padding
            ),
            run_time = 16, 
        )
        onScreen = VGroup(posTex, momTex, qa, kpsi)
        wait = Tex("Wait! Value of properties have limitations!").shift(UP * 1.5)
        # TODO: add mr starfruit shocked!
        self.play(
            Succession(
                Transform(onScreen, wait), 
                Wait(), 
                FadeOut(onScreen)
            )
        )

        discrete = Tex("1. Discrete infinite number of values").shift(UP * 2.7)
        spinVal = MathTex(r"\text{Spin} \in \left\{ m_s \in \mathbb{R} \;\middle|\; s \in \tfrac{1}{2} \mathbb{N}_0,\ m_s = -s + k,\ k \in \mathbb{Z},\ 0 \leq k \leq 2s \right\}",
            tex_template=self.qtex
        ).scale(0.8)
        strike = Line(spinVal.get_left(), spinVal.get_right(), color=RED)
        self.play(Succession(
            Create(discrete),
            FadeIn(spinVal),
            Create(strike),
        ))
        self.play(
            FadeOut(spinVal),
            FadeOut(strike),
        )
        orbitalSet = MathTex(r"L \in \left\{ m \in \mathbb{Z} \;\middle|\; l \in \mathbb{N}_0, \ m = -l + k, \ k \in \mathbb{Z},\ 0 \leq k \leq 2l \right\}",
                             tex_template=self.qtex).shift(UP * 1.3)
        number_line = NumberLine(
            x_range=[-4.5, 4.5, 1],  # Range from -5 to 5, step size of 1
            length=10,  # Length of the number line
            include_numbers=True,  # Include number labels
            label_direction=DOWN,  # Position the labels below the ticks
            numbers_to_include=[-4, -3, -2, -1, 0, 1, 2, 3, 4]  # Include integer values of hbar
        )
        
        # Add label for the axis
        label = MathTex(r"\text{Angular Momentum } \hbar").next_to(number_line, DOWN)

        # Create yellow dots on integer values of hbar
        yellow_dots = VGroup(*[
            Dot(number_line.n2p(i), color=YELLOW) for i in range(-4, 5)
        ])

        # Create an arrow pointing to 3.32 on the number line
        arrow = Arrow(start=number_line.n2p(3.32)+ DOWN * 2, end=number_line.n2p(3.32), color=WHITE, buff=0.1)

        # Create the label for the arrow
        label_text = Tex(r"Not allowed value $3.32 \hbar$").next_to(arrow.get_start(), DOWN)

        # Add number line, dots, and label to the scene
        self.play(Create(orbitalSet))
        self.play(Create(number_line), Write(label))
        self.play(FadeIn(yellow_dots))
        self.wait()
        self.play(GrowArrow(arrow), Write(label_text))

        nl = VGroup(number_line, label, yellow_dots, arrow, label_text)
        bound = MathTex(r"-m, -m+1, ..., -1, 0, 1, ..., m-1, m")
        circle = Circle(radius=0.4, color=RED).shift(UP * 1.3 + LEFT * 0.93)
        self.play(
            Transform(nl, bound),
            Write(circle),
            Wait(),
        )
        finite = Tex("Finite number of orientations?").shift(DOWN)
        hbar = MathTex(r"\hbar = 1.054571817... \times 10^{-34} \text{ Js}").shift(DOWN * 2)
        self.play(Create(finite))
        self.wait()
        self.play(Create(hbar))
        self.wait()
        m_val = MathTex(r"m \text{ is VERY large for macroscopic object!}").shift(DOWN * 2)
        self.play(Transform(hbar, m_val))
        self.wait(2)
        self.play(FadeOut(hbar), FadeOut(bound), 
                  FadeOut(circle), FadeOut(orbitalSet),
                  FadeOut(m_val), FadeOut(nl), FadeOut(finite))
        
        cont = Tex("2. Infinite continueous number of values").shift(UP * 2)

        xax = NumberLine(
            x_range=[-4.5, 4.5, 1],
            length=10,
            include_numbers=True,
        )
        xlabel = Tex("Position, Momentum, etc").next_to(xax, DOWN)

        highlight_box = Rectangle(
            width=xax.width + 0.4,
            height=0.8,
            color=PINK,
            fill_color = PINK,
            fill_opacity = 0.3,
            stroke_opacity = 0
        )
        highlight_box.move_to(xax)


        self.play(Create(cont))
        self.play(Create(xax))
        self.play(Write(xlabel), Create(highlight_box))

        self.wait()
        contScreen = VGroup(xax, xlabel, highlight_box)
        eigen = MathTex(r"\text{Allowed values} \to \text{eigenvalues}")
        self.play(Transform(contScreen, eigen))
        self.wait()

    def howPhycistDescribeNormalObject(self):
        a = self.getApple(size = SSize.S, sp=UP* 0.1)
        self.play(FadeIn(a))
        p = MathTex(r"\text{How to describe} \;\;\;\;\;\;\; ?")
        
        idea = MRSF.get_sfidea(size = SSize.M)
        idea.to_edge(DL).shift(RIGHT * 1.4 + UP * 0.2)

        # Flipping image... Manim pls fix #2412
        idea.pixel_array = np.fliplr(idea.pixel_array)
        
        self.play(
            a.animate.shift(RIGHT * 1.65),

        )
        self.play(Write(p))
        self.play(
            FadeIn(idea),
            a.animate.shift(UP * 3 + LEFT * 4),
            p.animate.shift(UP * 3 + LEFT * 4),
        )
        
        s1 = Tex("1. Assign properties").align_to(p, UL).shift(DOWN * 0.7)
        s2 = Tex("2. Attach Coordinate").align_to(p, UL).shift(DOWN * 1.4)
        s3 = Tex("3. Make Measurement").align_to(p, UL).shift(DOWN * 2.1)
        propText1 = Tex(r"Position", color = YELLOW).shift(RIGHT * 3 + DOWN  * 2.2)
        propText2 = Tex(r"Momentum", color = BLUE).shift(RIGHT * 3 + DOWN  * 2.9)
        a_mid = self.getApple(size = SSize.M, sp=RIGHT * 4 + UP * 2)
        self.play(FadeIn(a_mid))
        line = Line(a_mid.get_center() + DOWN * 0.6, propText1.get_center() + UP * 0.5)

        self.play(Create(s1), Create(line), Create(propText1), Create(propText2))
        
        self.wait()

        axes = Axes(
            x_range=[0, 5, 1],
            y_range=[0, 3, 1],
            x_length=5,
            y_length=3,
            tips=False,
        )
        paxes = Axes(
            x_range=[0, 3, 1],
            y_range=[0, 4, 1],
            x_length=3,
            y_length=4,
            tips=False,
        )

        # Label axes p
        paxes.shift(RIGHT * 3 + UP * 1)
        px_label = paxes.get_x_axis_label(r"p_x")
        py_label = paxes.get_y_axis_label(r"p_y")

        # Label axes x
        axes.shift(RIGHT * 2.5 + UP * 1.5)
        x_label = axes.get_x_axis_label("x")
        y_label = axes.get_y_axis_label("y")


        self.play(
            Create(axes), 
            Create(x_label), 
            Create(y_label),
            Create(px_label),
            Create(py_label),
            Create(s2),
            Create(paxes)
            )
        self.wait()

        xvec = Arrow(axes.c2p(0, 0), axes.c2p(0, 0) + RIGHT * 4 + UP * 2, buff=0, color = YELLOW)
        pvec = Arrow(paxes.c2p(0, 0), paxes.c2p(0, 0) + UP * 3+ RIGHT * 2.5, buff=0, color = BLUE)

        propTextNew1 = MathTex(r"\text{PositionRep(Apple)}=(x,y)").shift(RIGHT * 3 + DOWN  * 2.2).scale(0.8)
        propTextNew1.color = YELLOW
        
        propTextNew2 = MathTex(r"\text{MomentumRep(Apple)}=(p_x, p_y)").shift(RIGHT * 3 + DOWN  * 2.9).scale(0.8)
        propTextNew2.color = BLUE

        self.play(
            Transform(propText1, propTextNew1),
            Transform(propText2, propTextNew2),
            Create(xvec),
            Create(pvec)
        )
        self.wait()
        propTextNewNew1 = MathTex(r"\text{Position(Apple)}=(4,2)").shift(RIGHT * 3 + DOWN  * 2.2).scale(0.8)
        propTextNewNew1.color = YELLOW
        
        propTextNewNew2 = MathTex(r"\text{Momentum(Apple)}=(2.5, 3)").shift(RIGHT * 3 + DOWN  * 2.9).scale(0.8)
        propTextNewNew2.color = BLUE


        self.play(
            Transform(propText1, propTextNewNew1),
            Transform(propText2, propTextNewNew2),
            Create(s3),
        )
        
        self.wait(3)
        
        # Create a black transparent rectangle as a dimming overlay
        dim_overlay = Rectangle(
            width=config.frame_width,
            height=config.frame_height,
            fill_color=BLACK,
            fill_opacity=0.75,  # Adjust dimming strength (0 = transparent, 1 = full black)
            stroke_opacity=0  # No border
        )
        dim_overlay.move_to(ORIGIN)

        # Play fade in of dimming effect
        self.play(FadeIn(dim_overlay))
        t = ValueTracker(0)
        a1 = self.getApple(size = SSize.L, sp = LEFT * 2.5)
        self.play(FadeIn(a1))
        self.wait()
        a2 = self.getApple(size = SSize.L, t=t, sp=RIGHT * 2.5)
        self.play(FadeIn(a2))
        self.play(t.animate.increment_value(20 * PI), run_time=12, rate_func=linear)
    
    def getApple(self, t=None, size=SSize.M, sp = 0, o=1):
        # Get Apple
        # if t of ValueTracker provided track the color of apple
        # o is opacity
        # else return red apple
        apple = SVGMobject("apple1.svg").shift(sp)
        
        match size:
            case SSize.S:
                apple.scale(0.3)
                apple.set_stroke(width=2)
            case SSize.M:
                apple.scale(0.5)
                apple.set_stroke(width=4)
            case SSize.L:
                apple.scale(1)
                apple.set_stroke(width=6)
            case SSize.XL:
                apple.scale(2)
                apple.set_stroke(width=10)
        
        if t is None:
            # RED apple
            for part in apple.submobjects:
                if part.get_fill_color().to_hex() == "#000000":  # Only black parts
                    part.set_fill(RED, opacity=o)
                    return apple

        def get_gradient_color(alpha):
            c1 = interpolate_color(GREEN, BLUE, (np.sin(t.get_value()) + 1)/2)
            c2 = interpolate_color(BLUE, GREEN, (np.sin(t.get_value() + PI/2) + 1)/2)
            return interpolate_color(c1, c2, alpha)

        fill_parts = []
        # Initial fill only for black parts
        for part in apple.submobjects:
            if part.get_fill_color().to_hex() == "#000000":  # Only black parts
                part.set_fill(get_gradient_color(0), opacity=o)
                fill_parts.append(part)
        # Updater to animate gradient change for black parts only
        def update_gradient(mob):
            for part in mob.submobjects:
                if part in fill_parts:
                    part.set_fill(get_gradient_color(0), opacity=o)

        apple.add_updater(update_gradient)
        return apple

        

    def overView(self):
       
        start = 3.5 * UP
        t = Tex("In this video:")
        g1 = Tex("1. What is a Quantum State?")
        e1 = MathTex(r"\ket{a}", tex_template=self.qtex)
        g3 = Tex("2. Coordinate system and Wave Function")
        e3 = MathTex(r"\braket{ x |\psi  }=\psi(x)", tex_template=self.qtex)
        g4 = Tex("3. Uncertainty and measurement").move_to(start + DOWN * 2)
        e4 = MathTex(r"\Delta x\Delta p_{x} \ge \hbar/2", tex_template=self.qtex)
        g5 = Tex("4. Schrödinger equation").move_to(start + DOWN * 2.5)
        e5 = MathTex(r"\hat{H}\ket{\psi} & =E\ket{\psi}", tex_template=self.qtex)
        l = [t, g1, e1, g3, e3, g4, e4, g5, e5]

        b1 = SurroundingRectangle(e1, color=RED, buff=0.2)
        b3 = SurroundingRectangle(e3, color=RED, buff=0.2)
        b4 = SurroundingRectangle(e4, color=RED, buff=0.2)
        b5 = SurroundingRectangle(e5, color=RED, buff=0.2)
        b = [None, None, b1, None, b3, None, b4, None, b5]

        for i, tex in enumerate(l): tex.move_to(start + DOWN * i * 0.8)
        for i, box in enumerate(b): 
            if box is not None: 
                box.move_to(start + DOWN * i * 0.8)

        self.play(
            Succession(
                *(Write(tex) for tex in l),
                AnimationGroup(*(Create(box) for box in b if box is not None), lag_ratio=0.3),
                Wait(),
                ), run_time = 7
        )

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