from manim import *


class BackgroundImageScene(Scene):
    def construct(self):
        # 加载背景图像
        background = ImageMobject("Big_Sur_Simple.png")

        # 调整图像大小和位置
        background.scale(2)
        background.shift(UP * 0.5)

        # 将图像添加到场景
        self.add(background)

        # 添加其他Mobject或动画
        text = Text("Hello, Manim!").scale(2)
        self.play(Write(text))
        self.wait(2)

    def show1(self):
        text = Text("dedfe")
        self.play(Create(text))


class BlockchainIntroduction1(Scene):
    def construct(self):
        # 标题
        title = Text("Introduction to Blockchain Technology").scale(0.8)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # 区块的示例
        block1 = Rectangle(width=3, height=2, color=BLUE)
        block2 = Rectangle(width=3, height=2, color=BLUE)
        block3 = Rectangle(width=3, height=2, color=BLUE)

        # 布局
        block1.shift(LEFT * 4)
        block2.next_to(block1, RIGHT, buff=1.5)
        block3.next_to(block2, RIGHT, buff=1.5)

        block1_text = Text("Block 1").scale(0.5).move_to(block1.get_center())
        block2_text = Text("Block 2").scale(0.5).move_to(block2.get_center())
        block3_text = Text("Block 3").scale(0.5).move_to(block3.get_center())

        # 添加区块和文本
        self.play(FadeIn(block1), Create(block1_text))
        self.play(FadeIn(block2), Create(block2_text))
        self.play(FadeIn(block3), Create(block3_text))
        self.wait(1)
        # 链接区块
        arrow1 = Arrow(start=block1.get_right(), end=block2.get_left(), buff=0.1)
        arrow2 = Arrow(start=block2.get_right(), end=block3.get_left(), buff=0.1)
        self.play(GrowArrow(arrow1), GrowArrow(arrow2))
        self.wait(1)

        # 介绍哈希值
        hash_text1 = Text("Hash: 000x123").scale(0.5).next_to(block1, DOWN)
        prev_hash_text2 = Text("Prev Hash: 000x123").scale(0.5).next_to(block2, UP)
        hash_text2 = Text("Hash: 000x456").scale(0.5).next_to(block2, DOWN)
        prev_hash_text3 = Text("Prev Hash: 000x456").scale(0.5).next_to(block3, UP)
        hash_text3 = Text("Hash: 000x789").scale(0.5).next_to(block3, DOWN)

        self.play(FadeIn(hash_text1))
        self.play(FadeIn(prev_hash_text2))
        self.play(FadeIn(hash_text2))
        self.play(FadeIn(prev_hash_text3))
        self.play(FadeIn(hash_text3))
        self.wait(1)
        self.play(FadeOut(hash_text1))
        self.play(FadeOut(prev_hash_text2), FadeOut(hash_text2))
        self.play(FadeOut(prev_hash_text3), FadeOut(hash_text3))

        # 工作量证明
        pow_title = Text("Proof of Work").scale(0.7)
        pow_title.to_edge(UP)
        self.play(Transform(title, pow_title))

        pow_text = Text("Miners solve complex problems to add blocks").scale(0.5).next_to(title, DOWN)
        self.play(FadeIn(pow_text))
        self.wait(1)

        # 示意矿工工作
        miner1 = Circle(color=YELLOW).shift(LEFT * 4 + DOWN * 2)
        miner2 = Circle(color=YELLOW).shift(RIGHT * 4 + DOWN * 2)
        self.play(FadeIn(miner1), FadeIn(miner2))
        pow_problem = Text("Solve: 2 + 2 = ?").scale(0.5).move_to(UP * 2)
        self.play(FadeIn(pow_problem))
        self.wait(1)
        pow_solution = Text("4").scale(0.5).next_to(pow_problem, DOWN)
        self.play(FadeIn(pow_solution))
        self.wait(1)
        self.play(FadeOut(miner1), FadeOut(miner2), FadeOut(pow_problem), FadeOut(pow_solution))

        # 去中心化网络
        decentralization_title = Text("Decentralized Network").scale(0.7)
        decentralization_title.to_edge(UP)
        self.play(Transform(title, decentralization_title))

        nodes = VGroup(
            Dot(LEFT * 2 + DOWN * 2.5), Dot(LEFT * 1 + DOWN * 2.5), Dot(DOWN * 2.5),
            Dot(RIGHT * 1 + DOWN * 2.5), Dot(RIGHT * 2 + DOWN * 2.5)
        )
        edges = VGroup(
            Line(nodes[0].get_center(), nodes[1].get_center()),
            Line(nodes[1].get_center(), nodes[2].get_center()),
            Line(nodes[2].get_center(), nodes[3].get_center()),
            Line(nodes[3].get_center(), nodes[4].get_center()),
            Line(nodes[0].get_center(), nodes[2].get_center()),
            Line(nodes[1].get_center(), nodes[3].get_center()),
            Line(nodes[2].get_center(), nodes[4].get_center())
        )
        self.play(FadeIn(nodes), FadeIn(edges))
        self.wait(1)

        # 节点通信
        communication_text = Text("Nodes communicate to validate blocks").scale(0.5).next_to(title, DOWN)
        self.play(Transform(pow_text, communication_text))

        self.play(
            *[Indicate(node, scale_factor=1.5) for node in nodes],
            run_time=2
        )
        self.wait(1)

        # 结束
        end_text = Text("Blockchain: Secure and Decentralized").scale(0.7).to_edge(DOWN)
        self.play(Transform(decentralization_title, end_text))
        self.wait(2)


class BlockchainIntroduction2(Scene):
    def construct(self):
        # 标题
        title = Text("区块链技术简介").scale(0.8)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # 区块的示例
        block1 = Rectangle(width=3, height=2, color=BLUE)
        block2 = Rectangle(width=3, height=2, color=BLUE)
        block3 = Rectangle(width=3, height=2, color=BLUE)

        # 布局
        block1.shift(LEFT * 4)
        block2.next_to(block1, RIGHT, buff=1.5)
        block3.next_to(block2, RIGHT, buff=1.5)

        block1_text = Text("区块 1").scale(0.5).move_to(block1.get_center())
        block2_text = Text("区块 2").scale(0.5).move_to(block2.get_center())
        block3_text = Text("区块 3").scale(0.5).move_to(block3.get_center())

        # 添加区块和文本
        self.play(FadeIn(block1), Create(block1_text))
        self.play(FadeIn(block2), Create(block2_text))
        self.play(FadeIn(block3), Create(block3_text))
        self.wait(1)

        # 链接区块
        arrow1 = Arrow(start=block1.get_right(), end=block2.get_left(), buff=0.1)
        arrow2 = Arrow(start=block2.get_right(), end=block3.get_left(), buff=0.1)
        self.play(GrowArrow(arrow1), GrowArrow(arrow2))
        self.wait(1)

        # 介绍哈希值
        hash_text1 = Text("哈希: 000x123").scale(0.5).next_to(block1, DOWN)
        prev_hash_text2 = Text("前哈希: 000x123").scale(0.5).next_to(block2, UP)
        hash_text2 = Text("哈希: 000x456").scale(0.5).next_to(block2, DOWN)
        prev_hash_text3 = Text("前哈希: 000x456").scale(0.5).next_to(block3, UP)
        hash_text3 = Text("哈希: 000x789").scale(0.5).next_to(block3, DOWN)

        self.play(FadeIn(hash_text1))
        self.play(FadeIn(prev_hash_text2))
        self.play(FadeIn(hash_text2))
        self.play(FadeIn(prev_hash_text3))
        self.play(FadeIn(hash_text3))
        self.wait(1)

        # 清除哈希值
        self.play(FadeOut(hash_text1))
        self.play(FadeOut(prev_hash_text2), FadeOut(hash_text2))
        self.play(FadeOut(prev_hash_text3), FadeOut(hash_text3))

        # 工作量证明
        pow_title = Text("工作量证明").scale(0.7)
        pow_title.to_edge(UP)
        self.play(Transform(title, pow_title))

        pow_text = Text("矿工解决复杂问题来添加区块").scale(0.5).next_to(title, DOWN)
        self.play(FadeIn(pow_text))
        self.wait(1)

        # 示意矿工工作
        miner1 = Circle(color=YELLOW).shift(LEFT * 4 + DOWN * 2)
        miner2 = Circle(color=YELLOW).shift(RIGHT * 4 + DOWN * 2)
        self.play(FadeIn(miner1), FadeIn(miner2))
        pow_problem = Text("求解: 2 + 2 = ?").scale(0.5).move_to(UP * 2)
        self.play(FadeIn(pow_problem))
        self.wait(1)
        pow_solution = Text("4").scale(0.5).next_to(pow_problem, DOWN)
        self.play(FadeIn(pow_solution))
        self.wait(1)
        self.play(FadeOut(miner1), FadeOut(miner2), FadeOut(pow_problem), FadeOut(pow_solution))

        # 去中心化网络
        decentralization_title = Text("去中心化网络").scale(0.7)
        decentralization_title.to_edge(UP)
        self.play(Transform(title, decentralization_title))

        nodes = VGroup(
            Dot(LEFT * 2 + DOWN * 2.5), Dot(LEFT * 1 + DOWN * 2.5), Dot(DOWN * 2.5),
            Dot(RIGHT * 1 + DOWN * 2.5), Dot(RIGHT * 2 + DOWN * 2.5)
        )
        edges = VGroup(
            Line(nodes[0].get_center(), nodes[1].get_center()),
            Line(nodes[1].get_center(), nodes[2].get_center()),
            Line(nodes[2].get_center(), nodes[3].get_center()),
            Line(nodes[3].get_center(), nodes[4].get_center()),
            Line(nodes[0].get_center(), nodes[2].get_center()),
            Line(nodes[1].get_center(), nodes[3].get_center()),
            Line(nodes[2].get_center(), nodes[4].get_center())
        )
        self.play(FadeIn(nodes), FadeIn(edges))
        self.wait(1)

        # 节点通信
        communication_text = Text("节点通信验证区块").scale(0.5).next_to(title, DOWN)
        self.play(Transform(pow_text, communication_text))

        self.play(
            *[Indicate(node, scale_factor=1.5) for node in nodes],
            run_time=2
        )
        self.wait(1)

        # 结束
        end_text = Text("区块链：安全且去中心化").scale(0.7).to_edge(DOWN)
        self.play(Transform(decentralization_title, end_text))
        self.wait(2)


if __name__ == "__main__":
    from manim import config

    config.verbosity = "ERROR"
    config.quality = "high_quality"
    scene = BlockchainIntroduction2()
    scene.render(True)
