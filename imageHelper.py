from PIL import Image

def openImage(path):
    """Outputs an Image structure
    
    IN
        path : String
    OUT
        Image
    """
    im =  Image.open(path)
    return im.convert('RGB')

def getPixel(image, coords):
    """Returns the color located on an image
    at the given coordinates
    
    IN
        image : Image
        coords : Tuple of 2 integers
    OUT
        Tuple of 3 [0,255] integers
    """
    return image.getpixel(coords)

img = openImage("images/niko.png")
print(getPixel(img,(0,0)))