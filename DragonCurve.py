from manimlib.imports import *
import math

class scene1(Scene):
    CONFIG = {
        "times":16, 
    }
    def construct(self):

        a = [LEFT*2,RIGHT*3]
        colors = ['#8B5742','#FFA500','#FFE1FF','#7D26CD']
        My_colors = color_gradient(colors,len(a)-1)

        DragonCurve1 = VGroup(Line(*a).set_stroke(width=9,color=My_colors[0],opacity=0.4))
        
        DragonCurve2 = VGroup(Line(*a).set_stroke(width=1,color=My_colors[0],opacity=1.0))

        self.play(ShowCreation(DragonCurve1),ShowCreation(DragonCurve2))

        
        DragonCurve3,DragonCurve4 = VGroup(),VGroup()

        for i in range(self.times-1):
            b = []
            for j in range(len(a)):
                if j!=0:
                    b.append(point_rotate(a[j],(a[j]+a[j-1])/2,PI/2*(+1,-1)[j%2!=0]))
                b.append(a[j])

            My_colors = color_gradient(colors,len(b)-1)

            for j in range(len(b)-1):
                DragonCurve3.add(Line(b[j],b[j+1]).set_stroke(width=5,color=My_colors[j],opacity=0.4))
                DragonCurve4.add(Line(b[j],b[j+1]).set_stroke(width=1,color=My_colors[j],opacity=1.0))

            self.play(
                *[
                    ReplacementTransform(DragonCurve1[j],DragonCurve3[2*j:2*j+2])\
                    for j in range(len(DragonCurve1))
                ],
                *[
                    ReplacementTransform(DragonCurve2[j],DragonCurve4[2*j:2*j+2])\
                    for j in range(len(DragonCurve2))
                ],
                rate_func=rush_into,
                run_time=1,
                )
            self.wait(0.3)

            a = b
            [DragonCurve1.submobjects.pop() for _ in range(len(DragonCurve1))]
            [DragonCurve2.submobjects.pop() for _ in range(len(DragonCurve2))]
            DragonCurve1.add(*DragonCurve3)
            DragonCurve2.add(*DragonCurve4)
            [DragonCurve3.submobjects.pop() for _ in range(len(DragonCurve3))]
            [DragonCurve4.submobjects.pop() for _ in range(len(DragonCurve4))]
        
        self.wait(3)


class scene2(Scene):
    CONFIG = {
        "times":15, 
    }
    def construct(self):

        a = [UL*2+DOWN/2,UR*2+DOWN/2]
        colors = ['#8B5742','#FFA500','#FFE1FF','#7D26CD']
        My_colors = color_gradient(colors,len(a)-1)

        DragonCurve1 = VGroup(Line(*a).set_stroke(width=9,color=My_colors[0],opacity=0.4))
        
        DragonCurve2 = VGroup(Line(*a).set_stroke(width=1,color=My_colors[0],opacity=1.0))

        self.play(ShowCreation(DragonCurve1),ShowCreation(DragonCurve2))

        
        DragonCurve3,DragonCurve4 = VGroup(),VGroup()

        for i in range(self.times-1):
            b = []
            for j in range(len(a)):
                if j!=0:
                    b.append(point_rotate(a[j],(a[j]+a[j-1])/2,PI/2*(-1,-1)[j%2!=0]))
                b.append(a[j])

            My_colors = color_gradient(colors,len(b)-1)

            for j in range(len(b)-1):
                DragonCurve3.add(Line(b[j],b[j+1]).set_stroke(width=5,color=My_colors[j],opacity=0.4))
                DragonCurve4.add(Line(b[j],b[j+1]).set_stroke(width=1,color=My_colors[j],opacity=1.0))

            self.play(
                *[
                    ReplacementTransform(DragonCurve1[j],DragonCurve3[2*j:2*j+2])\
                    for j in range(len(DragonCurve1))
                ],
                *[
                    ReplacementTransform(DragonCurve2[j],DragonCurve4[2*j:2*j+2])\
                    for j in range(len(DragonCurve2))
                ],
                rate_func=rush_into,
                run_time=1,
                )
            self.wait(0.3)

            a = b
            [DragonCurve1.submobjects.pop() for _ in range(len(DragonCurve1))]
            [DragonCurve2.submobjects.pop() for _ in range(len(DragonCurve2))]
            DragonCurve1.add(*DragonCurve3)
            DragonCurve2.add(*DragonCurve4)
            [DragonCurve3.submobjects.pop() for _ in range(len(DragonCurve3))]
            [DragonCurve4.submobjects.pop() for _ in range(len(DragonCurve4))]
        
        self.wait(3)


class scene3(Scene):
    CONFIG = {
        "times":16, 
    }
    def construct(self):

        a = [LEFT*2,RIGHT*2]
        c = [RIGHT*2,LEFT*2]
        colors = ['#8B5742','#FFA500','#FFE1FF','#7D26CD']
        My_colors = color_gradient(colors,len(a)-1)

        DragonCurve1 = VGroup(Line(*a).set_stroke(width=9,color=My_colors[0],opacity=0.4))
        DragonCurve2 = VGroup(Line(*a).set_stroke(width=1,color=My_colors[0],opacity=1.0))

        DragonCurve5 = VGroup(Line(*c).set_stroke(width=9,color='#FFA500', opacity=0.4))
        DragonCurve6 = VGroup(Line(*c).set_stroke(width=1,color='#FFA500', opacity=1.0))

        self.play(
            ShowCreation(DragonCurve1),
            ShowCreation(DragonCurve2),
            ShowCreation(DragonCurve5),
            ShowCreation(DragonCurve6),
            )

        DragonCurve3,DragonCurve4 = VGroup(),VGroup()
        DragonCurve7,DragonCurve8 = VGroup(),VGroup()
        
        dis = (8-1)/self.times

        for i in range(self.times-1):
            b = []
            d = []
            for j in range(len(a)):
                if j!=0:
                    b.append(point_rotate(a[j],(a[j]+a[j-1])/2,PI/2*(+1,-1)[j%2!=0]))
                    d.append(point_rotate(c[j],(c[j]+c[j-1])/2,PI/2*(+1,-1)[j%2!=0]))
                b.append(a[j])
                d.append(c[j])

            My_colors = color_gradient(colors,len(b)-1)

            for j in range(len(b)-1):
                DragonCurve3.add(Line(b[j],b[j+1]).set_stroke(width=8-i*dis,color=My_colors[j],opacity=0.4))
                DragonCurve4.add(Line(b[j],b[j+1]).set_stroke(width=1-0*dis,color=My_colors[j],opacity=1.0))
                DragonCurve7.add(Line(d[j],d[j+1]).set_stroke(width=8-i*dis,color=My_colors[0],opacity=0.4))
                DragonCurve8.add(Line(d[j],d[j+1]).set_stroke(width=1-0*dis,color=My_colors[0],opacity=1.0))

            self.play(
                *[
                    ReplacementTransform(DragonCurve1[j],DragonCurve3[2*j:2*j+2])\
                    for j in range(len(DragonCurve1))
                ],
                *[
                    ReplacementTransform(DragonCurve2[j],DragonCurve4[2*j:2*j+2])\
                    for j in range(len(DragonCurve2))
                ],
                *[
                    ReplacementTransform(DragonCurve5[j],DragonCurve7[2*j:2*j+2])\
                    for j in range(len(DragonCurve5))
                ],
                *[
                    ReplacementTransform(DragonCurve6[j],DragonCurve8[2*j:2*j+2])\
                    for j in range(len(DragonCurve6))
                ],
                rate_func=rush_into,
                run_time=1,
                )
            self.wait(0.3)

            a = b
            [DragonCurve1.submobjects.pop() for _ in range(len(DragonCurve1))]
            [DragonCurve2.submobjects.pop() for _ in range(len(DragonCurve2))]
            DragonCurve1.add(*DragonCurve3)
            DragonCurve2.add(*DragonCurve4)
            [DragonCurve3.submobjects.pop() for _ in range(len(DragonCurve3))]
            [DragonCurve4.submobjects.pop() for _ in range(len(DragonCurve4))]

            c = d
            [DragonCurve5.submobjects.pop() for _ in range(len(DragonCurve5))]
            [DragonCurve6.submobjects.pop() for _ in range(len(DragonCurve6))]
            DragonCurve5.add(*DragonCurve7)
            DragonCurve6.add(*DragonCurve8)
            [DragonCurve7.submobjects.pop() for _ in range(len(DragonCurve7))]
            [DragonCurve8.submobjects.pop() for _ in range(len(DragonCurve8))]
        
        self.wait(3)


def GetDragon(start=LEFT/2, end=RIGHT/2, times=11, DexOrLev=1, color='#F08080'):
    #DexOrLev表示右旋或者左旋,1表示右旋
    if DexOrLev==1:
        dol = (+1,-1)
    else:
        dol = (-1,+1)
    a,b = [start, end],[]
    for i in range(times-1):
        for j in range(len(a)):
            if j!=0:
                b.append(point_rotate(a[j],(a[j]+a[j-1])/2,PI/2*dol[j%2!=0]))
            b.append(a[j])
        a = b
        b = []
    return VGroup(
        *[Line(a[i],a[i+1]).set_stroke(width=1,color=color,opacity=1.0) for i in range(len(a)-1)],
        *[Line(a[i],a[i+1]).set_stroke(width=4,color=color,opacity=0.4) for i in range(len(a)-1)],
        )

class scene4(Scene):
    def construct(self):
        colors = ['#8B5742','#FFA500','#FFE1FF','#7D26CD']
        My_colors = color_gradient(colors,6)
        
        dragon = GetDragon(start=LEFT*3,end=LEFT*2,color=My_colors[0])
        DragonCurveg = VGroup(
            VGroup(*dragon,*dragon.copy().rotate(about_point=LEFT*2.5,angle=PI)))
        for i in range(5):
            DragonCurveg.add(DragonCurveg[-1].copy().set_color(My_colors[i+1]).shift(RIGHT))
        
        for i in range(len(DragonCurveg)):
            self.play(FadeIn(DragonCurveg[i]))
            self.wait(0.3)

        DragonCurveg2 = DragonCurveg.copy()
        DragonCurveg3 = DragonCurveg.copy()
        
        for i in range(len(DragonCurveg)):
            DragonCurveg2[i].move_to(LEFT*2.5+RIGHT*(i+2)%6+UP)
            DragonCurveg3[i].move_to(LEFT*2.5+RIGHT*(i+4)%6+DOWN)
        
        for i in range(len(DragonCurveg)):
            self.play(
                FadeIn(DragonCurveg2[i]),
                FadeIn(DragonCurveg3[i]),
                )
            self.wait(0.3)

        self.wait(3)
    

class scene5(Scene):
    def construct(self):
        colors = ['#8B5742','#FFA500','#FFE1FF','#7D26CD']
        My_colors = color_gradient(colors,9)
        
        dragon = GetDragon(start=ORIGIN,end=UP,color=My_colors[0])
        DragonCurveg = VGroup(
            *[
                dragon.copy().rotate(about_point=ORIGIN,angle=i*PI/2).set_color(My_colors[i])\
                 for i in range(4)
            ])
            
        for i in range(len(DragonCurveg)):
            self.play(FadeIn(DragonCurveg[i]))
            self.wait(0.3)
        self.wait()

        self.play(DragonCurveg.set_color,My_colors[0])
        self.wait()

        pos = [2*LEFT, *[2*UL+i*2*RIGHT for i in range(3)], 2*RIGHT,  *[2*DR+i*2*LEFT for i in range(3)]]
        DragonCurveg2 = VGroup()
        for i in range(len(pos)):
            DragonCurveg2.add(DragonCurveg.copy().set_color(My_colors[i+1]).move_to(pos[i]))
        
        for i in range(len(DragonCurveg2)):
            self.play(FadeIn(DragonCurveg2[i]))
            self.wait(0.3)

        self.wait(3)


class scene5(Scene):
    def construct(self):
        colors = ['#8B5742','#FFA500','#FFE1FF','#7D26CD']
        My_colors = color_gradient(colors,9)
        
        dragon = GetDragon(start=ORIGIN,end=UP,color=My_colors[0])
        DragonCurveg = VGroup(
            *[
                dragon.copy().rotate(about_point=ORIGIN,angle=i*PI/2).set_color(My_colors[i])\
                 for i in range(4)
            ])
            
        for i in range(len(DragonCurveg)):
            self.play(FadeIn(DragonCurveg[i]))
            self.wait(0.3)
        self.wait()

        self.play(DragonCurveg.set_color,My_colors[0])
        self.wait()

        pos = [UL,UP*2,UR,RIGHT*2,DR,DOWN*2,DL,LEFT*2]
        DragonCurveg2 = VGroup()
        for i in range(len(pos)):
            DragonCurveg2.add(DragonCurveg.copy().set_color(My_colors[i+1]).move_to(pos[i]))
        
        for i in range(len(DragonCurveg2)):
            self.play(FadeIn(DragonCurveg2[i]))
            self.wait(0.3)

        self.wait(3)


class scene6(Scene):
    def construct(self):
        colors = ['#8B5742','#FFA500','#FFE1FF','#7D26CD']
        My_colors = color_gradient(colors,9)
        
        dragon = GetDragon(start=UP,end=ORIGIN,DexOrLev=0,color=My_colors[0])
        
        DragonCurveg = VGroup(
            *[
                dragon.copy().rotate(about_point=ORIGIN,angle=i*PI/2).set_color(My_colors[i])\
                 for i in range(4)
            ])
            
        for i in range(len(DragonCurveg)):
            self.play(FadeIn(DragonCurveg[i]))
            self.wait(0.3)
        self.wait()
        
        self.play(DragonCurveg.set_color,My_colors[0])
        self.wait()
        
        pos = [UL,UP*2,UR,RIGHT*2,DR,DOWN*2,DL,LEFT*2]
        DragonCurveg2 = VGroup()
        for i in range(len(pos)):
            DragonCurveg2.add(DragonCurveg.copy().set_color(My_colors[i+1]).move_to(pos[i]))
        
        for i in range(len(DragonCurveg2)):
            self.play(FadeIn(DragonCurveg2[i]))
            self.wait(0.3)

        self.wait(3)
        

class scene7(Scene):
    def construct(self):
        colors = ['#8B5742','#FFA500','#FFE1FF','#7D26CD']
        My_colors = color_gradient(colors,7)
        
        DragonCurveg = VGroup(
            GetDragon(start=DL/2,end=UL/2,DexOrLev=0).set_color(My_colors[0]),
            GetDragon(start=UR/2,end=UL/2,DexOrLev=0).set_color(My_colors[1]),
            GetDragon(start=UR/2,end=DR/2,DexOrLev=0).set_color(My_colors[2]),
            GetDragon(start=DL/2,end=DR/2,DexOrLev=0).set_color(My_colors[3]),
            )
            
        for i in range(len(DragonCurveg)):
            self.play(FadeIn(DragonCurveg[i]))
            self.wait(0.3)
        self.wait()
        
        self.play(DragonCurveg.set_color,My_colors[0])
        self.wait()
        
        pos = [LEFT*2,UL,UR,RIGHT*2,DR,DL]
        DragonCurveg2 = VGroup()
        for i in range(len(pos)):
            DragonCurveg2.add(DragonCurveg.copy().set_color(My_colors[i+1]).move_to(pos[i]))
        
        for i in range(len(DragonCurveg2)):
            self.play(FadeIn(DragonCurveg2[i]))
            self.wait(0.3)

        self.wait(3)

class test(Scene):
    def construct(self):
        self.add(GetDragon(start=DL/2,end=DR/2,DexOrLev=0))
        
        
