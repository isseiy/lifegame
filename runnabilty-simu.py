import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from datetime import datetime
import os


def make_conc():
# (100,200)をピーク座標として誘引物質の分布の配列
    ls = []
    for p in range(1000):
        for q in range(1000):
            value = 255-np.sqrt((p-100)*(p-100)+(q-200)*(q-200))/5
            ls.append(value)

    conc = np.array(ls).reshape(1000,1000)
    return conc

def move(conc, turnBase, turnCoeff, ax, col):
# 1個体について時刻で毎回計算
    xOld = round(random.random() * 1000)   # initial x
    yOld = round(random.random() * 1000)   # initial y
    direction = random.random()*2*np.pi    # initial direction
    dx = round(15 * np.cos(direction))     # initial dx
    dy = round(15 * np.sin(direction))     # initial dy
    concOld = conc[xOld][yOld]          # initial conc
    x = [xOld]
    y = [yOld]
    for t in range(100):
        xNew = int(xOld + dx)
        yNew = int(yOld + dy)
        
        if xNew > 1000:
            dx = -dx
        if xNew < 0:
            dx = -dx
        if yNew > 1000:
            dy = -dy
        if yNew < 0:
            dy = -dy
        #print(xNew,yNew)
        try:
            concNew = conc[xNew][yNew]
        except IndexError:
            concNew = concOld
        concDif = concNew - concOld
        turnProb = concDif * turnBase + turnCoeff
        r = random.random()
        if r < turnProb:
            direction = random.random()*2*np.pi
            dx = round(15 * np.cos(direction))
            dy = round(15 * np.sin(direction))
            print("CCCCCCCC", r, turnProb)
        else:
            print("NNNNNNNN", r, turnProb)
        
        x.append(xNew)
        y.append(yNew)
        xOld = xNew
        yOld = yNew
        concOld = concNew
        #print(r, turnProb)
    
    ax.plot(x, y, color=col)        

def main():
    # parameters  
    turnBase = 1   # if +, evated. if -, attracted.
    turnCoeff = -0.2  # if large, easy to change direction
    
    # colours
    cols = list(matplotlib.colors.cnames.keys())
    le = len(cols)
    
    # plot
    fig, ax = plt.subplots()
    conc = make_conc()   # concentration profile
    for _ in range(10):  # 50 indivisuals iteration
        move(conc, turnBase, turnCoeff, ax, col=cols[random.randint(0,le)])
    ax.pcolor(conc, cmap=plt.cm.binary)
    title = "TurnBase = " + str(turnBase) + ", TurnCoeff = " + str(turnCoeff)
    plt.title(title)
    
    name = datetime.now().strftime("%Y%m%d-%H%M%S") + ".png"
    os.makedirs("python_output", exist_ok=True)
    plt.savefig(os.path.join("python_output", name))
    plt.show()

if __name__ == "__main__":
    main()