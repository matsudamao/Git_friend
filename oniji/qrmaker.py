import sys
import qrcode
import os
args = sys.argv
file_name = args[1]

path = os.path.join("../",file_name)

with open (file_name, mode = "r", encoding = "utf-8") as file:
    for i, line in enumerate(file):
        # QRコードの作成
        img = qrcode.make(line)
        # ファイルに保存
        img.save(str(i) + ".png")