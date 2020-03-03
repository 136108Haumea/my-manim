from manimlib.imports import *

class polygon_area_scene1(Scene):
  def construct(self):

    text = VGroup(
      Text("你知道怎么求简单多边形的面积吗",font='未署名的信'),
      Text("简单多边形(Simple polygon)又称亚当多边形(Jordan polygon)",font='未署名的信'),
      Text("即满足亚当曲线(Jordan curve)的多边形",font='未署名的信'),
      Text("亚当曲线是平面上的非自交环路",font='未署名的信'),
      Text("即不存在点，边相交的情况",font='未署名的信'),
      Text("下面来看实例",font='未署名的信'),
    ).scale(0.5).set_color(color='#EEE9BF')
    text[0].move_to(ORIGIN)
    text[1].to_corner(UL)
    [text[i+2].next_to(text[i+1],DOWN,aligned_edge=LEFT) for i in range(len(text)-2)]
    text[0][6:11].set_color('#F08080')
    text[0][12:14].set_color('#FFBBFF')
    text[1][0:5].set_color('#F08080')
    text[1][23:28].set_color('#F08080')
    text[2][3:7].set_color('#BDB76B')
    text[3][0:4].set_color('#BDB76B')
    text[4][1:9].set_color('#FFFF00')
    text[5][4:6].set_color('#8B7500')
    text[0].bg = VGroup(
      SurroundingRectangle(text[0][6:11],stroke_width=0,fill_color='#AAAAAA',fill_opacity=0.3),
      SurroundingRectangle(text[0][12:14],stroke_width=0,fill_color='#AAAAAA',fill_opacity=0.3),
      )
    
    self.play(
      Write(text[0]), 
      FadeIn(text[0].bg), 
      run_time=2, 
      )
    self.wait(2)
    self.play(ReplacementTransform(VGroup(text[0],text[0].bg),text[1]))
    self.wait(2)
    [self.play(Write(text[int(i/2)+2], run_time=2)) if i%2==0 else self.wait(2) for i in range(2*(len(text)-2))]
    self.wait()
    self.play(Erase(text[1:]),run_time=2)

    polygon_inst = VGroup(
      Polygon(
        UP*0.6,UR*0.8+UP*0.3,DR*2,DR*0.1,DL*0.6+LEFT*0.2,UL*2,
        stroke_width=1,stroke_color=WHITE,fill_opacity=0.3,fill_color='#BF3EFF',
        ).shift(LEFT*3),
      VGroup(
        Polygon(
          UR,DL,DR,UL,
          stroke_width=1,stroke_color=WHITE,fill_opacity=0.5,fill_color='#FFE1FF',
          ),
        Dot(stroke_width=1,stroke_color=WHITE,fill_opacity=0.8,fill_color='#FF0000').scale(1.5)
        ).rotate(PI/6),
      VGroup(
        Polygon(
          DL,LEFT,RIGHT*1.3,DR*1.3,ORIGIN,
          stroke_width=1,stroke_color=WHITE,fill_opacity=0.5,fill_color='#FFE1FF',
          ),
        Dot(stroke_width=1,stroke_color=WHITE,fill_opacity=0.8,fill_color='#FF0000').scale(1.5)
        ).shift(RIGHT*3+UP*1.5),
      VGroup(
        Polygon(
          ORIGIN,DOWN+LEFT*0.5,DOWN+RIGHT*0.5,ORIGIN,DR*1.3+RIGHT*0.2,DL*1.3+LEFT*0.2,
          stroke_width=1,stroke_color=WHITE,fill_opacity=0.5,fill_color='#FFE1FF',
          ),
        Dot(stroke_width=1,stroke_color=WHITE,fill_opacity=0.8,fill_color='#FF0000').scale(1.5)
        ).shift(RIGHT*3+DOWN*0.5),
      )
    polygon_mark = VGroup(
      *[
        Text(("simple","non-simple")[i!=0],font='未署名的信')\
          .scale(0.3).move_to(polygon_inst[i].get_center()+UP*0.2)\
           for i in range(len(polygon_inst))
        ],
      )
    polygon_text = VGroup(
      Text("简单多边形",font='未署名的信'),
      Text("边边相交",font='未署名的信'),
      Text("点边相交",font='未署名的信'),
      Text("两点重合",font='未署名的信'),
      ).set_color('#FF7256')
    polygon_text[0].set_color('#EEE685')
    [polygon_text[i+1][2:4].set_color('#FF1493') for i in range(len(polygon_text)-1)]
    [polygon_text[i].scale(0.5).next_to(polygon_inst[i],[UP,DOWN,RIGHT,RIGHT][i]/2) for i in range(len(polygon_inst))]
    polygon_text[3].align_to(polygon_text[2], RIGHT)

    self.play(
      ShowCreation(polygon_inst),
      run_time=2,
      )
    self.play(FadeInFromDown(polygon_mark))
    self.wait()
    [self.play(Write(polygon_text[int(i/2)])) if i%2==0 else self.wait() for i in range(2*(len(polygon_text)))]
    self.wait(2)
    self.play(Group(*self.mobjects).shift,LEFT*15,run_time=2)

class polygon_area_scene2(Scene):
  def construct(self):

    polygon1 = RegularPolygon(n=5,stroke_width=2,stroke_color=WHITE,fill_opacity=1,fill_color='#FF82AB')
    polygon1_mark = VGroup(
      *[
        Text(['A','B','C','D','E'][i],font='未署名的信').scale(0.6)\
          .move_to(polygon1.get_center()+(polygon1.get_vertices()[i]-polygon1.get_center())*1.3)
          for i in range(len(polygon1.get_vertices()))
        ]
      ).set_color('#D2B48C')

    polygon2 = VGroup(
      *[
        Polygon(
          polygon1.get_vertices()[0],
          polygon1.get_vertices()[i+1],
          polygon1.get_vertices()[i+2],
          stroke_width=2,stroke_color=WHITE,fill_opacity=1,fill_color='#FF82AB',
          ) for i in range(3)]
      )
    polygon2_mark = VGroup(
      VGroup(*[
        Text(['A','B','C','D','E'][i],font='未署名的信').scale(0.6)\
          .move_to(polygon1.get_center()+(polygon1.get_vertices()[i]-polygon1.get_center())*1.3)
          for i in [0,1,2]
        ]), 
      VGroup(*[
        Text(['A','B','C','D','E'][i],font='未署名的信').scale(0.6)\
          .move_to(polygon1.get_center()+(polygon1.get_vertices()[i]-polygon1.get_center())*1.3)
          for i in [0,2,3]
        ]), 
      VGroup(*[
        Text(['A','B','C','D','E'][i],font='未署名的信').scale(0.6)\
          .move_to(polygon1.get_center()+(polygon1.get_vertices()[i]-polygon1.get_center())*1.3)
          for i in [0,3,4]
        ]), 
      ).set_color('#D2B48C')
    
    #polygon1 = RegularPolygon(n=5)
    polygon3 = Polygon(
      polygon1.get_vertices()[0],
      Dot(polygon1.get_vertices()[1]).rotate(
        2*get_angle(
          self, 
          polygon1.get_vertices()[1],
          polygon1.get_vertices()[0],
          polygon1.get_vertices()[2],
          ),
        about_point=polygon1.get_vertices()[0],
        ).get_center(),
      *polygon1.get_vertices()[2:],
      stroke_width=2,stroke_color=WHITE,fill_opacity=1,fill_color='#FF82AB',
      )
    polygon3_mark = VGroup(
      *[
        Text(['A','B','C','D','E'][i],font='未署名的信').scale(0.6)\
          .move_to(polygon3.get_center()+(polygon3.get_vertices()[i]-polygon3.get_center())*(-0.2,1.3)[i!=1])
          for i in range(len(polygon3.get_vertices()))
        ]
      )

    polygon4 = VGroup(
      *[Polygon(
        *[polygon3.get_vertices()[i] 
          for i in [0,j+1,j+2]],
          stroke_width=2,stroke_color=WHITE,fill_opacity=1,fill_color='#FF82AB',
        ) for j in range(3)
      ])
    polygon4_mark = VGroup(
      *[VGroup(
        *[polygon3_mark[i].copy().move_to(polygon4[j].get_center()+\
          (polygon4[j].get_vertices()[(i-j,i)[i==0]]-polygon4[j].get_center())*1.4)
          for i in [0,j+1,j+2]
        ])for j in range(3)
      ])

    text2 = VGroup(
      Text("对于简单多边形,你很大概率地知道一种方法",font='未署名的信'), 
      Text("即对简单多边形进行三角划分",font='未署名的信'), 
      Text("显然可以沿着AC,AD分割",font='未署名的信'), 
      Text("分别求每个三角形的面积,和即多边形面积",font='未署名的信'), 
      Text("但是，等等，看看这个栗子",font='未署名的信'), 
      Text("显然这样分割的面积可能不等于四边形面积",font='未署名的信'), 
      Text("因此沿着某一条边分割可能不具有普适性",font='未署名的信'),
      Text("但是，这种方法不可行吗?",font='未署名的信'),
      ).scale(0.5).set_color('#EEE8AA')
    text2[0][2:7].set_color('#EE82EE')
    text2[1][2:7].set_color('#EE82EE')
    text2[1][9:13].set_color('#FF3030')
    text2[2][11:13].set_color('#EE9572')	
    text2[4][10:12].set_color('#8B7500')
    text2[6][15:18].set_color('#B03060')	
    [text2[i+0].next_to(polygon1_mark,DOWN) for i in range(len(text2)-3)]
    [text2[i+5].move_to(ORIGIN) for i in range(3)]

    self.play(Write(text2[0]))
    self.wait(2)
    self.play(Erase(text2[0]))
    self.play(Write(text2[1]))
    self.wait(2)
    self.play(Erase(text2[1]))
    self.play(
      ShowCreation(polygon1),
      FadeInFromRandom(polygon1_mark),
      run_time=2,
      )
    self.wait()
    self.play(Write(text2[2]))
    self.wait(2)
    self.play(VGroup(polygon1,polygon1_mark).to_corner,UL)
    self.play(
      ReplacementTransform(polygon1.copy(),polygon2),
      ReplacementTransform(polygon1_mark.copy(),polygon2_mark),
      run_time=2,
      )
    self.play(
      *[
        ApplyMethod(polygon2[i].shift,[LEFT,ORIGIN,RIGHT][i])\
         for i in range(len(polygon2))
        ], 
      *[
        ApplyMethod(polygon2_mark[i].shift,[LEFT,ORIGIN,RIGHT][i])\
         for i in range(len(polygon2_mark))
        ], 
      )
    self.wait()
    self.play(Erase(text2[2]))
    self.play(Write(text2[3]))
    self.wait(2)
    self.play(Erase(text2[3]))
    self.play(Write(text2[4]))
    self.wait(2)
    self.play(Erase(text2[4]))
    self.play(VGroup(polygon2,polygon2_mark).to_corner,DL)
    self.play(
      ShowCreation(polygon3),
      FadeInFromRandom(polygon3_mark),
      run_time=2,
      )
    self.play(VGroup(polygon3,polygon3_mark).to_corner,UR)
    self.play(
      ReplacementTransform(polygon3.copy(),polygon4),
      ReplacementTransform(polygon3_mark.copy(),polygon4_mark),
      run_time=2,
      )
    self.wait()
    self.play(
      *[
        ApplyMethod(polygon4[i].shift,[LEFT*1.2,ORIGIN,RIGHT][i])\
         for i in range(len(polygon4))
        ], 
      *[
        ApplyMethod(polygon4_mark[i].shift,[LEFT*1.2,ORIGIN,RIGHT][i])\
         for i in range(len(polygon4_mark))
        ], 
      )
    self.play(VGroup(polygon4,polygon4_mark).to_corner,DR)
    self.wait()
    self.play(Write(text2[5]))
    self.wait(2)
    self.play(Erase(text2[5]))
    self.play(Write(text2[6]))
    self.wait(2)
    self.play(Erase(text2[6]))
    self.play(Write(text2[7]))
    self.wait(2)
    self.play(Erase(text2[7]))
    self.play(Group(*self.mobjects).shift,DOWN*8,run_time=2)

class polygon_area_scene3(Scene):
  def construct(self):
    text = VGroup(
      Text("通过邓老师讲解的割耳朵算法(ear-cutting algorithm/O(nlogn))", font='未署名的信'),
      Text("三角剖分计算简单多边形面积是可行的，但是不够快", font='未署名的信'),
      Text("接下来介绍另一种方法", font='未署名的信'),
      Text("先引入“有向面积”", font='未署名的信'),
      ).scale(0.5).set_color('#EEE8AA')
    text[0][2:5].set_color('#F08080').set_stroke(width=3)
    text[0][8:13].set_color('#FF3030')
    text[1][0:4].set_color('#CD919E')
    text[1][14:16].set_color('#66CD00')
    text[1][20:23].set_color('#66CD00')
    text[3][4:8].set_color('#7FFF00')
    text[0].to_corner(UL)
    [text[i+1].next_to(text[i],DOWN,aligned_edge=LEFT) for i in range(len(text)-1)]

    [self.play(Write(text[int(i/2)], run_time=2)) if i%2==0 else self.wait(2) for i in range(2*len(text))]
    self.wait()
    self.play(Erase(text),run_time=2)

    polygon1_mark = [ORIGIN,UR*1.5,DR]
    polygon1 = VGroup(
      Polygon(*polygon1_mark,stroke_width=0,fill_color='#CD96CD',fill_opacity=0.3),
      *[
        Arrow(
          polygon1_mark[i],polygon1_mark[(i+1)%3],
          max_tip_length_to_length_ratio=0.2/get_distance(self,polygon1_mark[i],polygon1_mark[(i+1)%3]),
          buff=0,stroke_width=1,stroke_color=WHITE,fill_opacity=0.3) for i in range(len(polygon1_mark)
        )],
      ).shift(RIGHT*4)
    polygon1_label = VGroup(
      *[
        Text(['A','C','B'][i],font='未署名的信').scale(0.6)\
          .move_to(polygon1[0].get_center()+(polygon1[0].get_vertices()[i]-polygon1[0].get_center())*1.3)
          for i in range(len(polygon1[0].get_vertices()))
        ],
      Text("负",font='未署名的信').scale(0.6).move_to(polygon1[0].get_center()),
      )
    polygon2 = VGroup(
      Polygon(*polygon1_mark,stroke_width=0,fill_color='#00CD00',fill_opacity=0.3),
      *[
        Arrow(
          polygon1_mark[(i+1)%3],polygon1_mark[i],
          max_tip_length_to_length_ratio=0.2/get_distance(self,polygon1_mark[i],polygon1_mark[(i+1)%3]),
          buff=0,stroke_width=1,stroke_color=WHITE,fill_opacity=0.3) for i in range(len(polygon1_mark)
        )],
      ).shift(RIGHT*2)
    polygon2_label = VGroup(
      *[
        Text(['A','C','B'][i],font='未署名的信').scale(0.6)\
          .move_to(polygon2[0].get_center()+(polygon2[0].get_vertices()[i]-polygon2[0].get_center())*1.3)
          for i in range(len(polygon2[0].get_vertices()))
        ],
      Text("正",font='未署名的信').scale(0.6).move_to(polygon2[0].get_center()),
      )
    
    self.play(
      ShowCreation(polygon1),
      ShowCreation(polygon2),
      Write(polygon1_label),
      Write(polygon2_label),
      run_time=2,
      )
    self.wait()
    
    text2 = VGroup(
      TexMobject(r"\text{定义三角形}A(x_1,y_1),B(x_2,y_2),C(x_3,y_3)\text{的“有向面积”：}", font='未署名的信'),
      TexMobject(
        r"2\widetilde{S}_{ABC}=\
          \begin{vmatrix}\
          x_1 & y_1 & 1\\\
          x_2 & y_2 & 1\\\
          x_3 & y_3 & 1\
          \end{vmatrix}=\
          x_1y_2-x_2y_1+x_2y_3-x_3y_2+x_3y_1-x_1y_3",
        ),
      TexMobject(
        r"2\widetilde{S}_{ACB}=\
          \begin{vmatrix}\
          x_1 & y_1 & 1\\\
          x_3 & y_3 & 1\\\
          x_2 & y_2 & 1\
          \end{vmatrix}=-2\widetilde{S}_{ABC}"
        ),
      TexMobject(
        r"\text{当C为原点时：}",
        ),
      TexMobject(
        r"\widetilde{S}_{ABC}=\frac{1}{2}(x_1y_2-x_2y_1)",
        ),
      TexMobject(
        r"\text{即以原点为起点的逆时针三角形面积为正，顺时针为负}"
      )
      ).scale(0.8).set_color('#EEE8AA')
    text2[0].to_corner(UL)
    [text2[i+1].next_to(text2[i],DOWN,aligned_edge=LEFT) for i in range(len(text2)-1)]
    VGroup(text2[1][0][35:44],text2[1][0][45:54],text2[1][0][55:64]).arrange(DOWN).next_to(text2[1][0][34],RIGHT*2)
    text2[1][0][44].move_to((text2[1][0][35].get_center()+text2[1][0][45].get_center())/2+LEFT*0.25)
    text2[1][0][54].move_to((text2[1][0][45].get_center()+text2[1][0][55].get_center())/2+LEFT*0.25)
    [text2[i+1][0][27].align_to(text2[i+1][0][22],RIGHT) for i in range(2)]
    text2_bg1 = SurroundingRectangle(text2[1][0][45:64],stroke_width=0,fill_color='#FFD700',fill_opacity=0.3)
    text2_bg1_supplement = TexMobject("=0").next_to(text2_bg1,RIGHT)
    
    [self.play(Write(text2[int(i/2)], run_time=(3,1)[i==0])) if i%2==0 else self.wait((3,2)[i==0]) for i in range(2*3)]
    self.play(Write(text2[3]))
    self.wait(2)
    self.play(FadeIn(text2_bg1))
    self.play(Write(text2_bg1_supplement))
    self.wait()
    self.play(
      ReplacementTransform(text2[1][0][0].copy(),text2[4][0][6:9]),
      ReplacementTransform(text2[1][0][1:7].copy(),text2[4][0][0:6]),
      ReplacementTransform(text2[1][0][35:44].copy(),text2[4][0][10:19]),
      FadeIn(VGroup(text2[4][0][9],text2[4][0][19])),
      run_time=2,
      )
    self.wait()
    self.play(Write(text2[5]),run_time=2)
    self.wait(5)
    self.play(Group(*self.mobjects).shift,LEFT*15,run_time=2)

class polygon_area_scene4(Scene):
  def construct(self):

    mark = VGroup(
      TexMobject("+"),
      TexMobject("-"),
      TexMobject("0"),
      ).set_stroke(width=5,color='#FF8C00')

    text = VGroup(
      Text("记：", font='未署名的信'),
      Text("“+”为计入了一块正面积", font='未署名的信'),
      Text("“-”为计入了一块负面积", font='未署名的信'),
      Text("“0”为计入相同数目的正负面积", font='未署名的信'),
      ).scale(0.5).set_color('#EEE8AA')
    text[0].to_corner(UL)
    [text[i+1][1].set_color('#FFD700') for i in range(3)]
    text[1][-3].set_color('#FFD700')
    text[2][-3].set_color('#FFD700')
    text[3][-4:-2].set_color('#FFD700')
    [text[i+1].next_to(text[i],DOWN,aligned_edge=LEFT) for i in range(3)]
    [self.play(Write(text[int(i/2)], run_time=(2,1)[i==0])) if i%2==0 else self.wait((2,1)[i==0]) for i in range(2*4)]
    self.wait(2)
    #self.play(Erase(text),run_time=2)
    numberplane = NumberPlane(lag_ratio=0.1).set_stroke(opacity=0.3)
    doto = Dot(ORIGIN)
    doto_mark = TexMobject("O").next_to(doto,DL/2)
    self.play(
      ShowCreation(numberplane),
      ShowCreation(VGroup(doto,doto_mark))
      )
    self.wait()

    polygon1_mark = [RIGHT*3,UR*2+UP,RIGHT*5+UP,RIGHT*4,RIGHT*5+DOWN,DR*2+DOWN]
    polygon1 = Polygon(*polygon1_mark,stroke_width=1,stroke_color=WHITE,fill_color='#FF69B4',fill_opacity=0.3)
    self.play(ShowCreation(polygon1))
    self.wait()

    dota = Dot(polygon1_mark[-1])
    dota_mark = TexMobject("P_0").next_to(dota,DL/2)
    self.play(ShowCreation(VGroup(dota,dota_mark)))
    self.wait()

    text2 = Text("接下来从A点逆时针遍历多边形", font='未署名的信')\
      .scale(0.5).set_color('#EEE8AA').next_to(text,DOWN,aligned_edge=LEFT)
    polygon1_arrow = VGroup(
      *[
        Arrow(
          polygon1_mark[(i+1)%len(polygon1_mark)],polygon1_mark[i],
          max_tip_length_to_length_ratio=0.2/get_distance(self,polygon1_mark[i],polygon1_mark[(i+1)%len(polygon1_mark)]),
          buff=0,stroke_width=1,stroke_color=WHITE,fill_opacity=0.3)\
        for i in range(len(polygon1_mark))
      ])
    
    self.play(Write(text2),run_time=2)
    self.wait(2)
    self.play(ShowCreation(polygon1_arrow))
    self.wait()

    polygon2 = VGroup(
      *[
        Polygon(
          ORIGIN,polygon1_mark[(i+1)%len(polygon1_mark)],polygon1_mark[i],
          fill_color=Mycolors[i*66],fill_opacity=0.3).set_stroke(width=1,color=WHITE)\
        for i in range(len(polygon1_mark))
      ])
    polygon2_arrow = VGroup(
      *[
        VGroup(
          *[
            Arrow(
              polygon2[j].get_vertices()[i],polygon2[j].get_vertices()[(i+1)%3],
              max_tip_length_to_length_ratio=0.2/get_distance(self,polygon2[j].get_vertices()[(i+1)%3],polygon2[j].get_vertices()[i]),
              buff=0).set_stroke(width=1,color=WHITE)\
            for i in range(3)
          ])\
        for j in range(len(polygon2))
      ])

    pos = [
      [3,-1.5,0],[1.75,-1.25,0],[3.75,-0.5,0],[2.5,-0.25,0],
      [3,+1.5,0],[1.75,+1.25,0],[3.75,+0.5,0],[2.5,+0.25,0],
      ]

    mark1 = VGroup(
      mark[0].copy().move_to(pos[0]),
      mark[0].copy().move_to(pos[1]),
      )
    self.play(ShowCreation(polygon2[4]))
    [self.play(ScaleInPlace(polygon2_arrow[4][i],2,rate_func=wiggle)) for i in range(3)]
    self.play(FadeIn(mark1))
    self.wait(2)
    self.play(FadeOut(polygon2_arrow[4]))

    mark2 = VGroup(
      mark[0].copy().move_to(pos[2]),
      mark[0].copy().move_to(pos[3]),
      )
    self.play(ShowCreation(polygon2[3]))
    [self.play(ScaleInPlace(polygon2_arrow[3][i],2,rate_func=wiggle)) for i in range(3)]
    self.play(FadeIn(mark2))
    self.wait(2)
    self.play(FadeOut(polygon2_arrow[3]))

    mark3 = VGroup(
      mark[0].copy().move_to(pos[6]),
      mark[0].copy().move_to(pos[7]),
      )
    self.play(ShowCreation(polygon2[2]))
    [self.play(ScaleInPlace(polygon2_arrow[2][i],2,rate_func=wiggle)) for i in range(3)]
    self.play(FadeIn(mark3))
    self.wait(2)
    self.play(FadeOut(polygon2_arrow[2]))

    mark4 = VGroup(
      mark[0].copy().move_to(pos[4]),
      mark[0].copy().move_to(pos[5]),
      )
    self.play(ShowCreation(polygon2[1]))
    [self.play(ScaleInPlace(polygon2_arrow[1][i],2,rate_func=wiggle)) for i in range(3)]
    self.play(FadeIn(mark4))
    self.wait(2)
    self.play(FadeOut(polygon2_arrow[1]))

    mark5 = VGroup(
      mark[2].copy().move_to(pos[5]),
      mark[2].copy().move_to(pos[7]),
      )
    self.play(ShowCreation(polygon2[0]))
    [self.play(ScaleInPlace(polygon2_arrow[0][i],2,rate_func=wiggle)) for i in range(3)]
    self.play(
      ReplacementTransform(mark4[1],mark5[0]),
      ReplacementTransform(mark3[1],mark5[1]),
      )
    self.wait(2)
    self.play(FadeOut(polygon2_arrow[0]))

    mark6 = VGroup(
      mark[2].copy().move_to(pos[1]),
      mark[2].copy().move_to(pos[3]),
      )
    self.play(ShowCreation(polygon2[5]))
    [self.play(ScaleInPlace(polygon2_arrow[5][i],2,rate_func=wiggle)) for i in range(3)]
    self.play(
      ReplacementTransform(mark1[1],mark6[0]),
      ReplacementTransform(mark2[1],mark6[1]),
      )
    self.wait(2)
    self.play(FadeOut(polygon2_arrow[5]))
    self.wait()

    self.play(
      FadeOut(VGroup(polygon2,mark5,mark6)),
      run_time=2,
      )
    self.wait()

    text3 = TexMobject(
      r"S_{\text{多边形}}=\sum_{k=0}^{\infty}S_{\Delta OP_{k}P_{k+1}}=\frac{1}{2}\sum_{k=0}^{\infty}(x_k y_{k+1}-x_{k+1}y_k)",
      ).set_color('#FF7F24').next_to(text2,DOWN,aligned_edge=LEFT)
    text3[0][19:43].next_to(text3[0][4:18],DOWN,aligned_edge=LEFT)
    text3.bg = SurroundingRectangle(text3,stroke_width=0,fill_color='#AAAAAA',fill_opacity=0.3)
    text4 = TexMobject(
      r"\text{其中}\infty\text{表示循环遍历}",
      ).set_color('#EEE8AA').next_to(text3,DOWN,aligned_edge=LEFT)
    text4[-4:].set_color('#CD1076')
    
    self.play(
      FadeIn(text3.bg),
      Write(text3),
      run_time=2,
      )
    self.play(Write(text4))
    self.wait(5)

    self.play(Group(*self.mobjects).shift,LEFT*15,run_time=2)
