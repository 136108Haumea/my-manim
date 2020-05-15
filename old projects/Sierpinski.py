from manimlib.imports import *
import math


class Sierpinski1(SpecialThreeDScene):
    CONFIG = {
        "default_angled_camera_position": {
            "phi": 70 * DEGREES,
            "theta": -45 * DEGREES,
            "distance": 50,
            },
        "camera_config": {
            "background_color":BLACK,
            },
        "iteration":4,
        "sponge_size":4,
        }
    def construct(self):
        self.set_camera_to_default_position()
        #self.add(self.get_axes())
        Sponge = MyBoxes(
            bottom_size=[self.sponge_size,self.sponge_size],
            box_height=self.sponge_size,
            resolution=(1,1),
            fill_color='#388E8E',
            )
        for _ in range(self.iteration-1):
            #mark = Sponge.scale(1/3).move_to(UL*self.sponge_size/3+IN*self.sponge_size/3)
            self.play(
                Sponge.scale,1/3,
                Sponge.move_to,UL*self.sponge_size/3+IN*self.sponge_size/3,
                rate_func=smooth,
                run_time=2,
                )
            mark = Sponge
            pos = [RIGHT,RIGHT,DOWN,DOWN,LEFT,LEFT,UP]
            a = VGroup(mark)
            for i in range(len(pos)):
                a.add(mark.copy().next_to(a[-1],pos[i],buff=0))
            for i in range(5):
                a.add(mark.copy().next_to(a[2*i],OUT,buff=0))
            for i in range(len(pos)):
                a.add(mark.copy().next_to(a[-1],pos[i],buff=0))
            Sponge = a
            self.play(ShowCreation(a[1:]),run_time=3)
        #self.add(Sponge)
        self.wait()
        self.move_camera(
            phi=90*DEGREES,
            theta=0*DEGREES,
            distance=40,
            rate_func=smooth,
            run_time=3,
            )
        self.move_camera(
            phi=45*DEGREES,
            theta=45*DEGREES,
            distance=30,
            rate_func=smooth,
            run_time=3,
            )
        self.move_camera(
            phi=15*DEGREES,
            theta=60*DEGREES,
            distance=30,
            rate_func=smooth,
            run_time=3,
            )
        self.move_camera(
            phi=30*DEGREES,
            theta=90*DEGREES,
            distance=5,
            rate_func=smooth,
            run_time=3,
            )
        self.move_camera(
            phi=30*DEGREES,
            theta=140*DEGREES,
            distance=6,
            rate_func=smooth,
            run_time=3,
            )
        self.wait(3)


class Sierpinski2(SpecialThreeDScene):
    CONFIG = {
        "default_angled_camera_position": {
            "phi": 70 * DEGREES,
            "theta": -60 * DEGREES,
            "distance": 50,
            },
        "camera_config": {
            "background_color":BLACK,
            },
        "iteration":5,
        "sponge_size":4,
        }
    def construct(self):
        self.set_camera_to_default_position()
        #self.add(self.get_axes())
        Snowflake = MyBoxes(
            bottom_size=[self.sponge_size,self.sponge_size],
            box_height=self.sponge_size,
            resolution=(1,1),
            fill_color='#F08080',
            )
        self.play(ShowCreation(Snowflake))

        for _ in range(self.iteration-1):
            #mark = Snowflake.scale(1/3).move_to(UL*self.sponge_size/3+IN*self.sponge_size/3)
            self.play(
                Snowflake.scale,1/3,
                Snowflake.move_to,UL*self.sponge_size/3+IN*self.sponge_size/3,
                rate_func=smooth,
                run_time=2,
                )
            mark = Snowflake
            pos = [
                UR*self.sponge_size/3+IN*self.sponge_size/3,
                DL*self.sponge_size/3+IN*self.sponge_size/3,
                DR*self.sponge_size/3+IN*self.sponge_size/3,
                ORIGIN,
                UL*self.sponge_size/3+OUT*self.sponge_size/3,
                UR*self.sponge_size/3+OUT*self.sponge_size/3,
                DL*self.sponge_size/3+OUT*self.sponge_size/3,
                DR*self.sponge_size/3+OUT*self.sponge_size/3,
            ]
            a = VGroup(mark)
            for i in range(len(pos)):
                a.add(mark.copy().move_to(pos[i]))
            Snowflake = a
            self.play(ShowCreation(a[1:]),run_time=4)
        #self.add(Snowflake)
        self.wait()
        self.move_camera(
            phi=90*DEGREES,
            theta=0*DEGREES,
            distance=40,
            rate_func=smooth,
            run_time=3,
            )
        self.move_camera(
            phi=45*DEGREES,
            theta=45*DEGREES,
            distance=30,
            rate_func=smooth,
            run_time=3,
            )
        self.move_camera(
            phi=15*DEGREES,
            theta=60*DEGREES,
            distance=30,
            rate_func=smooth,
            run_time=3,
            )
        self.move_camera(
            phi=30*DEGREES,
            theta=90*DEGREES,
            distance=5,
            rate_func=smooth,
            run_time=3,
            )
        self.move_camera(
            phi=30*DEGREES,
            theta=140*DEGREES,
            distance=6,
            rate_func=smooth,
            run_time=3,
            )
        
        self.wait(3)


class Sierpinski3(SpecialThreeDScene):
    CONFIG = {
        "default_angled_camera_position": {
            "phi": 70 * DEGREES,
            "theta": -60 * DEGREES,
            "distance": 50,
            },
        "camera_config": {
            "background_color":BLACK,
            },
        "iteration":7,
        "sponge_size":4,
        }
    def getTetra(self, color='#8B5F65', size=6):
        pos = [
            UP*np.sqrt(3)/3,
            LEFT*0.5+np.sqrt(3)/6*DOWN,
            RIGHT*0.5+np.sqrt(3)/6*DOWN,
            np.sqrt(6)/3*OUT,
        ]
        tetra = VGroup()
        for i in range(4):
            face =  Polygon(
                pos[(i+0)%4],
                pos[(i+1)%4],
                pos[(i+2)%4],
                stroke_width=0,
                fill_opacity=1,
                shade_in_3d=True,
                )
            tetra.add(face)
        tetra.scale(size)
        colors = color_gradient([WHITE, color, BLACK], 11)
        tetra[0].set_fill(color=colors[8])
        tetra[1].set_fill(color=colors[3])
        tetra[2].set_fill(color=colors[8])
        tetra[3].set_fill(color=colors[2])
        return tetra

    def construct(self):
        self.set_camera_to_default_position()
        #self.add(self.get_axes())

        tetra = self.getTetra().shift(OUT/2)
        pos = [
            tetra[0].get_vertices()[0],
            tetra[1].get_vertices()[0],
            tetra[2].get_vertices()[0],
            tetra[3].get_vertices()[0],
        ]
        self.play(ShowCreation(tetra))

        for _ in range(self.iteration-1):
            #mark = Snowflake.scale(1/3).move_to(UL*self.sponge_size/3+IN*self.sponge_size/3)
            mark = tetra.copy()
            self.play(
                tetra.scale,1/2,{"about_point":pos[0]},
                rate_func=smooth,
                run_time=2,
                )
            a = VGroup(tetra)
            for i in range(3):
                a.add(mark.copy().scale(1/2,about_point=pos[i+1]))
            tetra = a
            self.play(ShowCreation(a[1:]),run_time=3)
        
        self.wait()
        self.move_camera(
            phi=55*DEGREES,
            theta=-30*DEGREES,
            distance=50,
            rate_func=smooth,
            run_time=3,
            )
        self.move_camera(
            phi=90*DEGREES,
            theta=0*DEGREES,
            distance=40,
            rate_func=smooth,
            run_time=3,
            )
        self.move_camera(
            phi=45*DEGREES,
            theta=45*DEGREES,
            distance=30,
            rate_func=smooth,
            run_time=3,
            )
        self.move_camera(
            phi=15*DEGREES,
            theta=60*DEGREES,
            distance=30,
            rate_func=smooth,
            run_time=3,
            )
        self.move_camera(
            phi=30*DEGREES,
            theta=120*DEGREES,
            distance=6,
            rate_func=smooth,
            run_time=3,
            )
        
        self.wait(3)


class Sierpinski4(SpecialThreeDScene):
    CONFIG = {
        "default_angled_camera_position": {
            "phi": 70 * DEGREES,
            "theta": -30 * DEGREES,
            "distance": 50,
            },
        "camera_config": {
            "background_color":BLACK,
            },
        "iteration":6,
        "sponge_size":4,
        }
    def getPyramid(self, color='#8B5F65', size=6):
        pos = [
            UL,UR,DR,DL,OUT*np.sqrt(3),
        ]
        pyramid = VGroup(
            Polygon(
                *pos[:4],
                stroke_width=0,
                fill_opacity=1,
                shade_in_3d=True,
            ))
        for i in range(4):
            face =  Polygon(
                pos[(i+0)%4],
                pos[(i+1)%4],
                pos[4],
                stroke_width=0,
                fill_opacity=1,
                shade_in_3d=True,
                )
            pyramid.add(face)
        pyramid.scale(size/2)
        colors = color_gradient([WHITE, color, BLACK], 11)
        pyramid[0].set_fill(color=colors[8])
        pyramid[1].set_fill(color=colors[3])
        pyramid[2].set_fill(color=colors[8])
        pyramid[3].set_fill(color=colors[2])
        pyramid[4].set_fill(color=colors[5])
        return pyramid

    def construct(self):
        self.set_camera_to_default_position()
        #self.add(self.get_axes())

        pyramid = self.getPyramid()#.shift(OUT/2)
        self.play(ShowCreation(pyramid))
        
        
        pos = [
            *pyramid[0].get_vertices()[:4],
            pyramid[1].get_vertices()[2],
        ]

        for _ in range(self.iteration-1):
            #mark = Snowflake.scale(1/3).move_to(UL*self.sponge_size/3+IN*self.sponge_size/3)
            mark = pyramid.copy()
            self.play(
                pyramid.scale,1/2,{"about_point":pos[0]},
                rate_func=smooth,
                run_time=2,
                )
            a = VGroup(pyramid)
            for i in range(4):
                a.add(mark.copy().scale(1/2,about_point=pos[i+1]))
            pyramid = a
            self.play(ShowCreation(a[1:]),run_time=3)
        
        self.wait()
        self.move_camera(
            phi=55*DEGREES,
            theta=-30*DEGREES,
            distance=50,
            rate_func=smooth,
            run_time=3,
            )
        self.move_camera(
            phi=90*DEGREES,
            theta=0*DEGREES,
            distance=40,
            rate_func=smooth,
            run_time=3,
            )
        self.move_camera(
            phi=45*DEGREES,
            theta=45*DEGREES,
            distance=30,
            rate_func=smooth,
            run_time=3,
            )
        self.move_camera(
            phi=15*DEGREES,
            theta=60*DEGREES,
            distance=30,
            rate_func=smooth,
            run_time=3,
            )
        self.move_camera(
            phi=30*DEGREES,
            theta=120*DEGREES,
            distance=6,
            rate_func=smooth,
            run_time=3,
            )
        
        self.wait(3)

