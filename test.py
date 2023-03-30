from CuteR import CuteR as cr
from PIL import Image

g = globals()

def expand2square(pil_img, background_color):
    width, height = pil_img.size
    if width == height:
        return pil_img
    elif width > height:
        result = Image.new(pil_img.mode, (width, width), background_color)
        result.paste(pil_img, (0, (width - height) // 2))
        return result
    else:
        result = Image.new(pil_img.mode, (height, height), background_color)
        result.paste(pil_img, ((height - width) // 2, 0))
        return result

def add_margin(pil_img, top, right, bottom, left, color):
    width, height = pil_img.size
    new_width = width + right + left
    new_height = height + top + bottom
    result = Image.new(pil_img.mode, (new_width, new_height), color)
    result.paste(pil_img, (left, top))
    return result

def main(urlList,imageList):
    outputList =[]
    for i in range(0,len(urlList)):
        outputList.append(cr.produce(urlList[i],imageList[i],colourful=True))
    
    return outputList

if __name__ == '__main__':
    nameList = []
    urlList = []
    imageList = []

    nameList.append("blog")
    urlList.append("https://kin-archive.tistory.com/")
    imageList.append('kin.png')

    nameList.append("linkedin")
    urlList.append("https://www.linkedin.com/in/dongsik-kim-b1725b194/")
    imageList.append('kin.png')

    nameList.append("insta")
    urlList.append("https://www.instagram.com/initial_dongsik/")
    imageList.append('kin.png')

    nameList.append("katalk")
    urlList.append("https://kin-archive.tistory.com/")
    imageList.append("ajisai.jpg")

    nameList.append("line")
    urlList.append("https://www.linkedin.com/in/dongsik-kim-b1725b194/")
    imageList.append("ajisai.jpg")
    
    nameList.append("github")
    urlList.append("https://github.com/COREkin/COREkin")
    imageList.append('kin.png')

    outputList = main(urlList,imageList)
    for i in range(0,len(outputList)):
        outputList[i][0].save('kin{0}QR.png'.format(nameList[i]),save_all=True,append_images=[],duration=100,optimize=True)
    print("\n\n outputList: \n %s \n" % outputList)


    expand_num = 265
    expandedList=[]
    for i in range(0,len(outputList)):
        expandedList.append([add_margin(outputList[i][0],expand_num,expand_num,expand_num,expand_num,(255,255,255))])

    print("\n\n expandedList: \n %s \n" % expandedList)
    for i in range(0,len(expandedList)):
        expandedList[i][0].save('expandkin{0}QR.png'.format(nameList[i]),save_all=True,append_images=[],duration=100,optimize=True)
    
    print("complete.")