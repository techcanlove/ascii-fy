from PIL import Image
ASCII_CHARS = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'."
ASCII_FULL_CHARS = "＄＠Ｂ％８＆ＷＭ＃＊ｏａｈｋｂｄｐｑｗｍＺＯ０ＱＬＣＪＵＹＸｚｃｖｕｎｘｒｊｆｔ／｜（）１｛｝［］？－＿＋～＜＞ｉ！ｌＩ；：，＂＾｀＇．"
#ASCII_CHARS = ['.',',',':',';','+','*','?','%','S','#','@']
#ASCII_CHARS = ASCII_CHARS[::-1]

'''
method resize():
    - takes as parameters the image, and the final width
    - resizes the image into the final width while maintaining aspect ratio
'''
def resize(image, new_width=100):
    (old_width, old_height) = image.size
    aspect_ratio = float(old_height)/float(old_width)
    new_height = int(aspect_ratio * new_width)
    new_dim = (new_width, new_height)
    new_image = image.resize(new_dim)
    return new_image
'''
method grayscalify():
    - takes an image as a parameter
    - returns the grayscale version of image
'''
def grayscalify(image):
    return image.convert('L')

'''
method modify():
    - replaces every pixel with a character whose intensity is similar
'''
def modify(image):
    buckets = (255//len(ASCII_FULL_CHARS))+1 #25

    initial_pixels = list(image.getdata())
    #print(initial_pixels)
    new_pixels = [ASCII_FULL_CHARS[pixel_value//buckets] for pixel_value in initial_pixels]
    return ''.join(new_pixels)

'''
method do():
    - does all the work by calling all the above functions
'''
#def do(image, new_width=100):


'''
method runner():
    - takes as parameter the image path and runs the above code
    - handles exceptions as well
    - provides alternative output options
'''
def runner(path, resolution=100,web=False):
    image = None
    try:
        image = Image.open(path)
    except Exception:
        print("Unable to find image in",path)
        #print(e)
        return
        
        
    #image = do(image, resolution)
    image = resize(image, resolution)
    image = grayscalify(image)
    pixels = modify(image)
    
    len_pixels = len(pixels)

    # Construct the image from the character list
    new_image = [pixels[index:index+resolution] for index in range(0, len_pixels, resolution)]
    
    char_img=None
    if web:
        char_img = '</br>\n'.join(new_image)
    else:
        char_img = '\n'.join(new_image)
    
    # To print on console
    #print(char_img)

    with open('img.txt','w',encoding="utf-8") as f:
        f.write(char_img)
    

'''
method main():
    - reads input from console
    - profit
'''
if __name__ == '__main__':
    import sys
    # import urllib.request
    # if sys.argv[1].startswith('http://') or sys.argv[1].startswith('https://'):
        # urllib.request.urlretrieve(sys.argv[1], "asciify.jpg")
        # path = "asciify.jpg"
    # else:
        # path = sys.argv[1]
    path = sys.argv[1]
    try:
        resolution = int(sys.argv[2])
    except:
        resolution = 100
    try:
        if sys.argv[3]=="web":
            web=True
    except:
        web=False    
    runner(path,resolution,web)
