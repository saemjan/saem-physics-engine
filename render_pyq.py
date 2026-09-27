from manim import *
import csv

# Force 9:16 Portrait Mode for YouTube Shorts
config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16.0
config.frame_width = 9.0

class VerticalPhysics(Scene):
    def construct(self):
        # Read the CSV
        with open('content_batch.csv', mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader) 
            for row in reader:
                video_id, title_text, formula_tex, highlight_tex, script = row
                break 

        # 1. Title Styling (Smaller font, automatic scaling)
        title = Text(title_text, font_size=40, color=YELLOW).to_edge(UP, buff=2)
        if title.width > config.frame_width - 1:
            title.scale_to_fit_width(config.frame_width - 1.5)
        
        # 2. Equation Styling (Proper sizing and automatic boundary limits)
        equation = MathTex(formula_tex, font_size=64)
        equation.set_color_by_tex(highlight_tex, GOLD)
        
        # This is the magic line: it forces long formulas to shrink so they never get cut off
        if equation.width > config.frame_width - 1:
            equation.scale_to_fit_width(config.frame_width - 1.5)
        
        # 3. Tagline Styling
        tagline = Text("Physics Padh lo Yaar!", font_size=32, color=ORANGE).to_edge(DOWN, buff=2.5)

        # 4. Smoother Animations (Premium feel)
        self.play(FadeIn(title, shift=DOWN), run_time=1.2)
        self.wait(0.5)
        
        self.play(Write(equation), run_time=2)
        # A gentle 10% pop instead of a massive zoom that breaks the screen bounds
        self.play(equation.animate.scale(1.1))
        self.wait(1.5)
        
        self.play(FadeIn(tagline, shift=UP))
        self.wait(2)
