def line_br_smooth(win, p1, p2):
    if p1 == p2:
        win.image.setPixel(p1[0], p1[1], win.pen.color().rgb())
        return

    win.pen.setColor(win.color_line)
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    sx = sign(dx)
    sy = sign(dy)
    dx = abs(dx)
    dy = abs(dy)
    x = p1[0]
    y = p1[1]

    try:
        h = dy / dx
    except ZeroDivisionError:
        h = 0


    isBlack = False

    if win.pen.color() == Qt.black:
        i_max = 256
        isBlack = True
    else:
        i_max = 100

    change = False

    if dy > dx:
        temp = dx
        dx = dy
        dy = temp
        change = True
        if h:
            h = 1 / h

    h *= i_max
    e = i_max/2
    w = i_max - h
    i = 1
    while i <= dx:
        if not isBlack:
            new = win.pen.color()
            new.lighter(100 + e)
            win.pen.setColor(new)
            win.image.setPixel(x, y, win.pen.color().rgba())
        else:
            new = QColor()
            new.setRgb(0, 0, 0, alpha=255 - e)
            win.pen.setColor(new)
            win.image.setPixel(x, y, win.pen.color().rgba())
        if e <= w:
            if change:
                y += sy
            else:
                x += sx
            e += h
        else:
            x += sx
            y += sy
            e -= w
        i += 1
