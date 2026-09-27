from manim import *
import csv

# Force 9:16 Portrait Mode for YouTube Shorts
config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16.0
config.frame_width = 9.0

class VerticalPhysics(Scene):
    def construct(self):
        # Read the upgraded CSV
        with open('content_batch.csv', mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader) 
            for row in reader:
                video_id, title_text, formula_tex, highlight_tex, script = row
                break 

        title = Text(title_text, font_size=48, color=YELLOW).to_edge(UP, buff=1.5)
        
        equation = MathTex(formula_tex, font_size=82)
        # Dynamically highlight the specific variable in GOLD
        equation.set_color_by_tex(highlight_tex, GOLD)
        
        tagline = Text("Physics Padh lo Yaar!", font_size=40, color=ORANGE).to_edge(DOWN, buff=2)

        self.play(Write(title), run_time=1.5)
        self.play(Write(equation), run_time=2)
        self.play(equation.animate.scale(1.2))
        self.wait(1.5)
        
        self.play(FadeIn(tagline, shift=UP))
        self.wait(2)
