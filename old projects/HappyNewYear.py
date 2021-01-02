class HappyNewYear2(Scene):
    def construct(self):
        
        text = TexMobject(
            r'''\int\frac{\mathrm{d}x}{a\sin x+b\cos x}=\begin{cases}
            \displaystyle\frac{1}{\sqrt{a^2+b^2}}\ln\left|\csc\left(x+\arctan\displaystyle\frac{b}{a}\right)-\cot\left(x+\arctan\displaystyle\frac{b}{a}\right) \right|+C&a\ne0\\
            \displaystyle\frac{1}{b}\ln\left|\sec x+\tan x\right|+C&a=0\\
            \end{cases}''').scale(0.6).rotate(PI/6).to_corner(UL,buff=1).set_opacity(0.12)
        
        text2 = VGroup(
            *[
               text.copy().move_to(LEFT*9+RIGHT*3*i) for i in range(7) 
            ]
        )
        self.add(text2)

        text3 = Text(
            "Happy New Year", 
            font="Source Han Sans Bold",
            color="#EEAEEE",
            t2c={"H": "#EE3A8C","N": "#EE3A8C","Y": "#EE3A8C"},
        ).scale(0.8).to_corner(UL,buff=1.8).shift(LEFT)
        #self.wait(20454*24*60*60)
        self.add(text3)

        text4 = Text(
            "2077", font="DIN Black",
            t2c={"77": "#AFABB4",},
            ).scale(3).next_to(text3,RIGHT,aligned_edge=DOWN)
        self.add(text4)

        hp1 = Text(
            "text = Text(",
            font="Consolas",
            color="#8A81D1",
            t2s={"self": ITALIC},
            t2c={"text": "#AFABB4","=": "#AFABB4", "Text": "#75CB87", "(": "#E4C104"},
        )
        
        hp2 = Text(
            "\"Happy New Year\", ",
            font="Consolas",
            color="#E4C104",
            t2s={"self": ITALIC},
            t2c={",": "#AFABB4","\"":"#C6E2FF"},
        )

        hp3 = Text(
            "font = \"Source Han Sans Bold\",",
            font="Consolas",
            color="#E4C104",
            t2s={"self": ITALIC},
            t2c={"font":"#FF4040","=": "#AFABB4",",": "#AFABB4","\"":"#C6E2FF"},
        )

        hp4 = Text(
            "color = \"#EECFA1\",",
            font="Consolas",
            color="#E4C104",
            t2s={"self": ITALIC},
            t2c={"color":"#FF4040","=": "#AFABB4",",": "#AFABB4","\"":"#C6E2FF"},
        )

        hp5 = Text(
            "t2c = {\"H\": \"#AFABB4\",\"N\": \"#AFABB4\",\"Y\": \"#AFABB4\"})",
            font="Consolas",
            color="#E4C104",
            t2s={"self": ITALIC},
            t2c={"t2c":"#FF4040","{":"#FF83FA","}":"#FF83FA","=": "#AFABB4",":": "#AFABB4",",": "#AFABB4",")": "#E4C104","\"":"#C6E2FF"},
        )

        hp6 =  Text(
            "self.add(text)",
            font="Consolas",
            color="#8A81D1",
            t2s={"self": ITALIC},
            t2c={"self.": "#AFABB4", "add": "#75CB87", "(": "#E4C104","text":"#FFB5C5", ")": "#E4C104"}
        )

        hp7 =  Text(
            "self.wait(20454 * 24 * 60 * 60)",
            font="Consolas",
            color="#8A81D1",
            t2s={"self": ITALIC},
            t2c={"self.": "#AFABB4", "wait": "#75CB87", "(": "#E4C104", ")": "#E4C104","*":"#FFAEB9"}
        )

        hpvg = VGroup(hp1,hp2,hp3,hp4,hp5,hp6,hp7).scale(0.4).arrange(DOWN,aligned_edge=LEFT,buff=0.1)
        hpvg[1:5].shift(RIGHT)
        self.add(hpvg.to_edge(RIGHT).shift(DOWN*0.2))

        png = ImageMobject("D:\\Manim-master\\manim-master\\WaterMark_tf.png")
        png.scale(2).to_corner(DL,buff=-0.8).to_edge(LEFT)
        self.add(png)
