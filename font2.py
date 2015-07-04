import sys
from PIL import Image, ImageDraw, ImageOps
import numpy as np
import StringIO

fontsize = (5, 7)
font_small = {
    '/'  :  [0x20, 0x10, 0x08, 0x04, 0x02],
    ' '  :  [0x00, 0x00, 0x00, 0x00, 0x00],
    '+'  :  [0x08, 0x08, 0x3E, 0x08, 0x08],
    '-'  :  [0x08, 0x08, 0x08, 0x08, 0x08],
    '`'  :  [0x00, 0x01, 0x02, 0x04, 0x00],
    '.'  :  [0x00, 0x60, 0x60, 0x00, 0x00],
#    '<'  :  [0x00, 0x08, 0x14, 0x22, 0x41],
    '='  :  [0x14, 0x14, 0x14, 0x14, 0x14],
#    '>'  :  [0x41, 0x22, 0x14, 0x08, 0x00],
    '\\' :  [0x02, 0x04, 0x08, 0x10, 0x20],
    '^'  :  [0x04, 0x02, 0x01, 0x02, 0x04],
    '_'  :  [0x40, 0x40, 0x40, 0x40, 0x40],
    '|'  :  [0x00, 0x00, 0x7F, 0x00, 0x00],
}
font_big = {
    '/'  :  [0x20, 0x10, 0x08, 0x04, 0x02],
    ' '  :  [0x00, 0x00, 0x00, 0x00, 0x00],
    '!'  :  [0x00, 0x00, 0x5F, 0x00, 0x00],
    '"'  :  [0x00, 0x07, 0x00, 0x07, 0x00],
    '#'  :  [0x14, 0x7F, 0x14, 0x7F, 0x14],
    '$'  :  [0x24, 0x2A, 0x7F, 0x2A, 0x12],
    '%'  :  [0x23, 0x13, 0x08, 0x64, 0x62],
    '&'  :  [0x36, 0x49, 0x55, 0x22, 0x50],
    "'"  :  [0x00, 0x05, 0x03, 0x00, 0x00],
    '('  :  [0x00, 0x1C, 0x22, 0x41, 0x00],
    ')'  :  [0x00, 0x41, 0x22, 0x1C, 0x00],
    '*'  :  [0x08, 0x2A, 0x1C, 0x2A, 0x08],
    '+'  :  [0x08, 0x08, 0x3E, 0x08, 0x08],
    ','  :  [0x00, 0x50, 0x30, 0x00, 0x00],
    '-'  :  [0x08, 0x08, 0x08, 0x08, 0x08],
    '.'  :  [0x00, 0x60, 0x60, 0x00, 0x00],
    '0'  :  [0x3E, 0x51, 0x49, 0x45, 0x3E],
    '1'  :  [0x00, 0x42, 0x7F, 0x40, 0x00],
    '2'  :  [0x42, 0x61, 0x51, 0x49, 0x46],
    '3'  :  [0x21, 0x41, 0x45, 0x4B, 0x31],
    '4'  :  [0x18, 0x14, 0x12, 0x7F, 0x10],
    '5'  :  [0x27, 0x45, 0x45, 0x45, 0x39],
    '6'  :  [0x3C, 0x4A, 0x49, 0x49, 0x30],
    '7'  :  [0x01, 0x71, 0x09, 0x05, 0x03],
    '8'  :  [0x36, 0x49, 0x49, 0x49, 0x36],
    '9'  :  [0x06, 0x49, 0x49, 0x29, 0x1E],
    ':'  :  [0x00, 0x36, 0x36, 0x00, 0x00],
    ';'  :  [0x00, 0x56, 0x36, 0x00, 0x00],
    '<'  :  [0x00, 0x08, 0x14, 0x22, 0x41],
    '='  :  [0x14, 0x14, 0x14, 0x14, 0x14],
    '>'  :  [0x41, 0x22, 0x14, 0x08, 0x00],
    '?'  :  [0x02, 0x01, 0x51, 0x09, 0x06],
    '@'  :  [0x32, 0x49, 0x79, 0x41, 0x3E],
    'A'  :  [0x7E, 0x11, 0x11, 0x11, 0x7E],
    'B'  :  [0x7F, 0x49, 0x49, 0x49, 0x36],
    'C'  :  [0x3E, 0x41, 0x41, 0x41, 0x22],
    'D'  :  [0x7F, 0x41, 0x41, 0x22, 0x1C],
    'E'  :  [0x7F, 0x49, 0x49, 0x49, 0x41],
    'F'  :  [0x7F, 0x09, 0x09, 0x01, 0x01],
    'G'  :  [0x3E, 0x41, 0x41, 0x51, 0x32],
    'H'  :  [0x7F, 0x08, 0x08, 0x08, 0x7F],
    'I'  :  [0x00, 0x41, 0x7F, 0x41, 0x00],
    'J'  :  [0x20, 0x40, 0x41, 0x3F, 0x01],
    'K'  :  [0x7F, 0x08, 0x14, 0x22, 0x41],
    'L'  :  [0x7F, 0x40, 0x40, 0x40, 0x40],
    'M'  :  [0x7F, 0x02, 0x04, 0x02, 0x7F],
    'N'  :  [0x7F, 0x04, 0x08, 0x10, 0x7F],
    'O'  :  [0x3E, 0x41, 0x41, 0x41, 0x3E],
    'P'  :  [0x7F, 0x09, 0x09, 0x09, 0x06],
    'Q'  :  [0x3E, 0x41, 0x51, 0x21, 0x5E],
    'R'  :  [0x7F, 0x09, 0x19, 0x29, 0x46],
    'S'  :  [0x46, 0x49, 0x49, 0x49, 0x31],
    'T'  :  [0x01, 0x01, 0x7F, 0x01, 0x01],
    'U'  :  [0x3F, 0x40, 0x40, 0x40, 0x3F],
    'V'  :  [0x1F, 0x20, 0x40, 0x20, 0x1F],
    'W'  :  [0x7F, 0x20, 0x18, 0x20, 0x7F],
    'X'  :  [0x63, 0x14, 0x08, 0x14, 0x63],
    'Y'  :  [0x03, 0x04, 0x78, 0x04, 0x03],
    'Z'  :  [0x61, 0x51, 0x49, 0x45, 0x43],
    '['  :  [0x00, 0x00, 0x7F, 0x41, 0x41],
    '\\' :  [0x02, 0x04, 0x08, 0x10, 0x20],
    ']'  :  [0x41, 0x41, 0x7F, 0x00, 0x00],
    '^'  :  [0x04, 0x02, 0x01, 0x02, 0x04],
    '_'  :  [0x40, 0x40, 0x40, 0x40, 0x40],
    '`'  :  [0x00, 0x01, 0x02, 0x04, 0x00],
    'a'  :  [0x20, 0x54, 0x54, 0x54, 0x78],
    'b'  :  [0x7F, 0x48, 0x44, 0x44, 0x38],
    'c'  :  [0x38, 0x44, 0x44, 0x44, 0x20],
    'd'  :  [0x38, 0x44, 0x44, 0x48, 0x7F],
    'e'  :  [0x38, 0x54, 0x54, 0x54, 0x18],
    'f'  :  [0x08, 0x7E, 0x09, 0x01, 0x02],
    'g'  :  [0x08, 0x14, 0x54, 0x54, 0x3C],
    'h'  :  [0x7F, 0x08, 0x04, 0x04, 0x78],
    'i'  :  [0x00, 0x44, 0x7D, 0x40, 0x00],
    'j'  :  [0x20, 0x40, 0x44, 0x3D, 0x00],
    'k'  :  [0x00, 0x7F, 0x10, 0x28, 0x44],
    'l'  :  [0x00, 0x41, 0x7F, 0x40, 0x00],
    'm'  :  [0x7C, 0x04, 0x18, 0x04, 0x78],
    'n'  :  [0x7C, 0x08, 0x04, 0x04, 0x78],
    'o'  :  [0x38, 0x44, 0x44, 0x44, 0x38],
    'p'  :  [0x7C, 0x14, 0x14, 0x14, 0x08],
    'q'  :  [0x08, 0x14, 0x14, 0x18, 0x7C],
    'r'  :  [0x7C, 0x08, 0x04, 0x04, 0x08],
    's'  :  [0x48, 0x54, 0x54, 0x54, 0x20],
    't'  :  [0x04, 0x3F, 0x44, 0x40, 0x20],
    'u'  :  [0x3C, 0x40, 0x40, 0x20, 0x7C],
    'v'  :  [0x1C, 0x20, 0x40, 0x20, 0x1C],
    'w'  :  [0x3C, 0x40, 0x30, 0x40, 0x3C],
    'x'  :  [0x44, 0x28, 0x10, 0x28, 0x44],
    'y'  :  [0x0C, 0x50, 0x50, 0x50, 0x3C],
    'z'  :  [0x44, 0x64, 0x54, 0x4C, 0x44],
    '{'  :  [0x00, 0x08, 0x36, 0x41, 0x00],
    '|'  :  [0x00, 0x00, 0x7F, 0x00, 0x00],
    '}'  :  [0x00, 0x41, 0x36, 0x08, 0x00],
    }

displayscale=20

def map_data(arr):
    img = ImageOps.invert(Image.fromarray(np.uint8(arr*255)))
    return { "img" : img, "arr" : arr }

def data_to_arr(data):
    arr = np.zeros(fontsize).transpose()
    for x in range(fontsize[0]):
        for y in range(fontsize[1]):
            if (data[x] & (1<<y)):
                arr[y, x] = 1
    return arr
    
def fontToImages(font):
    results={}
    for ch in font:
        data = font[ch]
        data_arr = data_to_arr(data)
        ny, nx = np.shape(data_arr)
        # Create a new array that contains the character in the center.
        da2 = np.zeros((ny*3-2, nx*3-2))
        da2[ny-1:ny+ny-1, nx-1:nx+nx-1] = data_arr
        yoff = ny
        for xoff in range(0+2, nx*2-1-2):
            da3 = da2[yoff-1:yoff+ny-1, xoff:xoff+nx]
            r = map_data(da3)
            if ch not in results:
                results[ch] = list()
            results[ch].append(r)
        xoff = nx
        for yoff in range(0+2, ny*2-1-2):
            da3 = da2[yoff:yoff+ny, xoff-1:xoff+nx-1]
            r = map_data(da3)
            if ch not in results:
                results[ch] = list()
            results[ch].append(r)
    return results


def test_image():
    w = 400
    h = 220
    img = Image.new('L', (w, h))
    draw = ImageDraw.Draw(img)
    draw.rectangle((0, 0, w, h), fill=(255))
    draw.rectangle((11, 21, 40, 62), outline=(0))
    draw.rectangle((100, 21, 140, 62), outline=(0))
    draw.rectangle((0, 0, w-8, h-16), outline=(0))
    draw.line((0, 0, w/2, h), fill=(0))
    draw.line((40, 35, 100, 35), fill=(0))
    draw.pieslice((200, 20, 300, 150), 30, 320, outline=(0))
    #draw.ellipse((80, 80, 300, 180), outline=(0))
    pix = np.clip(np.array(ImageOps.invert(img)), 0, 1)
    return { "img" : img, "arr" : pix }

def match_image(font, image):
    """ Create an ascii array that matches image.  font:  the output
    of fontToImages(font_small).  image:  a dict of the form 
    { "arr" : np.array(), "img" : PIL image"""
    results = list()
    arr = image["arr"]
    h, w = np.shape(arr)
    nx = w / fontsize[0] - 1
    ny = h / fontsize[1] - 1
    for char_y in range(ny):
        line = ""
        for char_x in range(nx):
            ix = char_x*fontsize[0]
            ix1 = ix + fontsize[0]
            iy = char_y*fontsize[1]
            iy1 = iy + fontsize[1]
            snippet = arr[iy:iy1, ix:ix1]
            ch, ch_img, ch_arr = match_snippet(font, snippet)
            line = line + ch
        results.append(line)
    return results
                                                   
def match_snippet(font, snippet):
    arr = snippet
    best_ch = None
    best_dist = None
    if (np.sum(arr) == 0):
        return [" ", font[" "][0]["img"], font[" "][0]["arr"]]
    for ch in font:
        if ch == ' ':
            continue # Don't match " "
        for i in range(len(font[ch])):
            ch_img = font[ch][i]["img"]
            ch_arr = font[ch][i]["arr"]
            dist = np.sqrt(np.average(pow(ch_arr - arr, 2)))
            if (best_ch == None) or (dist < best_dist):
                best_ch = ch
                best_dist = dist
                best_img = ch_img
                best_arr = ch_arr
    return [best_ch, best_img, best_arr]

font = fontToImages(font_small)


def find_bounding_box(object_list):
    minx, maxx, miny, maxy = None, None, None, None
    
    for obj in object_list:
        if obj[0] == 'text':
            x1, y1 = obj[2:4]
            buf = StringIO.StringIO(obj[1])
            lines = buf.readlines()
            y2 = y1 + len(lines)*7
            mx2 = len(lines[0])
            for L in lines:
                mx2 = max(mx2, len(L))
            x2 = x1 + mx2
        else:
            x1, y1, x2, y2 = obj[1:]
            x2 = x2 + x1
            y2 = y2 + y1
        mxx = max(x1, x2)
        mnx = min(x1, x2)
        mxy = max(y1, y2)
        mny = min(y1, y2)
        if minx == None:
            minx = mnx
            maxx = mxx
            miny = mny
            maxy = mxy
        
        minx = min(mnx, minx)
        miny = min(mny, miny)
        maxx = max(mxx, maxx)
        maxy = max(mxy, maxy)
    return int(minx), int(maxx), int(miny), int(maxy)
            
def create_image(object_list):
    minx, maxx, miny, maxy = find_bounding_box(object_list)

    w = int(maxx - minx)+14
    h = int(maxy - miny)+14
    img = Image.new('L', (w, h))
    draw = ImageDraw.Draw(img)
    draw.rectangle((0, 0, w, h), fill=(255))
    for obj in object_list:
        if obj[0] == 'text':
            pass
        else:
            t, x1, y1, w, h = obj
            x1 = int(round(x1 - minx))
            y1 = int(round(y1 - miny))
            w  = int(round(w))
            h  = int(round(h))
                
            if t == 'rect':
                draw.rectangle((x1, y1, x1+w, y1+h), outline=(0))
            if t == 'ellipse':
                draw.ellipse((x1, y1, x1+w, y1+h), outline=(0))
            if t == 'line':
                draw.line((x1, y1, x1+w, y1+h), fill=(0))

    pix = np.clip(np.array(ImageOps.invert(img)), 0, 1)
    img =  { "img" : img, "arr" : pix }
    result = match_image(font, img)
    for obj in object_list:
        if obj[0] == 'text':
            text, x, y = obj[1:]
            x = x - minx
            y = y - miny
            buf = StringIO.StringIO(text)
            newx = int(x/fontsize[0])
            newy = int(y/fontsize[1])
            for line in buf.readlines():
                line = line.rstrip()
                # Replace the chars in results[newy] starting at newx with line
                starti = newx
                endi = newx + len(line)
                a = result[newy][0:starti]
                b = line
                c = result[newy][endi:]
                result[newy] = "%s%s%s" % (a, b, c)
                newy = newy + 1

    return result
                
if __name__ == '__main__':
    ti = test_image()
    #ti["img"].show()
    #font["|"]["img"].show()
    match_image(font, ti)
    exit()
    match_snippet(font, ti)


    #im = Image.new('RGB', fontsize)
    #draw = ImageDraw.Draw(im)
    #draw.rectangle((0, 0, 5, 7), fill=(255, 255, 255))
    #im = im.resize((50, 70), Image.ANTIALIAS)
    #im.show()
