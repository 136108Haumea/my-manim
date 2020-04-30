from manimlib.imports import *
import math

def iter_point(c, times=10):
    z=c
    for _ in range(times):
        if abs(z)>3:
            return False
        z=z**2+c
    return True

def GetVague(x_min=-4.5, x_max=3, y_min=-3, y_max=3, dis=0.1, color=YELLOW):
    vague = VGroup()
    x_times = int((x_max-x_min)/dis)
    y_times = int((y_max-y_min)/dis)
    for i in range(x_times):
        for j in range(y_times):
            vague.add(
                Square(
                    side_length=dis,
                    fill_color=color,
                    stroke_width=0,
                    fill_opacity=1,
                    plot_depth=0,
                    ).move_to([x_min+(i+0.5)*dis,y_min+(j+0.5)*dis,0])
                    #).move_to([x_min+i*dis,y_min+j*dis,0])
                )
    return vague

class mandelbrotset(Scene):
    def construct(self):
        tuifeibrot = VGroup()
        vague = GetVague(dis=0.01,color='#FFFF00')
        for i in vague:
            if iter_point(complex(*(i.get_center()/3)[:2]),times=25):
                tuifeibrot.add(i)
        self.add(tuifeibrot)
        self.wait()
