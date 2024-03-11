w, h, f, c, x1, y1, x2, y2 = map(int, input().split())
standard = min(f, w - f)
if x2 <= standard:
    print(w * h - (x2 - x1) * (y2 - y1) * (c + 1) * 2)
elif x1 < standard:
    print(w * h - ((y2 - y1) * (c + 1) * ((standard - x1) * 2 + (x2 - standard))))
else:
    print(w * h - (x2 - x1) * (y2 - y1) * (c + 1))
