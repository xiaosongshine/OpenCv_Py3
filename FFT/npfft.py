import numpy as np
import cv2
import matplotlib.pyplot as plt


img = cv2.imread("../image/lena.bmp", 0)

f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
rows, cols = (fshift.shape)
frows, fcols = int(rows / 2), int(cols / 2)
result = 20 * np.log(np.abs(fshift))

ffshift = np.zeros(shape=result.shape,dtype=np.float64)

ffshift *= result[frows-100: frows+100, fcols-100: fcols+100]


ishift = np.fft.ifftshift(ffshift)
iimg = np.fft.ifft2(ishift)
imgs= np.abs(iimg)



imgss = img - imgs



plt.subplot(221)
plt.imshow(img, cmap="gray")
plt.title("original")
plt.axis("off")

plt.subplot(222)
plt.imshow(result, cmap="gray")
plt.title("result")
plt.axis("off")

plt.subplot(223)
plt.imshow(imgs, cmap="gray")
plt.title("ifft")
plt.axis("off")

plt.subplot(224)
plt.imshow(imgss, cmap="gray")
plt.title("ifft")
plt.axis("off")


plt.show()
