from os import system
from manim import *
import math
from manim import *

class CoordsToPointExample(Scene):
    def construct(self):
        ax = Axes().add_coordinates()

        # a dot with respect to the axes
        dot_axes = Dot(ax.coords_to_point(2, 2), color=GREEN)
        lines = ax.get_lines_to_point(ax.c2p(2,2))

        # a dot with respect to the scene
        # the default plane corresponds to the coordinates of the scene.
        plane = NumberPlane()
        dot_scene = Dot((2,2,0), color=RED)
        self.play(Create(ax))
        self.wait(1)
        self.add(plane, dot_scene, ax, dot_axes, lines)
        self.wait(1)


class AnimatedAxes(Scene):
    def construct(self):
        # 创建一个坐标轴对象
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-3, 3, 1],
            axis_config={"color": BLUE}
        )

        # 创建坐标轴的动画效果
        self.play(Create(axes))  # 坐标轴出现的动画

        # 暂停一会儿
        self.wait(1)

        # 渐隐坐标轴的动画效果
        self.play(Uncreate(axes))


class GrowingAxes(Scene):
    def construct(self):
        # 创建一个坐标轴对象
        axes = Axes(
            x_range=[-10, 11,1],
            y_range=[-10, 11,1],
            axis_config={"color": BLUE,"include_numbers": True}
        )
        # 将坐标轴的箭头部分逐渐出现
        graph = ImplicitFunction(
            lambda x, y: y ** 2 - x ** 3 - x - 6,
            color=RED
        )
        axes.add(graph)
        self.add(axes)

class GetVerticalLinesToGraph(Scene):
    def construct(self):
        ax = Axes(
            axis_config={"font_size": 24},
        ).add_coordinates()

        curve = ax.plot(lambda x:x)

        lines = ax.get_vertical_lines_to_graph(
            curve, x_range=[0, 4], num_lines=30, color=BLUE
        )
        self.play(Create(ax))
        self.wait(1)
        self.play(Create(curve))
        self.wait(1)
        self.play(Create(lines))
        self.wait(2)


class PlotCurve(Scene):
    def construct(self):
        # 定义参数方程
        def parametric_function(t):
            x = t
            y = np.sqrt(t**3 + t + 6)
            return np.array([x, y, 0])

        # 创建曲线对象
        curve = ParametricFunction(parametric_function, t_range=[-3, 3], color=BLUE)

        self.add(curve)
class TwoDotsDiff(Scene):
    def construct(self):
        # text 椭圆曲线上的加法
        axes=Axes(
            x_range=(-10,10,1),
            y_range=(-8,8,1),
            x_axis_config = {"include_numbers": True},
            x_length=10,
            y_length=10,

        )
        graph=axes.plot_implicit_curve(
            lambda x,y:y**2-x**3-x-2,
            color=RED
        )
        #

        dotA=Dot(axes.coords_to_point(-1,0),color=WHITE)

        dotB=Dot(axes.coords_to_point(1,2),color=GREEN)
        # 在a点和b点画条直线 不是线段我的意思是超过ab的直线
        dotC=Dot(axes.coords_to_point(1,-2),color=PINK)
        lineAB=Line(dotA,dotB,buff=4,color=BLUE).set_length(5)
        # 虚线BC
        lineBC=DashedLine(dotB,dotC,color=BLUE).set_length(5)


        A_dot = Text("A(-1,0)",color=WHITE).next_to(dotA,LEFT,UP).scale(0.5)
        B_dot = Text("B(1,2)",color=GREEN).next_to(dotB,UP).scale(0.5)
        C_dot = Text("C(1,-2)",color=PINK).next_to(dotC,RIGHT).scale(0.5)
        msg1=Text("椭圆曲线E上的加法")
        msg2=Text("DotA+DotB=DotC")
        self.play(Write(msg1))
        self.play(msg1.animate.shift(UP*3).scale(0.5))
        self.play(FadeOut(msg1))
        self.play(Create(axes))
        self.wait(1)
        self.play(Create(graph),run_time=2)
        self.wait(1)
        fun=MathTex(r" y^2 = x^3 + x + 2 ").shift(UP*3).shift(RIGHT*3)
        self.play(Write(fun))
        self.wait(1)
        self.play(msg2.animate.shift(UP*3).scale(0.5))
        self.play(msg2.animate.shift(LEFT*3))
        self.play(Create(dotA),Create(dotB))
        self.wait(1)
        self.play(Create(lineAB))
        self.wait(1)
        self.play(Write(A_dot),Write(B_dot))
        self.wait(1)
        self.play(Create(lineBC))
        self.wait(1)
        self.play(Create(dotC))
        self.wait(1)
        self.play(Write(C_dot))
        self.wait(1)
        self.play(FadeOut(msg2))
        self.play(Create(Text("This is C ,the result A+B",color=GREEN).next_to(dotC,RIGHT).scale(0.5)))
        self.play(FadeOut(A_dot),FadeOut(B_dot),FadeOut(C_dot))
        self.wait(1)
        # self.add(axes,graph,dotA,A_dot,dotB,B_dot,lineAB,dotC,C_dot,lineBC)

class TwoDotsSame(Scene):
    def construct(self):
        Text("椭圆曲线E(1,1)23")
        axes=Axes(
            x_range=(-10,10,1),
            y_range=(-8,8,1),
            # axis_config = {"include_numbers": True},
            x_length=10,
            y_length=10,

        )
        graph=axes.plot_implicit_curve(
            lambda x,y:y**2-x**3-x-2,
            color=RED
        )
        #
        # 以k为斜率过b点的直线
        k=(3*1**2+1)/(2*2)
        print(k)
        print(math.atan(k))
        line=Line(axes.coords_to_point(1,2,),color=BLUE,).set_angle(math.atan(k)).set_length(5)
        dotA=Dot(axes.coords_to_point(-1,0.5),color=WHITE)
        dotC=Dot(axes.coords_to_point(-1,-0.5),color=PINK)

        dotB=Dot(axes.coords_to_point(1,2),color=GREEN)
        lineac=Line(dotA,dotC,color=WHITE).set_length(5)
        A=Text("A",color=WHITE).next_to(dotA,LEFT).scale(0.5)
        C=Text("C",color=PINK).next_to(dotC,DOWN).scale(0.5)
        B=Text("B",color=GREEN).next_to(dotB,RIGHT).scale(0.5)
        self.add(axes,graph,dotA,dotB,dotC,A,B,C,line,lineac)

class CoordsToPointExample(Scene):
    def construct(self):
        ax = Axes().add_coordinates()

        # a dot with respect to the axes
        dot_axes = Dot(ax.coords_to_point(2, 2), color=GREEN)
        lines = ax.get_lines_to_point(ax.c2p(2,2))

        # a dot with respect to the scene
        # the default plane corresponds to the coordinates of the scene.
        # plane = NumberPlane()
        dot_scene = Dot((2,2,1), color=RED)

        self.add(dot_scene, ax, dot_axes, lines)
if __name__ == "__main__":
    scence=TwoDotsDiff()
    scence.render(True)
    # system("manim -pql SM2.py TwoDotsDiff")