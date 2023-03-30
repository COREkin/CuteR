from CuteR import CuteR as cr
from PIL import Image
import glob
import os

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

def convert(url_dict,image_list, add_margin_num):
    output_list =[]
    expanded_list = []
    for image in image_list:
        image_name, a = os.path.splitext(os.path.basename(image))
        for name ,url in url_dict.items():
            output_list.append([cr.produce(url,image,colourful=True), name + "_" + image_name])
    print("\n output_list: \n %s" % output_list)
    print("\n saving images...")
    savepng(output_list)
    if add_margin_num:
        for output in output_list:
            output[1] = output[1] + "_expanded"
            expanded_list.append([[add_margin(output[0][0],add_margin_num,add_margin_num,add_margin_num,add_margin_num,(255,255,255))],output[1]])
    
        print("\n expanded_list: \n %s" % expanded_list)
        print("\n saving images...")
        savepng(expanded_list)

def savepng(output_list):
    for output in output_list:
        output[0][0].save(f'./output/{output[1]}_QR.png',save_all=True,append_images=[],duration=100,optimize=True)
    

if __name__ == '__main__':
    add_margin_num = 255 
    url_dict = {}
    image_list = []

    #path = os.path.abspath('.')
    print("import files.")
    files = glob.glob("./images/*")

    for file in files:
        image_list.append(file)

    print("\n image_list: %s" % image_list)

    print("setting urls.")
    url_dict["blog"] = "https://kin-archive.tistory.com/"
    url_dict["linkedin"] = "https://www.linkedin.com/in/dongsik-kim-b1725b194/"
    url_dict["insta"] = "https://www.instagram.com/initial_dongsik/"
    url_dict["github"] = "https://github.com/COREkin/COREkin"
    
    print("\n url_dict: %s" % url_dict)

    print("\n converting images...")
    output_list = convert(url_dict, image_list, add_margin_num)
    
    print("\ncomplete.\n")