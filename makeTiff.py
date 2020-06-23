from PIL import Image
import numpy as np
import glob
import os

def saveTiffStack(save_path, imgs):
    stack = []
    for img in imgs:
        stack.append(Image.fromarray(img))
    stack[0].save(save_path, compression="tiff_deflate", 
    save_all=True, append_images=stack[1:])

def make_imgs():
    imgs = []
    #for p in glob.glob(os.path.join("python_lifegame", "*.png")):
    for i in range(100):
        name = str(i) + ".png"
        p = os.path.join("python_lifegame", name)
        im = np.array(Image.open(p))
        imgs.append(im)
    return imgs

if __name__ == "__main__":
    imgs = make_imgs()
    save_path = os.path.join("python_lifegame", "st1.tif")
    saveTiffStack(save_path, imgs)


"""
reference
https://qiita.com/machisuke/items/0ca8a09d79bd5eba3cf3

"""