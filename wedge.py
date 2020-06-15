import argparse
from PIL import Image, ImageDraw, ImageFont

CELL_SIZE   = 50
COLORS      = list( [ int(i / 10 * 255) for i in range(11)] )
COLOR_NAMES = [ '0%', '10%', '20%', '30%', '40%', '50%', '60%', '70%', '80%', '90%', '100%' ]
GAMMAS      = [
                1 / 3.00,       1 / 2.75,       1 / 2.50,       1 / 2.25, 
                1 / 2.00,       1 / 1.75,       1 / 1.50,       1 / 1.25,   
                1.0, 
                1.25,           1.5,            1.75,           2.0, 
                2.25,           2.5,            2.75,           3.0 
            ]
GAMMA_NAMES = list([ 'y = \n%0.3f' % gamma for gamma in GAMMAS ])
                
NUM_ROWS    = len(COLORS) + 2
NUM_COLS    = len(GAMMAS) + 2 + 1
WIDTH       = CELL_SIZE * NUM_COLS + 1
HEIGHT      = CELL_SIZE * NUM_ROWS + 1
FONT_NAME   = "FreeMono.ttf" # https://github.com/python-pillow/Pillow/blob/master/Tests/fonts/FreeMono.ttf
FONT_SIZE   = 18

class App():
    
    def __init__(self, output):
        self.output = output
        self.font   = ImageFont.truetype(FONT_NAME, size=FONT_SIZE)
    
    def draw_frame(self, draw):
        x1 = 0
        y1 = 0
        x2 = NUM_COLS * CELL_SIZE
        y2 = NUM_ROWS * CELL_SIZE
        xy = [x1, y1, x2, y2]
        draw.rectangle(xy, fill=255, outline="black", width=1)
    
    def draw_text(self, draw, text, xy, color, direction=None):
        shade = int(color * 0.8)
        x1, y1 = xy
        xy = [ x1 - 1, y1]
        draw.text(xy, text, font=self.font, fill=shade, align="center")
        xy = [ x1 + 1, y1]
        draw.text(xy, text, font=self.font, fill=shade, align="center")
        xy = [ x1, y1 - 1]
        draw.text(xy, text, font=self.font, fill=shade, align="center")
        xy = [ x1, y1 + 1]
        draw.text(xy, text, font=self.font, fill=shade, align="center")
        xy = [ x1, y1 ]
        draw.text(xy, text, font=self.font, fill=color, align="center")

    def draw_hlabel(self, draw, row, color_name):
        x1 = 1 * CELL_SIZE 
        y1 = (row + 1) * CELL_SIZE + CELL_SIZE // 3
        xy = [ x1, y1 ]
        draw.text(xy, color_name, font=self.font, fill=0, align="center")

    def draw_vlabel(self, draw, col, gamma_name):
        font = ImageFont.truetype(FONT_NAME, size=12)
        x1 = (col + 2) * CELL_SIZE + CELL_SIZE // 4
        y1 = (NUM_ROWS - 1) * CELL_SIZE 
        xy = [ x1, y1 ]
        draw.text(xy, gamma_name, font=font, fill=0, align="center")
        
    def draw_cell(self, draw, col, row, color, gamma):
        gc = self.gamma_correct(color, gamma)
        x1 = col * CELL_SIZE
        y1 = row * CELL_SIZE
        x2 = col * CELL_SIZE + CELL_SIZE + 1
        y2 = row * CELL_SIZE + CELL_SIZE + 1
        xy = [x1, y1, x2, y2]
        draw.rectangle(xy, fill=gc, width=1, outline=128)
        reverse_color = self.gamma_correct(255 - color, gamma)

    def gamma_correct(self, color, gamma):
        if color == 0:
            return 0
        if gamma == 0:
            return color
        inv_gamma = 1.0 / gamma            
        return int(((color / 255.0) ** inv_gamma) * 255)
        
    def run(self):
        size = WIDTH, HEIGHT
        img = Image.new('L', size, color=255)
        draw = ImageDraw.Draw(img)
        self.draw_frame(draw)
        for row, color_name in enumerate(COLOR_NAMES):
            self.draw_hlabel(draw, row, color_name)
        for col, gamma_name in enumerate(GAMMA_NAMES):
            self.draw_vlabel(draw, col, gamma_name)
        for row, color in enumerate(COLORS):
            for col, gamma in enumerate(GAMMAS):
                self.draw_cell(draw, col + 2, row + 1, color, gamma)
        #img.show()
        img.save(self.output)
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('output', type=str, help='output image')
    args = parser.parse_args()
    App(args.output).run()