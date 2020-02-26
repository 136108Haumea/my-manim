from manimlib.imports import *

class Elizabeth_scene1(Scene):
    def construct(self):
        img1 = ImageMobject(r"C:\Users\Administrator\Desktop\伊丽莎白二世和一世的关系\新建文件夹\img1").scale(2.5).shift(UP*0.6)
        img1_supplement = Text("伊丽莎白二世", font='未署名的信')\
            .scale(0.5).set_stroke(width=2).set_color('#EE7600').next_to(img1, DOWN)
        

        self.play(
            FadeInFromDown(img1), 
            WriteRandom(img1_supplement), 
            run_time=2, 
            )
        self.wait(5)

        a=0.45

        img1_1 = ImageMobject(r"C:\Users\Administrator\Desktop\伊丽莎白二世和一世的关系\新建文件夹2\img1")\
            .scale(a).next_to(img1, RIGHT/2, aligned_edge=UP).shift(LEFT*3.2).shift(DOWN*0.5)
        img1_2 = ImageMobject(r"C:\Users\Administrator\Desktop\伊丽莎白二世和一世的关系\新建文件夹2\img2").scale(a).next_to(img1_1, RIGHT)
        img1_3 = ImageMobject(r"C:\Users\Administrator\Desktop\伊丽莎白二世和一世的关系\新建文件夹2\img3").scale(a).next_to(img1_2, RIGHT)
        img1_4 = ImageMobject(r"C:\Users\Administrator\Desktop\伊丽莎白二世和一世的关系\新建文件夹2\img4").scale(a).next_to(img1_3, RIGHT)
        img1_5 = ImageMobject(r"C:\Users\Administrator\Desktop\伊丽莎白二世和一世的关系\新建文件夹2\img5").scale(a).next_to(img1_1, DOWN)
        img1_6 = ImageMobject(r"C:\Users\Administrator\Desktop\伊丽莎白二世和一世的关系\新建文件夹2\img6").scale(a).next_to(img1_2, DOWN)
        img1_7 = ImageMobject(r"C:\Users\Administrator\Desktop\伊丽莎白二世和一世的关系\新建文件夹2\img7").scale(a).next_to(img1_3, DOWN)
        img1_8 = ImageMobject(r"C:\Users\Administrator\Desktop\伊丽莎白二世和一世的关系\新建文件夹2\img8").scale(a).next_to(img1_4, DOWN)
        img1_9 = ImageMobject(r"C:\Users\Administrator\Desktop\伊丽莎白二世和一世的关系\新建文件夹2\img9").scale(a).next_to(img1_5, DOWN)
        img1_10 = ImageMobject(r"C:\Users\Administrator\Desktop\伊丽莎白二世和一世的关系\新建文件夹2\img10").scale(a).next_to(img1_6, DOWN)
        img1_11 = ImageMobject(r"C:\Users\Administrator\Desktop\伊丽莎白二世和一世的关系\新建文件夹2\img11").scale(a).next_to(img1_7, DOWN)
        img1_12 = ImageMobject(r"C:\Users\Administrator\Desktop\伊丽莎白二世和一世的关系\新建文件夹2\img12").scale(a).next_to(img1_8, DOWN)
        img1_13 = ImageMobject(r"C:\Users\Administrator\Desktop\伊丽莎白二世和一世的关系\新建文件夹2\img13").scale(a).next_to(img1_9, DOWN)
        img1_14 = ImageMobject(r"C:\Users\Administrator\Desktop\伊丽莎白二世和一世的关系\新建文件夹2\img14").scale(a).next_to(img1_10, DOWN)
        img1_15 = ImageMobject(r"C:\Users\Administrator\Desktop\伊丽莎白二世和一世的关系\新建文件夹2\img15").scale(a).next_to(img1_11, DOWN)
        img1_16 = ImageMobject(r"C:\Users\Administrator\Desktop\伊丽莎白二世和一世的关系\新建文件夹2\img16").scale(a).next_to(img1_12, DOWN)
        
        self.play(
            ApplyMethod(img1.shift, LEFT*3.8), 
            ApplyMethod(img1_supplement.shift, LEFT*3.8), 
            FadeInFromDown(Group(
                img1_1, img1_2, img1_3, img1_4, 
                img1_5, img1_6, img1_7, img1_8, 
                img1_9, img1_10, img1_11, img1_12, 
                img1_13, img1_14, img1_15, img1_16)), 
            run_time=2, 
            )
        self.wait(5)
        
        img2 = ImageMobject(r"C:\Users\Administrator\Desktop\伊丽莎白二世和一世的关系\新建文件夹\img2")\
            .scale(1).next_to(img1, RIGHT/2, aligned_edge=UP).shift(RIGHT+DOWN*0.2)
        img2_supplement = Text("丹麦女王玛格丽特二世", font='未署名的信').scale(0.3).set_stroke(width=2)\
            .set_color('#F08080').next_to(img2, DOWN)
        
        img3 = ImageMobject(r"C:\Users\Administrator\Desktop\伊丽莎白二世和一世的关系\新建文件夹\img3")\
            .scale(1).next_to(img2, RIGHT, aligned_edge=UP).shift(RIGHT*2.5)
        img3_supplement = Text("挪威国王哈罗德五世", font='未署名的信').scale(0.3).set_stroke(width=2)\
            .set_color('#F08080').next_to(img3, DOWN)
        
        img4 = ImageMobject(r"C:\Users\Administrator\Desktop\伊丽莎白二世和一世的关系\新建文件夹\img4")\
            .scale(1).next_to(img2_supplement, DOWN, aligned_edge=UP)
        img4_supplement = Text("西班牙前国王胡安·卡洛斯一世", font='未署名的信').scale(0.3).set_stroke(width=2)\
            .set_color('#F08080').next_to(img4, DOWN)

        img5 = ImageMobject(r"C:\Users\Administrator\Desktop\伊丽莎白二世和一世的关系\新建文件夹\img5")\
            .scale(1).next_to(img3_supplement, DOWN, aligned_edge=UP)
        img5_supplement = Text("瑞典国王卡尔十六世·古斯塔夫", font='未署名的信').scale(0.3).set_stroke(width=2)\
            .set_color('#F08080').next_to(img5, DOWN)
        
        self.play(
            FadeOutAndShiftDown(Group(
                img1_1, img1_2, img1_3, img1_4, 
                img1_5, img1_6, img1_7, img1_8, 
                img1_9, img1_10, img1_11, img1_12, 
                img1_13, img1_14, img1_15, img1_16)), 
            FadeInFromDown(img2), 
            WriteRandom(img2_supplement), 
            FadeInFromDown(img3), 
            WriteRandom(img3_supplement), 
            FadeInFromDown(img4), 
            WriteRandom(img4_supplement), 
            FadeInFromDown(img5), 
            WriteRandom(img5_supplement), 
            run_time=3, 
            )
        self.wait(5)
        

        img6 = ImageMobject(r"C:\Users\Administrator\Desktop\伊丽莎白二世和一世的关系\新建文件夹\img6")\
            .scale(2.5).next_to(img1, RIGHT, aligned_edge=UP).shift(RIGHT*3)
        img6_supplement = Text("比利时前国王阿尔贝二世", font='未署名的信').scale(0.4).set_stroke(width=2)\
            .set_color('#F08080').next_to(img6, DOWN)
        
        self.play(
            FadeOutAndShiftDown(img2), 
            FadeOutRandom(img2_supplement), 
            FadeOutAndShiftDown(img3), 
            FadeOutRandom(img3_supplement), 
            FadeOutAndShiftDown(img4), 
            FadeOutRandom(img4_supplement), 
            FadeOutAndShiftDown(img5), 
            FadeOutRandom(img5_supplement), 
            FadeInFromDown(img6), 
            WriteRandom(img6_supplement), 
            run_time=2, 
        )
        self.wait(5)
        
        img7 = ImageMobject(r"C:\Users\Administrator\Desktop\伊丽莎白二世和一世的关系\新建文件夹\img7").scale(2.5).shift(UP*0.6)
        img7_supplement = Text("伊丽莎白一世", font='未署名的信')\
            .scale(0.5).set_stroke(width=2).set_color('#00CDCD').next_to(img7, DOWN)
        
        self.play(
            FadeOutAndShiftDown(img1), 
            FadeOutFromRandom(img1_supplement), 
            FadeOutAndShiftDown(img6), 
            FadeOutFromRandom(img6_supplement), 
            FadeInFromDown(img7), 
            WriteRandom(img7_supplement), 
            run_time=2, 
        )
        self.wait(5)
        self.play(
            FadeOutAndShiftDown(img7), 
            FadeOutFromRandom(img7_supplement), 
            )
        self.wait(3)

class Elizabeth_scene2(Scene):
    def construct(self):
        
        subtitle_bg = Polygon(LEFT*9+DOWN*2.5,RIGHT*9+DOWN*2.5,RIGHT*9+DOWN*6,LEFT*9+DOWN*6).set_color(BLACK).set_stroke(width=0).set_opacity(1)
        subtitle_bg.plot_depth=3
        self.add(subtitle_bg)
        

        get_arrow = lambda:VGroup(
            VGroup(
                Arrow(LEFT+UP,UP,max_tip_length_to_length_ratio=0.25,buff=0), 
                Line(LEFT+UP,LEFT+DOWN), 
                Line(LEFT+DOWN,DOWN), 
                ).set_color('#F4A460'), 
            VGroup(
                Arrow(LEFT+UP,UP,max_tip_length_to_length_ratio=0.25,buff=0).set_stroke(width=12, opacity=0.3), 
                Line(LEFT+UP,LEFT+DOWN).set_stroke(width=12, opacity=0.3), 
                Line(LEFT+DOWN,DOWN).set_stroke(width=12, opacity=0.3), 
                ).set_color('#CDC5BF'), 
                )

        
        img1 = ImageMobject(r"C:\Users\Administrator\Desktop\伊丽莎白二世和一世的关系\新建文件夹\img1").scale(2)
        img1_supplement = Text("伊丽莎白一世", font='未署名的信')\
            .scale(0.5).set_stroke(width=2).set_color('#FFFF00').next_to(img1, RIGHT).add_updater(lambda a:a.next_to(img1, RIGHT))
        
        
        img8 = ImageMobject(r"C:\Users\Administrator\Desktop\伊丽莎白二世和一世的关系\新建文件夹\img8").scale(2).next_to(img1, UP)\
            .add_updater(lambda a:a.next_to(img1, UP))
        img8_supplement = Text("乔治六世", font='未署名的信')\
            .scale(0.5).set_stroke(width=2).set_color('#FFFF00').next_to(img8, RIGHT).add_updater(lambda a:a.next_to(img8, RIGHT))
        img8_arrow = get_arrow().next_to(img1, LEFT/3).shift(UP*2).add_updater(lambda a:a.next_to(img1, LEFT/3).shift(UP*2))
        img8_arrow_supplement = Text("父亲", font='未署名的信')\
            .scale(0.5).set_stroke(width=2).set_color('#8E8E8E').next_to(img8_arrow, LEFT/2).add_updater(lambda a:a.next_to(img8_arrow, LEFT/2))


        img9 = ImageMobject(r"C:\Users\Administrator\Desktop\伊丽莎白二世和一世的关系\新建文件夹\img9").scale(2).next_to(img8, UP)\
            .add_updater(lambda a:a.next_to(img8, UP))
        img9_supplement = Text("乔治五世", font='未署名的信')\
            .scale(0.5).set_stroke(width=2).set_color('#FFFF00').next_to(img9, RIGHT).add_updater(lambda a:a.next_to(img9, RIGHT))
        img9_arrow = get_arrow().next_to(img8, LEFT/3).shift(UP*2).add_updater(lambda a:a.next_to(img8, LEFT/3).shift(UP*2))
        img9_arrow_supplement = Text("父亲", font='未署名的信')\
            .scale(0.5).set_stroke(width=2).set_color('#8E8E8E').next_to(img9_arrow, LEFT/2).add_updater(lambda a:a.next_to(img9_arrow, LEFT/2))


        img10 = ImageMobject(r"C:\Users\Administrator\Desktop\伊丽莎白二世和一世的关系\新建文件夹\img10").scale(2).next_to(img9, UP)\
            .add_updater(lambda a:a.next_to(img9, UP))
        img10_supplement = Text("爱德华七世", font='未署名的信')\
            .scale(0.5).set_stroke(width=2).set_color('#FFFF00').next_to(img10, RIGHT).add_updater(lambda a:a.next_to(img10, RIGHT))
        img10_arrow = get_arrow().next_to(img9, LEFT/3).shift(UP*2).add_updater(lambda a:a.next_to(img9, LEFT/3).shift(UP*2))
        img10_arrow_supplement = Text("父亲", font='未署名的信')\
            .scale(0.5).set_stroke(width=2).set_color('#8E8E8E').next_to(img10_arrow, LEFT/2).add_updater(lambda a:a.next_to(img10_arrow, LEFT/2))


        img11 = ImageMobject(r"C:\Users\Administrator\Desktop\伊丽莎白二世和一世的关系\新建文件夹\img11").scale(2).next_to(img10, UP)\
            .add_updater(lambda a:a.next_to(img10, UP))
        img11_supplement = Text("维多利亚女王", font='未署名的信')\
            .scale(0.5).set_stroke(width=2).set_color('#FFFF00').next_to(img11, RIGHT).add_updater(lambda a:a.next_to(img11, RIGHT))
        img11_arrow = get_arrow().next_to(img10, LEFT/3).shift(UP*2).add_updater(lambda a:a.next_to(img10, LEFT/3).shift(UP*2))
        img11_arrow_supplement = Text("母亲", font='未署名的信')\
            .scale(0.5).set_stroke(width=2).set_color('#8E8E8E').next_to(img11_arrow, LEFT/2).add_updater(lambda a:a.next_to(img11_arrow, LEFT/2))


        img12 = ImageMobject(r"C:\Users\Administrator\Desktop\伊丽莎白二世和一世的关系\新建文件夹\img12").scale(2).next_to(img11, UP)\
            .add_updater(lambda a:a.next_to(img11, UP))
        img12_supplement = Text("爱德华王子", font='未署名的信')\
            .scale(0.5).set_stroke(width=2).set_color('#FFFF00').next_to(img12, RIGHT).add_updater(lambda a:a.next_to(img12, RIGHT))
        img12_arrow = get_arrow().next_to(img11, LEFT/3).shift(UP*2).add_updater(lambda a:a.next_to(img11, LEFT/3).shift(UP*2))
        img12_arrow_supplement = Text("父亲", font='未署名的信')\
            .scale(0.5).set_stroke(width=2).set_color('#8E8E8E').next_to(img12_arrow, LEFT/2).add_updater(lambda a:a.next_to(img12_arrow, LEFT/2))


        img13 = ImageMobject(r"C:\Users\Administrator\Desktop\伊丽莎白二世和一世的关系\新建文件夹\img13").scale(2).next_to(img12, UP)\
            .add_updater(lambda a:a.next_to(img12, UP))
        img13_supplement = Text("乔治三世", font='未署名的信')\
            .scale(0.5).set_stroke(width=2).set_color('#FFFF00').next_to(img13, RIGHT).add_updater(lambda a:a.next_to(img13, RIGHT))
        img13_arrow = get_arrow().next_to(img12, LEFT/3).shift(UP*2).add_updater(lambda a:a.next_to(img12, LEFT/3).shift(UP*2))
        img13_arrow_supplement = Text("父亲", font='未署名的信')\
            .scale(0.5).set_stroke(width=2).set_color('#8E8E8E').next_to(img13_arrow, LEFT/2).add_updater(lambda a:a.next_to(img13_arrow, LEFT/2))


        img14 = ImageMobject(r"C:\Users\Administrator\Desktop\伊丽莎白二世和一世的关系\新建文件夹\img14").scale(2).next_to(img13, UP)\
            .add_updater(lambda a:a.next_to(img13, UP))
        img14_supplement = Text("弗雷德里克王子", font='未署名的信')\
            .scale(0.5).set_stroke(width=2).set_color('#FFFF00').next_to(img14, RIGHT).add_updater(lambda a:a.next_to(img14, RIGHT))
        img14_arrow = get_arrow().next_to(img13, LEFT/3).shift(UP*2).add_updater(lambda a:a.next_to(img13, LEFT/3).shift(UP*2))
        img14_arrow_supplement = Text("父亲", font='未署名的信')\
            .scale(0.5).set_stroke(width=2).set_color('#8E8E8E').next_to(img14_arrow, LEFT/2).add_updater(lambda a:a.next_to(img14_arrow, LEFT/2))


        img15 = ImageMobject(r"C:\Users\Administrator\Desktop\伊丽莎白二世和一世的关系\新建文件夹\img15").scale(2).next_to(img14, UP)\
            .add_updater(lambda a:a.next_to(img14, UP))
        img15_supplement = Text("乔治二世", font='未署名的信')\
            .scale(0.5).set_stroke(width=2).set_color('#FFFF00').next_to(img15, RIGHT).add_updater(lambda a:a.next_to(img15, RIGHT))
        img15_arrow = get_arrow().next_to(img14, LEFT/3).shift(UP*2).add_updater(lambda a:a.next_to(img14, LEFT/3).shift(UP*2))
        img15_arrow_supplement = Text("父亲", font='未署名的信')\
            .scale(0.5).set_stroke(width=2).set_color('#8E8E8E').next_to(img15_arrow, LEFT/2).add_updater(lambda a:a.next_to(img15_arrow, LEFT/2))


        img16 = ImageMobject(r"C:\Users\Administrator\Desktop\伊丽莎白二世和一世的关系\新建文件夹\img16").scale(2).next_to(img15, UP)\
            .add_updater(lambda a:a.next_to(img15, UP))
        img16_supplement = Text("乔治一世", font='未署名的信')\
            .scale(0.5).set_stroke(width=2).set_color('#FFFF00').next_to(img16, RIGHT).add_updater(lambda a:a.next_to(img16, RIGHT))
        img16_arrow = get_arrow().next_to(img15, LEFT/3).shift(UP*2).add_updater(lambda a:a.next_to(img15, LEFT/3).shift(UP*2))
        img16_arrow_supplement = Text("父亲", font='未署名的信')\
            .scale(0.5).set_stroke(width=2).set_color('#8E8E8E').next_to(img16_arrow, LEFT/2).add_updater(lambda a:a.next_to(img16_arrow, LEFT/2))


        img17 = ImageMobject(r"C:\Users\Administrator\Desktop\伊丽莎白二世和一世的关系\新建文件夹\img17").scale(2).next_to(img16, UP)\
            .add_updater(lambda a:a.next_to(img16, UP))
        img17_supplement = Text("汉诺威的索菲娅", font='未署名的信')\
            .scale(0.5).set_stroke(width=2).set_color('#FFFF00').next_to(img17, RIGHT).add_updater(lambda a:a.next_to(img17, RIGHT))
        img17_arrow = get_arrow().next_to(img16, LEFT/3).shift(UP*2).add_updater(lambda a:a.next_to(img16, LEFT/3).shift(UP*2))
        img17_arrow_supplement = Text("母亲", font='未署名的信')\
            .scale(0.5).set_stroke(width=2).set_color('#8E8E8E').next_to(img17_arrow, LEFT/2).add_updater(lambda a:a.next_to(img17_arrow, LEFT/2))


        img18 = ImageMobject(r"C:\Users\Administrator\Desktop\伊丽莎白二世和一世的关系\新建文件夹\img18").scale(2).next_to(img17, UP)\
            .add_updater(lambda a:a.next_to(img17, UP))
        img18_supplement = Text("伊丽莎白·斯图亚特", font='未署名的信')\
            .scale(0.5).set_stroke(width=2).set_color('#FFFF00').next_to(img18, RIGHT).add_updater(lambda a:a.next_to(img18, RIGHT))
        img18_arrow = get_arrow().next_to(img17, LEFT/3).shift(UP*2).add_updater(lambda a:a.next_to(img17, LEFT/3).shift(UP*2))
        img18_arrow_supplement = Text("母亲", font='未署名的信')\
            .scale(0.5).set_stroke(width=2).set_color('#8E8E8E').next_to(img18_arrow, LEFT/2).add_updater(lambda a:a.next_to(img18_arrow, LEFT/2))


        img19 = ImageMobject(r"C:\Users\Administrator\Desktop\伊丽莎白二世和一世的关系\新建文件夹\img19").scale(2).next_to(img18, UP)\
            .add_updater(lambda a:a.next_to(img18, UP))
        img19_supplement = Text("詹姆士一世", font='未署名的信')\
            .scale(0.5).set_stroke(width=2).set_color('#FFFF00').next_to(img19, RIGHT).add_updater(lambda a:a.next_to(img19, RIGHT))
        img19_arrow = get_arrow().next_to(img18, LEFT/3).shift(UP*2).add_updater(lambda a:a.next_to(img18, LEFT/3).shift(UP*2))
        img19_arrow_supplement = Text("父亲", font='未署名的信')\
            .scale(0.5).set_stroke(width=2).set_color('#8E8E8E').next_to(img19_arrow, LEFT/2).add_updater(lambda a:a.next_to(img19_arrow, LEFT/2))


        img20 = ImageMobject(r"C:\Users\Administrator\Desktop\伊丽莎白二世和一世的关系\新建文件夹\img20").scale(2).next_to(img19, UP)\
            .add_updater(lambda a:a.next_to(img19, UP))
        img20_supplement = Text("玛丽一世", font='未署名的信')\
            .scale(0.5).set_stroke(width=2).set_color('#FFFF00').next_to(img20, RIGHT).add_updater(lambda a:a.next_to(img20, RIGHT))
        img20_arrow = get_arrow().next_to(img19, LEFT/3).shift(UP*2).add_updater(lambda a:a.next_to(img19, LEFT/3).shift(UP*2))
        img20_arrow_supplement = Text("母亲", font='未署名的信')\
            .scale(0.5).set_stroke(width=2).set_color('#8E8E8E').next_to(img20_arrow, LEFT/2).add_updater(lambda a:a.next_to(img20_arrow, LEFT/2))


        img21 = ImageMobject(r"C:\Users\Administrator\Desktop\伊丽莎白二世和一世的关系\新建文件夹\img21").scale(2).next_to(img20, UP)\
            .add_updater(lambda a:a.next_to(img20, UP))
        img21_supplement = Text("詹姆士五世", font='未署名的信')\
            .scale(0.5).set_stroke(width=2).set_color('#FFFF00').next_to(img21, RIGHT).add_updater(lambda a:a.next_to(img21, RIGHT))
        img21_arrow = get_arrow().next_to(img20, LEFT/3).shift(UP*2).add_updater(lambda a:a.next_to(img20, LEFT/3).shift(UP*2))
        img21_arrow_supplement = Text("父亲", font='未署名的信')\
            .scale(0.5).set_stroke(width=2).set_color('#8E8E8E').next_to(img21_arrow, LEFT/2).add_updater(lambda a:a.next_to(img21_arrow, LEFT/2))


        img22 = ImageMobject(r"C:\Users\Administrator\Desktop\伊丽莎白二世和一世的关系\新建文件夹\img22").scale(2).next_to(img21, UP)\
            .add_updater(lambda a:a.next_to(img21, UP))
        img22_supplement = Text("玛格丽特·都铎", font='未署名的信')\
            .scale(0.5).set_stroke(width=2).set_color('#FFFF00').next_to(img22, RIGHT).add_updater(lambda a:a.next_to(img22, RIGHT))
        img22_arrow = get_arrow().next_to(img21, LEFT/3).shift(UP*2).add_updater(lambda a:a.next_to(img21, LEFT/3).shift(UP*2))
        img22_arrow_supplement = Text("母亲", font='未署名的信')\
            .scale(0.5).set_stroke(width=2).set_color('#8E8E8E').next_to(img22_arrow, LEFT/2).add_updater(lambda a:a.next_to(img22_arrow, LEFT/2))


        img23 = ImageMobject(r"C:\Users\Administrator\Desktop\伊丽莎白二世和一世的关系\新建文件夹\img23").scale(2).next_to(img22, UP)\
            .add_updater(lambda a:a.next_to(img22, UP))
        img23_supplement = Text("亨利七世", font='未署名的信')\
            .scale(0.5).set_stroke(width=2).set_color('#FFFF00').next_to(img23, RIGHT).add_updater(lambda a:a.next_to(img23, RIGHT))
        img23_arrow = get_arrow().next_to(img22, LEFT/3).shift(UP*2).add_updater(lambda a:a.next_to(img22, LEFT/3).shift(UP*2))
        img23_arrow_supplement = Text("父亲", font='未署名的信')\
            .scale(0.5).set_stroke(width=2).set_color('#8E8E8E').next_to(img23_arrow, LEFT/2).add_updater(lambda a:a.next_to(img23_arrow, LEFT/2))


        img24 = ImageMobject(r"C:\Users\Administrator\Desktop\伊丽莎白二世和一世的关系\新建文件夹\img24").scale(2).next_to(img23, UP)\
            .add_updater(lambda a:a.next_to(img23, UP))
        img24_supplement = Text("亨利八世", font='未署名的信')\
            .scale(0.5).set_stroke(width=2).set_color('#FFFF00').next_to(img24, RIGHT).add_updater(lambda a:a.next_to(img24, RIGHT))
        img24_arrow = get_arrow().next_to(img23, LEFT/3).shift(UP*2).add_updater(lambda a:a.next_to(img23, LEFT/3).shift(UP*2))
        img24_arrow_supplement = Text("次子", font='未署名的信')\
            .scale(0.5).set_stroke(width=2).set_color('#8E8E8E').next_to(img24_arrow, LEFT/2).add_updater(lambda a:a.next_to(img24_arrow, LEFT/2))


        img7 = ImageMobject(r"C:\Users\Administrator\Desktop\伊丽莎白二世和一世的关系\新建文件夹\img7").scale(2).next_to(img24, UP)\
            .add_updater(lambda a:a.next_to(img24, UP))
        img7_supplement = Text("伊丽莎白一世", font='未署名的信')\
            .scale(0.5).set_stroke(width=2).set_color('#FFFF00').next_to(img7, RIGHT).add_updater(lambda a:a.next_to(img7, RIGHT))
        img7_arrow = get_arrow().next_to(img24, LEFT/3).shift(UP*2).add_updater(lambda a:a.next_to(img24, LEFT/3).shift(UP*2))
        img7_arrow_supplement = Text("女儿", font='未署名的信')\
            .scale(0.5).set_stroke(width=2).set_color('#8E8E8E').next_to(img7_arrow, LEFT/2).add_updater(lambda a:a.next_to(img7_arrow, LEFT/2))



        self.add(
            img1, img1_supplement, 
            img8, img8_supplement, img8_arrow, img8_arrow_supplement, 
            img9, img9_supplement, img9_arrow, img9_arrow_supplement, 
            img10, img10_supplement, img10_arrow, img10_arrow_supplement, 
            img11, img11_supplement, img11_arrow, img11_arrow_supplement, 
            img12, img12_supplement, img12_arrow, img12_arrow_supplement, 
            img13, img13_supplement, img13_arrow, img13_arrow_supplement, 
            img14, img14_supplement, img14_arrow, img14_arrow_supplement, 
            img15, img15_supplement, img15_arrow, img15_arrow_supplement, 
            img16, img16_supplement, img16_arrow, img16_arrow_supplement, 
            img17, img17_supplement, img17_arrow, img17_arrow_supplement, 
            img18, img18_supplement, img18_arrow, img18_arrow_supplement, 
            img19, img19_supplement, img19_arrow, img19_arrow_supplement, 
            img20, img20_supplement, img20_arrow, img20_arrow_supplement, 
            img21, img21_supplement, img21_arrow, img21_arrow_supplement, 
            img22, img22_supplement, img22_arrow, img22_arrow_supplement, 
            img23, img23_supplement, img23_arrow, img23_arrow_supplement, 
            img24, img24_supplement, img24_arrow, img24_arrow_supplement, 
            img7, img7_supplement, img7_arrow, img7_arrow_supplement, 
            )
        
        for i in range(18):
            self.play(ApplyMethod(img1.shift, DOWN*4.23),run_time=2)
            self.wait(4)
        
        self.wait()
