import sys
from PIL import Image, ImageFilter
import numpy as np

src, dst = sys.argv[1], sys.argv[2]
im = Image.open(src).convert("RGBA").crop((1180, 30, 1910, 470))
w, h = im.size
arr = np.array(im).astype(np.float32)

alpha = Image.fromarray(arr[:, :, 3].astype(np.uint8))
alpha = alpha.point(lambda v: 0 if v < 120 else v).filter(ImageFilter.GaussianBlur(12))
a = np.array(alpha).astype(np.float32) / 255


def smooth(t):
    t = np.clip(t, 0, 1)
    return t * t * (3 - 2 * t)


ys = np.arange(h)[:, None] / h
xs = np.arange(w)[None, :] / w
mask = smooth((ys - 0.15) / 0.55) * smooth((xs - 0.02) / 0.4) * smooth((1 - ys) / 0.12)
arr[:, :, 3] = np.clip(a * mask, 0, 1) * 255

Image.fromarray(arr.astype(np.uint8)).save(dst)
print(dst, w, h)
