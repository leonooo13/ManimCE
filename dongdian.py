from manim import *


class DongDian1(Scene):
    """
    视频制作，懂点概率论
    """
    def construct(self):
        self.machine_learning()

    def machine_learning(self):
        """
        机器学习和人工智能相关视频
        :return:
        """
        title = Text("梯度下降算法").scale(1.2)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # 画一个简单的二次曲线
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[0, 10, 2],
            axis_config={"include_tip": False}
        )
        graph = axes.plot(lambda x: x ** 2, color=BLUE)
        self.play(Create(axes), Create(graph))
        self.wait(1)

        # 梯度下降点的初始位置
        point = Dot(axes.coords_to_point(2.5, 2.5 ** 2), color=RED)
        self.play(FadeIn(point))
        self.wait(1)

        # 演示梯度下降
        for i in range(10):
            new_point = Dot(axes.coords_to_point(2.5 - 0.1 * i, (2.5 - 0.1 * i) ** 2), color=RED)
            self.play(Transform(point, new_point), run_time=0.5)
            self.wait(0.5)


if __name__ == "__main__":
    config.quality = "low_quality"
    config.verbosity = "INFO"
    scene = DongDian1()
    scene.render(True)
