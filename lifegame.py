import matplotlib.pyplot as plt
import matplotlib.animation as anm
import numpy as np
import os
from PIL import Image
from tqdm import tqdm
from datetime import datetime

# size = 50x50
"""
# initial structures. "1" means LIVING.
"""
def glider():
    form = np.zeros((50,50), dtype=int)
    form[25][25] = 1
    form[25][26] = 1
    form[25][27] = 1
    form[26][25] = 1
    form[27][26] = 1
    return form

def pentadecathlon():
    form  = np.zeros((50,50), dtype=int)
    for p in range(10):
        form[15][10+p] = 1
    return form

def switchengine(): # needs 100x100 pixels
    form = np.zeros((50,50), dtype=int)
    return form

def glidergun():
    form = np.zeros((50,50), dtype=int)
    x = [2, 3, 2, 3,14,15,13,12,12,12,13,14,
         15,17,18,18,19,18,17,16,22,22,22,23,
         23,23,24,24,26,26,26,26,36,37,36,37]
    y = [6, 6, 7, 7, 4, 4, 5, 6, 7, 8, 9,10,
         10, 5, 6, 7, 7, 8, 9, 7, 4, 5, 6, 4,
         5, 6, 3, 7, 2, 3, 7, 8, 4, 4, 5, 5]
    for c in range(len(x)):
        i = x[c]
        j = y[c]
        form[j][i] = 1
    return form

def galaxy():
    form = np.zeros((50,50), dtype=int)
    ls = [[20, 20], [21, 20], [20, 21], [21, 21], [20, 22], [21, 22],
          [20, 23], [21, 23], [20, 24], [21, 24], [20, 25], [21, 25],
          [23, 20], [23, 21], [24, 20], [24, 21], [25, 20], [25, 21], 
          [26, 20], [26, 21], [27, 20], [27, 21], [28, 20], [28, 21], 
          [20, 27], [20, 28], [21, 27], [21, 28], [22, 27], [22, 28], 
          [23, 27], [23, 28], [24, 27], [24, 28], [25, 27], [25, 28], 
          [27, 23], [28, 23], [27, 24], [28, 24], [27, 25], [28, 25], 
          [27, 26], [28, 26], [27, 27], [28, 27], [27, 28], [28, 28]]
    for p,q in ls:
        form[p][q] = 1
    return form


"""
Lifegame's rule and making each image
"""
# 周囲のセルの情報を処理し生死の判定
def judge(x,y, form):
    ran = ((-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1))  # surrounded 8 cells
    c = 0 #counter of living cells nearby
    for p,q in ran:
        try:
            if form[x-p][y-q] == 1:
                c += 1
        except IndexError:
            pass
    
    # lod (live or die). "1" means LIVING
    if form[x][y] == 1:
        if c == 2 or c == 3:
            lod = 1
        else:
            lod = 0
    elif form[x][y] == 0:
        if c == 3:
            lod = 1
        else:
            lod = 0

    return lod

# 全セルの次世代の生死情報
def pic(oldform):
    size = 50
    newform = np.zeros((size,size), dtype=int)
    for i in range(size):
        for j in range(size):
            newform[i][j] = judge(x=i, y=j, form=oldform)
    #im = plt.pcolor(newform, cmap=plt.cm.binary)
    return newform

# 引数配列を描画して保存（画像生成）. dir作成して画像保存
def makepic(conc,a):
    im = plt.pcolor(conc, cmap=plt.cm.binary)
    os.makedirs("python_lifegame", exist_ok=True)
    name = str(a) + ".png"
    plt.savefig(os.path.join("python_lifegame", name))
    return im


"""
making stack tiff from each image
"""
# make tif
def saveTiffStack(save_path, imgs):
    stack = []
    print("\nmaking Tiff.....")
    for img in tqdm(imgs):
        stack.append(Image.fromarray(img))
    stack[0].save(save_path, compression="tiff_deflate", 
    save_all=True, append_images=stack[1:])

# images list
def make_imgs():
    imgs = []
    #for p in glob.glob(os.path.join("python_lifegame", "*.png")):
    print("\nmaking png list.....")
    for i in tqdm(range(100)):
        name = str(i) + ".png"
        p = os.path.join("python_lifegame", name)
        im = np.array(Image.open(p))
        imgs.append(im)
    return imgs


"""
main
"""
def main():
    print("\nSelect the initial structure")
    print("g: glider, p: pentadecathlon, gg: glidergun, sw: switchengine, gl: galaxy")
    st = input("g or p or or gg or sw or gl >>>")   # initial structureを選択できる
    sts = {"g": glider(), "p": pentadecathlon(), "gg": glidergun(), "sw": switchengine(), "gl": galaxy()}
    conc = sts[st] # initial structure

    fig = plt.figure() # figure instance
    #ims = []
    #plt.pcolor(conc, cmap=plt.cm.binary)
    #plt.show()
    print("calculation processing.....")
    for _ in tqdm(range(100)): # 100世代計算
        im = makepic(conc, _)  # tif用の一枚の画像を生成しpython_lifegameの直下に保存
        #ims.append(im)
        conc = pic(conc)       # 世代を次に
    
    imgs = make_imgs()                                             # 1枚ずつの画像をnumpyで読み込み
    save_path = datetime.now().strftime("%Y%m%d-%H%M%S") + ".tif"  # tifの保存先
    #save_path = os.path.join("python_lifegame", "st1.tif")
    saveTiffStack(save_path, imgs)                                 # 画像をtifに合成

if __name__ == "__main__":
    main()

#######################
## tif形式でしか出力ができないのが渋いかも
## ImageJでaviに変換すれば誰でも見れる？
#######################