from manim import *


class AvoidWastingTime(Scene):
    def construct(self):
        # Title
        title = Text("如何度过历史垃圾时间", font_size=48)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))

        # Definition of Wasting Time
        definition = Text("什么是历史垃圾时间？", font_size=36)
        self.play(Write(definition))
        self.wait(1)
        self.play(definition.animate.to_edge(UP))

        definition_text = Text(
            "历史垃圾时间是指那些低效或没有产出的时间段。\n例如：无目的的刷手机、发呆等。",
            font_size=24
        )
        self.play(Write(definition_text))
        self.wait(3)
        self.play(FadeOut(definition_text))

        # Why Avoid It
        importance = Text("为什么要避免历史垃圾时间？", font_size=36)
        self.play(Write(importance))
        self.wait(1)
        self.play(importance.animate.to_edge(UP))

        importance_text = Text(
            "避免历史垃圾时间可以提高效率、增加产出，\n并且有助于实现个人目标。",
            font_size=24
        )
        self.play(Write(importance_text))
        self.wait(3)
        self.play(FadeOut(importance_text))

        # How to Avoid It
        how_to_avoid = Text("如何避免历史垃圾时间？", font_size=36)
        self.play(Write(how_to_avoid))
        self.wait(1)
        self.play(how_to_avoid.animate.to_edge(UP))

        tips = [
            "1. 制定明确的计划和目标。",
            "2. 使用时间管理工具，如番茄工作法。",
            "3. 保持专注，减少分心。",
            "4. 定期反思，调整策略。"
        ]

        for tip in tips:
            tip_text = Text(tip, font_size=24)
            self.play(Write(tip_text))
            self.wait(2)
            self.play(FadeOut(tip_text))

        # Ending
        ending = Text("让我们一起高效利用时间！", font_size=36)
        self.play(Write(ending))
        self.wait(2)


# 保存代码为 draw_person.py 然后运行以下命令
# manim -pql draw_person.py DrawPerson

class Movie1(Scene):
    def construct(self):
        self.rainfull()
        self.drawline()
        # self.huahua()
        self.draw_person()
        self.what_is_waste()
        self.suggestions()
    def huahua(self):
        func = lambda pos: np.sin(pos[0] / 2) * UR + np.cos(pos[1] / 2) * LEFT
        stream_lines = StreamLines(func, stroke_width=2, max_anchors_per_line=30)
        self.add(stream_lines)
        stream_lines.start_animation(warm_up=False, flow_speed=1.5)
        self.wait(stream_lines.virtual_time / stream_lines.flow_speed)
    def rainfull(self):
        func = lambda pos: np.array([pos[0], pos[1] - 1, 0])

    # 创建雨滴效果
        raindrops = StreamLines(func, stroke_width=1, max_anchors_per_line=100)

        # 将雨滴效果添加到场景中
        self.add(raindrops)
        raindrops.start_animation(warm_up=False, flow_speed=1.5)

        # 等待片刻
        self.wait(raindrops.virtual_time / raindrops.flow_speed)

    def drawline(self):
        line = Line(start=3 * LEFT, end=3 * RIGHT)
        self.play(Create(line))
        FadeOut(self.play(line.animate.move_to(UP * 3)))
        text1 = Text("How to spend wasted time", color=BLUE)
        self.play(Write(text1))
        self.wait(1)
        self.play(text1.animate.scale(0.5).move_to(UP * 3.2))
        self.wait(1)
        self.play(Uncreate(text1))
        self.wait(1)

    def draw_person(self):
        head = Circle(radius=0.5, color=WHITE).move_to(UP * 2.5)

        # 创建身体
        body = Line(start=UP * 2, end=DOWN * 1, color=BLUE)  # 蓝色

        # 创建左臂
        left_arm = Line(start=UP * 1.5 + LEFT * 0.5, end=UP * 0.5 + LEFT * 1.5, color=RED)  # 红色

        # 创建右臂
        right_arm = Line(start=UP * 1.5 + RIGHT * 0.5, end=UP * 0.5 + RIGHT * 1.5, color=RED)  # 红色

        # 创建左腿
        left_leg = Line(start=DOWN * 1, end=DOWN * 2 + LEFT * 1, color=GREEN)  # 绿色

        # 创建右腿
        right_leg = Line(start=DOWN * 1, end=DOWN * 2 + RIGHT * 1, color=GREEN)  # 绿色

        # 创建棍子，位于右手
        stick = Line(start=UP * 0.5 + RIGHT * 1.5, end=UP * 2 + RIGHT * 2, color=WHITE)  # 白色，调整位置

        # 将所有部分组合在一起
        person = VGroup(head, body, left_arm, right_arm, left_leg, right_leg, stick)

        # 在场景中绘制整个组合图形
        self.play(Create(person))
        self.wait(1)

        # 缩小并移动整个组合图形
        self.play(person.animate.scale(0.5).move_to(RIGHT * 5 + DOWN * 2))
        self.wait(1)

    def what_is_waste(self):
        what_list = [
            "1. Ordinary people can no longer receive rewards through hard work.",

            "2. Follow the rules, being a good person no longer has a future.",

            "3. The law no longer protects ordinary people"
        ]
        for tip in what_list:
            tip_text = Text(tip, font_size=24)
            self.play(Write(tip_text))
            self.wait(2)
            self.play(tip_text.animate.scale(0.5).move_to(RIGHT * 4))
            self.play(FadeOut(tip_text))
    def suggestions(self):
        tips = [
            "1. Maintain a pessimistic view towards society, but remain optimistic about yourself.",

            "2. Either accumulate capital, experience, and connections during wasted time.",

            "3. Or explore, discuss, and live in places without wasted time.",

            "4. It's important not to let the tragedies of the era become your own tragedy."
        ]

        for tip in tips:
            tip_text = Text(tip, font_size=24)
            self.play(Write(tip_text))
            self.wait(2)
            self.play(tip_text.animate.scale(0.5).move_to(DOWN * 3))
            self.play(FadeOut(tip_text))


if __name__ == "__main__":
    from os import system

    system("manim -pqh demo5.py Movie1")
