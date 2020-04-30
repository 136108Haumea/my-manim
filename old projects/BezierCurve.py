##开发@鹤翔万里@136108Haumea
from manimlib.imports import *
from old_projects import *

class LinearBezierCurve(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE
        }
    }
    def construct(self):
        P0 = Dot(np.array([-1.5,  1.5, 0]))
        P1 = Dot(np.array([ 1.5, -1.5, 0]))
        P = VGroup(P0, P1).set_color(GRAY)

        P0_P1 = Line(P0, P1).set_color(GRAY)

        t = ValueTracker(0)

        B = Dot(color=RED).add_updater(lambda m: m.move_to((P1.get_center() - P0.get_center()) * t.get_value() + P0.get_center()))

        path = TracedPath(B.get_center, stroke_width=7, stroke_color=RED)

        label = Text("线性贝塞尔曲线", font="Source Han Serif CN").scale(0.9).set_color(BLACK).shift(DOWN * 3)
        self.add(label)
        self.add(P, P0_P1, B, path)
        self.wait()
        self.play(t.increment_value, 1, run_time=7, rate_func=linear)
        self.wait()


class QuadraticBezierCurve(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE
        }
    }
    def construct(self):
        P0 = Dot(np.array([ -3, -1.5, 0]))
        P1 = Dot(np.array([  0,  1.5, 0]))
        P2 = Dot(np.array([1.5, -1.5, 0]))
        P = VGroup(P0, P1, P2).set_color(GRAY)

        P0_P1 = Line(P0, P1)
        P1_P2 = Line(P1, P2)
        P_lines = VGroup(P0_P1, P1_P2).set_color(GRAY)

        t = ValueTracker(0)

        Q0 = Dot(color=BLUE).add_updater(lambda m: m.move_to((P1.get_center() - P0.get_center()) * t.get_value() + P0.get_center()))
        Q1 = Dot(color=BLUE).add_updater(lambda m: m.move_to((P2.get_center() - P1.get_center()) * t.get_value() + P1.get_center()))
        Q = VGroup(Q0, Q1)

        Q0_Q1 = Line().add_updater(lambda m: m.put_start_and_end_on(Q0.get_center(), Q1.get_center())).set_color(YELLOW)

        B = Dot(color=RED).add_updater(lambda m: m.move_to((Q1.get_center() - Q0.get_center()) * t.get_value() + Q0.get_center()))

        path = TracedPath(B.get_center, stroke_width=7, stroke_color=RED)

        label = Text("二次贝塞尔曲线", font="Source Han Serif CN").scale(0.9).set_color(BLACK).shift(DOWN * 3)
        self.add(label)
        self.add(P, P_lines)
        self.add(Q, Q0_Q1)
        self.add(B, path)
        self.wait()
        self.play(t.increment_value, 1, run_time=7, rate_func=linear)
        self.wait()


class CubicBezierCurve(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE
        }
    }
    def construct(self):
        P0 = Dot(np.array([  -3, -1.5, 0]))
        P1 = Dot(np.array([-3.6,  1.5, 0]))
        P2 = Dot(np.array([   0,  1.5, 0]))
        P3 = Dot(np.array([   3, -1.5, 0]))
        P = VGroup(P0, P1, P2, P3).set_color(GRAY)
        
        P0_P1 = Line(P0, P1)
        P1_P2 = Line(P1, P2)
        P2_P3 = Line(P2, P3)
        P_lines = VGroup(P0_P1, P1_P2, P2_P3).set_color(GRAY)

        t = ValueTracker(0)

        Q0 = Dot(color=BLUE).add_updater(lambda m: m.move_to((P1.get_center() - P0.get_center()) * t.get_value() + P0.get_center()))
        Q1 = Dot(color=BLUE).add_updater(lambda m: m.move_to((P2.get_center() - P1.get_center()) * t.get_value() + P1.get_center()))
        Q2 = Dot(color=BLUE).add_updater(lambda m: m.move_to((P3.get_center() - P2.get_center()) * t.get_value() + P2.get_center()))
        Q = VGroup(Q0, Q1, Q2)

        Q0_Q1 = Line().add_updater(lambda m: m.put_start_and_end_on(Q0.get_center(), Q1.get_center()))
        Q1_Q2 = Line().add_updater(lambda m: m.put_start_and_end_on(Q1.get_center(), Q2.get_center()))
        Q_lines = VGroup(Q0_Q1, Q1_Q2).set_color(YELLOW)

        R0 = Dot(color=GREEN).add_updater(lambda m: m.move_to((Q1.get_center() - Q0.get_center()) * t.get_value() + Q0.get_center()))
        R1 = Dot(color=GREEN).add_updater(lambda m: m.move_to((Q2.get_center() - Q1.get_center()) * t.get_value() + Q1.get_center()))
        R = VGroup(R0, R1)

        R0_R1 = Line().add_updater(lambda m: m.put_start_and_end_on(R0.get_center(), R1.get_center())).set_color(PURPLE)

        B = Dot(color=RED).add_updater(lambda m: m.move_to((R1.get_center() - R0.get_center()) * t.get_value() + R0.get_center()))

        path = TracedPath(B.get_center, stroke_width=7, stroke_color=RED)

        label = Text("三次贝塞尔曲线", font="Source Han Serif CN").scale(0.9).set_color(BLACK).shift(DOWN * 3)
        self.add(label)
        self.add(P, P_lines)
        self.add(Q, Q_lines)
        self.add(R, R0_R1)
        self.add(B, path)
        self.wait()
        self.play(t.increment_value, 1, run_time=7, rate_func=linear)
        self.wait()


class FourthOrderBezierCurve(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE
        }
    }
    def construct(self):
        P0 = Dot(np.array([-3.6, -1.5, 0]))
        P1 = Dot(np.array([-4.2,  1.5, 0]))
        P2 = Dot(np.array([   0,  1.5, 0]))
        P3 = Dot(np.array([   2, -1.5, 0]))
        P4 = Dot(np.array([   3,  0.5, 0]))
        P = VGroup(P0, P1, P2, P3, P4).set_color(GRAY)
        
        P0_P1 = Line(P0, P1)
        P1_P2 = Line(P1, P2)
        P2_P3 = Line(P2, P3)
        P3_P4 = Line(P3, P4)
        P_lines = VGroup(P0_P1, P1_P2, P2_P3, P3_P4).set_color(GRAY)

        t = ValueTracker(0)

        Q0 = Dot(color=BLUE).add_updater(lambda m: m.move_to((P1.get_center() - P0.get_center()) * t.get_value() + P0.get_center()))
        Q1 = Dot(color=BLUE).add_updater(lambda m: m.move_to((P2.get_center() - P1.get_center()) * t.get_value() + P1.get_center()))
        Q2 = Dot(color=BLUE).add_updater(lambda m: m.move_to((P3.get_center() - P2.get_center()) * t.get_value() + P2.get_center()))
        Q3 = Dot(color=BLUE).add_updater(lambda m: m.move_to((P4.get_center() - P3.get_center()) * t.get_value() + P3.get_center()))
        Q = VGroup(Q0, Q1, Q2, Q3)

        Q0_Q1 = Line().add_updater(lambda m: m.put_start_and_end_on(Q0.get_center(), Q1.get_center()))
        Q1_Q2 = Line().add_updater(lambda m: m.put_start_and_end_on(Q1.get_center(), Q2.get_center()))
        Q2_Q3 = Line().add_updater(lambda m: m.put_start_and_end_on(Q2.get_center(), Q3.get_center()))
        Q_lines = VGroup(Q0_Q1, Q1_Q2, Q2_Q3).set_color(YELLOW)

        R0 = Dot(color=GREEN).add_updater(lambda m: m.move_to((Q1.get_center() - Q0.get_center()) * t.get_value() + Q0.get_center()))
        R1 = Dot(color=GREEN).add_updater(lambda m: m.move_to((Q2.get_center() - Q1.get_center()) * t.get_value() + Q1.get_center()))
        R2 = Dot(color=GREEN).add_updater(lambda m: m.move_to((Q3.get_center() - Q2.get_center()) * t.get_value() + Q2.get_center()))
        R = VGroup(R0, R1, R2)

        R0_R1 = Line().add_updater(lambda m: m.put_start_and_end_on(R0.get_center(), R1.get_center())).set_color(PURPLE)
        R1_R2 = Line().add_updater(lambda m: m.put_start_and_end_on(R1.get_center(), R2.get_center())).set_color(PURPLE)
        R_lines = VGroup(R0_R1, R1_R2)

        S0 = Dot(color=ORANGE).add_updater(lambda m: m.move_to((R1.get_center() - R0.get_center()) * t.get_value() + R0.get_center()))
        S1 = Dot(color=ORANGE).add_updater(lambda m: m.move_to((R2.get_center() - R1.get_center()) * t.get_value() + R1.get_center()))
        S = VGroup(S0, S1)

        S0_S1 = Line().add_updater(lambda m: m.put_start_and_end_on(S0.get_center(), S1.get_center())).set_color(GOLD)

        B = Dot(color=RED).add_updater(lambda m: m.move_to((S1.get_center() - S0.get_center()) * t.get_value() + S0.get_center()))

        path = TracedPath(B.get_center, stroke_width=7, stroke_color=RED)

        label = Text("四次贝塞尔曲线", font="Source Han Serif CN").scale(0.9).set_color(BLACK).shift(DOWN * 3)
        self.add(label)
        self.add(P, P_lines)
        self.add(Q, Q_lines)
        self.add(R, R_lines)
        self.add(S, S0_S1)
        self.add(B, path)
        self.wait()
        self.play(t.increment_value, 1, run_time=7, rate_func=linear)
        self.wait()


class FifthOrderBezierCurve(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE
        }
    }
    def construct(self):
        P0 = Dot(np.array([  -3,   -2, 0]))
        P1 = Dot(np.array([-1.5,  2.5, 0]))
        P2 = Dot(np.array([   0, -0.5, 0]))
        P3 = Dot(np.array([ 1.5,    2, 0]))
        P4 = Dot(np.array([   3,    0, 0]))
        P5 = Dot(np.array([ 1.5,   -2, 0]))
        P = VGroup(P0, P1, P2, P3, P4, P5).set_color(GRAY)
        
        P0_P1 = Line(P0, P1)
        P1_P2 = Line(P1, P2)
        P2_P3 = Line(P2, P3)
        P3_P4 = Line(P3, P4)
        P4_P5 = Line(P4, P5)
        P_lines = VGroup(P0_P1, P1_P2, P2_P3, P3_P4, P4_P5).set_color(GRAY)

        t = ValueTracker(0)

        Q0 = Dot(color=BLUE).add_updater(lambda m: m.move_to((P1.get_center() - P0.get_center()) * t.get_value() + P0.get_center()))
        Q1 = Dot(color=BLUE).add_updater(lambda m: m.move_to((P2.get_center() - P1.get_center()) * t.get_value() + P1.get_center()))
        Q2 = Dot(color=BLUE).add_updater(lambda m: m.move_to((P3.get_center() - P2.get_center()) * t.get_value() + P2.get_center()))
        Q3 = Dot(color=BLUE).add_updater(lambda m: m.move_to((P4.get_center() - P3.get_center()) * t.get_value() + P3.get_center()))
        Q4 = Dot(color=BLUE).add_updater(lambda m: m.move_to((P5.get_center() - P4.get_center()) * t.get_value() + P4.get_center()))
        Q = VGroup(Q0, Q1, Q2, Q3, Q4)

        Q0_Q1 = Line().add_updater(lambda m: m.put_start_and_end_on(Q0.get_center(), Q1.get_center()))
        Q1_Q2 = Line().add_updater(lambda m: m.put_start_and_end_on(Q1.get_center(), Q2.get_center()))
        Q2_Q3 = Line().add_updater(lambda m: m.put_start_and_end_on(Q2.get_center(), Q3.get_center()))
        Q3_Q4 = Line().add_updater(lambda m: m.put_start_and_end_on(Q3.get_center(), Q4.get_center()))
        Q_lines = VGroup(Q0_Q1, Q1_Q2, Q2_Q3, Q3_Q4).set_color(YELLOW)

        R0 = Dot(color=GREEN).add_updater(lambda m: m.move_to((Q1.get_center() - Q0.get_center()) * t.get_value() + Q0.get_center()))
        R1 = Dot(color=GREEN).add_updater(lambda m: m.move_to((Q2.get_center() - Q1.get_center()) * t.get_value() + Q1.get_center()))
        R2 = Dot(color=GREEN).add_updater(lambda m: m.move_to((Q3.get_center() - Q2.get_center()) * t.get_value() + Q2.get_center()))
        R3 = Dot(color=GREEN).add_updater(lambda m: m.move_to((Q4.get_center() - Q3.get_center()) * t.get_value() + Q3.get_center()))
        R = VGroup(R0, R1, R2, R3)

        R0_R1 = Line().add_updater(lambda m: m.put_start_and_end_on(R0.get_center(), R1.get_center()))
        R1_R2 = Line().add_updater(lambda m: m.put_start_and_end_on(R1.get_center(), R2.get_center()))
        R2_R3 = Line().add_updater(lambda m: m.put_start_and_end_on(R2.get_center(), R3.get_center()))
        R_lines = VGroup(R0_R1, R1_R2, R2_R3).set_color(PURPLE)

        S0 = Dot(color=ORANGE).add_updater(lambda m: m.move_to((R1.get_center() - R0.get_center()) * t.get_value() + R0.get_center()))
        S1 = Dot(color=ORANGE).add_updater(lambda m: m.move_to((R2.get_center() - R1.get_center()) * t.get_value() + R1.get_center()))
        S2 = Dot(color=ORANGE).add_updater(lambda m: m.move_to((R3.get_center() - R2.get_center()) * t.get_value() + R2.get_center()))
        S = VGroup(S0, S1, S2)

        S0_S1 = Line().add_updater(lambda m: m.put_start_and_end_on(S0.get_center(), S1.get_center()))
        S1_S2 = Line().add_updater(lambda m: m.put_start_and_end_on(S1.get_center(), S2.get_center()))
        S_lines = VGroup(S0_S1, S1_S2).set_color(GOLD)

        T0 = Dot(color=PINK).add_updater(lambda m: m.move_to((S1.get_center() - S0.get_center()) * t.get_value() + S0.get_center()))
        T1 = Dot(color=PINK).add_updater(lambda m: m.move_to((S2.get_center() - S1.get_center()) * t.get_value() + S1.get_center()))
        T = VGroup(T0, T1)

        T0_T1 = Line().add_updater(lambda m: m.put_start_and_end_on(T0.get_center(), T1.get_center())).set_color(PINK)

        B = Dot(color=RED).add_updater(lambda m: m.move_to((T1.get_center() - T0.get_center()) * t.get_value() + T0.get_center()))

        path = TracedPath(B.get_center, stroke_width=7, stroke_color=RED)

        label = Text("五次贝塞尔曲线", font="Source Han Serif CN").scale(0.9).set_color(BLACK).shift(DOWN * 3)
        self.add(label)
        self.add(P, P_lines)
        self.add(Q, Q_lines)
        self.add(R, R_lines)
        self.add(S, S_lines)
        self.add(T, T0_T1)
        self.add(B, path)
        self.wait()
        self.play(t.increment_value, 1, run_time=7, rate_func=linear)
        self.wait()


class tTracker(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE
        }
    }
    def construct(self):
        t = ValueTracker(0)
        value = DecimalNumber(0, num_decimal_places=3).scale(3).add_updater(lambda m: m.set_value(t.get_value())).set_color(BLACK)
        label = TextMobject("t=").scale(3).next_to(value, LEFT).set_color(BLACK)
        self.add(value, label)
        self.wait()
        self.play(t.increment_value, 1, run_time=7, rate_func=linear)
        self.wait()


class WhiteBackground(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE
        }
    }


class scene1(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE
        }
    }
    def construct(self):
        P0 = Dot(np.array([  -2, -1.5, 0]))
        P1 = Dot(np.array([   0,  0.0, 0]))
        P2 = Dot(np.array([   0,  0.0, 0]))
        P3 = Dot(np.array([   2, -1.5, 0]))
        P = VGroup(P0, P1, P2, P3).set_color(GRAY)
        
        P0_P1 = Line(P0, P1, color=GRAY).add_updater(lambda m: m.put_start_and_end_on(P0.get_center(), P1.get_center()))
        P2_P3 = Line(P2, P3, color=GRAY).add_updater(lambda m: m.put_start_and_end_on(P2.get_center(), P3.get_center()))

        path = Dot().add_updater(
            lambda f:f.become(
                ParametricFunction(
                    lambda t:(\
                        ((((P3.get_center() - P2.get_center()) * t + P2.get_center()) - ((P2.get_center() - P1.get_center()) * t + P1.get_center())) * t + ((P2.get_center() - P1.get_center()) * t + P1.get_center())) - \
                        ((((P2.get_center() - P1.get_center()) * t + P1.get_center()) - ((P1.get_center() - P0.get_center()) * t + P0.get_center())) * t + ((P1.get_center() - P0.get_center()) * t + P0.get_center()))) * t + \
                        ((((P2.get_center() - P1.get_center()) * t + P1.get_center()) - ((P1.get_center() - P0.get_center()) * t + P0.get_center())) * t + ((P1.get_center() - P0.get_center()) * t + P0.get_center())),\
                        t_min=0,t_max=1,stroke_width=7, stroke_color=RED,
            )))
        
        self.add(P, P0_P1, P2_P3)
        self.add(path)
        self.play(
            P1.shift,UL*2,
            P2.shift,UR*3,
            rate_func=linear,
            run_time=3,
            )
        [self.play(
            P2.shift,(UR*3-[   2, -1.5, 0])*0.5*(1,-1)[i%2==0],
            rate_func=(rush_into,rush_from)[i%2==0],
            run_time=0.5,
            )for i in range(2)]
        self.play(
            P2.rotate,-PI/3,{"about_point":P3.get_center()},
            rate_func=linear,
            run_time=2,
            )
        self.wait()
        self.play(FadeOut(Group(*self.mobjects)))


class scene2(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE
        }
    }
    def construct(self):
        P0 = Dot(np.array([-1.5,  1.5, 0]))
        P1 = Dot(np.array([ 1.5, -1.5, 0]))
        P = VGroup(P0, P1).set_color(GRAY)
        label_P0 = TexMobject("P_0",color=BLACK).scale(0.8).next_to(P0,UL/2)
        label_P1 = TexMobject("P_1",color=BLACK).scale(0.8).next_to(P1,DR/2)

        P0_P1 = Line(P0, P1).set_color(GRAY)

        t = ValueTracker(0)

        B = Dot(color=RED).add_updater(lambda m: m.move_to((P1.get_center() - P0.get_center()) * t.get_value() + P0.get_center()))
        label_B = TexMobject("B",color=BLACK).scale(0.8).add_updater(lambda m:m.next_to(B,DL/2))

        path = TracedPath(B.get_center, stroke_width=7, stroke_color=RED)

        label = Text("线性贝塞尔曲线", font="Source Han Serif CN").scale(0.5).set_color('#FF7F24').to_corner(UL)
        
        text = TexMobject(r"t=\frac{P_0B}{P_0P_1}=",color=BLACK).scale(0.8)
        text2 = DecimalNumber().next_to(text,RIGHT).add_updater(lambda m: m.set_value(t.get_value())).set_color(BLACK)
        VGroup(text,text2).to_corner(UR)
        

        self.play(
            *[FadeIn(mob) for mob in [label,text,text2,P, P0_P1, B, path,label_P0,label_P1,label_B]],
            run_time=2,
            )
        self.wait()
        self.play(t.increment_value, 1, run_time=7, rate_func=linear)
        self.wait()
        self.play(FadeOut(Group(*self.mobjects)))


class scene3(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE
        }
    }
    def construct(self):
        P0 = Dot(np.array([ -3, -1.5, 0]))
        P1 = Dot(np.array([  0,  1.5, 0]))
        P2 = Dot(np.array([1.5, -1.5, 0]))
        P = VGroup(P0, P1, P2).set_color(GRAY)
        label_P0 = TexMobject("P_0",color=BLACK).scale(0.8).next_to(P0,DL/2)
        label_P1 = TexMobject("P_1",color=BLACK).scale(0.8).next_to(P1,UP/2)
        label_P2 = TexMobject("P_1",color=BLACK).scale(0.8).next_to(P2,DR/2)
        label_P = VGroup(label_P0,label_P1,label_P2)

        P0_P1 = Line(P0, P1)
        P1_P2 = Line(P1, P2)
        P_lines = VGroup(P0_P1, P1_P2).set_color(GRAY)

        t = ValueTracker(0)

        Q0 = Dot(color=BLUE).add_updater(lambda m: m.move_to((P1.get_center() - P0.get_center()) * t.get_value() + P0.get_center()))
        Q1 = Dot(color=BLUE).add_updater(lambda m: m.move_to((P2.get_center() - P1.get_center()) * t.get_value() + P1.get_center()))
        Q = VGroup(Q0, Q1)
        label_Q0 = TexMobject("Q_0",color=BLACK).scale(0.8).add_updater(lambda m:m.next_to(Q0,UL/2))
        label_Q1 = TexMobject("Q_1",color=BLACK).scale(0.8).add_updater(lambda m:m.next_to(Q1,UR/2))
        label_Q = VGroup(label_Q0,label_Q1)

        Q0_Q1 = Line().add_updater(lambda m: m.put_start_and_end_on(Q0.get_center(), Q1.get_center())).set_color(YELLOW)

        B = Dot(color=RED).add_updater(lambda m: m.move_to((Q1.get_center() - Q0.get_center()) * t.get_value() + Q0.get_center()))
        label_B = TexMobject("B",color=BLACK).scale(0.8).add_updater(lambda m:m.next_to(B,DOWN/2))

        path = TracedPath(B.get_center, stroke_width=7, stroke_color=RED)

        label = Text("二次贝塞尔曲线", font="Source Han Serif CN").scale(0.5).set_color('#FF7F24').to_corner(UL)

        text = TexMobject(r"t=\frac{P_0Q_0}{P_0P_1}=\frac{P_1Q_1}{P_1P_2}=\frac{Q_0B}{Q_0Q_1}=",color=BLACK).scale(0.8)
        text2 = DecimalNumber().next_to(text,RIGHT).add_updater(lambda m: m.set_value(t.get_value())).set_color(BLACK)
        VGroup(text,text2).to_corner(UR)

        self.play(
            *[FadeIn(mob) for mob in \
                [label,text,text2,P,P_lines,Q,Q0_Q1,B,path,label_P,label_Q,label_B]
            ],
            run_time=2,
            )
        self.wait()
        self.play(t.increment_value, 1, run_time=7, rate_func=linear)
        self.wait()
        self.play(FadeOut(Group(*self.mobjects)))


class scene4(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE
        }
    }
    def construct(self):
        P0 = Dot(np.array([  -3, -1.5, 0]))
        P1 = Dot(np.array([-3.6,  1.5, 0]))
        P2 = Dot(np.array([   0,  1.5, 0]))
        P3 = Dot(np.array([   3, -1.5, 0]))
        P = VGroup(P0, P1, P2, P3).set_color(GRAY)
        label_P0 = TexMobject("P_0",color=BLACK).scale(0.8).next_to(P0,DL)
        label_P1 = TexMobject("P_1",color=BLACK).scale(0.8).next_to(P1,UL)
        label_P2 = TexMobject("P_2",color=BLACK).scale(0.8).next_to(P2,UR)
        label_P3 = TexMobject("P_3",color=BLACK).scale(0.8).next_to(P3,DR)
        label_P = VGroup(label_P0,label_P1,label_P2,label_P3)
        
        P0_P1 = Line(P0, P1)
        P1_P2 = Line(P1, P2)
        P2_P3 = Line(P2, P3)
        P_lines = VGroup(P0_P1, P1_P2, P2_P3).set_color(GRAY)

        t = ValueTracker(0)

        Q0 = Dot(color=BLUE).add_updater(lambda m: m.move_to((P1.get_center() - P0.get_center()) * t.get_value() + P0.get_center()))
        Q1 = Dot(color=BLUE).add_updater(lambda m: m.move_to((P2.get_center() - P1.get_center()) * t.get_value() + P1.get_center()))
        Q2 = Dot(color=BLUE).add_updater(lambda m: m.move_to((P3.get_center() - P2.get_center()) * t.get_value() + P2.get_center()))
        Q = VGroup(Q0, Q1, Q2)
        label_Q0 = TexMobject("Q_0",color=BLACK).scale(0.8).add_updater(lambda m:m.next_to(Q0,LEFT))
        label_Q1 = TexMobject("Q_1",color=BLACK).scale(0.8).add_updater(lambda m:m.next_to(Q1,UP/3))
        label_Q2 = TexMobject("Q_2",color=BLACK).scale(0.8).add_updater(lambda m:m.next_to(Q2,UR/3))
        label_Q = VGroup(label_Q0,label_Q1,label_Q2)

        Q0_Q1 = Line().add_updater(lambda m: m.put_start_and_end_on(Q0.get_center(), Q1.get_center()))
        Q1_Q2 = Line().add_updater(lambda m: m.put_start_and_end_on(Q1.get_center(), Q2.get_center()))
        Q_lines = VGroup(Q0_Q1, Q1_Q2).set_color(YELLOW)

        R0 = Dot(color=GREEN).add_updater(lambda m: m.move_to((Q1.get_center() - Q0.get_center()) * t.get_value() + Q0.get_center()))
        R1 = Dot(color=GREEN).add_updater(lambda m: m.move_to((Q2.get_center() - Q1.get_center()) * t.get_value() + Q1.get_center()))
        R = VGroup(R0, R1)
        label_R0 = TexMobject("R_0",color=BLACK).scale(0.8).add_updater(lambda m:m.next_to(R0,DR/2))
        label_R1 = TexMobject("R_1",color=BLACK).scale(0.8).add_updater(lambda m:m.next_to(R1,DL/2))
        label_R = VGroup(label_R0,label_R1)

        R0_R1 = Line().add_updater(lambda m: m.put_start_and_end_on(R0.get_center(), R1.get_center())).set_color(PURPLE)

        B = Dot(color=RED).add_updater(lambda m: m.move_to((R1.get_center() - R0.get_center()) * t.get_value() + R0.get_center()))
        label_B = TexMobject("B",color=BLACK).scale(0.8).add_updater(lambda m:m.next_to(B,DOWN/2))

        path = TracedPath(B.get_center, stroke_width=7, stroke_color=RED)

        label = Text("三次贝塞尔曲线", font="Source Han Serif CN").scale(0.5).set_color('#FF7F24').to_corner(UL)
        
        text = TexMobject(
            r"t=\frac{P_0Q_0}{P_0P_1}=\frac{P_1Q_1}{P_1P_2}=\frac{P_2Q_2}{P_2P_3}",
            r"=\frac{Q_0R_0}{Q_0Q_1}=\frac{Q_1R_1}{Q_1Q_2}=\frac{R_0B}{R_0R_1}=",
            color=BLACK).scale(0.6)
        text[1].next_to(text[0][1:],DOWN,aligned_edge=LEFT)
        text2 = DecimalNumber().next_to(text[1],RIGHT).add_updater(lambda m: m.set_value(t.get_value())).set_color(BLACK)
        VGroup(text,text2).to_corner(UR)

        self.play(
            *[FadeIn(mob) for mob in \
                [label,text,text2,P,P_lines,Q,Q_lines,R,R0_R1,B,path,label_P,label_Q,label_R,label_B]
            ],
            run_time=2,
            )
        self.wait()
        self.play(t.increment_value, 1, run_time=7, rate_func=linear)
        self.wait()
        self.play(FadeOut(Group(*self.mobjects)))


class scene5(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE
        }
    }
    def construct(self):
        numberplane = NumberPlane(lag_ratio=0.1).set_stroke(opacity=0.3)
        self.play(ShowCreation(numberplane))

        label = Text("贝塞尔曲线原理", font="Source Han Serif CN").scale(0.5).set_color('#FF7F24').to_corner(UL)
        self.play(Write(label))

        O = Dot(color=BLACK)
        label_O = TexMobject("O",color=BLACK).scale(0.8).add_updater(lambda m:m.next_to(O,UR/2))
        
        P0 = Dot([-3,0,0],color=BLACK)
        P1 = Dot([-1,-3,0],color=BLACK)
        label_P0 = TexMobject("P_0",color=BLACK).scale(0.8).add_updater(lambda m:m.next_to(P0,UL/2))
        label_P1 = TexMobject("P_1",color=BLACK).scale(0.8).add_updater(lambda m:m.next_to(P1,DR/2))

        t = ValueTracker(0.001)

        B = Dot(color=RED).add_updater(lambda m: m.move_to((P1.get_center() - P0.get_center()) * t.get_value() + P0.get_center()))
        label_B = TexMobject("B",color=BLACK).scale(0.8).add_updater(lambda m:m.next_to(B,DL/2))

        path = Line().add_updater(
            lambda p:p.become(
                ParametricFunction(
                    lambda t:(P1.get_center() - P0.get_center()) * t + P0.get_center(),
                    t_min=0,t_max=t.get_value(),stroke_width=7, stroke_color=RED,
            )))

        self.play(
            *[FadeIn(mob) for mob in \
                [O,label_O,P0,B,P1,label_P0,label_B,label_P1,path]
            ],
            run_time=2,
            )
        self.wait()
        
        text = TexMobject(
            r"P_0=\overrightarrow{OP_0}\ \ B=\overrightarrow{OB}\ \ P_1=\overrightarrow{OP_1}",
            r"\frac{\overrightarrow{P_0B}}{\overrightarrow{P_0P_1}}=t",
            r"\overrightarrow{P_0B}=t\overrightarrow{P_0P_1}",
            r"\overrightarrow{OB}-\overrightarrow{OP_0}=t(\overrightarrow{OP_1}-\overrightarrow{OP_0})",
            r"B-P_0=t(P_1-P_0)",
            r"B(t)=(1-t)P_0+tP_1\ \ t\in[0,1]",
            #r"B(t)=\sum_{i=0}^1C_1^i(1-t)^{1-i}t^iP_i",
            color=BLACK,
            ).scale(0.8)
        [text[i+1].next_to(text[i],DOWN,aligned_edge=LEFT) for i in range(len(text)-1)]
        text[2:].next_to(text[0],DOWN,aligned_edge=LEFT)
        text[4:].next_to(text[2],DOWN,aligned_edge=LEFT)
        text.to_corner(UR)
        textbg = BackgroundRectangle(text,fill_opacity=0.3)

        OP0 = Arrow(
            O.get_center(),P0.get_center(),
            max_tip_length_to_length_ratio=0.2/get_distance(O.get_center(),P0.get_center()),
            buff=0,stroke_width=3,color=BLACK,
            )
        OB = Arrow(
            O.get_center(),B.get_center(),
            max_tip_length_to_length_ratio=0.2/get_distance(O.get_center(),B.get_center()),
            buff=0,stroke_width=3,color=BLACK,
            )
        OP1 = Arrow(
            O.get_center(),P1.get_center(),
            max_tip_length_to_length_ratio=0.2/get_distance(O.get_center(),P1.get_center()),
            buff=0,stroke_width=3,color=BLACK,
            )

        #[debugTex(self,text[i]) for i in range(len(text))]

        self.play(ShowCreation(textbg))
        self.play(Write(text[0]),run_time=2)
        self.wait()
        self.play(ReplacementTransform(text[0][ 3: 9].copy(),OP0))
        self.play(ReplacementTransform(text[0][11:16].copy(),OB ))
        self.play(ReplacementTransform(text[0][19:25].copy(),OP1))
        self.wait()

        OB.add_updater(lambda m:m.put_start_and_end_on(O.get_center(),B.get_center()))

        self.play(
            t.increment_value,0.7,
            rate_func=linear,
            run_time=2,
            )
        self.play(
            t.increment_value,-0.35,
            rate_func=linear,
            run_time=1,
            )
        self.play(
            t.increment_value,0.40,
            rate_func=linear,
            run_time=1,
            )
        self.play(
            t.increment_value,-0.25,
            rate_func=linear,
            run_time=1,
            )
        self.wait()
        
        P0B = Arrow(
            P0.get_center(),B.get_center(),
            max_tip_length_to_length_ratio=0.2/get_distance(P0.get_center(), B.get_center()),
            buff=0,stroke_width=3,color=BLACK,
            )
        P0P1 = Arrow(
            P0.get_center(),P1.get_center(),
            max_tip_length_to_length_ratio=0.2/get_distance(P0.get_center(),P1.get_center()),
            buff=0,stroke_width=3,color=BLACK,
            )
        
        self.play(
            FadeInFromLarge(P0B ,about_point=ORIGIN),
            FadeInFromLarge(P0P1,about_point=ORIGIN),
            )
        self.wait()
        self.play(
            ReplacementTransform(P0B ,text[1][0:6]),
            ReplacementTransform(P0P1,text[1][7:15]),
            )
        self.play(
            Write(text[1][6]),
            Write(text[1][15:]),
            )
        self.wait(2)
        self.play(
            ReplacementTransform(text[1][0:6],text[2][0:6]),
            ReplacementTransform(text[1][7:15],text[2][8:16]),
            ReplacementTransform(text[1][15:17],text[2][6:8]),
            FadeOut(text[1][6]),
            run_time=2,
            )
        self.wait()
        self.play(
            ReplacementTransform(text[2][0:3].copy(),text[3][0:3]),
            ReplacementTransform(text[2][0:3].copy(),text[3][6:9]),
            ReplacementTransform(text[2][3:5].copy(),text[3][10:12]),
            ReplacementTransform(text[2][5].copy(),text[3][4]),
            ReplacementTransform(text[2][6:8].copy(),text[3][12:14]),
            ReplacementTransform(text[2][8:12].copy(),text[3][15:18]),
            ReplacementTransform(text[2][8:12].copy(),text[3][22:25]),
            ReplacementTransform(text[2][12:14].copy(),text[3][26:28]),
            ReplacementTransform(text[2][14:16].copy(),text[3][19:21]),
            ShowCreation(VGroup(*[text[3][i] for i in [3,5,9,14,18,21,25,28]])),
            run_time=2,
            )
        self.wait(2)
        self.play(ShowCreationThenDestructionAround(text[0]))
        self.play(
            ReplacementTransform(text[3][4:6],text[4][0:2]),
            ReplacementTransform(text[3][10:15],text[4][2:7]),
            ReplacementTransform(text[3][19:22],text[4][7:10]),
            ReplacementTransform(text[3][26:29],text[4][10:13]),
            Erase(VGroup(text[3][0:4],text[3][6:10],text[3][15:19],text[3][22:26])),
            run_time=2,
            )
        self.wait()
        self.play(Write(text[5]),run_time=2)

        text2 =TexMobject(r"\text{线性贝塞尔曲线的参数方程}",color=BLACK).scale(0.8).next_to(text,DOWN)

        self.play(
            ShowCreationThenDestructionAround(text[5]),
            Write(text2),
            run_time=2,
            )
        
        self.wait(2)
        self.play(FadeOut(Group(*self.mobjects[2:])),FadeOut(path))


class scene6(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE
        }
    }
    def construct(self):
        numberplane = NumberPlane(lag_ratio=0.1).set_stroke(opacity=0.3)
        #self.play(ShowCreation(numberplane))
        self.add(numberplane)
        label = Text("贝塞尔曲线原理", font="Source Han Serif CN").scale(0.5).set_color('#FF7F24').to_corner(UL)
        self.add(label)

        t = ValueTracker(0.001)

        P0 = Dot([-5,-3,0],color=BLACK)
        P1 = Dot([-3,+1,0],color=BLACK)
        P2 = Dot([-1,-2,0],color=BLACK)
        label_P0 = TexMobject("P_0",color=BLACK).scale(0.8).next_to(P0,DL/2)
        label_P1 = TexMobject("P_1",color=BLACK).scale(0.8).next_to(P1,UP/2)
        label_P2 = TexMobject("P_2",color=BLACK).scale(0.8).next_to(P2,DR/2)

        Q0 = Dot(color=BLACK).add_updater(lambda m: m.move_to((P1.get_center() - P0.get_center()) * t.get_value() + P0.get_center()))
        Q1 = Dot(color=BLACK).add_updater(lambda m: m.move_to((P2.get_center() - P1.get_center()) * t.get_value() + P1.get_center()))
        label_Q0 = TexMobject("P_0^1",color=BLACK).scale(0.8).add_updater(lambda m:m.next_to(Q0,UL/2))
        label_Q1 = TexMobject("P_1^1",color=BLACK).scale(0.8).add_updater(lambda m:m.next_to(Q1,UR/2))
        
        B  = Dot(color=BLACK).add_updater(lambda m: m.move_to((Q1.get_center() - Q0.get_center()) * t.get_value() + Q0.get_center()))
        label_B  = TexMobject("B  ",color=BLACK).scale(0.8).add_updater(lambda m:m.next_to(B,DOWN/2))
        
        self.play(
            *[FadeIn(mob) for mob in \
                [P0,P1,P2,label_P0,label_P1,label_P2,Q0,Q1,label_Q0,label_Q1,B,label_B]
            ],
            run_time=2,
            )

        path = Line().add_updater(
            lambda pt:pt.become(
                ParametricFunction(
                    lambda t:(
                        ((P2.get_center() - P1.get_center()) * t + P1.get_center()) - \
                        ((P1.get_center() - P0.get_center()) * t + P0.get_center())) * t + \
                        ((P1.get_center() - P0.get_center()) * t + P0.get_center()),
                    t_min = 0,t_max = t.get_value(),stroke_width=7, stroke_color=RED,
            )))

        path_Q0 = Line(stroke_width=10, stroke_color=RED).add_updater(lambda l: l.put_start_and_end_on(P0.get_center(),Q0.get_center()))
        path_Q1 = Line(stroke_width=10, stroke_color=RED).add_updater(lambda l: l.put_start_and_end_on(P1.get_center(),Q1.get_center()))
        path_P0B= Line(stroke_width=10, stroke_color=RED).add_updater(lambda l: l.put_start_and_end_on(Q0.get_center(), B.get_center()))
        path_Q0_sup = Line(P0.get_center(),P1.get_center(),stroke_width=2, stroke_color=BLACK,plot_depth=-1)
        path_Q1_sup = Line(P1.get_center(),P2.get_center(),stroke_width=2, stroke_color=BLACK,plot_depth=-1)
        path_P0B_sup= Line(stroke_width=2, stroke_color=BLACK,plot_depth=-1).add_updater(lambda l: l.put_start_and_end_on(Q0.get_center(), Q1.get_center()))
        self.add(path_Q0,path_Q1,path_P0B,path_Q0_sup,path_Q1_sup,path_P0B_sup)
        
        self.play(
            t.increment_value,0.998,
            rate_func=linear,
            run_time=2,
            )
        self.play(
            t.increment_value,-0.7,
            rate_func=linear,
            run_time=2,
            )

        [mob.clear_updaters() for mob in [path_Q0,path_Q1,path_P0B]]

        text = TexMobject(
            r"P_0^1(t)=(1-t)P_0+tP_1",
            r"P_1^1(t)=(1-t)P_1+tP_2",
            r"B(t)=(1-t)P_0^1+tP_1^1",
            r"B(t)=(1-t)^2P_0+2t(1-t)P_1+t^2P_2",
            color=BLACK,
            ).scale(0.8)
        [text[i+1].next_to(text[i],DOWN,aligned_edge=LEFT) for i in range(len(text)-1)]
        text[2][4].align_to(text[1][6],RIGHT)
        text[2][0:4].align_to(text[1][5],RIGHT)
        text[2][5:].align_to(text[1][7],LEFT)
        text[3].align_to(text[2],LEFT)
        text.to_corner(UR)
        text_P_index = [[0,12,16],[0,12,16],[0,10,15],[0,11,21,26]]
        [[text[j][i].set_color(ORANGE) for i in text_P_index[j]] for j in range(len(text_P_index))]
        text_t_index = [[4,10,15],[4,10,15],[2,8,14],[2,8,15,19,24]]
        [[text[j][i].set_color(RED) for i in text_t_index[j]] for j in range(len(text_t_index))]
        text_lower_index = [[2,13,17],[2,13,17],[12,17],[12,22,27]]
        [[text[j][i].set_color(GOLD) for i in text_lower_index[j]] for j in range(len(text_lower_index))]
        text_upper_index = [[1],[1],[11,16],[10,25]]
        [[text[j][i].set_color('#BF3EFF') for i in text_upper_index[j]] for j in range(len(text_upper_index))]
        textbg = BackgroundRectangle(text,fill_opacity=0.3)
        #[debugTex(self,text[i]) for i in range(len(text))]

        self.play(ShowCreation(textbg))
        self.play(
            ReplacementTransform(path_Q0 ,text[0]),
            ReplacementTransform(path_Q1 ,text[1]),
            ReplacementTransform(path_P0B,text[2]),
            run_time=2,
            )
        self.play(
            t.set_value,0.001,
            rate_func=rush_into,
            run_time=1,
            )
        self.add(path)
        self.play(
            t.increment_value,0.998,
            rate_func=linear,
            run_time=2,
            )
        self.play(
            t.increment_value,-0.5,
            rate_func=rush_into,
            run_time=2,
            )
        self.wait()

        self.play(
            ShowCreationThenDestructionAround(text[0][7:]),
            ShowCreationThenDestructionAround(text[1][7:]),
            ReplacementTransform(text[0][0:3].copy(),text[2][10:13].copy()),
            ReplacementTransform(text[1][0:3].copy(),text[2][15:17].copy()),
            run_time=2,
            )
        self.wait()
        self.play(Write(text[3]))

        text2 =TexMobject(r"\text{二次贝塞尔曲线的参数方程}",color=BLACK).scale(0.8).next_to(text,DOWN)

        self.play(
            ShowCreationThenDestructionAround(text[3]),
            Write(text2),
            run_time=2,
            )
        self.wait(3)
        self.play(FadeOut(Group(*self.mobjects)),FadeOut(VGroup(path,path_Q0_sup,path_Q1_sup)))


class scene7(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE
        }
    }
    def construct(self):
        P0 = Dot(np.array([-5.5, -1.5, 0]),color=BLACK)
        P1 = Dot(np.array([-6.1,  1.5, 0]),color=BLACK)
        P2 = Dot(np.array([-3.0,  1.5, 0]),color=BLACK)
        P3 = Dot(np.array([-1.0, -1.5, 0]),color=BLACK)
        P = VGroup(P0, P1, P2, P3)
        label_P0 = TexMobject("P_0",color=BLACK).scale(0.8).next_to(P0,DL)
        label_P1 = TexMobject("P_1",color=BLACK).scale(0.8).next_to(P1,UL)
        label_P2 = TexMobject("P_2",color=BLACK).scale(0.8).next_to(P2,UR)
        label_P3 = TexMobject("P_3",color=BLACK).scale(0.8).next_to(P3,DR)
        label_P = VGroup(label_P0,label_P1,label_P2,label_P3)
        
        P0_P1 = Line(P0, P1, stroke_width=2, stroke_color=BLACK, plot_depth=-1)
        P1_P2 = Line(P1, P2, stroke_width=2, stroke_color=BLACK, plot_depth=-1)
        P2_P3 = Line(P2, P3, stroke_width=2, stroke_color=BLACK, plot_depth=-1)
        P_lines = VGroup(P0_P1, P1_P2, P2_P3)

        t = ValueTracker(0.001)

        Q0 = Dot(color=BLUE).add_updater(lambda m: m.move_to((P1.get_center() - P0.get_center()) * t.get_value() + P0.get_center()))
        Q1 = Dot(color=BLUE).add_updater(lambda m: m.move_to((P2.get_center() - P1.get_center()) * t.get_value() + P1.get_center()))
        Q2 = Dot(color=BLUE).add_updater(lambda m: m.move_to((P3.get_center() - P2.get_center()) * t.get_value() + P2.get_center()))
        Q = VGroup(Q0, Q1, Q2)
        label_Q0 = TexMobject("P_0^1",color=BLACK).scale(0.8).add_updater(lambda m:m.next_to(Q0,LEFT))
        label_Q1 = TexMobject("P_1^1",color=BLACK).scale(0.8).add_updater(lambda m:m.next_to(Q1,UP/3))
        label_Q2 = TexMobject("P_2^1",color=BLACK).scale(0.8).add_updater(lambda m:m.next_to(Q2,UR/3))
        label_Q = VGroup(label_Q0,label_Q1,label_Q2)

        Q0_Q1 = Line(stroke_width=2, stroke_color=BLACK,plot_depth=-1)\
            .add_updater(lambda m: m.put_start_and_end_on(Q0.get_center(), Q1.get_center()))
        Q1_Q2 = Line(stroke_width=2, stroke_color=BLACK,plot_depth=-1)\
            .add_updater(lambda m: m.put_start_and_end_on(Q1.get_center(), Q2.get_center()))
        Q_lines = VGroup(Q0_Q1, Q1_Q2)

        R0 = Dot(color=GREEN).add_updater(lambda m: m.move_to((Q1.get_center() - Q0.get_center()) * t.get_value() + Q0.get_center()))
        R1 = Dot(color=GREEN).add_updater(lambda m: m.move_to((Q2.get_center() - Q1.get_center()) * t.get_value() + Q1.get_center()))
        R = VGroup(R0, R1)
        label_R0 = TexMobject("P_0^2",color=BLACK).scale(0.8).add_updater(lambda m:m.next_to(R0,DR/2))
        label_R1 = TexMobject("P_1^2",color=BLACK).scale(0.8).add_updater(lambda m:m.next_to(R1,DL/2))
        label_R = VGroup(label_R0,label_R1)

        R0_R1 = Line(stroke_width=2, stroke_color=BLACK,plot_depth=-1)\
            .add_updater(lambda m: m.put_start_and_end_on(R0.get_center(), R1.get_center()))

        B = Dot(color=RED).add_updater(lambda m: m.move_to((R1.get_center() - R0.get_center()) * t.get_value() + R0.get_center()))
        label_B = TexMobject("B",color=BLACK).scale(0.8).add_updater(lambda m:m.next_to(B,DOWN/2))

        path_Q0 = Line(stroke_width=10, stroke_color=BLUE)\
            .add_updater(lambda m: m.put_start_and_end_on(P0.get_center(), Q0.get_center()))
        path_Q1 = Line(stroke_width=10, stroke_color=BLUE)\
            .add_updater(lambda m: m.put_start_and_end_on(P1.get_center(), Q1.get_center()))
        path_Q2 = Line(stroke_width=10, stroke_color=BLUE)\
            .add_updater(lambda m: m.put_start_and_end_on(P2.get_center(), Q2.get_center()))
        path_R0 = Line(stroke_width=10, stroke_color=GREEN)\
            .add_updater(lambda m: m.put_start_and_end_on(Q0.get_center(), R0.get_center()))
        path_R1 = Line(stroke_width=10, stroke_color=GREEN)\
            .add_updater(lambda m: m.put_start_and_end_on(Q1.get_center(), R1.get_center()))
        path_B  = Line(stroke_width=10, stroke_color=RED)\
            .add_updater(lambda m: m.put_start_and_end_on(R0.get_center(),  B.get_center()))
        path = TracedPath(B.get_center, stroke_width=7, stroke_color=RED)

        text = TexMobject(
            r"P_0^1(t)=(1-t)P_0+tP_1",
            r"P_1^1(t)=(1-t)P_1+tP_2",
            r"P_2^1(t)=(1-t)P_2+tP_3",
            r"P_0^2(t)=(1-t)P_0^1+tP_1^1",
            r"P_1^2(t)=(1-t)P_1^1+tP_2^1",
            r"    B(t)=(1-t)P_0^2+tP_1^2",
            r"B(t)=(1-t)^3P_0+3t(1-t)^2P_1\\+3t^2(1-t)P_2+t^3P_3",
            color=BLACK,
            ).scale(0.8)
        [text[i+1].next_to(text[i],DOWN,aligned_edge=LEFT) for i in range(len(text)-1)]
        text.to_corner(UR)
        text_P_index = [[0,12,16],[0,12,16],[0,12,16],[0,12,17],[0,12,17],[0,10,15],[0,11,22,33,38]]
        [[text[j][i].set_color(ORANGE) for i in text_P_index[j]] for j in range(len(text_P_index))]
        text_t_index = [[4,10,15],[4,10,15],[4,10,15],[4,10,16],[4,10,16],[2,8,14],[2,8,15,19,26,31,36]]
        [[text[j][i].set_color(RED) for i in text_t_index[j]] for j in range(len(text_t_index))]
        text_lower_index = [[2,13,17],[2,13,17],[2,13,17],[2,14,19],[2,14,19],[12,17],[12,23,34,39]]
        [[text[j][i].set_color(GOLD) for i in text_lower_index[j]] for j in range(len(text_lower_index))]
        text_upper_index = [[1],[1],[1],[1,13,18],[1,13,18],[11,16],[10,21,27,37]]
        [[text[j][i].set_color('#BF3EFF') for i in text_upper_index[j]] for j in range(len(text_upper_index))]
        textbg = BackgroundRectangle(text,fill_opacity=0.3)
        #self.add(text,textbg)
        #[debugTex(self,text[i]) for i in range(len(text))]

        label = Text("三次贝塞尔曲线", font="Source Han Serif CN").scale(0.5).set_color('#FF7F24').to_corner(UL)
        
        self.play(
            *[FadeIn(mob) for mob in \
                [
                    P,label_P,P_lines,
                    Q,label_Q,Q_lines,
                    R,label_R,R0_R1,
                    B,label_B,
                    path_Q0,path_Q1,path_Q2,
                    path_R0,path_R1,
                    path_B,
                    path,
                ]
            ],
            run_time=2,
            )

        self.play(
            t.increment_value,0.5,
            rate_func=rush_into,
            run_time=3,
            )
        self.wait()

        self.play(ShowCreation(textbg))

        path_Q0.clear_updaters()
        path_Q1.clear_updaters()
        path_Q2.clear_updaters()
        self.play(
            ReplacementTransform(path_Q0,text[0]),
            ReplacementTransform(path_Q1,text[1]),
            ReplacementTransform(path_Q2,text[2]),
            run_time=2,
            )
        self.wait()

        path_R0.clear_updaters()
        path_R1.clear_updaters()
        self.play(
            ReplacementTransform(path_R0,text[3]),
            ReplacementTransform(path_R1,text[4]),
            run_time=2,
            )
        self.wait()

        path_B.clear_updaters()
        self.play(
            ReplacementTransform(path_B ,text[5]),
            run_time=2,
            )
        self.wait()

        self.play(
            t.increment_value,0.498,
            rate_func=rush_into,
            run_time=2,
            )
        
        self.play(
            ShowCreationThenDestructionAround(text[0][7:]),
            ShowCreationThenDestructionAround(text[1][7:]),
            ReplacementTransform(text[0][:6].copy(),text[3][12:15]),
            ReplacementTransform(text[1][:6].copy(),text[3][17:20]),
            )
        self.wait()

        self.play(
            ShowCreationThenDestructionAround(text[1][7:]),
            ShowCreationThenDestructionAround(text[2][7:]),
            ReplacementTransform(text[1][:6].copy(),text[4][12:15]),
            ReplacementTransform(text[2][:6].copy(),text[4][17:20]),
            )
        self.wait()
        
        self.play(
            ShowCreationThenDestructionAround(text[3][7:]),
            ShowCreationThenDestructionAround(text[4][7:]),
            ReplacementTransform(text[3][:6].copy(),text[5][10:13]),
            ReplacementTransform(text[4][:6].copy(),text[5][15:18]),
            )
        self.wait()
        
        self.play(
            Write(text[6]),
            run_time=2,
            )

        text2 =TexMobject(r"\text{三次贝塞尔曲线的参数方程}",color=BLACK).scale(0.8).next_to(text,DOWN)
        self.play(ShowCreation(SurroundingRectangle(text[6])))
        self.play(ReplacementTransform(Group(*self.mobjects[-1]),text2))

        self.wait(3)
        self.play(FadeIn(Square(fill_opacity=1,fill_color=WHITE).scale(10)))


class scene8(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE
        }
    }
    def construct(self):

        text = TexMobject(
            r"\text{线性贝塞尔：}P^1(t)=(1-t)P_0+tP_1=\sum_{i=0}^{1}C_1^i(1-t)^{1-i}t^iP_i",
            r"\text{二次贝塞尔：}P^2(t)=(1-t)^2P_0+2t(1-t)P_1+t^2P_2=\sum_{i=0}^{2}C_2^i(1-t)^{1-i}t^iP_i",
            r"\text{三次贝塞尔：}P^3(t)=(1-t)^3P_0+3t(1-t)^2P_1+3t^2(1-t)P_2+t^3P_3=\sum_{i=0}^{3}C_3^i(1-t)^{1-i}t^iP_i",
            color=BLACK,
            ).scale(0.6)
        [text[i+1].next_to(text[i],DOWN,aligned_edge=LEFT) for i in range(len(text)-1)]
        text.to_corner(UL)
        #[debugTex(self,text[i]) for i in range(len(text))]
        text_P_index = [[6,17,21,42],[6,18,28,33,54],[6,18,29,40,45,66]]
        [[text[j][i].set_color(ORANGE) for i in text_P_index[j]] for j in range(len(text_P_index))]
        text_t_index = [[9,15,20,35,40],[9,15,22,26,31,47,52],[9,15,22,26,33,38,43,59,64]]
        [[text[j][i].set_color(RED) for i in text_t_index[j]] for j in range(len(text_t_index))]

        text2 = TexMobject(
            r"P_0\ \ P_1\ \ P_2\ \ P_3",
            r"P_0^1\ \ P_1^1\ \ P_2^1",
            r"P_0^2\ \ P_1^2",
            r"P_0^3",
            color=BLACK,
            ).scale(0.6)
        [text2[i+1].next_to(text2[i],DOWN) for i in range(len(text2)-1)]
        text2.to_corner(DR)
        text2_P_index = [[0,2,4,6],[0,3,6],[0,3],[0]]
        [[text2[j][i].set_color(ORANGE) for i in text2_P_index[j]] for j in range(len(text2_P_index))]

        #text2bg = BackgroundRectangle(text2,fill_opacity=0.3,fill_color=YELLOW)
        #[debugTex(self,text2[i]) for i in range(len(text2))]

        text3 = TexMobject(
            r'''
            P_i^k=\begin{cases}
            P_i & k=0\\
            (1-t)P_i{k-1}+tP_{i+1}^{k-1} & k>0\\
            \end{cases}
            ''',
            color=BLACK,
            ).scale(0.6).next_to(text2,UP,aligned_edge=RIGHT)
        text3_P_index = [[0,5,15,22]]
        [[text3[j][i].set_color(ORANGE) for i in text3_P_index[j]] for j in range(len(text3_P_index))]
        text3_t_index = [[13,21]]
        [[text3[j][i].set_color(RED) for i in text3_t_index[j]] for j in range(len(text3_t_index))]

        #text3bg = BackgroundRectangle(text3,fill_opacity=0.3)
        #[debugTex(self,text3[i]) for i in range(len(text3))]

        text4 = TexMobject(
            r"\cdots\cdots\cdots",
            r"n\text{次贝塞尔：}P^n(t)=\sum_{i=0}^{n}C_n^i(1-t)^{1-i}t^iP_i",
            r"\Rightarrow B(t)=P^n(t)=\sum_{i=0}^{n}P_ib_{i,n}(t)\ \ (b_{i,n}(t)=C_n^i(1-t)^{1-i}t^i,\text{伯恩斯坦基多项式})",
            color=BLACK,
            ).scale(0.6).next_to(text,DOWN,aligned_edge=LEFT)
        [text4[i+1].next_to(text4[i],DOWN,aligned_edge=LEFT) for i in range(len(text4)-1)]
        [text4[0][3*i:3*i+3].rotate(PI/2)for i in range(3)]
        text4.next_to(text,DOWN)
        text4[1:].next_to(text4[0],DOWN).align_to(text,LEFT)
        text4_P_index = [[],[6,30],[1,6,17]]
        [[text4[j][i].set_color(ORANGE) for i in text4_P_index[j]] for j in range(len(text4_P_index))]
        text4_t_index = [[],[9,23,28],[3,9,24,32,41,46]]
        [[text4[j][i].set_color(RED) for i in text4_t_index[j]] for j in range(len(text4_t_index))]
        #[debugTex(self,text4[i]) for i in range(len(text4))]

        text5 = TexMobject(
            r"B(t)=\sum_{i=0}^{n}P_ib_{i,n}(t)",
            color=BLACK,
            )

        self.play(
            Write(text[0][:23]),
            run_time=2,
            )
        self.play(
            Write(text[1][:35]),
            run_time=2,
            )
        self.play(
            Write(text[2][:47]),
            run_time=2,
            )
        self.wait()

        self.play(
            Write(text[0][23:]),
            Write(text[1][35:]),
            Write(text[2][47:]),
            run_time=2,
            )
        self.wait()

        self.play(
            Write(text2[0]),
            #FadeIn(text2bg),
            run_time=2,
            )
        self.play(
            *[
                ReplacementTransform(text2[0][0+2*i:4+2*i].copy(),text2[1][0+3*i:3+3*i])\
                for i in range(3)
            ],
            run_time=1,
            )
        self.play(
            *[
                ReplacementTransform(text2[1][0+3*i:6+3*i].copy(),text2[2][0+3*i:3+3*i])\
                for i in range(2)
            ],
            run_time=1,
            )
        self.play(
            *[
                ReplacementTransform(text2[2][0+3*i:6+3*i].copy(),text2[3][0+3*i:3+3*i])\
                for i in range(1)
            ],
            run_time=1,
            )
        self.play(
            Write(text3),
            #FadeIn(text3bg),
            run_time=2,
            )
        self.wait()
        [self.play(Write(text4[int(i/2)], run_time=(2,1)[i==0])) if i%2==0 else self.wait((2,1)[i==0]) for i in range(2*3)]
        self.wait(2)

        self.play(
            FadeOut(Group(*self.mobjects[:-1],*self.mobjects[-1][0],*self.mobjects[-1][5:11],*self.mobjects[-1][26:])),
            ReplacementTransform(Group(*self.mobjects[-1][1:5]),text5[0][0:4]),
            ReplacementTransform(Group(*self.mobjects[-1][11:26]),text5[0][4:]),
            )
        self.wait(2)


class scene9(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE
        }
    }
    def construct(self):
        img1 =ImageMobject(r"C:\Users\Administrator\Desktop\BezierCurve\img1.png").scale(2).shift(LEFT*2.5)
        text1 = Text("@鹤翔万里",font='未署名的信',color='#D15FEE').scale(0.5).next_to(img1,DOWN)
        img2 =ImageMobject(r"C:\Users\Administrator\Desktop\BezierCurve\img2.png").scale(2).shift(RIGHT*2.5)
        text2 = Text("@有一种悲伤叫颓废",font='未署名的信',color='#DB7093').scale(0.5).next_to(img2,DOWN)

        self.play(FadeInFromDown(img1),FadeInFromDown(img2))
        self.play(FadeInFromDown(text1),FadeInFromDown(text2))
        self.wait(3)
