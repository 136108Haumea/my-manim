# my-manim
# Decadance
# 仅供学习用

class ruledsurfacedef(Scene):
    def construct(self):
        text = Text(
            "def:直纹曲面，由一条直线连续运动所构成的曲面", 
            font='Source Han Sans Bold',
            ).scale(0.6)
        text2 = Text(
            "下面看看一组直纹曲面的例子吧", 
            font='Source Han Sans Bold',
            ).scale(0.6)
        VGroup(text, text2).arrange(DOWN)
        
        text[4:8].set_color('#D02090')
        text[12:14].set_color('#FF8C00')
        text[14:18].set_color('#1E90FF')
        text[22:24].set_color('#CD853F')
        text2[6:10].set_color('#D02090')

        #debugTex(self, text)
        #debugTex(self, text2)

        self.play(
            FadeInFromRandom(text), 
            run_time = 3, 
            rate_func=linear, 
            )
        self.wait(4)
        self.play(
            FadeInFromRandom(text2), 
            run_time = 3, 
            rate_func=linear, 
            )
        self.wait(3)
        self.play(
            FadeOutFromRandom(text),
            FadeOutFromRandom(text2), 
            run_time = 3, 
            rate_func=linear, 
            )

        #self.add(text, text2)


class SweepSurface1(SpecialThreeDScene):
    CONFIG = {
        "default_angled_camera_position": {
            "phi": 70 * DEGREES,
            "theta": -60 * DEGREES,
            "distance": 50,
            },
        "camera_config": {
            "background_color":BLACK,
            },
        }
    def construct(self):
        #axes = ThreeDAxes()
        #self.add(axes)
        self.set_camera_to_default_position()

        var = ValueTracker(0)
        a,d = 2,2

        par = ParametricSurface(lambda u, v: ORIGIN)\
            .add_updater(
                lambda p:p.become(
                    ParametricSurface(
                        lambda u, v: np.array([a*np.cos(u), a*np.sin(u), v]),
                        u_min=0, u_max=var.get_value(), v_min=-d, v_max=+d,
                        stroke_color=WHITE, stroke_opacity=1,
                        fill_color='#FFBBFF', fill_opacity=0.5,
                        checkerboard_colors=['#FFE1FF','#FFBBFF'],
                        resolution=(20,40), 
                    )))
        self.add(par)
        
        line = Line()\
            .add_updater(lambda l: l.become(
            Line(
                np.array([a*np.cos(var.get_value()), a*np.sin(var.get_value()), +d]),
                np.array([a*np.cos(var.get_value()), a*np.sin(var.get_value()), -d]),
                color='#A0522D', stroke_withd=15,
                )))
        self.add(line)

        self.play(var.set_value, 2*PI, run_time=6, rate_func=linear)
        line.clear_updaters()
        self.mobjects.remove(line)
        self.move_camera(
            phi=30*DEGREES,
            theta=120*DEGREES,
            distance=6,
            rate_func=smooth,
            run_time=3,
            )

        self.wait(2)


class SweepSurface2(SpecialThreeDScene):
    CONFIG = {
        "default_angled_camera_position": {
            "phi": 70 * DEGREES,
            "theta": -60 * DEGREES,
            "distance": 50,
            },
        "camera_config": {
            "background_color":BLACK,
            },
        }
    def construct(self):
        #axes = ThreeDAxes()
        #self.add(axes)
        self.set_camera_to_default_position()

        var = ValueTracker(0)
        a,d = 1.5,2

        par = ParametricSurface(lambda u, v: ORIGIN)\
            .add_updater(
                lambda p:p.become(
                    ParametricSurface(
                        lambda u, v: v*np.array([a*np.cos(u), a*np.sin(u), a]),
                        u_min=0, u_max=var.get_value(), v_min=-d, v_max=+d,
                        stroke_color=WHITE, stroke_opacity=1,
                        fill_color='#EEEE00', fill_opacity=0.5,
                        checkerboard_colors=['#EEE685','#EEEE00'],
                        resolution=(20,40), 
                    )))
        self.add(par)
        
        line = Line()\
            .add_updater(lambda l: l.become(
            Line(
                +d*np.array([a*np.cos(var.get_value()), a*np.sin(var.get_value()), a]),
                -d*np.array([a*np.cos(var.get_value()), a*np.sin(var.get_value()), a]),
                color='#A0522D', stroke_withd=15,
                )))
        self.add(line)

        self.play(var.set_value, 2*PI, run_time=6, rate_func=linear)
        line.clear_updaters()
        self.mobjects.remove(line)
        self.move_camera(
            phi=30*DEGREES,
            theta=120*DEGREES,
            distance=6,
            rate_func=smooth,
            run_time=3,
            )

        self.wait(2)


class SweepSurface3(SpecialThreeDScene):
    CONFIG = {
        "default_angled_camera_position": {
            "phi": 70 * DEGREES,
            "theta": -60 * DEGREES,
            "distance": 50,
            },
        "camera_config": {
            "background_color":BLACK,
            },
        }
    def construct(self):
        #axes = ThreeDAxes()
        #self.add(axes)
        self.set_camera_to_default_position()

        var = ValueTracker(0)
        t = ValueTracker(0)
        umax = ValueTracker(0)
        a,d = 1.5,1.5

        par = ParametricSurface(lambda u, v: ORIGIN)\
            .add_updater(
                lambda p:p.become(
                    ParametricSurface(
                        lambda u, v: (1-v)*np.array([a*np.cos(u-t.get_value()), a*np.sin(u-t.get_value()), -1])+
                            v*np.array([a*np.cos(u+t.get_value()), a*np.sin(u+t.get_value()), +1]),
                        u_min=0, u_max=umax.get_value(), v_min=d-2, v_max=d,
                        stroke_color=WHITE, stroke_opacity=1,
                        fill_color='#0000CD', fill_opacity=0.8,
                        checkerboard_colors=['#00BFFF','#0000CD'],
                        resolution=(20,50), 
                    )))
        #self.add(par)
        
        line = Line()\
            .add_updater(lambda l: l.become(
            Line(
                (3-d)*np.array([a*np.cos(umax.get_value()-t.get_value()), a*np.sin(umax.get_value()-t.get_value()), -1])+
                    (d-2)*np.array([a*np.cos(umax.get_value()+t.get_value()), a*np.sin(umax.get_value()+t.get_value()), +1]),
                (1-d)*np.array([a*np.cos(umax.get_value()-t.get_value()), a*np.sin(umax.get_value()-t.get_value()), -1])+
                    (d-0)*np.array([a*np.cos(umax.get_value()+t.get_value()), a*np.sin(umax.get_value()+t.get_value()), +1]),
                color='#A0522D', stroke_withd=15,
                )))
        self.add(line)

        t.increment_value(PI/3)

        self.add(par)
        self.play(umax.increment_value, 2*PI, run_time=6, rate_func=linear)
        line.clear_updaters()
        self.mobjects.remove(line)
        self.move_camera(
            phi=55*DEGREES,
            theta=-30*DEGREES,
            distance=50,
            rate_func=smooth,
            run_time=3,
            )
        self.wait(2)


class SweepSurface4(SpecialThreeDScene):
    CONFIG = {
        "default_angled_camera_position": {
            "phi": 70 * DEGREES,
            "theta": -60 * DEGREES,
            "distance": 50,
            },
        "camera_config": {
            "background_color":BLACK,
            },
        }
    def construct(self):
        #axes = ThreeDAxes()
        #self.add(axes)
        self.set_camera_to_default_position()

        var = ValueTracker(0)
        a,d,phi = 3,0.8,PI/3

        par = ParametricSurface(lambda u, v: ORIGIN)\
            .add_updater(
                lambda p:p.become(
                    ParametricSurface(
                        lambda u, v: np.array([
                        a*np.cos(2*u)+v*np.cos(u)*np.cos(2*u), 
                        a*np.sin(2*u)+v*np.cos(u)*np.sin(2*u), 
                        np.sin(u)*v]),
                        u_min=0, u_max=var.get_value(), v_min=-d, v_max=+d,
                        stroke_color=WHITE, stroke_opacity=1,
                        fill_color='#8B1C62', fill_opacity=0.8,
                        checkerboard_colors=['#FF34B3','#8B1C62'],
                        resolution=(30,40), 
                    )))
        self.add(par)
        
        line = Line()\
            .add_updater(lambda l: l.become(
            Line(
                np.array([
                    a*np.cos(2*var.get_value())+d*np.cos(var.get_value())*np.cos(2*var.get_value()), 
                    a*np.sin(2*var.get_value())+d*np.cos(var.get_value())*np.sin(2*var.get_value()), 
                    np.sin(var.get_value())*(+d)]),
                np.array([
                    a*np.cos(2*var.get_value())-d*np.cos(var.get_value())*np.cos(2*var.get_value()), 
                    a*np.sin(2*var.get_value())-d*np.cos(var.get_value())*np.sin(2*var.get_value()), 
                    np.sin(var.get_value())*(-d)]),
                color='#A0522D', stroke_withd=15,
                )))
        self.add(line)

        self.play(var.set_value, PI, run_time=6, rate_func=linear)
        line.clear_updaters()
        self.mobjects.remove(line)
        self.move_camera(
            phi=30*DEGREES,
            theta=120*DEGREES,
            distance=6,
            rate_func=smooth,
            run_time=3,
            )

        self.wait(2)


class SweepSurface5(SpecialThreeDScene):
    CONFIG = {
        "default_angled_camera_position": {
            "phi": 70 * DEGREES,
            "theta": -60 * DEGREES,
            "distance": 50,
            },
        "camera_config": {
            "background_color":BLACK,
            },
        }
    def construct(self):
        #axes = ThreeDAxes()
        #self.add(axes)
        self.set_camera_to_default_position()

        var = ValueTracker(0)
        a,d,phi = 0.4,2,PI/3

        par = ParametricSurface(lambda u, v: ORIGIN)\
            .add_updater(
                lambda p:p.become(
                    ParametricSurface(
                        lambda u, v: np.array([v*np.cos(u), v*np.sin(u), a*u])+2*IN, 
                        u_min=0, u_max=var.get_value(), v_min=0, v_max=d,
                        stroke_color=WHITE, stroke_opacity=1,
                        fill_color='#FFDAB9', fill_opacity=0.8,
                        checkerboard_colors=['#FFF8DC','#FFDAB9'],
                        resolution=(20,50), 
                    )))
        self.add(par)
        
        line = Line()\
            .add_updater(lambda l: l.become(
            Line(
                np.array([0, 0, a*var.get_value()])+2*IN,
                np.array([
                    d*np.cos(var.get_value()), d*np.sin(var.get_value()), a*var.get_value()
                    ])+2*IN,
                color='#A0522D', stroke_withd=15,
                )))
        self.add(line)

        self.play(var.set_value, 4*PI, run_time=6, rate_func=linear)
        line.clear_updaters()
        self.mobjects.remove(line)
        self.move_camera(
            phi=30*DEGREES,
            theta=120*DEGREES,
            distance=6,
            rate_func=smooth,
            run_time=3
            )

        self.wait(2)


class SweepSurface6(SpecialThreeDScene):
    CONFIG = {
        "default_angled_camera_position": {
            "phi": 90 * DEGREES,
            "theta": 0 * DEGREES,
            "distance": 50,
            },
        "camera_config": {
            "background_color":BLACK,
            },
        }
    def construct(self):
        axes = ThreeDAxes()
        self.add(axes)
        self.set_camera_to_default_position()

        var = ValueTracker(0)
        t = ValueTracker(0)
        umax = ValueTracker(0)
        a,d = 1.5,1.5

        par = ParametricSurface(lambda u, v: ORIGIN)\
            .add_updater(
                lambda p:p.become(
                    ParametricSurface(
                        lambda u, v: (1-v)*np.array([a*np.cos(u-t.get_value()), a*np.sin(u-t.get_value()), -1])+
                            v*np.array([a*np.cos(u+t.get_value()), a*np.sin(u+t.get_value()), +1]),
                        u_min=0, u_max=umax.get_value(), v_min=d-2, v_max=d,
                        stroke_color=WHITE, stroke_opacity=1,
                        fill_color='#FFDAB9', fill_opacity=0.8,
                        checkerboard_colors=['#FFF8DC','#FFDAB9'],
                        resolution=(20,50), 
                    )))
        #self.add(par)
        
        line = Line()\
            .add_updater(lambda l: l.become(
            Line(
                (3-d)*np.array([a*np.cos(umax.get_value()-t.get_value()), a*np.sin(umax.get_value()-t.get_value()), -1])+
                    (d-2)*np.array([a*np.cos(umax.get_value()+t.get_value()), a*np.sin(umax.get_value()+t.get_value()), +1]),
                (1-d)*np.array([a*np.cos(umax.get_value()-t.get_value()), a*np.sin(umax.get_value()-t.get_value()), -1])+
                    (d-0)*np.array([a*np.cos(umax.get_value()+t.get_value()), a*np.sin(umax.get_value()+t.get_value()), +1]),
                color='#A0522D', stroke_withd=15,
                )))
        self.add(line)

        self.wait()
        self.play(t.increment_value, 2*PI, run_time=4, rate_func=linear)
        self.move_camera(
            phi=70*DEGREES,
            theta=-60*DEGREES,
            distance=50,
            rate_func=smooth,
            run_time=3
            )
        self.add(par)
        self.play(umax.increment_value, 2*PI, run_time=6, rate_func=linear)
        line.clear_updaters()
        self.mobjects.remove(line)
        self.wait(2)
        self.play(t.increment_value, 1*PI, run_time=6, rate_func=linear)

        self.wait(2)


class SweepSurface7(SpecialThreeDScene):
    CONFIG = {
        "default_angled_camera_position": {
            "phi": 70 * DEGREES,
            "theta": -60 * DEGREES,
            "distance": 50,
            },
        "camera_config": {
            "background_color":BLACK,
            },
        }
    def construct(self):
        #axes = ThreeDAxes()
        #self.add(axes)
        self.set_camera_to_default_position()

        var = ValueTracker(0)
        t = ValueTracker(0)
        a,d,phi = 0.4,3,PI/3
        a1 = np.array([-d, -d, +d])
        b1 = np.array([-d, +d, -0])
        a2 = np.array([+d, -d, -0])
        b2 = np.array([+d, +d, +d])

        par = ParametricSurface(lambda u, v: ORIGIN)\
            .add_updater(
                lambda p:p.become(
                    ParametricSurface(
                        lambda u, v: 
                            (1-v)*((1-u)*a1+u*a2)+
                            (0+v)*((1-u)*b1+u*b2), 
                        u_min=0, u_max=t.get_value(), v_min=0, v_max=1,
                        stroke_color=WHITE, stroke_opacity=1,
                        fill_color='#DA70D6', fill_opacity=0.8,
                        checkerboard_colors=['#DDA0DD','#DA70D6'],
                        resolution=(40,40), 
                    )))
        self.add(par)
        
        line = Line()\
            .add_updater(lambda l: l.become(
            Line(
                (1-0)*((1-t.get_value())*a1+t.get_value()*a2)+
                (0+0)*((1-t.get_value())*b1+t.get_value()*b2),
                (1-1)*((1-t.get_value())*a1+t.get_value()*a2)+
                (0+1)*((1-t.get_value())*b1+t.get_value()*b2),
                color='#A0522D', stroke_withd=15,
                )))
        self.add(line)

        self.play(t.set_value, 1, run_time=6, rate_func=linear)
        line.clear_updaters()
        self.mobjects.remove(line)
        self.move_camera(
            phi=55*DEGREES,
            theta=60*DEGREES,
            distance=50,
            rate_func=smooth,
            run_time=3,
            )

        self.wait(2)


