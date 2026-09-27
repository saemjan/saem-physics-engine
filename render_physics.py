from manim import *
import csv

class PhysicsShort(Scene):
    def construct(self):
        # 1. Read the data from your CSV
        with open('content_batch.csv', mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader) # Skip the header row
            for row in reader:
                video_id, title_text, formula_tex = row
                break # We just grab the top row for now

        # 2. Setup the visual elements
        title = Text(title_text, font_size=40, color=YELLOW).to_edge(UP)
        
        # We use MathTex for professional LaTeX rendering (Ohanian/Feynman style!)
        equation = MathTex(formula_tex, font_size=56)
        
        tagline = Text("Physics Padh lo Yaar!", font_size=32, color=ORANGE).to_edge(DOWN)

        # 3. Animate! (The magic part)
        self.play(Write(title), run_time=1.5)
        self.wait(0.5)
        
        self.play(Write(equation), run_time=2)
        self.play(equation.animate.scale(1.5).set_color(BLUE))
        self.wait(2)
        
        self.play(FadeIn(tagline, shift=UP))
        self.wait(2)
