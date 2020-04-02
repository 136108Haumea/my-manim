# my-manim
Decadance

class scene1(Scene):
  CONFIG = {
        "camera_config": {
            "background_color": '#FFDEAD'
        }
    }
  def construct(self):
    a = ValueTracker(0)
    
    heart1 = Dot().add_updater(
      lambda f: f.become(
        ParametricFunction(
          lambda t:[t,(t**2)**(1/3)+0.9*np.sqrt(8-t**2)*np.sin(a.get_value()*PI*t),0],
          t_min=-2*np.sqrt(2)+0.001,t_max=2*np.sqrt(2)-0.01,
          stroke_width=1,stroke_color='#FF1493',stroke_opacity=1,
        )))
    heart2 = Dot().add_updater(
      lambda f: f.become(
        ParametricFunction(
          lambda t:[t,(t**2)**(1/3)+0.9*np.sqrt(8-t**2)*np.sin(a.get_value()*PI*t),0],
          t_min=-2*np.sqrt(2)+0.001,t_max=2*np.sqrt(2)-0.01,
          stroke_width=10,stroke_color='#FF1493',stroke_opacity=0.3,
        )))
    text = TexMobject(r"f(x)=x^{\frac{2}{3}}+0.9\sqrt{8-x^2}\sin(a\pi x)",color='#FF1493').scale(0.5).to_corner(UL)
    text_supplement = Text("0",font='未署名的信').add_updater(
      lambda f: f.become(
        Text("a="+str(a.get_value()),font='未署名的信',color='#FF1493').scale(0.5).next_to(text,DOWN,aligned_edge=LEFT)
      ))
    
    self.add(heart1,heart2,text,text_supplement)
    self.play(a.set_value,10,func_rate=linear,run_time=10)
    self.wait(5)
    self.play(FadeOut(Group(*self.mobjects)))

class scene2(Scene):
  CONFIG = {
        "camera_config": {
            "background_color": '#FFDEAD'
        }
    }
  def construct(self):

    heart1 = ParametricFunction(
      lambda t:[2*np.cos(t)-np.cos(2*t),2*np.sin(t)-np.sin(2*t),0],
      t_min=0,t_max=2*PI,
      stroke_width=1,stroke_color='#FF1493',stroke_opacity=1,
      fill_color='#FF1493',fill_opacity=0.6,
      )
    heart2 = heart1.copy().set_stroke(width=12)

    text = VGroup(
      Brace(Rectangle(height=1,width=0.25),LEFT),
      TexMobject(r"x=2\cos t-\cos 2t"),
      TexMobject(r"y=2\sin t-\sin 2t"),
      ).scale(0.8).set_color('#FF1493')
    VGroup(text[1],text[2]).arrange(DOWN).next_to(text[0],RIGHT)
    text.to_corner(UL)
    
    self.play(
      ShowCreation(heart1),
      ShowCreation(heart2),
      run_time=2,
      )
    self.wait()
    self.play(
      FadeInFromRandom(text[0]),
      *[FadeInFromRandom(text[i+1][0]) for i in range(2)],
      run_time=2,
      )
    self.wait(3)
    self.play(FadeOut(Group(*self.mobjects)))

class scene3(Scene):
  CONFIG = {
      "camera_config": {
          "background_color": '#FFDEAD'
      },
      "const":0.21,
    }
  def construct(self):
    
    fxy = lambda a:(self.const*a[0]**2+self.const*a[1]**2-1)**3-self.const*a[0]**2*self.const*a[1]**3
    
    text = Text("I Love U",font='未署名的信',color='#FF69B4',stroke_width=2).scale(0.2)
    text2 = VGroup(*[text.copy() for i in range(30)])
    text2[0].move_to([-10,4,0])
    [text2[i+1].next_to(text2[i],RIGHT/3) for i in range(len(text2)-1)]
    text3 = VGroup(*[text2.copy() for i in range(40)])
    [text3[i+1].next_to(text3[i],DOWN/3).shift(RIGHT*0.12) for i in range(len(text3)-1)]
    
    text4 = VGroup()

    for i in range(len(text3)):
      for j in range(len(text3[i])):
        for k in range(len(text3[i][j])):
          if fxy(text3[i][j][k].get_center())<0:
            text4.add(text3[i][j][k])
    
    text4.shift(DOWN/2)

    text5 = TexMobject("(x^2+z^2-1)^3-x^2z^3<0",color='#FF1493').to_corner(UL)

    self.play(Write(text5),run_time=2)
    self.wait()
    self.play(
      *[
        GrowFromRandom(text4[i])\
          for i in range(len(text4))
      ],
      run_time=7,
      )
    self.wait(5)
    self.play(FadeOut(Group(*self.mobjects)))

class scene4(Scene):
  CONFIG = {
      "camera_config": {
          "background_color": '#FFDEAD'
      },
      "consts":0.2,
      "divide":1024
    }
  def construct(self):
    heart1 = ParametricFunction(
      lambda t:[16*np.sin(t)**3/5,(13*np.cos(t)-5*np.cos(2*t)-2*np.cos(3*t)-np.cos(4*t))/5,0],
      t_min=0,t_max=2*PI,
      stroke_width=1,stroke_color='#FF69B4',stroke_opacity=1,
      #fill_color='#FF69B4',fill_opacity=0.6,
      )
    heart2 = ParametricFunction(
      lambda t:[16*np.sin(t)**3/5,(13*np.cos(t)-5*np.cos(2*t)-2*np.cos(3*t)-np.cos(4*t))/5,0],
      t_min=0,t_max=2*PI,
      stroke_width=12,stroke_color='#FF69B4',stroke_opacity=0.3,
      #fill_color='#FF69B4',fill_opacity=0.6,
      )

    a = [
      [
        16*np.sin(i*2*PI/self.divide)**3/5*(0.95,1.05)[i%2==0],
        (
          13*np.cos(1*i*2*PI/self.divide)-\
           5*np.cos(2*i*2*PI/self.divide)-\
           2*np.cos(3*i*2*PI/self.divide)-\
           1*np.cos(4*i*2*PI/self.divide)\
          )/5*(0.95,1.05)[i%2==0],
        0] for i in range(self.divide)
      ]
    heart3 = Polygon(*a,stroke_width=2,stroke_color='#FF69B4',stroke_opacity=1)

    text = VGroup(
      Brace(Rectangle(height=1,width=0.25),LEFT),
      TexMobject(r"x=16\sin ^3t"),
      TexMobject(r"y=13\cos t-5\cos2t-2\cos3t -\cos4t"),
      ).scale(0.8).set_color('#FF1493')
    VGroup(text[1],text[2].next_to(text[1],DOWN,aligned_edge=LEFT)).next_to(text[0],RIGHT)
    text.to_corner(UL)

    self.play(*[WriteRandom(text[i]) for i in range(len(text))],run_time=2)
    self.wait(2)
    self.play(ShowCreation(heart1),ShowCreation(heart2),run_time=2)
    self.wait(2)
    self.play(ReplacementTransform(heart1,heart3),run_time=2)
    self.play(heart3.set_fill,'#FF69B4',0.8)
    self.wait(3)
    self.play(FadeOut(Group(*self.mobjects)))

class scene5(Scene):
  CONFIG = {
      "camera_config": {
          "background_color": '#FFDEAD'
      }
    }
  def construct(self):
    fxy = lambda a:(17*a[0]**2-16*abs(a[0])*a[1]+17*a[1]**2+150/abs(5*a[0]+np.sin(5*a[1]))-255)

    text = Text("I Hate U",font='未署名的信',color='#B8860B',stroke_width=2).scale(0.2)
    text2 = VGroup(*[text.copy() for i in range(30)])
    text2[0].move_to([-10,4,0])
    [text2[i+1].next_to(text2[i],RIGHT/3) for i in range(len(text2)-1)]
    text3 = VGroup(*[text2.copy() for i in range(40)])
    [text3[i+1].next_to(text3[i],DOWN/3).shift(RIGHT*0.12) for i in range(len(text3)-1)]
    
    text4 = VGroup()

    for i in range(len(text3)):
      for j in range(len(text3[i])):
        for k in range(len(text3[i][j])):
          if fxy(text3[i][j][k].get_center())<0:
            text4.add(text3[i][j][k])
    
    text4.shift(DOWN/2).scale(0.8)

    text5 = TexMobject(
      r"17x^2-16|x|y+17y^2+\frac{150}{|5x+\sin5y|}<255",
      color='#B8860B',stroke_width=2,
      ).scale(0.6).to_edge(UL/2)
    
    self.play(Write(text5),run_time=2)
    self.wait()
    self.play(
      *[
        GrowFromRandom(text4[i])\
          for i in range(len(text4))
      ],
      run_time=7,
      )
    self.wait(5)
    self.play(FadeOut(Group(*self.mobjects)))
    
    
class heart_boxes(SpecialThreeDScene):

  CONFIG = {
    "default_angled_camera_position": {
      "phi": 70 * DEGREES,
      "theta": -45 * DEGREES,
      "distance": 50,
      },
    "camera_config": {
      "background_color": '#FFDEAD'
      },
    "const":0.5
    }

  def construct(self):

    self.set_camera_to_default_position()
    self.var_phi = 0

    boxes = MyBoxes(
      fill_color=average_color('#FF4040', '#FF69B4'), 
      box_height=0.25,
      bottom_size=(0.25, 0.25), 
      resolution=(50,50),
      )

    boxes2 = VGroup(*[boxes.copy().shift(i*OUT*0.25) for i in range(50)]).shift(25*IN*0.25).scale(0.5)
    
    fxyz = lambda a:(\
      (self.const*a[0])**2+9/4*(self.const*a[1])**2+(self.const*a[2])**2-1)**3-\
      (self.const*a[0])**2*(self.const*a[2])**3-9/80*(self.const*a[1])**2*(self.const*a[2])**3

    heart = VGroup()
    for i in boxes2:
      for j in i:
        if fxyz(j.get_center())<0:
          heart.add(j)

    text = TexMobject(
      r"(x^2+\frac{9}{4}y^2+z^2-1)^3-x^2z^3-\frac{9}{80}y^2z^3=0",
      color='#FF69B4',stroke_width=2,
      ).scale(0.6)
    
    self.add_fixed_in_frame_mobjects(text.to_corner(UL))
    self.play(ShowCreation(heart),run_time=3)
    self.play(Rotating(mobject=heart,radians=2*PI,about_point=ORIGIN),run_time=10)
    self.wait(5)
        
