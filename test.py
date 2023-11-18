from os import system
from manim import *

class ExampleFunctionGraph(Scene):
    def construct(self):
        cos_func = FunctionGraph(
            lambda t: np.cos(t) + 0.5 * np.cos(7 * t) + (1 / 7) * np.cos(14 * t),
            color=RED,
        )

        self.play(Create(cos_func))
if __name__ == "__main__":
    # 设置 Manim 配置参数
    # 运行我们的场景类，并将生成的动画保存到视频中
    scene = FunctionGraphAnimation()
    scene.render()
    # system("manim -pql test.py ExampleFunctionGraph")