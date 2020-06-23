import glob
import os
import cv2

output_dirpath = "~/python_lifegame"

# VideoCapture を作成する。
img_path = glob.glob(os.path.join(output_dirpath, '0.png'))  # 画像ファイルのパス
cap = cv2.VideoCapture(img_path)

# 画像の大きさを取得
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# フレームレートを設定
fps = 60 
print('width: {}, height: {}, fps: {}'.format(width, height, fps))

# VideoWriter を作成する。
fourcc = cv2.VideoWriter_fourcc(*'X264')
writer = cv2.VideoWriter('output.mp4', fourcc, fps, (width, height))

while True:
   # 1フレームずつ取得する。
   ret, frame = cap.read()
   if not ret:
       break  # 映像取得に失敗
   
   writer.write(frame)  # フレームを書き込む。

writer.release()
cap.release()