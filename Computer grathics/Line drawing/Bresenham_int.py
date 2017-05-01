def line_br_int(win, p1, p2):
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

    e = 2 * dy - dx
    i = 1
    while i <= dx:
        win.image.setPixel(x, y, win.pen.color().rgb())
        if e >= 0:
            if change == 0:
                y += sy
            else:
                x += sx
            e -= 2 * dx

        if e < 0:
            if change == 0:
                x += sx
            else:
                y += sy
            e += (2 * dy)
        i += 1
