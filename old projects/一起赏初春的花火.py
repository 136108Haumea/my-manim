from manimlib.imports import *
import math


class scene(Scene):
    def construct(self):

        mycolors = color_gradient(
            [
                '#ccff33','#ffcc00','#ff9900','#ff6600','#ff3300',
                '#ff0000',
                '#ff3300','#ff6600','#ff9900','#ffcc00','#ccff33',
            ], 100)

        text = Text("先来制作花火",font='未署名的信').set_color_by_gradient(*mycolors)
        self.play(Write(text))
        self.wait()
        self.play(Erase(text))

        dotg = VGroup(*[Dot(i) for i in [DL,DL+UL,UR+DR,UR]])
        self.play(ShowCreation(dotg))
        bez = BezierCurve(dotg)
        curve = VGroup(*[
            bez.copy().rotate(i*TAU/66)
              for i in range(33)
            ])
        curve2 = VGroup(*[
            bez.copy().rotate(i*TAU/66).set_color(mycolors[i*3])\
              for i in range(33)
            ]).set_stroke(width=6,opacity=0.5)
        
        self.play(ShowCreation(curve[0]))
        arrow = Arrow(DOWN*2,ORIGIN)
        text2 = Text("贝塞尔曲线",font='未署名的信').scale(0.5).next_to(arrow,DOWN)
        self.play(
            ShowCreation(arrow), 
            Write(text2),
            )
        self.wait()
        self.play(
           Uncreate(arrow), 
           Uncreate(dotg),
           Erase(text2),
           )

        
        [
            self.play(
                ReplacementTransform(
                    curve[i].copy(),
                    curve[i+1],   
                ),
                rate_func=smooth,
                run_time=0.1,
            )for i in range(len(curve)-1)]
        
        self.wait()

        self.play(ReplacementTransform(curve,curve2))
        self.wait(2)

        text3 = Text("如此，可以制作各式各样的花火图案",font='未署名的信').scale(0.5)
        self.play(ReplacementTransform(curve2,text3))
        self.wait()
        self.play(FadeOut(text3))
        self.wait()
        
        colors = [
            '#666600','#6633FF','#660066','#336600',
            '#FF1493','#FFD39B','#E9967A','#F08080',
            '#FF0000','#CDB38B','#00BFFF','#C0FF3E',
            ]
        
        np.random.seed(int(time.time()))
        for i in range(12):
            pos = [
                np.random.randint(-200,200)/100*LEFT+np.random.randint(-200,200)/100*UP\
                for i in range(4)
                ]
            max_distance = max([
                    max([
                        get_distance(pos[i+j+1],pos[j])\
                            for i in range(3-j)
                        ])  for j in range(3)])

            bez = BezierCurve(pos).scale(5/max_distance).move_to(ORIGIN)

            color1 = colors[np.random.randint(0,len(colors))]
            color2 = colors[np.random.randint(0,len(colors))]

            while color1==color2:
                color2 = colors[np.random.randint(0,len(colors))]

            colorg = color_gradient([color1,color2],55)+color_gradient([color2,color1],11)

            curve = VGroup(*[
                bez.copy().rotate(i*TAU/66).set_color(colorg[i])\
                  for i in range(66)
                ]).scale(0.5).set_stroke(width=3,opacity=0.8)\
                    .move_to((-5+10/3*(i%4))*RIGHT+(2.5-2.5*int(i/4))*UP)

            self.play(FadeInFromDown(curve))
        
        self.wait(3)
        
            
class scene2(Scene):
    def construct(self):
        text = VGroup(
            Text("樱花落下的速度是每秒五厘米，我该用怎么样的速度，才能与你相遇。",font='未署名的信'),
            Text("雨滴降落的速度是每秒十米，我该用怎么样的速度，才能将你挽留。",font='未署名的信'),
            Text("陨石坠落的速度是每秒十千米，我该用怎么样的速度，才能将你拯救。",font='未署名的信'),
            Text("烟花消散的速度是每秒三亿米，我该用什么样的速度，才能将你追回。",font='未署名的信'),
            Line(ORIGIN,RIGHT*2),Text("云村",font='未署名的信'),
            ).scale(0.4).set_color('#EEC591')
        [text[i+1].next_to(text[i],DOWN,aligned_edge=LEFT) for i in range(3)]
        text[1][13:].align_to(text[0],RIGHT)
        VGroup(text[4],text[5].scale(1.5)).arrange(RIGHT).next_to(text[3],DOWN,aligned_edge=RIGHT)
        text.move_to(ORIGIN)
        #[text[i][0:2].set_color('#EEAEEE') for i in range(4)]
        #[text[i][2:4].set_color('#5F9EA0') for i in range(4)]
        #[text[i][5:7].set_color('#00FF00') for i in range(4)]
        #[text[i][-10:-8].set_color('#00FF00') for i in range(4)]
        #[text[i][-3:-1].set_color('#FF7F24') for i in range(4)]
        #[text[i][8:8+(5,4)[i==1]].set_color('#9B30FF') for i in range(4)]

        [
            VGroup(
                text[i][0:2].set_color('#EEAEEE'),
                text[i][2:4].set_color('#5F9EA0'),
                text[i][5:7].set_color('#00FF00'),
                text[i][-10:-8].set_color('#00FF00'),
                text[i][-3:-1].set_color('#FF7F24'),
                text[i][8:8+(5,4)[i==1]].set_color('#9B30FF'),
            ) for i in range(4)]

        #[debugTex(self,text[i]) for i in range(4)]
        #self.add(text)

        for i in range(4):
            self.play(Write(text[i]),run_time=2)
            self.wait()
        self.play(FadeInFromDown(text[4:]))
        self.wait(2)
        self.play(FadeOut(Group(*self.mobjects)))
        

class scene3(Scene):
    def construct(self):
        [
            self.play((
                FadeIn(Text(str(int(3-i/2)),font='未署名的信').scale(3),run_time=0.7),
                FadeOut(Group(*self.mobjects),run_time=0.3),
                )[i%2==1]) if i<6 else\
            self.play((
                FadeIn(Text("开始",font='未署名的信').scale(3),run_time=0.7),
                FadeOut(Group(*self.mobjects),run_time=0.3),
                )[i%2==1])
                for i in range(8)]


class scene4(Scene):
    def Cup(self,x,dt):
        x.t-=dt
        if x.t<0: self.remove(x)
        x.set_width(2*(x.edr-rush_into(x.t/x.allt)*(x.edr-x.opr)))
        x.set_stroke(width=rush_into(x.t/x.allt)*x.st)
  
    def Ripples(self,mobject,pos=ORIGIN,stroke_width=6,start_radius=1,end_radius=2,time=1):
        C=mobject
        C.move_to(pos)
        C.opr=start_radius
        C.edr=end_radius
        C.st=stroke_width
        C.t=time
        C.allt=time
        self.add(C)
        C.add_updater(self.Cup)
  
    def construct(self):

        colors = [
            '#666600','#6633FF','#660066','#336600',
            '#FF1493','#FFD39B','#E9967A','#F08080',
            '#FF0000','#CDB38B','#00BFFF','#C0FF3E',
            ]
        
        np.random.seed(int(time.time()))
        for i in range(100):
            pos = [
                np.random.randint(-200,200)/100*LEFT+np.random.randint(-200,200)/100*UP\
                for i in range(4)
                ]
            max_distance = max([
                    max([
                        get_distance(pos[i+j+1],pos[j])\
                            for i in range(3-j)
                        ])  for j in range(3)])

            bez = BezierCurve(pos).scale(5/max_distance).move_to(ORIGIN)

            color1 = colors[np.random.randint(0,len(colors))]
            color2 = colors[np.random.randint(0,len(colors))]

            while color1==color2:
                color2 = colors[np.random.randint(0,len(colors))]

            colorg = color_gradient([color1,color2],55)+color_gradient([color2,color1],11)

            curve = VGroup(*[
                bez.copy().rotate(i*TAU/66).set_color(colorg[i])\
                  for i in range(66)
                ]).scale(0.5).set_stroke(width=3,opacity=0.8)

            self.Ripples(
                mobject=curve,
                pos=np.random.randint(-600,600)/100*LEFT+np.random.randint(-400,400)/100*UP,
                end_radius=np.random.randint(3,6),
                time=np.random.randint(5,10)/10,
                )
            self.wait(np.random.randint(3,7)/10)

            #self.add(curve.\
            #    move_to(np.random.randint(-800,800)/100*LEFT+np.random.randint(-500,500)/100*UP)\
            #        .set_stroke(opacity=np.random.randint(0,8)/10)\
            #            .scale(np.random.randint(15,30)/10))

        self.wait(5)

