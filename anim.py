import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()

ims = []

for i in range(1000):
        rand = np.random.randn(100)     # 100個の乱数を生成
        im = plt.plot(rand)             # 乱数をグラフにする
        ims.append(im)                  # グラフを配列 ims に追加

# 10枚のプロットを 100ms ごとに表示
ani = animation.ArtistAnimation(fig, ims, interval=10)
plt.show()
#ani.save("output.gif", writer="pillow")


def galaxy():
    form = np.zeros((50,50), dtype=int)
    ls = [[20, 20], [21, 20], [20, 21], [21, 21], [20, 22], [21, 22],
          [20, 23], [21, 23], [20, 24], [21, 24], [20, 25], [21, 25],
          [23, 20], [23, 21], [24, 20], [24, 21], [25, 20], [25, 21], 
          [26, 20], [26, 21], [27, 20], [27, 21], [28, 20], [28, 21], 
          [20, 27], [20, 28], [21, 27], [21, 28], [22, 27], [22, 28], 
          [23, 27], [23, 28], [24, 27], [24, 28], [25, 27], [25, 28], 
          [27, 23], [28, 23], [27, 24], [28, 24], [27, 25], [28, 25], 
          [27, 26], [28, 26], [27, 27], [28, 27]]
    for p,q in ls:
        form[p][q] = 1
    return form

print(galaxy())