from PIL import Image as img
from math import gcd, sqrt, inf

SIGNES = ["$","@","B","%","8","&","W","M","#","*","o","a","h","k","b","d","p","q","w","m","Z","O","0","Q","L","C","J","U","Y","X","z","c","v","u","n","x","r","j","f","t","/","|","(",")","1","{","}","[","]","?","-","_","+","~","<",">","i","!","l","I",";",":",",","^","`","'","."," "]

def format_convertion(name : str, character_limit : int):
    im = img.open(name)
    im = im.convert("RGB")
    x, y = im.size[0], im.size[1]
    if x * y > character_limit:
        d = gcd(x,y)
        x_reduced = x // d
        y_reduced = y // d
        k_max = int(sqrt(character_limit / (x_reduced * y_reduced)))
        if k_max != 0:
            im.thumbnail([x_reduced * k_max, y_reduced * k_max])
        else:
            raise ValueError('The character limit is not compatible with your image, you may have to change image or disable the limit')
    result = [[] for i in range(y)]
    for x in range(im.size[0]):
        for y in range(im.size[1]):
            brightness = sum(im.getpixel((x,y)))/3/255*67
            brightness = brightness.__round__()
            result[y].append(brightness)
    im.close()
    return result

def map_to_str(map : list):
    result = []
    for x in range(len(map)):
        result.append('')
        for y in range(len(map[0])):
            result[x] += (SIGNES[map[x][y]])
    return result

def txt(liste : list):
    o = open("result.txt","w")
    for i in range(len(liste)):
        o.write(liste[i]+"\n")

def main(name : str, character_limit : int = inf):
    """
    Convert any image into a text file.

    :param str name: the name of you image, for example 'image.png'
    :param int character_limit: if you want to set a limit to the number of characters in the text file, default is orignial size
    :return: none,the text file will appear in the same folder as this python file
    """
    map = format_convertion(name, character_limit)
    liste = map_to_str(map)
    txt(liste)
