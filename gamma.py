import argparse
from PIL import Image, ImageFilter, ImageMath, ImageChops, ImageOps

A4_LANDSCAPE    = (3543, 2362)
A4_VERTICAL     = (2362, 3543)

class App():

    def __init__(self, input, output, gamma, overlay):
        self.input = input
        self.output = output
        self.gamma = gamma
        self.overlay = overlay
    
    def gamma_correct(self, img):
        if self.gamma == 1.0:
            return img
        inv_gamma = 1.0 / self.gamma
        expr = "int(((float(x) / 255.0) ** inv_gamma) * 255)"
        img = ImageMath.eval(expr, x=img, inv_gamma=inv_gamma)
        return img.convert('L', palette='ADAPTIVE')
    
    def apply_overlay(self, img, blur=True):
        if not self.overlay:
            return img
        if blur:
            img2 = img.filter(ImageFilter.GaussianBlur())
        else:
            img2 = img
        return ImageChops.overlay(img, img)
    
    def resize_to_a4(self, img):
        bbox = img.getbbox()
        width, height = bbox[2], bbox[3]
        if width >= height:
            new_size = A4_LANDSCAPE
        else:
            new_size = A4_VERTICAL
        img = ImageOps.fit(img, new_size)
        return img.filter(ImageFilter.UnsharpMask())
    
    def to_negative(self, img):
        img = ImageOps.mirror(img)
        img = ImageChops.invert(img)
        black = 50
        white = 205
        img = ImageOps.colorize(img, (50, 50, 0), (205, 205, 0), (127, 127, 127))
        return img
        
    def run(self):
        img = Image.open(self.input)
        img = img.convert('L', palette='ADAPTIVE')
        img = self.apply_overlay(img, blur=False)
        img = self.gamma_correct(img)
        img = self.resize_to_a4(img)
        img = self.to_negative(img)
        img.show()
        img.save(self.output)
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--gamma', type=float, default=1.0, help='gamma')
    parser.add_argument('--overlay', action='store_true', default=False, help='applies an overlay blend of the image with itself')
    parser.add_argument('input', type=str, help='input image')
    parser.add_argument('output', type=str, help='output image')
    args = parser.parse_args()
    App(args.input, args.output, args.gamma, args.overlay).run()