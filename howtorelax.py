from os import system

from manim import *


class AnxietySolution(Scene):
    def construct(self):
        # Title
        title = Text("如何解决焦虑", font_size=72, color=BLUE)
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))

        # Identifying Anxiety
        anxiety_text = Text("焦虑", font_size=48, color=RED)
        anxiety_circle = Circle(color=RED, fill_opacity=0.5).surround(anxiety_text)
        self.play(Write(anxiety_text), Create(anxiety_circle))

        identify_text = Text("识别焦虑", font_size=36, color=WHITE).to_edge(DOWN)
        self.play(Write(identify_text))
        self.wait(2)
        self.play(FadeOut(anxiety_text), FadeOut(anxiety_circle), FadeOut(identify_text))

        # Breathing Exercise
        breathe_in = Text("吸气", font_size=48, color=GREEN)
        breathe_out = Text("呼气", font_size=48, color=GREEN)
        breathe_circle = Circle(color=GREEN, fill_opacity=0.5)

        breathe_text = Text("呼吸练习", font_size=36, color=WHITE).to_edge(DOWN)
        self.play(Transform(anxiety_circle, breathe_circle))
        self.play(Write(breathe_text))
        self.wait(1)

        self.play(Write(breathe_in))
        self.play(breathe_circle.animate.scale(1.5), run_time=2)
        self.play(FadeOut(breathe_in))

        self.play(Write(breathe_out))
        self.play(breathe_circle.animate.scale(1 / 1.5), run_time=2)
        self.play(FadeOut(breathe_out))

        self.wait(1)
        self.play(FadeOut(breathe_text))

        # Positive Affirmations
        affirmations = [
            "我很平静",
            "我能掌控局面",
            "我很坚强",
            "我很有能力"
        ]
        affirm_text = Text("积极肯定", font_size=36, color=WHITE).to_edge(DOWN)
        self.play(Write(affirm_text))

        for affirmation in affirmations:
            text = Text(affirmation, font_size=48, color=YELLOW)
            self.play(Write(text))
            self.wait(1)
            self.play(FadeOut(text))

        self.play(FadeOut(affirm_text))

        # Mindfulness Exercise
        mindfulness_text = Text("正念练习", font_size=48, color=PURPLE)
        serene_landscape = Rectangle(color=BLUE, height=3, width=4, fill_opacity=0.5)
        serene_text = Text("冥想和放松", font_size=36, color=WHITE).to_edge(DOWN)

        self.play(Write(mindfulness_text))
        self.play(FadeOut(mindfulness_text), Create(serene_landscape))
        self.play(Write(serene_text))

        self.wait(2)
        self.play(FadeOut(serene_landscape), FadeOut(serene_text))


if __name__ == "__main__":
    system("manim -pql howtorelax.py AnxietySolution")