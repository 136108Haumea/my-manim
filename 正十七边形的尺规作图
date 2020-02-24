class polygon17_scene1(Scene):
    def construct(self):
        text = Text("Definition 1.A point is that which has no part.", font='未署名的信')\
            .scale(0.6).shift(UP*2)
        text_supplement = Text("点是没有部分的东西", font='未署名的信')\
            .next_to(text,DOWN).shift(RIGHT)

        text[0:10].set_color('#EE9A00').set_stroke(width=3)
        text[15:20].set_color('#EE7AE9')
        text[24:28].set_color('#DEB887')
        text[-5:-1].set_color('#7FFF00')
        text_supplement[0].set_color('#EE7AE9')
        text_supplement[7:9].set_color('#DEB887')
        text_supplement[4:6].set_color('#7FFF00')

        self.play(FadeInRandom(text))
        self.play(FadeInRandom(text_supplement))
        self.wait()

        text2 = Text("Definition 2.A line is breadthless length.", font='未署名的信')\
            .scale(0.6).next_to(text_supplement, DOWN).align_to(text, LEFT)

        text2_supplement = Text("线是没有宽度的长度", font='未署名的信')\
            .next_to(text2, DOWN).align_to(text_supplement, RIGHT)
        text2[0:10].set_color('#EE9A00').set_stroke(width=3)
        text2[15:19].set_color('#EE7AE9')
        text2[23:30].set_color('#7FFF00')
        text2[-7:-1].set_color('#DEB887')
        text2_supplement[0].set_color('#EE7AE9')
        text2_supplement[7:9].set_color('#DEB887')
        text2_supplement[4:6].set_color('#7FFF00')

        self.play(FadeInRandom(text2))
        self.play(FadeInRandom(text2_supplement))
        self.wait()

        text3 =VGroup(
            Line(LEFT,RIGHT).set_stroke(width=5).make_smooth(), 
            Text("《原本》(Stoicheia)", font='未署名的信').scale(0.8), 
            ).arrange(RIGHT/2).next_to(text2_supplement, DOWN).align_to(text_supplement, RIGHT)
        text3[0].shift(0.1*DOWN)
        text3[1][1:3].set_color('#CD6090')
        text3[1][5:14].set_color('#CDBA96')

        self.play(Write(text3[0]))
        self.play(WriteRandom(text3[1]))
        
        self.wait(2)

class polygon17_scene2(Scene):
    CONFIG = {
        "compass": None,
        "angle": 0, 
    }

    def MyCompass(self):
        compass_center = Dot().scale(0).set_color('#87CEFA')
        compass_part1 = Polygon(ORIGIN,UP*3,0.15*LEFT+UP*2.7,0.15*LEFT)\
            .set_color('#FF7F00').set_opacity(1).set_stroke(width=0)
        compass_part2 = Polygon(ORIGIN,UP*3,0.15*RIGHT+UP*2.7,0.15*RIGHT)\
            .set_color('#FF7F00').set_opacity(1).set_stroke(width=0)
        compass_part3 = Polygon(LEFT/2,DOWN*4+LEFT/2,DOWN*4+RIGHT/2,RIGHT/2)\
            .set_color('#FF7F00').set_opacity(1).set_stroke(width=0).scale(0.15).round_corners(0.08)

        compass_part4 = Circle(fill_color='#87CEFA',fill_opacity=1).scale(0.3).set_stroke(width=6, color='#8470FF', opacity=0.5)

        compass_part3.next_to(compass_part4, DOWN).shift(UP*0.4)
        compass_part4.plot_depth=3
        
        self.angle = 0
        compass = VGroup(compass_center, compass_part1, compass_part2, compass_part3, compass_part4).scale(0.8)
        compass.plot_depth=3
        
        #compass[4].add_updater(lambda a:a.move_to(compass[0].get_center_of_mass()))
        '''
        compass[1].add_updater(
            lambda a:a.shift(
                [a.get_vertices()[0][0]-compass[0].get_center_of_mass()[0], 
                a.get_vertices()[0][1]-compass[0].get_center_of_mass()[1], 0]
                )
            )

        compass[2].add_updater(
            lambda a:a.shift(
                [a.get_vertices()[0][0]-compass[0].get_center_of_mass()[0], 
                a.get_vertices()[0][1]-compass[0].get_center_of_mass()[1], 0]
                )
            )
        '''
        self.compass = compass

    def get_compass_center(self):
        return self.compass[0].get_center()
        
    def set_angle(self, angle):
        rotate_angle = (angle-self.angle)/2
        self.play(
            Rotating(mobject=self.compass[1], radians=rotate_angle, about_point=self.compass[0].get_center_of_mass()), 
            Rotating(mobject=self.compass[2], radians=-rotate_angle, about_point=self.compass[0].get_center_of_mass()), 
            run_time=1
            )
        self.angle = angle

    def let_left_rotate(self, angle):
        self.play(
            Rotating(mobject=self.compass[1], radians=angle, about_point=self.compass[0].get_center_of_mass()), 
            Rotating(mobject=self.compass[3], radians=angle/2, about_point=self.compass[0].get_center_of_mass()), 
        )
        self.angle = self.angle+angle
    
    def let_left_rotate_2(self, angle):
        mobject=self.compass[1].rotate(angle=angle, about_point=self.compass[0].get_center_of_mass())
        mobject=self.compass[3].rotate(angle=angle/2, about_point=self.compass[0].get_center_of_mass())
        self.angle = self.angle+angle
    
    def let_right_rotate(self, angle):
        self.play(
            Rotating(mobject=self.compass[2], radians=-angle, about_point=self.compass[0].get_center_of_mass()), 
            Rotating(mobject=self.compass[3], radians=-angle/2, about_point=self.compass[0].get_center_of_mass()), 
        )
        self.angle = self.angle+angle

    def let_right_rotate_2(self, angle):
        mobject=self.compass[2].rotate(angle=-angle, about_point=self.compass[0].get_center_of_mass())
        mobject=self.compass[3].rotate(angle=-angle/2, about_point=self.compass[0].get_center_of_mass())
        self.angle = self.angle+angle

    def set_origin(self):
        self.set_angle(0)
        self.angle=0
        o = self.compass[0].get_center_of_mass()
        a = [self.get_left_claw()[0]+self.get_right_claw()[0],
            self.get_left_claw()[1]+self.get_right_claw()[1],0]
        oa = [a[0]-o[0], a[1]-o[1], 0]
        rotate_angle = ((0,PI/2)[oa[0]<0],(PI,PI*3/2)[oa[0]>0])[oa[1]<0]+math.atan(abs(oa[1]/oa[0]))
        Rotating(mobject=self.compass, radians=PI/2-rotate_angle, about_point=self.compass[0].get_center_of_mass())
        self.compass.move_to(ORIGIN)

    def show_origin(self):
        self.set_angle(0)
        self.angle=0
        o = self.compass[0].get_center_of_mass()
        a = [self.get_left_claw()[0]+self.get_right_claw()[0],
            self.get_left_claw()[1]+self.get_right_claw()[1],0]
        oa = [a[0]-o[0], a[1]-o[1], 0]
        rotate_angle = (((0,PI/2)[oa[0]<0]),((PI,PI*3/2)[oa[0]>0]))[oa[1]<0]+math.atan(abs(oa[1]/oa[0]))
        self.play(
            Rotating(mobject=self.compass, radians=PI/2-rotate_angle, about_point=self.compass[0].get_center_of_mass()), 
            ApplyMethod(self.compass.move_to, ORIGIN), 
            )

    def get_left_claw(self):
        return self.compass[1].get_vertices()[1]

    def get_right_claw(self):
        return self.compass[2].get_vertices()[1]  
    
    def set_left_claw_tip(self, pos):
        self.play(
            ApplyMethod(self.compass.move_to, pos, self.get_left_claw())
        )
    
    def set_right_claw_tip(self, pos):
        self.play(
            ApplyMethod(self.compass.move_to, pos, self.get_right_claw())
        )

    def set_left_claw_align(self, dot):
        self.compass.add_updater(
            lambda a:a.shift(
                [self.get_left_claw()[0]-dot.get_center_of_mass()[0], 
                self.get_left_claw()[1]-dot.get_center_of_mass()[1], 0]
            )
        )

    def thetax(self,point,m):
        if point[0]==0:
            if point[1]>0:
                return PI/2
            else:return PI*3/2
        if point[1]==0:
            if point[0]>0:
                if m==0:return 0
                else:return PI*2
            else:return PI
        a = math.atan(abs(point[1]/point[0]))

        
        if point[0]>0 and point[1]>0:
            if m==0:return a
            else:return a+2*PI
        if point[0]<0 and point[1]>0:
            return PI-a
        if point[0]<0 and point[1]<0:
            return PI+a
        if point[0]>0 and point[1]<0:
            return 2*PI-a

    def get_distance_between_point(self, a, b):
        return np.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)

    def get_distance_between_tip(self):
        return self.get_distance_between_point(self.get_left_claw(), self.get_right_claw())
    
    def get_vector(self,a,b):
        return [b[0]-a[0], b[1]-a[1], 0]

    def get_angle_o(self, O, A, B):
        b = self.get_distance_between_point(O,A)
        a = self.get_distance_between_point(O,B)
        o = self.get_distance_between_point(A,B)
        return math.acos((a**2+b**2-o**2)/(2*a*b))

    def get_angle_by_tip_distance(self,o):
        a = b = self.get_distance_between_point(self.get_left_claw(), self.get_compass_center())
        return math.acos((a**2+b**2-o**2)/(2*a*b))
    
    def get_mid_point(self, p, q):
        return [(p[0]+q[0])/2,(p[1]+q[1])/2,0]

    def construct(self):
        
        self.MyCompass()
        '''
        self.play(ShowCreation(self.compass))
        self.set_angle(PI/3)
        self.set_right_claw_tip(ORIGIN)
        '''
        doto = Dot()
        doto_label = Text("O", font='未署名的信').scale(0.5).next_to(doto, DOWN/3)
        '''
        self.play(ScaleInPlace(doto, 3, rate_func = wiggle))
        self.play(FadeInFromLarge(doto_label))
        '''
        self.add(VGroup(doto,doto_label))

        line = Line(LEFT*8, RIGHT*8)
        #self.play(ShowCreation(line))
        self.add(line)

        #self.play(Rotating(mobject=self.compass, radians=PI, about_point=ORIGIN), run_time=0.5)

        
        #theta = Dot().scale(0).shift(RIGHT*0.001)
        '''
        mark=0
        arc1_annotation = self.get_left_claw()[0]-self.get_right_claw()[0]
        arc1 = VGroup(
            Arc(0,0.001).scale(arc1_annotation).set_stroke(width=2,color='#00EE00',opacity=0.7).add_updater(
                lambda a:a.become(Arc(0,self.thetax(self.get_left_claw(),mark))\
                    .scale(arc1_annotation).set_stroke(width=2,color='#00EE00',opacity=0.7
                ).move_arc_center_to(ORIGIN))), 
            Arc(0,0.001).scale(arc1_annotation).set_stroke(width=10,color='#00EE00',opacity=0.3).add_updater(
                lambda a:a.become(Arc(0,self.thetax(self.get_left_claw(),mark))\
                    .scale(arc1_annotation).set_stroke(width=10,color='#00EE00',opacity=0.3
                ).move_arc_center_to(ORIGIN))), 
            )
        
        self.add(arc1)
        self.play(
            Rotating(mobject=self.compass, radians=PI, about_point=ORIGIN), 
            run_time=1, 
        )
        mark=1
        self.play(
            Rotating(mobject=self.compass, radians=PI, about_point=ORIGIN), 
            run_time=1, 
        )
        '''
        arc1_annotation = 2.4
        arc1 = VGroup(
            Arc(0,2*PI).scale(arc1_annotation).set_stroke(width=2,color='#00EE00',opacity=0.7), 
            Arc(0,2*PI).scale(arc1_annotation).set_stroke(width=10,color='#00EE00',opacity=0.3), 
            )
        self.add(arc1)
        #self.play(FadeOut(self.compass))

        dota = Dot().shift(LEFT*arc1_annotation)
        dota_label = Text("A", font='未署名的信').scale(0.5).next_to(dota, (DOWN+LEFT)/3)
        dotb = Dot().shift(RIGHT*arc1_annotation)
        dotb_label = Text("B", font='未署名的信').scale(0.5).next_to(dotb, (DOWN+RIGHT)/3)
        self.add(VGroup(dota, dotb, dota_label, dotb_label))

        '''
        self.play(ScaleInPlace(dota, 3, rate_func = wiggle))
        self.play(FadeInFromLarge(dota_label))
        self.play(ScaleInPlace(dotb, 3, rate_func = wiggle))
        self.play(FadeInFromLarge(dotb_label))
        '''

        '''
        self.set_origin()
        self.compass.next_to(dota, UP).align_to(line, DOWN)
        self.let_left_rotate_2(PI*0.6)
        self.compass.rotate(angle=-PI*0.7, about_point=dota.get_center())

        self.play(FadeIn(self.compass))

        arc2_annotation = self.get_distance_between_tip()
        arc2_origin_angle = self.thetax(self.get_vector(dota.get_center(),self.get_left_claw()),0)
        arc2 = Arc(arc2_origin_angle,0.001)\
            .scale(arc2_annotation).set_stroke(width=3,color='#A2B5CD',opacity=0.7).move_arc_center_to(dota.get_center())\
            .add_updater(lambda a:a.become(
                Arc(arc2_origin_angle, 
                (0,2*PI)[self.get_left_claw()[1]>0]+
                self.thetax(self.get_vector(dota.get_center(),self.get_left_claw()),0)-arc2_origin_angle+0.001)\
                    .scale(arc2_annotation).set_stroke(width=3,color='#A2B5CD',opacity=0.7).move_arc_center_to(dota.get_center())
            ))
        self.add(arc2)
        
        self.play(
            Rotating(mobject=self.compass, radians=PI*0.78, about_point=dota.get_center()), 
            run_time=2, 
        )

        self.play(FadeOut(self.compass))
        '''
        ###
        '''
        arc2 = Arc(5.02655,2.45044)\
            .scale(3.8832816).set_stroke(width=3,color='#A2B5CD',opacity=0.7).move_arc_center_to(dota.get_center())
        self.add(arc2)
        
        self.MyCompass()
        self.compass.rotate(PI)
        self.compass.next_to(dotb, UP).align_to(line, DOWN)
        self.let_right_rotate_2(PI*0.6)
        self.compass.rotate(angle=PI*0.7, about_point=dotb.get_center())
        
        self.play(FadeIn(self.compass))
        
        arc3_annotation = self.get_distance_between_tip()
        arc3_origin_angle = self.thetax(self.get_vector(dotb.get_center(),self.get_right_claw()),0)
        arc3 = Arc(arc3_origin_angle,0.001)\
            .scale(arc3_annotation).set_stroke(width=3,color='#A2B5CD',opacity=0.7).move_arc_center_to(dotb.get_center())\
            .add_updater(lambda a:a.become(
                Arc(arc3_origin_angle, (self.thetax(self.get_vector(dotb.get_center(),self.get_right_claw()),0)-arc3_origin_angle)+0.001)\
                    .scale(arc3_annotation).set_stroke(width=3,color='#A2B5CD',opacity=0.7).move_arc_center_to(dotb.get_center())
            ))
        self.add(arc3)
        
        self.play(
            Rotating(mobject=self.compass, radians=-PI*0.78, about_point=dotb.get_center()), 
            run_time=2, 
        )
        self.play(FadeOut(self.compass))
        
        line2 = Line(UP*5, DOWN*5).set_stroke(width=5,color='#3CB371',opacity=0.5)
        #self.play(FadeIn(line2))
        '''
        dotc = Dot().shift(UP*arc1_annotation)
        dotc_label = Text("C", font='未署名的信').scale(0.5).next_to(dotc, UP/3)
        self.add(VGroup(dotc,dotc_label))
        
        '''
        self.play(ScaleInPlace(dotc, 3, rate_func = wiggle))
        self.play(FadeInFromLarge(dotc_label))
        self.play(FadeOut(VGroup(line2,arc2,arc3)))
        '''
        
        line3 = Line(doto.get_center()*UP,dotc.get_center()*UP)\
            .set_stroke(width=3, color='#EEA2AD', opacity=0.7)
        line3_supplement = Line(doto.get_center()*UP,dotc.get_center()*UP)\
            .set_stroke(width=10, color='#EEA2AD', opacity=0.3)

        self.add(VGroup(line3,line3_supplement))

        '''
        self.MyCompass()
        self.compass.rotate(PI)
        self.compass.next_to(dota, UP).align_to(line, DOWN)
        self.let_left_rotate_2(
            self.get_angle_by_tip_distance(
                self.get_distance_between_point(
                    dota.get_center(),doto.get_center()
                    )))
        self.compass.rotate(angle=-PI*0.7, about_point=dota.get_center())

        self.play(FadeIn(self.compass))
        
        arc4_annotation = self.get_distance_between_tip()
        arc4_origin_angle = self.thetax(self.get_vector(dota.get_center(),self.get_left_claw()),0)
        arc4 = Arc(arc4_origin_angle,0.001)\
            .scale(arc4_annotation).set_stroke(width=3,color='#A2B5CD',opacity=0.7).move_arc_center_to(dota.get_center())\
            .add_updater(lambda a:a.become(
                Arc(arc4_origin_angle, 
                (0,2*PI)[self.get_left_claw()[1]>0]+
                self.thetax(self.get_vector(dota.get_center(),self.get_left_claw()),0)-arc4_origin_angle+0.001)\
                    .scale(arc4_annotation).set_stroke(width=3,color='#A2B5CD',opacity=0.7).move_arc_center_to(dota.get_center())
            ))
        self.add(arc4)
        self.play(
            Rotating(mobject=self.compass, radians=PI*1.05, about_point=dota.get_center()), 
            run_time=2, 
        )
        self.play(FadeOut(self.compass))
        '''
        '''
        arc4 = Arc(4.60767,3.3)\
            .scale(2.4).set_stroke(width=3,color='#A2B5CD',opacity=0.7).move_arc_center_to(dota.get_center())
        self.add(arc4)
        '''

        mid_oa = self.get_mid_point(dota.get_center(),doto.get_center())
        '''
        line4 = Line(UP*5, DOWN*5).shift(mid_oa).set_stroke(width=5,color='#3CB371',opacity=0.5)
        self.play(FadeIn(line4))
        self.wait()
        '''

        dot_mid_oa = Dot().shift(mid_oa)
        #self.play(ScaleInPlace(dot_mid_oa, 3, rate_func = wiggle))
        #self.play(FadeOut(line4))

        '''
        self.MyCompass()
        self.compass.rotate(PI)
        self.compass.next_to(dot_mid_oa, UP).align_to(line, DOWN)
        self.let_left_rotate_2(
            self.get_angle_by_tip_distance(
                self.get_distance_between_point(
                    dot_mid_oa.get_center(),doto.get_center()
                    )))
        self.compass.rotate(angle=-PI*0.7, about_point=dot_mid_oa.get_center())

        self.play(FadeIn(self.compass))
        
        arc5_annotation = self.get_distance_between_tip()
        arc5_origin_angle = self.thetax(self.get_vector(dot_mid_oa.get_center(),self.get_left_claw()),0)
        arc5 = Arc(arc5_origin_angle,0.001)\
            .scale(arc5_annotation).set_stroke(width=3,color='#A2B5CD',opacity=0.7).move_arc_center_to(dot_mid_oa.get_center())\
            .add_updater(lambda a:a.become(
                Arc(arc5_origin_angle, 
                (0,2*PI)[self.get_left_claw()[1]>0]+
                self.thetax(self.get_vector(dot_mid_oa.get_center(),self.get_left_claw()),0)-arc5_origin_angle+0.001)\
                    .scale(arc5_annotation).set_stroke(width=3,color='#A2B5CD',opacity=0.7).move_arc_center_to(dot_mid_oa.get_center())
            ))
        self.add(arc5)
        self.play(
            Rotating(mobject=self.compass, radians=PI*1.2, about_point=dot_mid_oa.get_center()), 
            run_time=2, 
        )
        self.play(FadeOut(self.compass))
        print(arc5_annotation)
        print(arc5_origin_angle)
        print((0,2*PI)[self.get_left_claw()[1]>0]+
                self.thetax(self.get_vector(dot_mid_oa.get_center(),self.get_left_claw()),0)-arc5_origin_angle)
        '''

        arc5 = Arc(4.33675,3.77)\
            .scale(1.2).set_stroke(width=3,color='#A2B5CD',opacity=0.7).move_arc_center_to(dot_mid_oa.get_center())
        #self.add(arc5)

        '''
        self.MyCompass()
        self.compass.rotate(PI)
        self.compass.next_to(doto, UP).align_to(line, DOWN)
        self.let_right_rotate_2(
            self.get_angle_by_tip_distance(
                self.get_distance_between_point(
                    dot_mid_oa.get_center(),doto.get_center()
                    )))
        self.compass.rotate(angle=PI*0.7, about_point=doto.get_center())
        
        self.play(FadeIn(self.compass))
        
        arc6_annotation = self.get_distance_between_tip()
        arc6_origin_angle = self.thetax(self.get_vector(doto.get_center(),self.get_right_claw()),0)
        arc6 = Arc(arc6_origin_angle,0.001)\
            .scale(arc6_annotation).set_stroke(width=3,color='#A2B5CD',opacity=0.7).move_arc_center_to(doto.get_center())\
            .add_updater(lambda a:a.become(
                Arc(arc6_origin_angle, (self.thetax(self.get_vector(doto.get_center(),self.get_right_claw()),0)-arc6_origin_angle)+0.001)\
                    .scale(arc6_annotation).set_stroke(width=3,color='#A2B5CD',opacity=0.7).move_arc_center_to(doto.get_center())
            ))
        self.add(arc6)
        
        self.play(
            Rotating(mobject=self.compass, radians=-PI*1.2, about_point=doto.get_center()), 
            run_time=2, 
        )
        self.play(FadeOut(self.compass))
        '''
        
        line4 = Line(UP*5, DOWN*5).shift(self.get_mid_point(mid_oa,doto.get_center())).set_stroke(width=5,color='#3CB371',opacity=0.5)
        #self.play(FadeIn(line4))

        dotd = Dot().shift(self.get_mid_point(mid_oa,doto.get_center()))
        dotd_label = Text("D", font='未署名的信').scale(0.5).next_to(dotd, DOWN/3)
        #self.play(ScaleInPlace(dotd, 3, rate_func = wiggle))
        #self.play(FadeInFromLarge(dotd_label))
        #self.wait()

        #self.play(FadeOut(VGroup(arc5, arc6, line4, dot_mid_oa)))

        self.add(VGroup(dotd,dotd_label))


        line5 = Line(dotd.get_center(), dotc.get_center())\
            .set_stroke(width=3, color='#EEA2AD', opacity=0.7)
        line5_supplement = Line(dotd.get_center(), dotc.get_center())\
            .set_stroke(width=10, color='#EEA2AD', opacity=0.3)
        #self.play(ShowCreation(VGroup(line5, line5_supplement)))
        #self.wait()

        self.add(VGroup(line5, line5_supplement))


        circle_d_R = self.get_distance_between_point(dotd.get_center(),dotc.get_center())
        dote = Dot().shift(dotd.get_center()+LEFT*circle_d_R)
        dote_label = Text("E", font='未署名的信').scale(0.5).next_to(dote, DOWN/3)
        dotf = Dot().shift(dotd.get_center()+RIGHT*circle_d_R)
        dotf_label = Text("F", font='未署名的信').scale(0.5).next_to(dotf, DOWN/3)
        self.add(VGroup(dote,dotf,dote_label,dotf_label))

        '''
        self.MyCompass()
        self.compass.rotate(PI)
        self.compass.next_to(dotd, UP).align_to(line, DOWN)
        self.let_right_rotate_2(
            self.get_angle_by_tip_distance(
                self.get_distance_between_point(
                    dotd.get_center(),dotc.get_center()
                    )))
        self.compass.rotate(angle=self.get_angle_o(dotd.get_center(),self.get_right_claw(),dote.get_center()), about_point=dotd.get_center())
        self.compass.shift(RIGHT*self.get_distance_between_tip())
        self.play(FadeIn(self.compass))

        arc7_annotation = self.get_distance_between_tip()
        arc7_origin_angle = self.thetax(self.get_vector(dotd.get_center(),self.get_left_claw()),0)
        arc7 = Arc(arc7_origin_angle,0.001)\
            .scale(arc7_annotation).set_stroke(width=3,color='#A2B5CD',opacity=0.7).move_arc_center_to(dotd.get_center())\
            .add_updater(lambda a:a.become(
                Arc(arc7_origin_angle, 
                (0,2*PI)[self.get_left_claw()[1]>0]+
                self.thetax(self.get_vector(dotd.get_center(),self.get_left_claw()),0)-arc7_origin_angle+0.001)\
                    .scale(arc7_annotation).set_stroke(width=3,color='#A2B5CD',opacity=0.7).move_arc_center_to(dotd.get_center())
            ))
        self.add(arc7)
        self.play(
            Rotating(mobject=self.compass, radians=PI, about_point=dotd.get_center()), 
            run_time=2, 
        )
        self.play(FadeOut(self.compass))

        self.play(ScaleInPlace(dote, 3, rate_func = wiggle))
        self.play(FadeInFromLarge(dote_label))
        self.play(ScaleInPlace(dotf, 3, rate_func = wiggle))
        self.play(FadeInFromLarge(dotf_label))
        self.wait()
        '''
        
        arc7 = Arc(2*PI,PI).scale(2.473863).set_stroke(width=3,color='#A2B5CD',opacity=0.7).move_arc_center_to(dotd.get_center())
        arc7_supplement = Arc(2*PI,PI).scale(2.473863).set_stroke(width=10,color='#A2B5CD',opacity=0.3).move_arc_center_to(dotd.get_center())
        #self.play(ShowCreation(arc7_supplement))
        self.add(VGroup(arc7,arc7_supplement))
        #self.play(FadeOut(arc7))

        '''
        self.MyCompass()
        self.compass.rotate(PI)
        self.compass.next_to(dote, UP).align_to(line, DOWN)
        self.let_left_rotate_2(
            self.get_angle_by_tip_distance(
                self.get_distance_between_point(
                    dote.get_center(),dotc.get_center()
                    )))
        self.compass.rotate(angle=-self.get_angle_o(dote.get_center(),self.get_left_claw(),dotc.get_center()+0.001), about_point=dote.get_center())
        self.play(FadeIn(self.compass))

        arc8_annotation = self.get_distance_between_tip()
        arc8_origin_angle = self.thetax(self.get_vector(dote.get_center(),self.get_left_claw()),0)
        arc8 = Arc(arc8_origin_angle,0.001)\
            .scale(arc8_annotation).set_stroke(width=3,color='#A2B5CD',opacity=0.7).move_arc_center_to(dote.get_center())\
            .add_updater(lambda a:a.become(
                Arc(arc8_origin_angle, 
                (0,2*PI)[self.get_left_claw()[1]>0 and self.get_left_claw()[0]>0]+
                self.thetax(self.get_vector(dote.get_center(),self.get_left_claw()),0)-arc8_origin_angle)\
                    .scale(arc8_annotation).set_stroke(width=3,color='#A2B5CD',opacity=0.7).move_arc_center_to(dote.get_center())
            ))
        self.add(arc8)
        self.play(
            Rotating(mobject=self.compass, radians=2*PI-self.get_angle_o(
                dote.get_center(),dotc.get_center(),dotb.get_center()
            ), about_point=dote.get_center()), 
            run_time=2, 
        )
        self.play(FadeOut(self.compass))
        '''
        arc8 = Arc(0.66295,5.62).scale(3.9).set_stroke(width=3,color='#A2B5CD',opacity=0.7).move_arc_center_to(dote.get_center())
        arc8_supplement = Arc(0.66295,5.62).scale(3.9).set_stroke(width=10,color='#A2B5CD',opacity=0.3).move_arc_center_to(dote.get_center())
        #self.play(ShowCreation(arc8_supplement))
        self.add(VGroup(arc8,arc8_supplement))
        dotg = Dot().shift(dote.get_center()+RIGHT*self.get_distance_between_point(dote.get_center(),dotc.get_center()))
        dotg_label = Text("G", font='未署名的信').scale(0.5).next_to(dotg, DOWN/3)
        '''
        self.play(ScaleInPlace(dotg, 3, rate_func = wiggle))
        self.play(FadeInFromLarge(dotg_label))
        '''
        self.add(VGroup(dotg,dotg_label))

        #self.play(FadeOut(arc8))

        doth = Dot().move_to(dotf.get_center()).shift(RIGHT*self.get_distance_between_point(dotc.get_center(),dotf.get_center()))
        doth_label = Text("H", font='未署名的信').scale(0.5).next_to(doth, DOWN/3)
        self.add(VGroup(doth, doth_label))
        '''
        self.MyCompass()
        self.compass.rotate(PI)
        self.compass.next_to(dotf, UP).align_to(line, DOWN)
        self.let_left_rotate_2(
            self.get_angle_by_tip_distance(
                self.get_distance_between_point(
                    dotf.get_center(),dotc.get_center()
                    )))
        self.compass.rotate(angle=-self.get_angle_o(dotf.get_center(),self.get_left_claw(),doth.get_center()+0.001), about_point=dotf.get_center())
        self.play(FadeIn(self.compass))
        
        arc9_annotation = self.get_distance_between_tip()
        arc9_origin_angle = self.thetax(self.get_vector(dotf.get_center(),self.get_left_claw()),0)
        arc9 = Arc(arc9_origin_angle,0.001)\
            .scale(arc9_annotation).set_stroke(width=3,color='#E9967A',opacity=0.7).move_arc_center_to(dotf.get_center())\
            .add_updater(lambda a:a.become(
                Arc(arc9_origin_angle, 
                self.thetax(self.get_vector(dotf.get_center(),self.get_left_claw()),0)-arc9_origin_angle)\
                    .scale(arc9_annotation).set_stroke(width=3,color='#E9967A',opacity=0.7).move_arc_center_to(dotf.get_center())
            ))
        self.add(arc9)
        self.play(
            Rotating(mobject=self.compass, radians=self.get_angle_o(
                dotf.get_center(),doth.get_center(),dotc.get_center()
            ), about_point=dotf.get_center()), 
            run_time=2, 
        )
        self.play(FadeOut(self.compass))
        '''
        arc9 = Arc(0,2.2337).scale(3.0449).set_stroke(width=3,color='#E9967A',opacity=0.7).move_arc_center_to(dotf.get_center())
        arc9_supplement = Arc(0,2.2337).scale(3.0449).set_stroke(width=10,color='#E9967A',opacity=0.3).move_arc_center_to(dotf.get_center())
        self.add(VGroup(arc9, arc9_supplement))
        '''
        self.play(ShowCreation(arc9_supplement))
        self.play(ScaleInPlace(doth, 3, rate_func = wiggle))
        self.play(FadeInFromLarge(doth_label))
        '''

        '''
        self.MyCompass()
        self.compass.rotate(PI)
        self.compass.next_to(dota, UP).align_to(line, DOWN)
        self.let_left_rotate_2(
            self.get_angle_by_tip_distance(2.2))
        self.compass.rotate(angle=-PI*0.7, about_point=dota.get_center())

        self.play(FadeIn(self.compass))
        
        arc10_annotation = self.get_distance_between_tip()
        arc10_origin_angle = self.thetax(self.get_vector(dota.get_center(),self.get_left_claw()),0)
        arc10 = Arc(arc10_origin_angle,0.001)\
            .scale(arc10_annotation).set_stroke(width=3,color='#FFBBFF',opacity=0.7).move_arc_center_to(dota.get_center())\
            .add_updater(lambda a:a.become(
                Arc(arc10_origin_angle, 
                (0,2*PI)[self.get_left_claw()[1]>0]+
                self.thetax(self.get_vector(dota.get_center(),self.get_left_claw()),0)-arc10_origin_angle+0.001)\
                    .scale(arc10_annotation).set_stroke(width=3,color='#FFBBFF',opacity=0.7).move_arc_center_to(dota.get_center())
            ))
        self.add(arc10)
        self.play(
            Rotating(mobject=self.compass, radians=PI*1.1, about_point=dota.get_center()), 
            run_time=2, 
        )
        self.play(FadeOut(self.compass))

        arc10_supplement = Arc(4.56,3.456752)\
            .scale(2.2).set_stroke(width=3,color='#FFBBFF',opacity=0.7).move_arc_center_to(dota.get_center())
        self.add(arc10_supplement)


        
        self.MyCompass()
        self.compass.rotate(PI)
        self.compass.next_to(dotg, UP).align_to(line, DOWN)
        self.let_right_rotate_2(
            self.get_angle_by_tip_distance(2.2))
        self.compass.rotate(angle=PI*0.7, about_point=dotg.get_center())
        
        self.play(FadeIn(self.compass))
        
        arc11_annotation = self.get_distance_between_tip()
        arc11_origin_angle = self.thetax(self.get_vector(dotg.get_center(),self.get_right_claw()),0)
        arc11 = Arc(arc11_origin_angle,0.001)\
            .scale(arc11_annotation).set_stroke(width=3,color='#FFBBFF',opacity=0.7).move_arc_center_to(dotg.get_center())\
            .add_updater(lambda a:a.become(
                Arc(arc11_origin_angle, (self.thetax(self.get_vector(dotg.get_center(),self.get_right_claw()),0)-arc11_origin_angle)+0.001)\
                    .scale(arc11_annotation).set_stroke(width=3,color='#FFBBFF',opacity=0.7).move_arc_center_to(dotg.get_center())
            ))
        self.add(arc11)
        
        self.play(
            Rotating(mobject=self.compass, radians=-PI*1.1, about_point=dotg.get_center()), 
            run_time=2, 
        )
        self.play(FadeOut(self.compass))

        line_perpendicular_ag = Line(UP*8, DOWN*8).set_stroke(width=3, color='#EEA2AD', opacity=0.7)\
            .move_to(self.get_mid_point(dota.get_center(),dotg.get_center()))
        self.play(ShowCreation(line_perpendicular_ag))
        '''
        
        dot_circle_ag_center = Dot().move_to(self.get_mid_point(dota.get_center(),dotg.get_center()))
        #self.add(dot_circle_ag_center)
        '''
        self.play(ScaleInPlace(dot_circle_ag_center, 3, rate_func = wiggle))

        self.wait()
        self.play(FadeOut(VGroup(arc10, arc11, arc10_supplement, line_perpendicular_ag)))
        '''
        
        '''
        self.MyCompass()
        self.compass.rotate(PI)
        self.compass.next_to(dot_circle_ag_center, UP).align_to(line, DOWN)
        self.let_left_rotate_2(
            self.get_angle_by_tip_distance(
                self.get_distance_between_point(
                    dot_circle_ag_center.get_center(),dotg.get_center()
                    )))
        self.compass.rotate(angle=-self.get_angle_o(dot_circle_ag_center.get_center(),self.get_left_claw(),dotg.get_center())+0.001, about_point=dot_circle_ag_center.get_center())
        self.play(FadeIn(self.compass))
        

        arc12_annotation = self.get_distance_between_tip()
        arc12_origin_angle = self.thetax(self.get_vector(dot_circle_ag_center.get_center(),self.get_left_claw()),0)
        arc12 = Arc(arc12_origin_angle,0.001)\
            .scale(arc12_annotation).set_stroke(width=3,color='#DEB887',opacity=0.7).move_arc_center_to(dot_circle_ag_center.get_center())\
            .add_updater(lambda a:a.become(
                Arc(arc12_origin_angle, 
                #(0,2*PI)[self.get_left_claw()[1]>0 and self.get_left_claw()[0]>0]+
                self.thetax(self.get_vector(dot_circle_ag_center.get_center(),self.get_left_claw()),0)-arc12_origin_angle)\
                    .scale(arc12_annotation).set_stroke(width=3,color='#DEB887',opacity=0.7).move_arc_center_to(dot_circle_ag_center.get_center())
            ))
        self.add(arc12)
        self.play(
            Rotating(mobject=self.compass, radians=2*PI-0.002, 
            about_point=dot_circle_ag_center.get_center()), 
            run_time=2, 
        )
        self.play(FadeOut(self.compass))
        self.play(FadeOut(dot_circle_ag_center))
        '''

        arc12 = Arc(0,2*PI).scale(1.613).set_stroke(width=3,color='#DEB887',opacity=0.7).move_arc_center_to(dot_circle_ag_center.get_center())
        arc12_supplement = Arc(0,2*PI).scale(1.613).set_stroke(width=10,color='#DEB887',opacity=0.3).move_arc_center_to(dot_circle_ag_center.get_center())
        self.add(VGroup(arc12, arc12_supplement))
        '''
        self.play(ShowCreation(arc12_supplement))
        self.wait()
        '''

        
        dotj = Dot().move_to(
            UP*np.sqrt(
                self.get_distance_between_point(dot_circle_ag_center.get_center(), dotg.get_center())**2-
                self.get_distance_between_point(dot_circle_ag_center.get_center(), doto.get_center())**2
                )
        )
        dotj_label = Text("J", font='未署名的信').scale(0.5).next_to(dotj, (UP+RIGHT)/3)
        self.add(VGroup(dotj, dotj_label))
        '''
        self.play(ScaleInPlace(dotj, 3, rate_func = wiggle))
        self.play(FadeInFromLarge(dotj_label))
        '''
        
        
        '''
        self.MyCompass()
        self.compass.rotate(PI)
        self.compass.next_to(doto, UP).align_to(line, DOWN)
        self.let_left_rotate_2(
            self.get_angle_by_tip_distance(3))
        self.compass.rotate(angle=-PI*0.7, about_point=doto.get_center())

        self.play(FadeIn(self.compass))
        
        arc13_annotation = self.get_distance_between_tip()
        arc13_origin_angle = self.thetax(self.get_vector(doto.get_center(),self.get_left_claw()),0)
        arc13 = Arc(arc13_origin_angle,0.001)\
            .scale(arc13_annotation).set_stroke(width=3,color='#FFBBFF',opacity=0.7).move_arc_center_to(doto.get_center())\
            .add_updater(lambda a:a.become(
                Arc(arc13_origin_angle, 
                (0,2*PI)[self.get_left_claw()[1]>0]+
                self.thetax(self.get_vector(doto.get_center(),self.get_left_claw()),0)-arc13_origin_angle+0.001)\
                    .scale(arc13_annotation).set_stroke(width=3,color='#FFBBFF',opacity=0.7).move_arc_center_to(doto.get_center())
            ))
        self.add(arc13)
        self.play(
            Rotating(mobject=self.compass, radians=PI*0.95, about_point=doto.get_center()), 
            run_time=2, 
        )
        self.play(FadeOut(self.compass))
        '''
        
        arc13_supplement = Arc(4.7592,PI*0.95)\
            .scale(3).set_stroke(width=3,color='#FFBBFF',opacity=0.7).move_arc_center_to(doto.get_center())
        #self.add(arc13_supplement)
        
        '''
        self.MyCompass()
        self.compass.rotate(PI)
        self.compass.next_to(doth, UP).align_to(line, DOWN)
        self.let_right_rotate_2(
            self.get_angle_by_tip_distance(3))
        self.compass.rotate(angle=PI*0.7, about_point=doth.get_center())
        
        self.play(FadeIn(self.compass))
        
        arc14_annotation = self.get_distance_between_tip()
        arc14_origin_angle = self.thetax(self.get_vector(doth.get_center(),self.get_right_claw()),0)
        arc14 = Arc(arc14_origin_angle,0.001)\
            .scale(arc14_annotation).set_stroke(width=3,color='#FFBBFF',opacity=0.7).move_arc_center_to(doth.get_center())\
            .add_updater(lambda a:a.become(
                Arc(arc14_origin_angle, (self.thetax(self.get_vector(doth.get_center(),self.get_right_claw()),0)-arc14_origin_angle)+0.001)\
                    .scale(arc14_annotation).set_stroke(width=3,color='#FFBBFF',opacity=0.7).move_arc_center_to(doth.get_center())
            ))
        self.add(arc14)
        
        self.play(
            Rotating(mobject=self.compass, radians=-PI*0.95, about_point=doth.get_center()), 
            run_time=2, 
        )
        self.play(FadeOut(self.compass))

        arc14_supplement = Arc(4.665576,-PI*0.95)\
            .scale(3).set_stroke(width=3,color='#FFBBFF',opacity=0.7).move_arc_center_to(doth.get_center())
        self.add(arc14_supplement)

        line_perpendicular_oh = Line(UP*8, DOWN*8).set_stroke(width=3, color='#EEA2AD', opacity=0.7)\
            .move_to(self.get_mid_point(doto.get_center(),doth.get_center()))
        self.play(ShowCreation(line_perpendicular_oh))
        '''

        dot_circle_oh_center = Dot().move_to(self.get_mid_point(doto.get_center(), doth.get_center()))

        '''
        self.MyCompass()
        self.compass.rotate(PI)
        self.compass.next_to(dot_circle_oh_center, UP).align_to(line, DOWN)
        self.let_left_rotate_2(
            self.get_angle_by_tip_distance(
                self.get_distance_between_point(dot_circle_oh_center.get_center(),doth.get_center())
            ))
        self.compass.rotate(angle=-self.get_angle_o(
            dot_circle_oh_center.get_center(), self.get_left_claw(), doth.get_center()
        ), about_point=dot_circle_oh_center.get_center())
        self.play(FadeIn(self.compass))
        self.wait()
        self.play(FadeOut(VGroup(arc13_supplement, arc14, arc14_supplement, line_perpendicular_oh)))
        '''

        '''
        self.MyCompass()
        self.compass.rotate(PI)
        self.compass.next_to(dot_circle_oh_center, UP).align_to(line, DOWN)
        self.let_left_rotate_2(
            self.get_angle_by_tip_distance(
                self.get_distance_between_point(dot_circle_oh_center.get_center(),doth.get_center())
            ))
        self.compass.rotate(angle=-self.get_angle_o(
            dot_circle_oh_center.get_center(), self.get_left_claw(), doth.get_center()
        ), about_point=dot_circle_oh_center.get_center())
        self.add(self.compass)
        self.play(ApplyMethod(self.compass.shift,self.get_vector(self.get_right_claw(),dotj.get_center())))


        arc15_annotation = self.get_distance_between_tip()
        arc15_origin_angle = self.thetax(self.get_vector(dotj.get_center(),self.get_left_claw()),0)
        arc15 = Arc(arc15_origin_angle,0.001)\
            .scale(arc15_annotation).set_stroke(width=3,color='#DEB887',opacity=0.7).move_arc_center_to(dotj.get_center())\
            .add_updater(lambda a:a.become(
                Arc(arc15_origin_angle, 
                #(0,2*PI)[self.get_left_claw()[1]>0 and self.get_left_claw()[0]>0]+
                self.thetax(self.get_vector(dotj.get_center(),self.get_left_claw()),0)-arc15_origin_angle)\
                    .scale(arc15_annotation).set_stroke(width=3,color='#DEB887',opacity=0.7).move_arc_center_to(dotj.get_center())
            ))
        self.add(arc15)
        self.play(
            Rotating(mobject=self.compass, radians=2*PI-0.002, 
            about_point=dotj.get_center()), 
            run_time=2, 
        )
        self.play(FadeOut(self.compass))
        '''

        dotk = Dot().move_to(
            LEFT*np.sqrt(2.45938**2-self.get_distance_between_point(doto.get_center(),dotj.get_center())**2)
            )
        dotk_label = Text("K", font='未署名的信').scale(0.5).next_to(dotk, DOWN/3)
        self.add(VGroup(dotk,dotk_label))
        '''
        self.play(ScaleInPlace(dotk, 3, rate_func = wiggle))
        self.play(FadeInFromLarge(dotk_label))
        self.play(FadeOut(arc15))
        '''

        '''
        self.MyCompass()
        self.compass.rotate(PI)
        self.compass.next_to(dotk, UP).align_to(line, DOWN)
        self.let_left_rotate_2(
            self.get_angle_by_tip_distance(
                self.get_distance_between_point(dotk.get_center(),dotj.get_center())
            ))
        self.compass.rotate(angle=self.get_angle_o(
            dotk.get_center(), self.get_left_claw(), dotj.get_center()
        ), about_point=dotk.get_center())
        self.play(FadeIn(self.compass))

        arc16_annotation = self.get_distance_between_tip()
        arc16_origin_angle = self.thetax(self.get_vector(dotk.get_center(),self.get_left_claw()),0)
        arc16 = Arc(arc16_origin_angle,0.001)\
            .scale(arc16_annotation).set_stroke(width=3,color='#AAAAAA',opacity=0.7).move_arc_center_to(dotk.get_center())\
            .add_updater(lambda a:a.become(
                Arc(arc16_origin_angle, 
                #(0,2*PI)[self.get_left_claw()[1]>0]+
                self.thetax(self.get_vector(dotk.get_center(),self.get_left_claw()),0)-arc16_origin_angle+0.001)\
                    .scale(arc16_annotation).set_stroke(width=3,color='#AAAAAA',opacity=0.7).move_arc_center_to(dotk.get_center())
            ))
        self.add(arc16)
        self.play(
            Rotating(mobject=self.compass, radians=self.get_angle_o(
                dotk.get_center(), LEFT*8, dotj.get_center()), about_point=dotk.get_center()), 
            run_time=2, 
        )
        self.play(FadeOut(self.compass))
        '''
        
        arc16 = Arc(0.6095,2.532066)\
            .scale(2.45938).set_stroke(width=3,color='#AAAAAA',opacity=0.7).move_arc_center_to(dotk.get_center())
        arc16_supplement = Arc(0.6095,2.532066)\
            .scale(2.45938).set_stroke(width=10,color='#AAAAAA',opacity=0.3).move_arc_center_to(dotk.get_center())
        #self.play(ShowCreation(arc16_supplement))
        self.add(VGroup(arc16, arc16_supplement))


        dotl = Dot().move_to(dotk.get_center()).shift(
            LEFT*self.get_distance_between_point(dotk.get_center(), dotj.get_center())
            )
        dotl_label = Text("L", font='未署名的信').scale(0.5).next_to(dotl, DOWN/3)
        self.add(VGroup(dotl,dotl_label))
        '''
        self.play(ScaleInPlace(dotl, 3, rate_func = wiggle))
        self.play(FadeInFromLarge(dotl_label))
        '''

        '''
        self.MyCompass()
        self.compass.rotate(PI)
        self.compass.next_to(dotl, UP).align_to(line, DOWN)
        self.let_left_rotate_2(
            self.get_angle_by_tip_distance(3))
        self.compass.rotate(angle=-PI*0.7, about_point=dotl.get_center())

        self.play(FadeIn(self.compass))
        
        arc17_annotation = self.get_distance_between_tip()
        arc17_origin_angle = self.thetax(self.get_vector(dotl.get_center(),self.get_left_claw()),0)
        arc17 = Arc(arc17_origin_angle,0.001)\
            .scale(arc17_annotation).set_stroke(width=3,color='#FFBBFF',opacity=0.7).move_arc_center_to(dotl.get_center())\
            .add_updater(lambda a:a.become(
                Arc(arc17_origin_angle, 
                (0,2*PI)[self.get_left_claw()[1]>0]+
                self.thetax(self.get_vector(dotl.get_center(),self.get_left_claw()),0)-arc17_origin_angle+0.001)\
                    .scale(arc17_annotation).set_stroke(width=3,color='#FFBBFF',opacity=0.7).move_arc_center_to(dotl.get_center())
            ))
        self.add(arc17)
        self.play(
            Rotating(mobject=self.compass, radians=PI*0.95, about_point=dotl.get_center()), 
            run_time=2, 
        )
        self.play(FadeOut(self.compass))
        '''

        '''
        arc17_supplement = Arc(4.7592,PI*0.95)\
            .scale(3).set_stroke(width=3,color='#FFBBFF',opacity=0.7).move_arc_center_to(dotl.get_center())
        self.add(arc17_supplement)
        
        self.MyCompass()
        self.compass.rotate(PI)
        self.compass.next_to(doto, UP).align_to(line, DOWN)
        self.let_right_rotate_2(
            self.get_angle_by_tip_distance(3))
        self.compass.rotate(angle=PI*0.7, about_point=doto.get_center())
        
        self.play(FadeIn(self.compass))
        
        arc18_annotation = self.get_distance_between_tip()
        arc18_origin_angle = self.thetax(self.get_vector(doto.get_center(),self.get_right_claw()),0)
        arc18 = Arc(arc18_origin_angle,0.001)\
            .scale(arc18_annotation).set_stroke(width=3,color='#FFBBFF',opacity=0.7).move_arc_center_to(doto.get_center())\
            .add_updater(lambda a:a.become(
                Arc(arc18_origin_angle, (self.thetax(self.get_vector(doto.get_center(),self.get_right_claw()),0)-arc18_origin_angle)+0.001)\
                    .scale(arc18_annotation).set_stroke(width=3,color='#FFBBFF',opacity=0.7).move_arc_center_to(doto.get_center())
            ))
        self.add(arc18)
        
        self.play(
            Rotating(mobject=self.compass, radians=-PI*0.95, about_point=doto.get_center()), 
            run_time=2, 
        )
        self.play(FadeOut(self.compass))

        arc18_supplement = Arc(4.665576,-PI*0.95)\
            .scale(3).set_stroke(width=3,color='#FFBBFF',opacity=0.7).move_arc_center_to(doto.get_center())
        #self.add(arc14_supplement)

        line_perpendicular_lo = Line(UP*8, DOWN*8).set_stroke(width=3, color='#EEA2AD', opacity=0.7)\
            .move_to(self.get_mid_point(doto.get_center(),dotl.get_center()))
        self.play(ShowCreation(line_perpendicular_lo))
        '''


        line_pq_x = self.get_distance_between_point(dotl.get_center(), doto.get_center())/2
        line_pq_y = np.sqrt(self.get_distance_between_point(dota.get_center(), doto.get_center())**2-line_pq_x**2)

        dotp = Dot().move_to([-line_pq_x,line_pq_y,0])
        dotp_label = Text("P", font='未署名的信').scale(0.5).next_to(dotp, (LEFT+UP)/3)
        self.add(VGroup(dotp,dotp_label))
        '''
        self.play(ScaleInPlace(dotp, 3, rate_func = wiggle))
        self.play(FadeInFromLarge(dotp_label))
        '''

        dotq = Dot().move_to([-line_pq_x,-line_pq_y,0])
        dotq_label = Text("Q", font='未署名的信').scale(0.5).next_to(dotq, (LEFT+DOWN)/3)
        self.add(VGroup(dotq,dotq_label))
        '''
        self.play(ScaleInPlace(dotq, 3, rate_func = wiggle))
        self.play(FadeInFromLarge(dotq_label))
        '''

        #self.play(FadeOut(VGroup(arc17_supplement, arc18, line_perpendicular_lo)))
        
        self.play(
            FadeOut(VGroup(line, line3, line3_supplement, line5, line5_supplement, 
            arc7, arc7_supplement, arc8, arc8_supplement, arc9, arc9_supplement, arc12, arc12_supplement, arc16, arc16_supplement, 
            dotj, dotj_label, dotc, dotc_label, dotl, dotl_label, dote, dote_label, dotk, dotk_label, dotd, dotd_label, 
            dotg, dotg_label, dotf, dotf_label, doth, doth_label)), 
            run_time=5, 
            )
        
        angle_17_polygon = self.get_angle_o(doto.get_center(), dota.get_center(), dotp.get_center())

        line6 = VGroup(
            Line(dota.get_center(), dotp.get_center())\
                .set_stroke(width=3, color='#CD96CD', opacity=0.7), 
            Line(dota.get_center(), dotp.get_center())\
                .set_stroke(width=10, color='#CD96CD', opacity=0.3),  
                )
        self.play(ShowCreation(line6))
        

        self.MyCompass()
        self.compass.rotate(PI)
        self.compass.next_to(dota, UP).align_to(Dot(dota.get_center()).scale(0), DOWN)
        self.let_right_rotate_2(
            self.get_angle_by_tip_distance(
                self.get_distance_between_point(dota.get_center(), dotp.get_center())
            ))
        self.compass.rotate(angle=-self.get_angle_o(
            dota.get_center(), self.get_right_claw(), dotp.get_center()
        ), about_point=dota.get_center())
        
        self.play(FadeIn(self.compass))

        polygon_17 = VGroup(line6)

        for i in range(16):
            self.play(
                Rotating(mobject=self.compass, radians=-angle_17_polygon, about_point=doto.get_center()), 
                run_time=1
            )
            polygon_17.add(
                VGroup(
                    Line(self.get_left_claw(), self.get_right_claw())\
                        .set_stroke(width=3, color='#CD96CD', opacity=0.7), 
                    Line(self.get_left_claw(), self.get_right_claw())\
                        .set_stroke(width=10, color='#CD96CD', opacity=0.3),  
                    )
            )
            self.play(ShowCreation(polygon_17[-1]))
        
        self.play(FadeOut(VGroup(
            self.compass, doto, doto_label, dota, dota_label, dotb, dotb_label, dotp, dotp_label, dotq, dotq_label, arc1, 
        )))
        
        polygon_17_supplement = Polygon(*[polygon_17[i][0].get_start() for i in range(17)])\
            .set_stroke(width=0, color='#FFFF00', opacity=0).set_color('#FFFF00').set_opacity(1)
        
        self.play(ShowCreation(polygon_17_supplement))
        self.wait(2)

        all_bg = Square(color='#FFAEB9').scale(10).set_opacity(0.3)
        self.play(FadeIn(all_bg))

        text2 = Text("参考资料：《圆之吻》", font='未署名的信').set_color('#FF7F24').set_stroke(width=5)
        text2[-4:-1].set_color('#D02090')
        self.play(WriteRandom(text2))

        self.wait(2)
  
