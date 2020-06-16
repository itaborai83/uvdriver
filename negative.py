import argparse
from PIL import Image, ImageFilter, ImageMath, ImageChops, ImageOps

# TODO: Add configurable unsharp mask filter
# TODO: Add black remapping
# TODO: Add white remapping
# TODO: Add color cast
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

    def __init__(self, input, output, border, resize, dpi, gamma, blur, blurradius):
        self.input = input
        self.output = output
        self.border = border
        self.resize = resize
        self.dpi = dpi
        self.gamma = gamma
        self.blur = blur
        self.blurradius = blurradius
    
    def gamma_correct(self, img):
        if self.gamma == 1.0:
            return img
        inv_gamma = 1.0 / self.gamma
        expr = "int(((float(x) / 255.0) ** inv_gamma) * 255)"
        img = ImageMath.eval(expr, x=img, inv_gamma=inv_gamma)
        return img.convert('L', palette='ADAPTIVE')
    
    def apply_blur(self, img):
        if self.blurradius <= 0:
            return img
        img2 = img.filter(ImageFilter.GaussianBlur(self.blurradius))
        if self.blur == 'overlay':
            return ImageChops.overlay(img, img2)
        elif self.blur == 'screen':
            return ImageChops.screen(img, img2)
        elif self.blur == 'multiply':
            return ImageChops.multiply(img, img2)
        else:
            assert 1 == 2
    
    def add_border(self, img):
        if self.border == 0.0:
            return img
        assert self.border <= 0.25
        inner_width, inner_height = img.size
        x_offset = int(self.border * inner_width)
        y_offset = int(self.border * inner_height)
        outer_width = inner_width + int(2.0 * x_offset)
        outer_height = inner_height + int(2.0 * y_offset)
        outer_size = (outer_width, outer_height)
        outer_img = Image.new("L", outer_size, color=255)
        bbox = [x_offset, y_offset, x_offset + inner_width, y_offset + inner_height]
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
        img = ImageOps.pad(img, size, color=255)
        return img.filter(ImageFilter.UnsharpMask())
            
    def to_negative(self, img):
        img = ImageOps.mirror(img)
        img = ImageChops.invert(img)
        black = 50
        white = 205
        #img = ImageOps.colorize(img, (25, 25, 0), (235, 235, 0), (127, 127, 0))
        return img
        
    def run(self):
        img = Image.open(self.input)
        img = img.convert('L', palette='ADAPTIVE')
        img = self.gamma_correct(img)
        img = self.apply_blur(img)
        img = self.add_border(img)
        img = self.resize_padding(img)
        img = self.to_negative(img)
        img.show()
        #img.save(self.output)
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--gamma', type=float, default=1.0, help='gamma')
    parser.add_argument('--border', type=float, default=0.05, help='border as % of the final image')
    parser.add_argument('--resize', choices=[ 'a3', 'a4', 'a5', 'a6', 'no' ], default='no', help='resize to fit an ISO paper size')
    parser.add_argument('--dpi', type=int, default=300, help='dots per inch')
    parser.add_argument('--blur', choices=[ 'overlay', 'multiply', 'screen' ], default='overlay', help='applies an blurred blend of the image with itself. When --blurradius > 0')
    parser.add_argument('--blurradius', type=int, default=0.0, help='blur radius')
    parser.add_argument('input', type=str, help='input image')
    parser.add_argument('output', type=str, help='output image')
    args = parser.parse_args()
    App(args.input, args.output, args.border, args.resize, args.dpi, args.gamma, args.blur, args.blurradius).run()