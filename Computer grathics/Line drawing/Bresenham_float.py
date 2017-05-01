def line_br_float(win, p1, p2):
    if p1 == p2:
        win.image.setPixel(p1[0], p1[1], win.pen.color().rgb())
        return

    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    sx = sign(dx)
    sy = sign(dy)
    dx = abs(dx)
    dy = abs(dy)
    x = p1[0]
    y = p1[1]

    change = False

    if dy > dx:
        temp = dx
        dx = dy
        dy = temp
        change = True

    h = dy / dx

    e = h - 0.5
    i = 1
    while i <= dx:
        win.image.setPixel(x, y, win.pen.color().rgb())
        if e >= 0:
            if change is False:
                y += sy
            else:
                x += sx
            e -= 1

        if e < 0:
            if change is False:
                x += sx
            else:
                y += sy
            e += h
        i+=1