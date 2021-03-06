import numpy as np
import cv2

# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_image_display/py_image_display.html

# 1. membuat objek dengan nama img, untuk menampung gambarnya
# kalau nilainya 1 -> berwarna, kalau 0 jadi hitam putih
img = cv2.imread('test_gambar.png', 1)

# 2. cara menampilkan gambar si objek img
cv2.imshow('gambarnya', img)

# 4. cara menambahkan aksi jika di pencet kecuali esc maka gambar akan di save
k = cv2.waitKey(0)
if k == 27:
    print(k)
    cv2.destroyAllWindows()
else:
    # 3. cara nge write gambar atau nge save/save as gambar
    print(k)
    cv2.imwrite('gambar_baru.png', img)

    # 3. test save gambar menjadi hitam putih
    print(k)
    img_hitam_putih = cv2.imread('test_gambar.png', 0)
    cv2.imwrite('gambar_hitam_putih.png', img_hitam_putih)
