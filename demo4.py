from manim import *

class CognitiveEnhancementAnimation(Scene):
    def construct(self):
        # Title
        title = Text("Enhancing Cognitive Abilities", font_size=48).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Introductory text
        intro_text = Text("Enhancing cognitive abilities improves mental processes and performance.",
                          font_size=28).next_to(title, DOWN)
        self.play(Write(intro_text))
        self.wait(2)

        # Technique 1: Mind Mapping
        mind_mapping_text = Text("1. Mind Mapping", font_size=28).to_edge(LEFT)
        self.play(Write(mind_mapping_text))
        self.wait(1)

        # Mind mapping example
        mind_map = VGroup(
            Circle(radius=1, color=BLUE, fill_opacity=0.5).shift(LEFT),
            Triangle(color=BLUE).next_to(mind_mapping_text, DOWN, buff=1),
            Ellipse(width=1.5, height=1, color=BLUE).shift(RIGHT)
        )
        self.play(Create(mind_map))
        self.wait(2)

        mind_mapping_example = Text("Mind maps organize thoughts visually and aid in brainstorming.",
                                    font_size=24).next_to(mind_mapping_text, DOWN)
        self.play(Write(mind_mapping_example))
        self.wait(2)

        # Technique 2: Memory Techniques
        memory_text = Text("2. Memory Techniques", font_size=28).next_to(mind_mapping_example, DOWN)
        self.play(Write(memory_text))
        self.wait(1)

        # Memory techniques example
        memory_palace = VGroup(
            Rectangle(width=2, height=1, color=GREEN, fill_opacity=0.5).shift(LEFT * 1.5),
            Circle(radius=0.5, color=GREEN).next_to(memory_text, DOWN, buff=1),
            Polygon(np.array([0, 0, 1]), np.array([1, 0.5, 1]), np.array([0, 1, 1]), color=GREEN).shift(RIGHT * 1.5)
        )
        self.play(Create(memory_palace))
        self.wait(2)

        memory_example = Text("Memory techniques like mnemonics enhance retention and recall.",
                              font_size=24).next_to(memory_text, DOWN)
        self.play(Write(memory_example))
        self.wait(2)

        # Technique 3: Problem-solving Strategies
        problem_solving_text = Text("3. Problem-solving Strategies", font_size=28).next_to(memory_example, DOWN)
        self.play(Write(problem_solving_text))
        self.wait(1)

        # Problem-solving strategies example
        problem_solving = VGroup(
            RegularPolygon(n=5, color=ORANGE, fill_opacity=0.5).shift(LEFT * 2),
            Square(color=ORANGE).next_to(problem_solving_text, DOWN, buff=1),
            RegularPolygon(n=3, color=ORANGE).shift(RIGHT * 2)
        )
        self.play(Create(problem_solving))
        self.wait(2)

        problem_solving_example = Text("Strategies such as breaking down problems improve analytical skills.",
                                       font_size=24).next_to(problem_solving_text, DOWN)
        self.play(Write(problem_solving_example))
        self.wait(2)

        # Conclusion
        conclusion_text = Text("Enhancing cognitive abilities leads to better learning and productivity.",
                               font_size=28).to_edge(DOWN)
        self.play(Write(conclusion_text))
        self.wait(3)

        # Fade out all elements
        self.play(
            FadeOut(title),
            FadeOut(intro_text),
            FadeOut(mind_mapping_text),
            FadeOut(mind_mapping_example),
            FadeOut(memory_text),
            FadeOut(memory_example),
            FadeOut(problem_solving_text),
            FadeOut(problem_solving_example),
            FadeOut(conclusion_text),
            FadeOut(mind_map),
            FadeOut(memory_palace),
            FadeOut(problem_solving)
        )
class ContinuousMotion(Scene):
    def construct(self):
        func = lambda pos: np.sin(pos[0] / 2) * UR + np.cos(pos[1] / 2) * LEFT
        stream_lines = StreamLines(func, stroke_width=2, max_anchors_per_line=30)
        self.add(stream_lines)
        stream_lines.start_animation(warm_up=False, flow_speed=1.5)
        self.wait(stream_lines.virtual_time / stream_lines.flow_speed)
class UnionExample(Scene):
    def construct(self):
        sq = Square(color=RED, fill_opacity=1).move_to([-2, 0, 0])
        self.play(Create(sq))
        cr = Circle(color=BLUE, fill_opacity=1).move_to([-1.3, 0.7, 0])
        self.play(Create(cr))
        un = Union(sq, cr, color=GREEN, fill_opacity=1).move_to([1.5, 0.3, 0])
        self.play(Create(un))
        self.add(sq, cr, un)
if __name__ == "__main__":
    from os import system

    system("manim -pql demo4.py UnionExample")
