import argparse
from PIL import Image, ImageFilter, ImageMath, ImageChops, ImageOps

# TODO: Add configurable unsharp mask filter
# TODO: Add gray wedge
# TODO: Add title

PRINTER_DPI     = 300
MM2INCH         = 0.0393701

LANDSCAPE_SIZES = {
    'a3': (420.0, 297.0), 
    'a4': (297.0, 210.0), 
    'a5': (210.0, 148.0), 
    'a6': (148.0, 105.0), 
}

PORTRAIT_SIZES = {
    'a3': (297.0, 420.0), 
    'a4': (210.0, 297.0), 
    'a5': (148.0, 210.0), 
    'a6': (105.0, 148.0), 
}

class App():

    def __init__(self, input, output, autoblend, border, resize, dpi, gamma, equalize, black, white):
        self.input = input
        self.output = output
        self.autoblend = autoblend
        self.border = border
        self.resize = resize
        self.dpi = dpi
        self.gamma = gamma
        self.equalize = equalize
        self.black = black
        self.white = white
    
    def gamma_correct(self, img):
        if self.gamma == 1.0:
            return img
        inv_gamma = 1.0 / self.gamma
        expr = "int(((float(x) / 255.0) ** inv_gamma) * 255)"
        img = ImageMath.eval(expr, x=img, inv_gamma=inv_gamma)
        return img.convert('L', palette='ADAPTIVE')
    
    def equalize_histogram(self, img):
        if not self.equalize:
            return img
        return ImageOps.equalize(img)
    
    def apply_auto_blend(self, img):
        if not self.autoblend:
            return img
        if self.autoblend == 'overlay':
            return ImageChops.overlay(img, img)
        elif self.autoblend == 'screen':
            return ImageChops.screen(img, img)
        elif self.autoblend == 'multiply':
            return ImageChops.multiply(img, img)
        elif self.autoblend == 'softlight':
            return ImageChops.soft_light(img, img)
        elif self.autoblend == 'hardlight':
            return ImageChops.hard_light(img, img)
        else:
            assert 1 == 2
    
    def add_border(self, img):
        if self.border == 0.0:
            return img
        assert self.border <= 0.25
        inner_width, inner_height = img.size
        x_offset = int(self.border * inner_width)
        y_offset = int(self.border * inner_height)
        offset = max(x_offset, y_offset)
        outer_width = inner_width + int(2.0 * offset)
        outer_height = inner_height + int(2.0 * offset)
        outer_size = (outer_width, outer_height)
        outer_img = Image.new("L", outer_size, color=255)
        bbox = [ offset, offset, offset + inner_width, offset + inner_height]
        outer_img.paste(img, bbox)
        return outer_img
        
    def resize_padding(self, img):
        if self.resize == 'no':
            return img
        width, height = img.size
        factor = MM2INCH * self.dpi
        if width > height: # landscape:
            width_mm, height_mm = LANDSCAPE_SIZES[ self.resize ]
        else: # portrait
            width_mm, height_mm = LANDSCAPE_SIZES[ self.resize ]
        width_inch, height_inch = width_mm * MM2INCH, height_mm * MM2INCH
        width_px, width_px = int(self.dpi * width_inch), int(self.dpi * height_inch)        
        size = (width_px, width_px)
        return ImageOps.pad(img, size, color=0)
        
    
    def remap_bw(self, img):
        black = self.black, self.black, self.black
        white = self.white, self.white, self.white, 
        return ImageOps.colorize(img, black, white)
        
    def to_negative(self, img):
        img = ImageOps.mirror(img)
        img = ImageChops.invert(img)
        return img
    
    def unsharp_mask(self, img):
        return img.filter(ImageFilter.UnsharpMask(radius=2, percent=50, threshold=3))
        
    def run(self):
        img = Image.open(self.input)
        img = img.convert('L', palette='ADAPTIVE')
        img = self.equalize_histogram(img)
        img = self.apply_auto_blend(img)
        img = self.gamma_correct(img)
        img = self.remap_bw(img)
        img = self.add_border(img)
        img = self.resize_padding(img)
        img = self.to_negative(img)
        img = self.unsharp_mask(img)
        img.show()
        img.save(self.output)
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--overlay', action='store_const', dest='autoblend', const='overlay')
    group.add_argument('--screen', action='store_const', dest='autoblend', const='screen')
    group.add_argument('--multiply', action='store_const', dest='autoblend', const='multiply')
    group.add_argument('--softlight', action='store_const', dest='autoblend', const='softlight')
    group.add_argument('--hardlight', action='store_const', dest='autoblend', const='hardlight')    
    parser.add_argument('-g', '--gamma', type=float, default=1.0, help='gamma')
    parser.add_argument('-e', '--equalize', action='store_true', help='histogram equalization')
    parser.add_argument('-B', '--border', type=float, default=0.05, help='border as % of the final image')
    parser.add_argument('-r', '--resize', choices=[ 'a3', 'a4', 'a5', 'a6', 'no' ], default='no', help='resize to fit an ISO paper size')
    parser.add_argument('-d', '--dpi', type=int, default=300, help='dots per inch')
    parser.add_argument('-b', '--black', type=int, default=0, help='black')    
    parser.add_argument('-w', '--white', type=int, default=255, help='white')
    parser.add_argument('input', type=str, help='input image')
    parser.add_argument('output', type=str, help='output image')
    args = parser.parse_args()
    App(
        args.input, 
        args.output, 
        args.autoblend, 
        args.border, 
        args.resize, 
        args.dpi, 
        args.gamma, 
        args.equalize, 
        args.black, 
        args.white
    ).run()