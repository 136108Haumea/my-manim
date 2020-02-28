from manimlib.imports import *

class scene1(Scene):
  CONFIG = {
    'c':1/3,
  }
  def construct(self):
    colors = color_gradient(['#CD3333','#EE7621','#FFFF00','#BDB76B','#FA8072','#BF3EFF','#0000CD','#191970','#D02090'], 150)# '#FFB90F', '#FFD700','#00FF00','#C0FF3E',
    
    text = Text("费马螺线", font='未署名的信').scale(2).set_color_by_gradient(colors)
    text2 = text.copy().rotate(PI/2.2,axis=RIGHT).align_to(text,DOWN).set_color('#4F4F4F').set_opacity(0.5)
    
    dotg = VGroup(
      *[Dot([self.c*np.sqrt(t)*np.cos(t),self.c*np.sqrt(t)*np.sin(t),0]).scale(0.2).set_color(colors[t]) for t in range(150)]
      )

    lineg1 = VGroup()
    for j in range(5):
      lineg1.add(
        *[Line(dotg[j+5*i].get_center(),dotg[j+5+5*i].get_center()).set_stroke(width=1,color=colors[j+i*5],opacity=1) for i in range(20)], 
        *[Line(dotg[j+5*i].get_center(),dotg[j+5+5*i].get_center()).set_stroke(width=12,color=colors[j+i*5],opacity=0.3) for i in range(20)], 
        )

    lineg2 = VGroup()
    for j in range(8):
      lineg2.add(
        *[Line(dotg[j+8*i].get_center(),dotg[j+8+8*i].get_center()).set_stroke(width=1,color=colors[j+i*8],opacity=1) for i in range(15)], 
        *[Line(dotg[j+8*i].get_center(),dotg[j+8+8*i].get_center()).set_stroke(width=12,color=colors[j+i*8],opacity=0.3) for i in range(15)], 
        )
    
    lineg3 = VGroup()
    for j in range(13):
      lineg3.add(
        *[Line(dotg[j+13*i].get_center(),dotg[j+13+13*i].get_center()).set_stroke(width=1,color=colors[j+i*13],opacity=1) for i in range(10)], 
        *[Line(dotg[j+13*i].get_center(),dotg[j+13+13*i].get_center()).set_stroke(width=12,color=colors[j+i*13],opacity=0.3) for i in range(10)], 
        )
    
    self.play(Write(VGroup(text,text2)))
    self.wait(2)
    self.play(ReplacementTransform(VGroup(text,text2),dotg), run_time=2)
    self.play(FadeInFromRandom(lineg1), run_time=3)
    self.wait(2)
    self.play(FadeOutFromRandom(lineg1), run_time=3)
    self.wait()
    self.play(FadeInFromRandom(lineg2), run_time=3)
    self.wait(2)
    self.play(FadeOutFromRandom(lineg2), run_time=3)
    self.wait()
    self.play(FadeOutFromRandom(dotg), run_time=3)
    self.wait(2)
    
class scene2(Scene):
  def construct(self):
    colors = color_gradient(['#CD3333','#FFFF00','#FA8072','#BF3EFF','#0000CD','#191970','#D02090'], 150)# '#FFB90F', '#FFD700','#00FF00','#C0FF3E',

    text = Text("斐波那契螺线", font='未署名的信').scale(2).set_color_by_gradient(colors)
    text2 = text.copy().rotate(PI/2.2,axis=RIGHT).align_to(text,DOWN).set_color('#4F4F4F').set_opacity(0.5)

    self.play(
      Write(text), 
      Write(text2), 
      )
    self.wait(2)

    direction = [RIGHT,DOWN,LEFT,UP]
    fibonacci_numb = [0,1]
    [fibonacci_numb.append(fibonacci_numb[i]+fibonacci_numb[i+1]) for i in range(9)]
    
    fibonacci_rect = VGroup(*[Square(stroke_width=1,stroke_opacity=1).scale(fibonacci_numb[-i-1]/20) for i in range(10)])
    [fibonacci_rect[i+1].next_to(fibonacci_rect[i],direction[i%4],aligned_edge=direction[(i+3)%4],buff=0) for i in range(9)]
    fibonacci_rect.set_color_by_gradient(*colors).move_to(ORIGIN)
    fibonacci_rect_supplement = fibonacci_rect.copy().set_stroke(width=8,opacity=0.3)
    fibonacci_rect_supplement.set_color_by_gradient(*colors)

    fibonacci_arc = VGroup(*[
      Arc(radius = fibonacci_numb[-i-1]/10,stroke_width=1,stroke_opacity=1)\
        .move_arc_center_to(fibonacci_rect[i].get_vertices()[(i+2)%4])\
        .rotate(-PI/2*(i%4-1),about_point=fibonacci_rect[i].get_vertices()[(i+2)%4]) for i in range(10)]
      ).set_color_by_gradient(*colors)
    
    fibonacci_arc_supplement = fibonacci_arc.copy().set_stroke(width=8,opacity=0.3)
    
    VGroup(fibonacci_rect,fibonacci_rect_supplement,fibonacci_arc,fibonacci_arc_supplement).scale(1.2)
    
    fibonacci_text = VGroup(*[
      Text(str(fibonacci_numb[-i-1]),font='未署名的信')\
        .scale(fibonacci_numb[-i-1]/50+0.5)\
        .move_to(fibonacci_rect[i].get_center_of_mass()) for i in range(10)]
      ).set_color_by_gradient(*colors)
    
    self.play(
      Erase(text), 
      Erase(text2), 
      FadeInFromRandom(fibonacci_rect), 
      FadeInFromRandom(fibonacci_rect_supplement), 
      run_time=3, 
      )
    self.play(
      FadeInFromRandom(fibonacci_arc), 
      FadeInFromRandom(fibonacci_arc_supplement),
      run_time=3, 
    )
    self.play(FadeInFromRandom(fibonacci_text), run_time=2)
    self.wait(5)
    self.play(
      FadeOutRandom(fibonacci_rect), 
      FadeOutRandom(fibonacci_rect_supplement), 
      FadeOutRandom(fibonacci_arc), 
      FadeOutRandom(fibonacci_arc_supplement), 
      FadeOutRandom(fibonacci_text), 
    )
    self.wait(2)

class scene3(Scene):
  def construct(self):

    colors = color_gradient(['#CD3333','#EE7621','#FFFF00','#BDB76B','#FA8072','#BF3EFF','#0000CD','#191970','#D02090'], 150)# '#FFB90F', '#FFD700','#00FF00','#C0FF3E',
    
    fibonacci_numb = [0,1]
    [fibonacci_numb.append(fibonacci_numb[i]+fibonacci_numb[i+1]) for i in range(20)]

    text = Text("帕斯卡三角形", font='未署名的信').scale(2).set_color_by_gradient(colors)
    text2 = text.copy().rotate(PI/2.2,axis=RIGHT).align_to(text,DOWN).set_color('#4F4F4F').set_opacity(0.5)
    
    self.play(
      Write(text), 
      Write(text2), 
      )
    self.wait(2)
    
    Pascal_trangle = [[1],[1,1]]
    
    [Pascal_trangle.append([
      1,
      *[Pascal_trangle[-1][i]+Pascal_trangle[-1][i+1] for i in range(len(Pascal_trangle[-1])-1)], 
      1, 
      ])for i in range(9)]
  
    Pascal_trangle_text = VGroup(*[VGroup(*[
      Text(str(Pascal_trangle[j][i]),font='未署名的信').scale(0.5)\
        .set_stroke(width=3).move_to(j/2*DL+i*RIGHT) for i in range(len(Pascal_trangle[j]))]) for j in range(len(Pascal_trangle))])\
        .set_color_by_gradient(*colors).move_to(ORIGIN)
    
    line_mark = Line(Pascal_trangle_text[2][0].get_center(),Pascal_trangle_text[1][1].get_center())
    Pascal_line = VGroup(
      *[line_mark.copy().scale(i*0.56+1)\
        .move_to(Pascal_trangle_text[0][0].get_center()+DOWN/3*i)\
        .shift((line_mark.get_start()-line_mark.get_end())*i/10)\
        .set_stroke(width=2) for i in range(11)]
      ).set_color_by_gradient(*colors[0:50])
    Pascal_line_text = VGroup(*[
      Text(str(fibonacci_numb[i+1]),font='未署名的信').scale(0.6)\
        .move_to(Pascal_line[i].get_start()).shift(LEFT*0.2) for i in range(11)
      ]).set_color_by_gradient(*colors[0:50])
    Pascal_line_text_supplement = Pascal_line_text.copy().arrange(RIGHT)
    
    self.play(
      ReplacementTransform(
        VGroup(text,text2), 
        VGroup(*[
          Pascal_trangle_text[0][0], 
          *[Pascal_trangle_text[i+1][0] for i in range(len(Pascal_trangle_text)-1)], 
          *[Pascal_trangle_text[i+1][-1] for i in range(len(Pascal_trangle_text)-1)], 
        ])))

    [[self.play(
      ReplacementTransform(
        VGroup(Pascal_trangle_text[j+1][i],Pascal_trangle_text[j+1][i+1]).copy(), 
        VGroup(Pascal_trangle_text[j+2][i+1]), 
        run_time=1/3
        )) 
      for i in range(len(Pascal_trangle_text[j+1])-1)] 
      for j in range(len(Pascal_trangle_text)-2)]

    self.play(FadeInFromRandom(Pascal_line))
    
    self.wait()

    [self.play(Write(Pascal_line_text[i])) for i in range(len(Pascal_line_text))]

    self.wait(2)

    self.play(
      ReplacementTransform(Pascal_line_text, Pascal_line_text_supplement), 
      FadeOutFromRandom(Pascal_trangle_text), 
      FadeOutFromRandom(Pascal_line), 
      run_time=2
      )
    
    self.wait(2)

class scene4(Scene):
  def construct(self):
    
    colors = color_gradient(['#CD3333','#EE7621','#FFFF00','#BDB76B','#FA8072','#BF3EFF','#0000CD','#191970','#D02090'], 150)# '#FFB90F', '#FFD700','#00FF00','#C0FF3E',
    
    fibonacci_numb = [0,1]
    [fibonacci_numb.append(fibonacci_numb[i]+fibonacci_numb[i+1]) for i in range(20)]

    Pascal_line_text = VGroup(*[
      Text(str(fibonacci_numb[i+1]),font='未署名的信').scale(0.6) for i in range(11)
      ]).set_color_by_gradient(*colors[0:50]).arrange(RIGHT)
    
    self.add(Pascal_line_text)
    self.play(Pascal_line_text.to_corner, UL)

    text = VGroup(
      Text("这是一个斐波那契数列",font='未署名的信').scale(0.5), 
      Text("他的递推公式(不唯一）：",font='未署名的信').scale(0.5), 
      TexMobject("F_0=0,F_1=1").set_color('#FF8C00'), 
      TexMobject("F_n=F_{n-1}+F_{n-2},n>1").set_color('#FF8C00'),
      Text("你知道他的通向公式吗？",font='未署名的信').scale(0.5), 
      ).scale(1.2)
    text[0][4:10].set_color('#FFEC8B')
    text[1][2:6].set_color('#FF3E96')
    text[4][5:9].set_color('#FF3E96')                           
    [text[i].next_to((text[i-1],Pascal_line_text)[i==0],DOWN,aligned_edge=LEFT) for i in range(len(text))]
    [text[2][0][i].set_color('#C0FF3E') for i in [0,5]]
    [text[3][0][i].set_color('#C0FF3E') for i in [0,3,8]]

    [self.play(Write(text[int(i/2)], run_time=2)) if i%2==0 else self.wait() for i in range(2*len(text))]
    self.wait(2)
    self.play(VGroup(*self.mobjects).shift,LEFT*8,run_time=2)
    
    text2 = VGroup(
      Text("接下来介绍一种母函数(Generating function)的求解方法",font='未署名的信').scale(0.5).set_stroke(width=2), 
      Text("什么是母函数？",font='未署名的信').scale(0.5), 
      VGroup(
        Text("设想有一个序列：",font='未署名的信').scale(0.5), 
        TexMobject(r"a_0,a_1,a_2,\cdots,a_n"), 
        Text("我们把他挂到",font='未署名的信').scale(0.5),
        TexMobject(r"x^0,x^1,x^2,\cdots,x_n"), 
        Text("前面做系数",font='未署名的信').scale(0.5),
        TexMobject(r"a_0x^0+a_1x^1+a_2x^2+\cdots+a_nx^n"), 
        TexMobject(r"G(a_n;x)="),
        Text("称G为序列a的母函数,或称普通母函数(OGF)",font='未署名的信').scale(0.5),
        ).arrange(DOWN), 
      Text("母函数本身不是(从某个定义域射到某个到达域的)函数",font='未署名的信').scale(0.5), 
      Text("名字中的\"函数\"是出于历史原因而保留的",font='未署名的信').scale(0.5), 
      ).set_color('#B4EEB4')

    text2[0:2].move_to(ORIGIN)
    text2[0][7:10].set_color('#D15FEE')
    text2[0][11:30].set_color('#66CD00')
    text2[1][3:6].set_color('#D15FEE')

    self.play(Write(text2[0]), run_time=2)
    self.wait(3)
    self.play(ReplacementTransform(text2[0],text2[1]))
    self.play(text2[1].to_corner,UL)
    self.wait()

    text2[2][1].next_to(text2[2][0],RIGHT)
    text2[2][0:2].next_to(text2[1],DOWN,aligned_edge=LEFT)
    VGroup(*[text2[2][i+2] for i in range(3)]).arrange(RIGHT)\
      .next_to(text2[2][0:2],DOWN,aligned_edge=LEFT)
    text2[2][5].move_to(ORIGIN)
    text2[2][0][5:7].set_color('#FFBBFF')
    [text2[2][1][0][i].set_color('#7FFF00') for i in [0,3,6,13]]
    [text2[2][3][0][i].set_color('#F08080') for i in [0,3,6,13]]
    [text2[2][5][0][i].set_color('#7FFF00') for i in [0,5,10,19]]
    [text2[2][5][0][i].set_color('#F08080') for i in [2,7,12,21]]
    text2_2_supplement = [1,4,7,14]
    text2_2_supplement2 = [1,6,11,20]
    text2_2_supplement3 = [3,8,13,22]
    [text2[2][1][0][text2_2_supplement[i]].set_color(colors[i*30]) for i in range(4)]
    [text2[2][3][0][text2_2_supplement[i]].set_color(colors[i*30]) for i in range(4)]
    [text2[2][5][0][text2_2_supplement2[i]].set_color(colors[i*30]) for i in range(4)]
    [text2[2][5][0][text2_2_supplement3[i]].set_color(colors[i*30]) for i in range(4)]
    text2[2][6].next_to(text2[2][5],LEFT/2)
    text2[2][6][0][0].set_color('#CD1076')
    text2[2][6][0][2].set_color('#7FFF00')
    text2[2][6][0][3].set_color(colors[90])
    text2[2][6][0][5].set_color('#F08080')
    text2[2][7][1].set_color('#CD1076')
    text2[2][7][3:5].set_color('#FFBBFF')
    text2[2][7][5].set_color('#7FFF00')
    text2[2][7][7:10].set_color('#D15FEE')
    text2[2][7][14:18].set_color('#D15FEE')
    
    self.play(Write(text2[2][0:2]), run_time=2)
    self.wait(2)
    self.play(Write(text2[2][2:5]), run_time=2)
    self.wait(2)
    self.play(
      ReplacementTransform(
        VGroup(*[text2[2][1][0][i] for i in [0,1,3,4,6,7,9,10,11,13,14]]).copy(), 
        VGroup(*[text2[2][5][0][i] for i in [0,1,5,6,10,11,15,16,17,19,20]]), 
        ), 
      ReplacementTransform(
        VGroup(*[text2[2][3][0][i] for i in [0,1,3,4,6,7,9,10,11,13,14]]).copy(), 
        VGroup(*[text2[2][5][0][i] for i in [2,3,7,8,12,13,15,16,17,21,22]]), 
        ), 
      run_time=2, 
      )
    self.play(FadeInFromDown(VGroup(*[text2[2][5][0][i] for i in [4,9,14,18]])))
    self.wait()
    self.play(Write(text2[2][6]))
    self.wait()
    self.play(ApplyMethod(text2[2][5:7].next_to,text2[2][2:5],DOWN,aligned_edge=LEFT))
    #[debugTex(self,text2[2][i][0]) for i in [1,3,5]]
    text2[2][7].next_to(text2[2][5:7],DOWN,aligned_edge=LEFT)
    self.play(Write(text2[2][7]), run_time=2)
    self.wait(3)
    #debugTex(self,text2[2][7])
    text2[3].next_to(text2[2],DOWN,aligned_edge=LEFT)
    text2[4].next_to(text2[3],DOWN,aligned_edge=LEFT)
    text2[3][0:3].set_color('#D15FEE')
    text2[3][7:23].set_opacity(0.3)
    text2[3][23:25].set_color('#B8860B')
    text2[4][5:7].set_color('#B8860B')

    self.play(Write(text2[3]),run_time=2)
    self.wait(2)
    self.play(Write(text2[4]),run_time=2)
    self.wait(3)
    self.play(VGroup(*self.mobjects).shift,LEFT*14,run_time=2)
    self.wait(2)

class scene5(Scene):
  def construct(self):

    rectg = Square(color=WHITE,fill_opacity=1).round_corners(0.25)

    dice = VGroup(
      VGroup(
        rectg.copy(), 
        Circle(color=BLACK,fill_opacity=1).scale(0.2), 
        ), 
      VGroup(
        rectg.copy(), 
        Circle(color=BLACK,fill_opacity=1).scale(0.2).shift(UL*0.6), 
        Circle(color=BLACK,fill_opacity=1).scale(0.2).shift(DR*0.6), 
        ), 
      VGroup(
        rectg.copy(), 
        Circle(color=BLACK,fill_opacity=1).scale(0.2), 
        Circle(color=BLACK,fill_opacity=1).scale(0.2).shift(UL*0.6), 
        Circle(color=BLACK,fill_opacity=1).scale(0.2).shift(DR*0.6), 
        ), 
      VGroup(
        rectg.copy(), 
        Circle(color=BLACK,fill_opacity=1).scale(0.2).shift(UR*0.6), 
        Circle(color=BLACK,fill_opacity=1).scale(0.2).shift(UL*0.6), 
        Circle(color=BLACK,fill_opacity=1).scale(0.2).shift(DR*0.6), 
        Circle(color=BLACK,fill_opacity=1).scale(0.2).shift(DL*0.6), 
        ), 
      VGroup(
        rectg.copy(), 
        Circle(color=BLACK,fill_opacity=1).scale(0.2), 
        Circle(color=BLACK,fill_opacity=1).scale(0.2).shift(UR*0.6), 
        Circle(color=BLACK,fill_opacity=1).scale(0.2).shift(UL*0.6), 
        Circle(color=BLACK,fill_opacity=1).scale(0.2).shift(DR*0.6), 
        Circle(color=BLACK,fill_opacity=1).scale(0.2).shift(DL*0.6), 
        ), 
        VGroup(
        rectg.copy(), 
        Circle(color=BLACK,fill_opacity=1).scale(0.2).shift(UR*0.6), 
        Circle(color=BLACK,fill_opacity=1).scale(0.2).shift(UL*0.6), 
        Circle(color=BLACK,fill_opacity=1).scale(0.2).shift(DR*0.6), 
        Circle(color=BLACK,fill_opacity=1).scale(0.2).shift(DL*0.6), 
        Circle(color=BLACK,fill_opacity=1).scale(0.2).shift(LEFT*0.6), 
        Circle(color=BLACK,fill_opacity=1).scale(0.2).shift(RIGHT*0.6), 
        ), 
      ).scale(0.25).arrange(RIGHT*2.2)
    
    dice1,dice2 = dice.copy().shift(LEFT*3.3),dice.copy().shift(RIGHT*3.3)
    
    dice3 = VGroup(
      *[VGroup(
        dice1[0+i].copy(), 
        dice2[3-i].copy(), 
        ).arrange(RIGHT/2) for i in range(4)]
      ).arrange(RIGHT*3)

    text = VGroup(
      Text("到这里你可能对母函数的概念还是模糊的",font='未署名的信').scale(0.6), 
      Text("下面举个栗子吧",font='未署名的信').scale(0.6), 
      Text("两粒色子抛出5点，有多少种可能？",font='未署名的信').scale(0.6), 
      ).set_color('#B4EEB4').arrange(DOWN)
    text[0][7:10].set_color('#D15FEE')
    text[1][4:6].set_color('#8B7500')
    text[2][2:4].set_color('#8E8E8E')
    #[debugTex(self,text[i]) for i in range(len(text))]
    
    text5 = Text("或或或或或", font='未署名的信').scale(0.6).set_color('#B4EEB4')
    [text5[i].move_to((dice1[i].get_center()+dice1[i+1].get_center())/2) for i in range(5)]
    text6= Text("或或或或或", font='未署名的信').scale(0.6).set_color('#B4EEB4')
    [text6[i].move_to((dice2[i].get_center()+dice2[i+1].get_center())/2) for i in range(5)]

    [self.play(Write(text[int(i/2)], run_time=2)) if i%2==0 else self.wait() for i in range(2*len(text))]
    self.wait(2)
    self.play(
      ReplacementTransform(
        VGroup(*self.mobjects), 
        VGroup(dice1,dice2), 
        ),
      run_time=2, 
      )
    self.wait()
    self.play(
      FadeInFromDown(text5), 
      FadeInFromDown(text6), 
      )
    self.wait(2)
    
    text2 = TexMobject("()()")
    text2[0][0].next_to(dice1,LEFT)
    text2[0][1].next_to(dice1,RIGHT)
    text2[0][2].next_to(dice2,LEFT)
    text2[0][3].next_to(dice2,RIGHT)
    
    self.play(FadeInFromRandom(text2[0]))

    text3 = Text("或或或", font='未署名的信').scale(0.6).set_color('#B4EEB4')
    [text3[i].move_to((dice3[i].get_center()+dice3[i+1].get_center())/2) for i in range(3)]

    self.play(ApplyMethod(Group(*self.mobjects).shift,UP))
    [self.play(
      ReplacementTransform(
        dice1[0+i].copy(), 
        dice3[i][0], 
        ), 
      ReplacementTransform(
        dice2[3-i].copy(), 
        dice3[i][1], 
        ), 
      ) for i in range(len(dice3))]
    self.wait()
    self.play(ScaleInPlace(text3,3,rate_func=wiggle))

    text7 = VGroup(
      TexMobject("x^1+x^2+x^3+x^4+x^5+x^6"), 
      TexMobject("x^1+x^2+x^3+x^4+x^5+x^6"), 
      text2.copy().shift(UP*0.7), 
      )
    text7[0].next_to(dice1,UP)
    text7[1].next_to(dice2,UP)
    [text7[0][0][3*i:3*i+2].next_to(dice1[i],UP) for i in range(len(dice1))]
    [text7[0][0][3*i+2].next_to(text5[i],UP) for i in range(len(text5))]
    [text7[1][0][3*i:3*i+2].next_to(dice2[i],UP) for i in range(len(dice2))]
    [text7[1][0][3*i+2].next_to(text6[i],UP) for i in range(len(text6))]
    text7_supplement = VGroup(
      SurroundingRectangle(text7[0],color='#919191',stroke_width=0,fill_opacity=0.3), 
      SurroundingRectangle(text7[1],color='#919191',stroke_width=0,fill_opacity=0.3), 
      )
    
    text8 = TexMobject("x^1 x^4 + x^2 x^3 + x^3 x^2 + x^4 x^1")
    [text8[0][i*5+0:i*5+2].next_to(dice3[i][0],DOWN) for i in range(len(dice3))]
    [text8[0][i*5+2:i*5+4].next_to(dice3[i][1],DOWN) for i in range(len(dice3))]
    [text8[0][i*5+4].next_to(text3[i],DOWN).align_to(text8[0][0],DOWN) for i in range(len(text3))]

    text8_supplement = VGroup(
      SurroundingRectangle(text8[0],color='#919191',stroke_width=0,fill_opacity=0.3), 
      )
    
    self.play(
      *[
        ReplacementTransform(
          dice1[i].copy(),
          text7[0][0][3*i+0:3*i+2],
          ) for i in range(len(dice1))
      ], 
      *[
        ReplacementTransform(
          text5[i].copy(),
          text7[0][0][3*i+2],
          ) for i in range(len(text5))
      ], 
      *[
        ReplacementTransform(
          dice2[i].copy(),
          text7[1][0][3*i+0:3*i+2],
          ) for i in range(len(dice2))
      ], 
      *[
        ReplacementTransform(
          text6[i].copy(),
          text7[1][0][3*i+2],
          ) for i in range(len(text6))
      ], 
      ReplacementTransform(text2.copy(), text7[2]), 
      FadeIn(text7_supplement), 
      run_time=2, 
      )
    
    self.wait()
    
    self.play(
      *[
        ReplacementTransform(
          dice3[i][0].copy(), 
          text8[0][5*i+0:5*i+2], 
          ) for i in range(len(dice3))
      ], 
      *[
        ReplacementTransform(
          dice3[i][1].copy(), 
          text8[0][5*i+2:5*i+4], 
          ) for i in range(len(dice3))
      ], 
      *[
        ReplacementTransform(
          text3[i].copy(), 
          text8[0][5*i+4], 
          ) for i in range(len(text3))
      ], 
      FadeIn(text8_supplement), 
      run_time=2, 
      )

    self.wait()

    text9 = VGroup(
      TexMobject("\\Rightarrow").set_stroke(width=5,color='#00CD66').rotate(PI/2), 
      TexMobject("G(x)=(x^1+x^2+x^3+x^4+x^5+x^6)^2"), 
      )
    [text9[i].next_to((text9[i-1],text7)[i==0],UP) for i in range(len(text9))]
    text9_supplement = VGroup(
      SurroundingRectangle(text9[1],color='#919191',stroke_width=0,fill_opacity=0.3), 
      )
    
    self.play(FadeIn(text9[0]))
    self.wait()
    self.play(
      Write(text9[1]), 
      FadeIn(text9_supplement), 
      run_time=3, 
      )
    self.wait()

    text10 = VGroup(
      TexMobject("=").scale(1.2).set_stroke(width=5,color='#00CD66').rotate(-PI/2), 
      TexMobject("4x^5"), 
      )
    [text10[i].next_to((text10[i-1],text8)[i==0],DOWN) for i in range(len(text10))]
    text10_supplement = VGroup(
      SurroundingRectangle(text10[1],color='#919191',stroke_width=0,fill_opacity=0.3), 
      )

    self.play(FadeIn(text10[0]))
    self.wait()
    self.play(
      Write(text10[1]), 
      FadeIn(text10_supplement), 
      run_time=3, 
      )
    self.wait(3)

    self.play(Group(*self.mobjects).shift,LEFT*15,run_time=2)

class scene6(Scene):
  def construct(self):
    text = VGroup(
      Text("通过母函数，可以把点数和为n和母函数中n次幂联系起来",font='未署名的信').scale(0.5), 
      Text("这样母函数中n次幂的系数即问题的解",font='未署名的信').scale(0.5), 
      Text("不难看出，母函数是一种计数方法，它，似函数，非函数",font='未署名的信').scale(0.5), 
      Text("读者可以试着推广m个色子抛出点数为n有多少种",font='未署名的信').scale(0.5), 
      Text("下面进入正题",font='未署名的信').scale(0.7), 
      ).set_color('#B4EEB4').arrange(DOWN)
    text[0][2:5].set_color('#D15FEE')
    text[0][15:18].set_color('#D15FEE')
    text[1][2:5].set_color('#D15FEE')
    text[2][5:8].set_color('#D15FEE')
    text[2][18:21].set_color('#8B1C62')
    text[2][22:25].set_color('#8B1C62')
    text[3][10:12].set_color('#8B7500')
    text[4].set_color('#F08080')
    
    [self.play(Write(text[int(i/2)], run_time=2)) if i%2==0 else self.wait() for i in range(2*len(text))]

    self.wait()
    
    self.play(Group(*self.mobjects).shift,LEFT*15,run_time=2)

class scene7(Scene):
  def construct(self):
    text = VGroup(
      TexMobject("F_0=1,F_1=1"), 
      TexMobject("F_n=F_{n-1}+F_{n-2},n>1"),
      ).scale(0.6).arrange(DOWN).to_corner(UR)
    text_supplement = SurroundingRectangle(text,color='#FF8C00',stroke_width=0,fill_opacity=0.3)
    
    self.play(
      Write(text), 
      FadeIn(text_supplement), 
      run_time=2, 
      )
    
    text2 = Text("设斐波那契数列的母函数为G(x)：",font='未署名的信')\
      .set_color('#B4EEB4').scale(0.5)
    text2[8:11].set_color('#D15FEE')

    self.play(Write(text2))
    self.play(text2.to_corner,UL)

    text3 = TexMobject(
      r"G(x)=F_0+F_1x+F_2x^2+\cdots+F_nx^n+\cdots", 
      r"=1+F_1x+F_2x^2+\cdots+F_nx^n+\cdots", 
      r"=1+x+(F_0+F_1)x^2+\cdots+(F_{n-1}+F_{n-2})x^n+\cdots", 
      r"=1+x(1+F_1x+\cdots+F_nx^n+\cdots)+x^2(1+F_1x+\cdots+F_nx^n+\cdots)", 
      r"=1+(x+x^2)G(x)", 
      ).scale(0.6)
    text3[0].next_to(text2,DOWN,aligned_edge=LEFT)
    [text3[i+1].next_to(text3[i],DOWN).align_to(text3[0][4],LEFT) for i in range(4)]
    
    [self.play(Write(text3[int(i/2)], run_time=2)) if i%2==0 else self.wait(2) for i in range(2*len(text3))]
    self.wait()
    
    text4 = TexMobject(
      r"G(x)=\frac{1}{1-x-x^2}", 
      r"=\frac{1}{\sqrt{5}}\cdot\frac{1}{x+\frac{1+\sqrt{5}}{2}}-\frac{1}{\sqrt{5}}\cdot\frac{1}{x+\frac{1-\sqrt{5}}{2}}", 
      r"=\frac{1}{\sqrt{5}}\cdot\frac{1+\sqrt{5}}{2}\cdot\frac{1}{1-\frac{1+\sqrt{5}}{2}x}-\
         \frac{1}{\sqrt{5}}\cdot\frac{1-\sqrt{5}}{2}\cdot\frac{1}{1-\frac{1-\sqrt{5}}{2}x}", 
      ).scale(0.6)
    text4[0].next_to(text3,DOWN).align_to(text3,LEFT)

    self.play(Write(text4[0]))
    self.play(
      text3[1:].shift, LEFT*14, 
      text4[0].next_to, text3[0],DOWN,DEFAULT_MOBJECT_TO_MOBJECT_BUFFER,LEFT, 
      run_time=2, 
      )

    [text4[i+1].next_to(text4[i],DOWN).align_to(text4[0][4],LEFT) for i in range(2)]
    
    [self.play(Write(text4[int(i/2)+1], run_time=2)) if i%2==0 else self.wait(2) for i in range(2*(len(text4)-1))]
    self.wait()

    text5 = TexMobject(r"\frac{1}{1-x}=1+x+x^2+\cdots+x^n+\cdots,(|x|<1)")\
      .scale(0.6).next_to(text,DOWN,aligned_edge=RIGHT)
    text5_supplement = SurroundingRectangle(text5,color='#FF8C00',stroke_width=0,fill_opacity=0.3)
    
    self.play(
      Write(text5), 
      FadeInFromDown(text5_supplement), 
      run_time=2, 
      )
    self.wait()

    text6 = TexMobject(
      r"=\frac{1}{\sqrt{5}}\cdot\frac{1+\sqrt{5}}{2}\cdot\
        \left(1+\frac{1+\sqrt{5}}{2}x+(\frac{1+\sqrt{5}}{2})^2x^2+\cdots+(\frac{1+\sqrt{5}}{2})^nx^n+\cdots\right)", 
      r"-\frac{1}{\sqrt{5}}\cdot\frac{1-\sqrt{5}}{2}\cdot\
        \left(1+\frac{1-\sqrt{5}}{2}x+(\frac{1-\sqrt{5}}{2})^2x^2+\cdots+(\frac{1-\sqrt{5}}{2})^nx^n+\cdots\right)", 
    ).scale(0.6)
    text6[0].next_to(text4[-1],DOWN,aligned_edge=LEFT)
    text6[1].next_to(text6[-2],DOWN,aligned_edge=LEFT)

    [self.play(Write(text6[int(i/2)], run_time=2)) if i%2==0 else self.wait(2) for i in range(2*len(text6))]
    self.wait(3)

    self.play(
      VGroup(text5,text5_supplement,text4[0][4:],text4[1:]).shift, LEFT*15, 
      text6.shift, UP*3.2, 
      run_time=2, 
      )
    self.wait()

    text7 = Text("对比系数：",font='未署名的信')\
      .set_color('#B4EEB4').scale(0.5).next_to(text6,DOWN).align_to(text2,LEFT).shift(DOWN*0.2)
    self.play(Write(text7))
    self.wait()

    text8 = TexMobject(r"F_n=\frac{1}{\sqrt{5}}\left[(\frac{1+\sqrt{5}}{2})^{n+1}-(\frac{1-\sqrt{5}}{2})^{n+1}\right]")\
      .scale(0.7).next_to(text7,RIGHT)
    text8_supplement = SurroundingRectangle(text8,color='#EE8262',stroke_width=0,fill_opacity=0.3)
    
    self.play(Write(text8), run_time=3)
    self.wait(2)
    self.play(FadeInFromLarge(text8_supplement))
    self.wait(2)
    self.play(Group(*self.mobjects).shift,LEFT*15,run_time=2)

