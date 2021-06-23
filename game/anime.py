from manim import *
from math import *
import numpy as np
from re import I, T
from manim_fonts import *
from typing import Literal


class dd(Scene):
    def construct(self):
        
        t1 = Text("Do you know about various tricks which are given by Vedic Maths?")
        t2 = Text("We are going to learn about one of the basic rules of vedic maths. This involves multiplication of two digit numbers.")
        t3 = Text("Say you have any two digit numbers : ab and cd, where a is in tenth place of number \"ab\" and b is in ones place, similarly for \"cd\".")
        t7 = Text("So the trick is to take the ones digit of both numbers and multiply it (i.e. b x d) and write the ones digit of their product as the ones digit of a new number. And carry forward the tens place digit.")
        l1 = Line(np.array([0,0,0]),np.array([-2.5,2.5,0]))     

        t1.surround(Rectangle(height=2.6,width=6))
        t2.surround(Rectangle(height=2,width=6))
        t3.surround(Rectangle(height=2,width=6))
        t7.surround(Rectangle(height=2,width=6))
        self.play(FadeIn(t1.scale(2).align_on_border(UP),rate_func=smooth),run_time=2)
        self.wait(2)
        self.play(FadeOut(t1))
        self.play(Write(t2.scale(2)),run_time=4)
        self.play(t2.animate().scale(0.6).shift((UP+LEFT)*3+UP/2))
        self.play(Write(t3.scale(2)),run_time=4)
        self.play(t3.animate().scale(0.6).shift((LEFT)*3+UP*3))
        self.play(Write(t7.scale(2).shift(DOWN)))
        self.play(t7.animate().scale(0.6).shift((LEFT)*3+UP*3.5))
        self.wait()
        #self.play(FadeOutAndShift(VGroup(t2,t3,t7),DOWN*2))
        
        t4=Text("Now take the following problem where we have to multiply 39 and 78", color=BLUE_D)
        t5 = Text(
            "39"
        )
        t6 = Text(
            "78"
        )
        t8 = Text("x")
        t9 = Text(
            "9 x 8 = 72"
        )
        t10 = Text(
            "3 x 8 = 24",
            color=PINK
        )
        t11 = Text(
            "9 x 7 = 63",
            color=PINK
        )
        t12 = Text("_______")
        t13 = Text("2",color=GREEN)

        t4.surround(Rectangle(height=2,width=5))
        self.play(Write(t4.scale(1.5)),run_time=2.5)
        self.play(t4.animate().shift(LEFT*2.5+UP*2).scale(1))
        self.play(Write(t5.scale(1.5)),Write(t6.scale(1.5).shift(DOWN)),Write(t8.scale(1.5).shift(DOWN+LEFT)),Write(t12.shift(DOWN*1.5)))

        t6.set_color_by_t2c(t2c={"8":GREEN,"7":BLUE})
        t5.set_color_by_t2c(t2c={"9":GREEN,"3":BLUE})
        t9.set_color(GREEN)

        t14 = Text("63 + 24 + 7 = 94",color=PINK)
        t15 = Text("4",color=PINK)
        t16 = Text("3 x 7 = 21",color=BLUE)
        t17 = Text("21 + 9 = 30",color=BLUE)
        t18 = Text("30",color=BLUE)

        rect1 = Rectangle(height=1, width=3, color=ORANGE)
        rect2 = Rectangle(height=2, width=3.2, color=ORANGE)
        rect = Rectangle(height=1, width=3.2, color=ORANGE)
        rect3 = Rectangle(height=1.5, width=3, color=ORANGE)
        t9.surround(rect1)
        ts = VGroup(t10,t11,t14)
        ts.surround(rect2)
        ts2 = VGroup(t16,t17)
        ts2.surround(rect3)

        self.wait(2)
        
        self.play(
            t5.animate().scale(1).shift(LEFT*3+UP),
            t6.animate().scale(1).shift(LEFT*3+UP),
            t8.animate().scale(1).shift(LEFT*3+UP),
            t9.animate().scale(0.7).shift(UP*2.2+RIGHT*4.5),
            t12.animate().scale(1).shift(LEFT*3+UP),
            t13.animate().scale(1.2).shift(LEFT*3+DOWN*2+RIGHT/3+UP)
        )
        self.play(ShowCreation(rect.shift(UP*2.2+RIGHT*4.5)))
        self.wait(2.7)

        self.play(
            t10.animate().scale(0.7).shift(RIGHT),
            t11.animate().scale(0.7).shift(RIGHT+DOWN/2),
            t14.animate().scale(0.7).shift(RIGHT+DOWN),
            t15.animate().scale(1.2).shift(LEFT*3.5+DOWN*2+RIGHT/3+UP)
        )
        self.play(ShowCreation(rect2.shift(RIGHT+DOWN/2)))
        self.wait(2.7)

        self.play(
            t16.animate().scale(0.7).shift(RIGHT*4.2),
            t17.animate().scale(0.7).shift(RIGHT*4.2+DOWN/2),
            t18.animate().scale(1.2).shift(LEFT*4+DOWN*2+UP)
        )
        self.play(ShowCreation(rect3.shift(RIGHT*4.2+DOWN/3)))



class elev(Scene):
    def construct(self):
        
        t1 = Text("Do you know about various tricks which are given by Vedic Maths?")
        t2 = Text("We will learn about the a trick to ease our calculations when we multiply any number by n-digit number having 1s only (like 11, 1111, or any other such number), for instance 423 times 11.")
        t3 = Text("Let us see how,")

        t1.surround(Rectangle(height=2.6,width=6))
        t2.surround(Rectangle(height=2,width=6))
        t3.surround(Rectangle(height=2,width=6))
        #t7.surround(Rectangle(height=2,width=6))
        self.play(FadeIn(t1.scale(2).align_on_border(UP),rate_func=smooth),run_time=2)
        self.wait(2)
        self.play(FadeOut(t1))
        self.play(Write(t2.scale(2)),run_time=4)
        self.wait(3)
        self.play(FadeOut(t2))
        
        self.play(Write(t3.scale(1.9)),run_time=4)
        self.play(t3.animate().scale(0.7).shift((LEFT)*3+UP*3))
        #self.play(Write(t7.scale(2).shift(DOWN)))
        #self.play(t7.animate().scale(0.6).shift((LEFT)*3+UP*3.5))
        self.wait()
        #self.play(FadeOutAndShift(VGroup(t2,t3,t7),DOWN*2))
        
        t7 = Text("First multiply 3 and 1 and write it down.")
        #t4=Text("Now take the following problem where we have to multiply 423 and 78", color=BLUE_D)
        t5 = Text(
            "4223"
        )
        t6 = Text(
            "111"
        )
        t8 = Text(
            "2 + 3 = 5",
            color=GREEN
            )
        t9 = Text(
            "3 x 1 = 3",
            color=BLUE
        )
        t10 = Text(
            "2 + 2 + 3 = 7",
            color=RED
        )
        t20 = Text(
            "2 + 4 = 6",
            color=TEAL_D
        )
        t21 = Text(
            "4 x 1 = 4",
            color=GREY_BROWN
        )
        t11 = Text(
            "2 + 2 + 4 = 8",
            color=PINK
        )
        t111 = Text("x")
        t12 = Text("_________")
        t13 = Text("3",color=BLUE)
        t14 = Text("5",color=GREEN)
        t15 = Text("7", color=RED)
        t16 = Text("8",color=PINK)
        t17 = Text("6",color=TEAL_D)
        t18 = Text("4",color=GREY_BROWN)

        t7.surround(Rectangle(height=2,width=5))
        self.play(Write(t7.scale(1.6)),run_time=2.5)
        self.play(t7.animate().shift(LEFT*2.3+UP*2).scale(1))
        self.play(Write(t5.scale(1.5)),Write(t6.scale(1.5).shift(DOWN)),Write(t111.scale(1.5).shift(DOWN+LEFT)),Write(t12.shift(DOWN*1.5)))

        rect1 = Rectangle(height=1, width=3, color=ORANGE)
        rect2 = Rectangle(height=2, width=3, color=ORANGE)
        rect = Rectangle(height=1, width=3, color=ORANGE)
        rect3 = Rectangle(height=1.5, width=3, color=ORANGE)
        #t9.surround(rect1)
        #ts = VGroup(t10,t11,t14)
        #ts.surround(rect2)
        #ts2 = VGroup(t16,t17)
        #ts2.surround(rect3)

        self.wait(2)
        
        self.play(
            t5.animate().scale(1).shift(LEFT*3+UP),
            t6.animate().scale(1).shift(LEFT*3+UP),
            t111.animate().scale(1).shift(LEFT*3+UP),
            t9.animate().scale(0.7).shift(UP*2.2+RIGHT*4.5),
            t12.animate().scale(1).shift(LEFT*3+UP+LEFT/3),
            t13.animate().scale(1.2).shift(LEFT*3+DOWN*2+RIGHT/3+UP)
        )
        self.play(Create(rect.surround(t9, buff=0.2)))
        self.wait(3)
#done

        self.play(
            t8.animate().scale(0.7).shift(RIGHT),
            t10.animate().scale(0.7).shift(RIGHT+DOWN),
            t15.animate().scale(1.2).shift(LEFT*3.6+DOWN*2+UP),
            t14.animate().scale(1.2).shift(LEFT*3.5+DOWN*2+RIGHT/3+UP)
        )
        self.play(Create(rect.surround(t8,buff=0)))
        self.play(Create(rect.surround(t10,buff=0)))
        self.wait(3)

        self.play(
            t11.animate().scale(0.7).shift(RIGHT*4.2),
            t16.animate().scale(1.2).shift(LEFT*4+DOWN*2+UP)
        )
        self.play(Create(rect.surround(t11,buff=0.1)))
        self.wait(3)

        self.play(
            t20.animate().scale(0.7).shift(RIGHT*4.2+DOWN/1.4),
            t17.animate().scale(1.2).shift(LEFT*4+DOWN*2+UP+LEFT/2.5)
        )
        self.play(Create(rect.surround(t20,buff=0.1)))
        self.wait(3)

        self.play(
            t21.animate().scale(0.7).shift(RIGHT*4.2+DOWN*1.7),
            t18.animate().scale(1.2).shift(LEFT*4+DOWN*2+UP+LEFT/1.2)
        )
        self.play(Create(rect.surround(t21,buff=0)))
        self.play(Uncreate(rect))
        self.wait()


"""
        t9,t13
        t8,t14
        t10,t15
        t11,t16
        t20,t17
        t21,t18
"""

class multi(Scene):
    def construct(self):
        a = Text("Multiplication is one of the elementary operations of mathematics.",color=BLUE_D)
        a.surround(Rectangle(height=5,width=6))
        self.play(Write(a.scale(2)),run_time=4.5)
        self.play(FadeOut(a))

        a1 = Text(
            "Multiplication involves the repeated addition of elements."
        )
        a2 = Text("Say you want to find the sum --> 4 + 4 + 4 + 4 + 4 + 4 = 24")
        a3 = Text("This sum looks rather simple and you might be able to find the sum normally; however, if the sum becomes too large it becomes more and more difficult.")
        a2.surround(Rectangle())
        a3.surround(Rectangle(height=5))
        self.play(Write(a2.scale(2)),run_time=3)
        self.play(a2.animate().shift(UP*3).scale(1))
        self.wait(2)
        self.play(Write(a3.scale(2)),run_time=3)
        self.play(a3.animate().shift(UP*2).scale(1.5))
        self.wait(2.5)
        self.play(FadeOut(a2),FadeOut(a3))

        a4 = Text("We usually write this sum in the following way:")
        a5 = Text("4 x 6 = 24")
        a4.surround(Rectangle(width=2.5))
        a5.surround(Rectangle(height=1))
        self.play(
            a4.animate().scale(1.5).shift(UP*3),
            a5.animate().scale(0.5).shift(UP*2)
        )

        a6 = Text("Consider a farmer who grows 4 plants each day. He needs to find the number of plants he has grown after a 6 days.")
        a6.surround(Rectangle())
        a6.scale(2)
        ss = VGroup()
        for i in range(6):
            for j in range(4):
                s = Square(0.4,fill_opacity=1,color=PURPLE_D)
                ss.add(s)
        ss.arrange_in_grid(buff=0.12)
        ss.shift(DOWN*1.6+LEFT*3)
        self.play(Write(a6.shift(LEFT+UP)))
        self.play(Write(ss))
        self.wait()

        a7 = Text("4",color=RED)
        ss1 = VGroup(*[Square(0.4,fill_opacity=1,color=RED_C) for _ in range(4)])
        ss1.arrange(buff=0.1)

        a8 = Text("6",color=PINK)
        ss2 = VGroup(*[Square(0.4,fill_opacity=1,color=PINK) for _ in range(6)])
        ss2.arrange(buff=0.1)

        r = Brace(ss,LEFT)
        ra = Brace(ss,UP)
        lol = MathTex("4")
        lol1 = MathTex("6")
        self.add(r)
        self.add(ra)
        self.play(Write(lol.shift(DOWN*1.6+LEFT*3+UP*2.3)))
        self.play(Write(lol1.shift(DOWN*1.6+LEFT*3+LEFT*2)))
        self.play(
            ss1.animate().shift(RIGHT*2),
            a7.animate().shift(RIGHT*4),
            ss2.animate().shift(RIGHT*2+DOWN),
            a8.animate().shift(RIGHT*4+DOWN),
        )

        a9 = Text("= 24")
        a10 = Text("4 x 6 = 24")
        self.play(
            Write(a9.shift(DOWN*1.6+LEFT*3+RIGHT*1.75)),
            Write(a10.shift(RIGHT*2+DOWN*2.3))
        )
        self.wait()
        self.play(FadeOut(a5),FadeOut(a4),FadeOut(a6))
        x = VGroup(ss,ss1,ss2,a9,a10,r,ra,a8,a7,lol,lol1)
        self.play(
            x.animate().shift(UP*2.5)
        )

        a11 = Text("Thus, rather than writing 4 + 4 ... 6 times the farmer can multiply and write it as 4 x 6. First we need to remember these results which are obtained from the so called \"multiplication tables\"")
        a11.surround(Rectangle(width=6))
        a11.scale(2)
        self.play(Write(a11.shift(DOWN*1.7)),run_time=3.5)
        self.wait(8)


class div(Scene):
    def construct(self):
        m = Text("Suppose its your birthday and you're on your way to the local market to get a bunch of chocolates. Each pack of chocolates has 24 chocolates in it. Say you have 12 friends and you have to give 4 chocolates to each friend. How will you figure out the number of packs to buy in this case.")
        m1 = Text("You see that 24 - 4 - 4 - 4 - 4 - 4 - 4 = 0")
        m2 = Text("So one pack of chocolates will be enough for 6 of your friends. Therefore you need to get 2 packs.")
        m3 = Text("This approch of repeated multiplication is extremely tedious and for large numbers you would be pulling your hair out in no time, so to say.")
        
        m.surround(Rectangle(hieght=2,width=6))
        m1.surround(Rectangle(hieght=2,width=6))
        m2.surround(Rectangle(hieght=2,width=6))
        m3.surround(Rectangle(hieght=2,width=6))

        m.scale(2)
        m2.scale(2)
        m3.scale(2)

        m.set_color(GREEN_D)
        self.play(Write(m),run_time=4)
        self.play(m.animate().shift(UP*3.4))
        self.wait()

        m1.set_color(GREEN_E)
        self.play(Write(m1),run_time=3)
        self.play(m1.animate().shift(UP*2.3))

        m2.set_color(GREEN_E)
        self.play(Write(m2),run_time=6)
        self.play(m2.animate().shift(UP*1.6))
        self.wait()

        m3.set_color(GREEN_E)
        self.play(Write(m3),run_time=5)
        self.play(m3.animate().shift(UP*0.5))
        self.wait(3)
        self.play(FadeOut(VGroup(m,m1,m2,m3)))

        choco = VGroup(*[Rectangle(height=0.6,width=0.3,fill_opacity=1,color=LIGHT_BROWN) for _ in range(4)])
        choco2 = choco.copy()
        choco3 = choco.copy()
        choco4 = choco.copy()
        choco5 = choco.copy()
        choco6 = choco.copy()

        fr1 = Text("Friend 1")
        fr2 = Text("Friend 2")
        fr3 = Text("Friend 3")
        fr4 = Text("Friend 4")
        fr5 = Text("Friend 5")
        fr6 = Text("Friend 6")

        VGroup(fr1,fr2,fr3,fr4,fr5,fr6).set_color(RED_E)

        oo = Text("Let's say you distribute 24 chocolates among 6 friends. This is how you would do it.")

        oo.scale(0.4)
        self.play(FadeIn(oo))
        self.wait()
        self.play(FadeOut(oo))
        self.wait()

        self.play(
            fr1.animate().shift(3*(UP+LEFT)+LEFT*2),
            fr2.animate().shift(3*UP),
            fr3.animate().shift(3*(UP+RIGHT)+RIGHT*2),
            fr4.animate().shift(3*(DOWN+RIGHT)+RIGHT*2),
            fr5.animate().shift(3*DOWN),
            fr6.animate().shift(3*(DOWN+LEFT)+LEFT*2)
        )
        self.wait()

        choco.arrange_in_grid(buff=0.2)
        self.play(Write(choco))
        self.play(choco.animate().shift(1.5*(UP+LEFT)+LEFT*3.5))

        choco2.arrange_in_grid(buff=0.2)
        self.play(Write(choco2))
        self.play(choco2.animate().shift(1.5*(UP)))

        choco3.arrange_in_grid(buff=0.2)
        self.play(Write(choco3))
        self.play(choco3.animate().shift(1.5*(UP+RIGHT)+RIGHT*3.5))

        choco4.arrange_in_grid(buff=0.2)
        self.play(Write(choco4))
        self.play(choco4.animate().shift(1.5*(DOWN+LEFT)+LEFT*3.5))

        choco5.arrange_in_grid(buff=0.2)
        self.play(Write(choco5))
        self.play(choco5.animate().shift(1.5*(DOWN)))

        choco6.arrange_in_grid(buff=0.2)
        self.play(Write(choco6))
        self.play(choco6.animate().shift(1.5*(DOWN+RIGHT)+RIGHT*3.5))


        self.wait(2)
        self.play(FadeOut(VGroup(fr1,fr2,fr3,fr4,fr5,fr6,choco,choco2,choco3,choco4,choco5,choco6)))

        n = Text("How would you do this in a simpler way?")
        self.play(Write(n))
        self.wait(3)
        self.play(FadeOut(n))

        n1 = Text("For this we use an operation called division, which is basically repeated subtraction or reverse multiplication.")
        n2 = Text("In order to distribute 24 chocolates among 6 friends we divide the number 24 by 6.")
        n3 = MathTex(
            "\\frac{24}{4}",
        )
        n4 = MathTex(
            "\\frac{6 \\times 4}{4}"
        )
        n5 = MathTex(
            "= 6"
        )

        #n1.surround(Rectangle(width=5,height=5))
        #n2.surround(Rectangle(width=5,height=5))
        n1.scale(0.5)
        n2.scale(0.5)
        self.wait()
        self.play(Write(n1.shift(UP)),Write(n2))
        self.wait(2.5)
        self.play(FadeOut(VGroup(n1,n2)))
        self.play(Write(n3.scale(2).shift(UP*2)))
        self.play(Write(n4.scale(2)))
        self.wait(2.6)
        self.play(Transform(n4,n5.scale(2)))


        oof = Text("Therefore, you've found out the easy way that 24 chocolates can be distributed among 6 friends getting 4 chocolates each.")
        oof.scale(0.5)
        self.play(Write(oof.shift(DOWN*2)))

class sqr5(Scene):
    def construct(self):
        a = Text("Now we will learn about a very simple and extremely helpful trick to reduce your calculations.")
        #a.surround(Rectangle(height=8))
        a.scale(0.5)
        self.play(Write(a))
        self.wait()
        self.play(FadeOut(a))

        a2 = Text("This involves finding out the squares of 2 digit numbers ending with the digit 5")
        a2.surround(Rectangle(height=10,width=10))
        a2.scale(1)
        self.play(Write(a2))
        self.wait()
        self.play(FadeOut(a2))
        self.wait()
        c = Text("I will be taking 85 x 85 as an example")
        self.play(FadeIn(c))
        self.play(FadeOut(c))

        a3 = Text("STEP - 1")
        a4 = Text("STEP - 2")
        a5 = Text("Simply write down the square of 5 i.e. 25 at the right most position as done below:")
        a6 = Text(
            "85"
        )
        a7 = a6.copy()
        a8 = Text("____")
        a9 = Text("25")
        a10 = Text("72")
        a11 = MathTex(
            "5^{2} = 25",
            color=RED_E
        )

        self.wait()
        self.play(Write(a3.scale(3)))
        self.wait()
        self.play(FadeOut(a3))
        self.play(Write(a5.scale(0.5)))

        a6.scale(1.75)
        a7.scale(1.75)
        a8.scale(1.75)
        a9.scale(1.75)
        a10.scale(1.75)
        a11.scale(1.75)

        self.play(
            a5.animate().shift(UP*3)
        )
        self.wait()
        self.play(
            a6.animate().shift(LEFT*3),
            a7.animate().shift(LEFT*3+DOWN),
            a11.animate().shift(RIGHT*3+UP),
            a8.animate().shift(LEFT*3+DOWN*2),
        )
        self.play(ShowCreationThenDestruction(Rectangle(color=BLUE_D).surround(a11, buff=0.25)))
        a9.set_color(RED_E)
        self.wait()
        self.play(
            a9.animate().shift(LEFT*3+DOWN*3+RIGHT/1.5)
        )
        self.wait(4)

        self.play(FadeOut(a5))
        rofl = VGroup(a6,a7,a8,a9,a11)
        self.play(FadeOut(rofl))

        self.play(Write(a4.scale(3)))
        self.wait()
        self.play(FadeOut(a4))
        self.wait()

        z = Text("Multiply the tens digit of the number with its successor and write down the number obtained on the left of 25.")
        
        self.play(Write(z.scale(0.35)))
        self.play(z.animate().shift(UP*3))

        z2 = MathTex(
            "8 \\times {(8+1)} = 72",
            color=GREEN_E
        )

        self.play(
            FadeIn(
                rofl
            )
        )

        self.wait()
        z2.set_color(GREEN_E)
        a10.set_color(GREEN_E)
        self.play(
            z2.animate().shift(RIGHT*3+DOWN),
            a10.animate().shift(LEFT*4+DOWN*3+RIGHT/2),
        )
        self.play(ShowCreationThenDestruction(Rectangle(color=GREEN_E).surround(z2, buff=0.25)))

        no = VGroup(z2,a10,a6,a7,a8,a9,a11,z)

        d011011110110111001100101 = Text("And there you have it \"7225\".")
        s01101111011100100111001001111001 = Text("i.e. the square of 85.")

        self.wait(5)
        self.play(
            FadeOut(
                no
            )
        )

        self.play(Write(d011011110110111001100101.shift(UP)))
        self.play(Write(s01101111011100100111001001111001.shift(DOWN)))


class add(Scene):
    def construct(self):
        t = Text("We shall now learn the concept of addition and subtraction.")
        t2 = Text("Addition is basically the increment of objects.")
        btw = Text("And subtraction is the decrement of objects.")
        t.scale(0.5)
        self.play(Write(t))
        self.wait()
        self.play(FadeOut(t))
        self.play(Write(t2))
        self.play(FadeOut(t2))
        self.wait()
        self.play(Write(btw))
        self.wait()
        self.play(FadeOut(btw))

        a = Text("Say you have 1 ball and your friend has 3 balls.")
        b = Text("If your friend were to give 1 ball to you then you would have 2 balls")
        b.scale(0.65)
        c = Text("Because 1 + 1 = 2")
        r = Circle(radius=0.5,fill_opacity=1)
        r2 = r.copy()
        r3 = r.copy()
        r4 = r.copy()
        r5 = Text("YOU")
        r6 = Text("Friend")

        self.play(Write(a))
        self.wait()
        self.play(FadeOut(a))
        
        self.play(
            Write(b)
        )
        self.wait()
        self.play(FadeOut(b))
        self.play(Write(c))
        self.wait()
        self.play(FadeOut(c))

        self.play(Write(r5.shift(3*UP+LEFT*3)))
        self.play(Write(r6.shift(3*UP+RIGHT*3)))

        self.play(Write(r.shift(2*(UP+LEFT)+LEFT)))

        self.play(Write(r2.shift(2*(UP+RIGHT)+RIGHT)))

        self.play(Write(r3.shift(2*UP+RIGHT*1.5)))

        self.play(Write(r4.shift(2*UP+RIGHT*4.5)))

        xoxo = Text("After your friend gives you 1 ball--")

        self.play(Write(xoxo))
        self.wait()
        self.play(FadeOut(xoxo))

        self.play(
            r3.animate().shift(4*LEFT),
            r.animate().shift(LEFT)
        )
        d = Text("This is what we call addition.")
        self.play(Write(d))
        self.wait(2)
        self.play(FadeOut(d))

        d2 = Text("Now your friend originally had 3 balls but after giving one to you he got 2 balls")
        d2.scale(0.5)
        d3 = Text("3 - 1 = 2")

        self.play(Write(d2))
        self.play(Write(d3.shift(DOWN)))
        self.wait()
        self.play(FadeOut(d2))
        self.play(FadeOut(d3))

        marcus = r.copy()
        wrench = r2.copy()
        sitara = r3.copy()
        samljackson = r4.copy()

        ted = r5.copy()
        pewdiepie = r6.copy()

        self.play(Write(ted.shift(DOWN*3)),Write(pewdiepie.shift(DOWN*3)))
        self.wait()

        self.play(Write(marcus.shift(DOWN*4+RIGHT)))
        self.play(Write(sitara.shift(DOWN*4+4*RIGHT)))
        self.play(Write(wrench.shift(4*DOWN)))
        self.play(Write(samljackson.shift(4*DOWN)))

        self.wait()

        deadpool = Text("Again when your friend gives you a ball--")
        self.play(Write(deadpool.shift(UP*0.75)))
        self.play(FadeOut(deadpool))

        self.play(
            marcus.animate().shift(LEFT),
            sitara.animate().shift(4*LEFT)
        )
        self.wait()

        hahaha = VGroup(marcus,sitara,wrench,samljackson,ted,pewdiepie,r,r2,r3,r4,r5,r6)

        deltapsifi = Text("Thus we see that you experience addition")
        uh = Text("as 1 + 1 = 2")
        huh = Text("and your friend experiences subtraction")
        umm = Text("as 3 - 1 = 2")

        self.play(FadeOut(hahaha))

        self.play(Write(deltapsifi.shift(2*UP)))
        self.play(Write(uh.shift(UP)))
        self.play(Write(huh))
        self.play(Write(umm.shift(DOWN)))



class marcopolo(Scene):
    def construct(self):

        con = {
                "stroke_width" : 37,
                "color" : ORANGE,
            }

        lin = Line(start=UP+LEFT, end=UP+RIGHT*7, **con)

        with RegisterFont("Noto Sans") as fonts:
            a = Text("ग",font = fonts[0],color=ORANGE)
            a.scale(8)

            self.play(Write(a),run_time=2,rate_func=rush_into)
            self.wait()
            self.play(a.animate(run_time=2,rate_func=rate_functions.ease_in_sine).shift(LEFT*3.65))  
            self.wait()
        x = VGroup()
        with RegisterFont("Big Shoulders Stencil Display") as fonts:
            r = Text("anitansh",font=fonts[0])
            r.scale(2.8)

            r.set_color_by_t2c(t2c={'an' : ORANGE})
            r.set_color_by_t2c(t2c={'ita' : WHITE})
            r.set_color_by_t2c(t2c={'nsh' : GREEN})
            #r.scale(2)

            self.play(Write(r),run_time=2)
            self.play(Create(lin.shift(UP/2.2+LEFT+LEFT/4)))

