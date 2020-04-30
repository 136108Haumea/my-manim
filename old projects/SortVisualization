from manimlib.imports import *
import math


class quick_sort_visualization(Scene):
    CONFIG = {
        "amount":300,
        "interval":0.3,
    }
    def construct(self):
        np.random.seed(int(time.time()))

        lower_height,upper_height = 100000,3000000
        sort_amount = self.amount

        My_colors = color_gradient(['#8B5742','#FFA500','#FFE1FF','#7D26CD'],sort_amount)
        random_height = [
            np.random.randint(lower_height,upper_height)/upper_height*6\
                for i in range(sort_amount)
            ]
        rectag_width = 12/sort_amount#-0.05
        random_height_copy = random_height.copy()
        random_height_copy.sort()

        array = [
            Rectangle(height = random_height[i], width = rectag_width).set_stroke(width=0)\
                .set_fill(opacity=1,color=My_colors[random_height_copy.index(random_height[i])])\
                .move_to(6*LEFT+(i+0.5)*12/sort_amount*RIGHT).align_to(3*DOWN,DOWN)\
                    for i in range(sort_amount)
            ]

        self.add(VGroup(*array))

        def partion(list,p,r):
        	i=p-1
        	for j in range(p,r):
        		if list[j]<=list[r]:
        			i+=1
        			list[i],list[j]=list[j],list[i]
        	list[i+1],list[r]=list[r],list[i+1]
        	return i

        def quicksort(list,p,r):
            if p<r:
                q=partion(list,p,r)
                n = (-6+(p)*12/sort_amount)*RIGHT
                m = (-6+(r+1)*12/sort_amount)*RIGHT
                rect = Polygon(n+DOWN*3,m+DOWN*3,m+UP*3.5,n+UP*3.5,stroke_width=0,fill_color='#878787',fill_opacity=0.3,plot_depth=-1)
                self.add(rect)
                self.play(
                    *[
                        ApplyMethod(
                            array[i].move_to, 
                            [-6+(list.index(array[i].get_height())+0.5)*12/sort_amount, array[i].get_center()[1], 0], 
                        ) for i in range(sort_amount)
                    ], rate_func=rush_into, run_time=self.interval)
                self.mobjects.remove(rect)
                #self.mobjects.pop(0)

                quicksort(list,p,q)
                quicksort(list,q+1,r)

        quicksort(random_height,0,sort_amount-1)
        self.wait(3)


class merge_sort_visualization(Scene):
    CONFIG = {
        "amount":300,
        "interval":0.3,
    }
    def construct(self):
        np.random.seed(int(time.time()))

        lower_height,upper_height = 100000,3000000
        sort_amount = self.amount

        My_colors = color_gradient(['#8B5742','#FFA500','#FFE1FF','#7D26CD'],sort_amount)
        random_height = [
            np.random.randint(lower_height,upper_height)/upper_height*6\
                for i in range(sort_amount)
            ]
        rectag_width = 12/sort_amount#-0.05
        random_height_copy = random_height.copy()
        random_height_copy.sort()

        array = [
            Rectangle(height = random_height[i], width = rectag_width).set_stroke(width=0)\
                .set_fill(opacity=1,color=My_colors[random_height_copy.index(random_height[i])])\
                .move_to(6*LEFT+(i+0.5)*12/sort_amount*RIGHT).align_to(3*DOWN,DOWN)\
                    for i in range(sort_amount)
            ]

        self.add(VGroup(*array))


        def merge(arr, l, m, r): 
            n1 = m - l + 1
            n2 = r- m 

            L = [0] * (n1)
            R = [0] * (n2)

            for i in range(0 , n1): 
                L[i] = arr[l + i] 

            for j in range(0 , n2): 
                R[j] = arr[m + 1 + j] 

            i,j,k = 0,0,1

            while i < n1 and j < n2 : 
                if L[i] <= R[j]: 
                    arr[k] = L[i] 
                    i += 1
                else: 
                    arr[k] = R[j] 
                    j += 1
                k += 1

            while i < n1: 
                arr[k] = L[i] 
                i += 1
                k += 1

            while j < n2: 
                arr[k] = R[j] 
                j += 1
                k += 1

            n = (-6+(l)*12/sort_amount)*RIGHT
            m = (-6+(r+1)*12/sort_amount)*RIGHT
            rect = Polygon(n+DOWN*3,m+DOWN*3,m+UP*3.5,n+UP*3.5,stroke_width=0,fill_color='#878787',fill_opacity=0.3,plot_depth=-1)
            self.add(rect)
            self.play(
                *[
                    ApplyMethod(
                        array[i].move_to, 
                        [-6+(arr.index(array[i].get_height())+0.5)*12/sort_amount, array[i].get_center()[1], 0], 
                    ) for i in range(sort_amount)
                ], rate_func=rush_into, run_time=self.interval)
            self.mobjects.remove(rect)
            #self.mobjects.pop(0)
  
        def mergeSort(arr,l,r): 
            if l < r: 
                m = int((l+(r-1))/2)
                mergeSort(arr, l, m) 
                mergeSort(arr, m+1, r)
                merge(arr, l, m, r) 

        mergeSort(random_height,0,len(random_height)-1)
        self.wait(3)


class bubble_sort_visualization(Scene):
    CONFIG = {
        "amount":50,
        "interval":0.333,
        "rect_distance":0.05,
    }
    def construct(self):
        np.random.seed(int(time.time()))

        lower_height,upper_height = 100000,3000000
        sort_amount = self.amount

        My_colors = color_gradient(['#8B5742','#FFA500','#FFE1FF','#7D26CD'],sort_amount)
        random_height = [
            np.random.randint(lower_height,upper_height)/upper_height*6\
                for i in range(sort_amount)
            ]
        rectag_width = 12/sort_amount-self.rect_distance
        random_height_copy = random_height.copy()
        random_height_copy.sort()

        array = [
            Rectangle(height = random_height[i], width = rectag_width).set_stroke(width=0)\
                .set_fill(opacity=1,color=My_colors[random_height_copy.index(random_height[i])])\
                .move_to(6*LEFT+(i+0.5)*12/sort_amount*RIGHT).align_to(3*DOWN,DOWN)\
                    for i in range(sort_amount)
            ]

        #self.play(ShowCreation(VGroup(*array)))
        self.add(VGroup(*array))

        for i in range(len(array)-1):
            mark=0
            for j in range(i+1,len(array)):
                n1 = (-6+(i)*12/sort_amount)*RIGHT
                m1 = (-6+(i+1)*12/sort_amount)*RIGHT
                rect1 = Polygon(n1+DOWN*3,m1+DOWN*3,m1+UP*3.5,n1+UP*3.5,stroke_width=0,fill_color='#878787',fill_opacity=0.3,plot_depth=-1)
                n2 = (-6+(j)*12/sort_amount)*RIGHT
                m2 = (-6+(j+1)*12/sort_amount)*RIGHT
                rect2 = Polygon(n2+DOWN*3,m2+DOWN*3,m2+UP*3.5,n2+UP*3.5,stroke_width=0,fill_color='#878787',fill_opacity=0.3,plot_depth=-1)
                self.add(rect1,rect2)
                if array[i].get_height()>array[j].get_height():
                    self.play(
                        array[i].move_to,[array[j].get_center()[0],array[i].get_center()[1],0],
                        array[j].move_to,[array[i].get_center()[0],array[j].get_center()[1],0],
                        rate_func=smooth,
                        run_time=self.interval,
                    )
                    array[i],array[j] = array[j],array[i]
                    mark=1
                self.wait(0.5)
                self.mobjects.remove(rect1)
                self.mobjects.remove(rect2)
                #self.mobjects.pop(0)
                #self.mobjects.pop(0)
            if mark==0:
                break
        
        self.wait(3)
