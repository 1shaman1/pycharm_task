from PIL import Image
import numpy as np
img = Image.open("img2.jpg")
arr = np.array(img)
a = len(arr)
a1 = len(arr[1])
i = 0
while i < a:
    j = 0
    while j < a1:
        s = 0
        for n in range(i, i + 10):
            if n >= a:
                break
            for n1 in range(j, j + 10):
                if n1 >= a1:
                    break
                r = int(arr[n][n1][0])
                g = int(arr[n][n1][1])
                b = int(arr[n][n1][2])
                M = int(r + g + b)
                s += M
        s = int(s // 100) / 3
        for n in range(i, i + 10):
            if n >= a:
                break
            for n1 in range(j, j + 10):
                if n1 >= a1:
                    break
                arr[n][n1][0] = int(s // 50) * 50
                arr[n][n1][1] = int(s // 50) * 50
                arr[n][n1][2] = int(s // 50) * 50
        j = j + 10
    i = i + 10
res = Image.fromarray(arr)
res.save('res.jpg')