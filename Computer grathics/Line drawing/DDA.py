

def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0


def line_DDA(win, p1, p2):
    # Длина и высота линии
    deltaX = abs(p1[0] - p2[0])
    deltaY = abs(p1[1] - p2[1])

    # Считаем минимальное количество итераций, необходимое для отрисовки отрезка.
    # Выбирая максимум из длины и высоты линии, обеспечиваем связность линии

    length = max(deltaX, deltaY)

    # особый случай, на экране закрашивается ровно один пиксел
    if length == 0:
        win.image.setPixel(p1[0], p1[1], win.pen.color().rgb())
        return

    # Вычисляем приращения на каждом шаге по осям абсцисс и ординат double
    dX = (p2[0] - p1[0]) / length
    dY = (p2[1] - p1[0]) / length

    # Начальные значения
    x = p1[0] + 0.5 * sign(dX)
    y = p1[1] + 0.5 * sign(dY)

    # Основной цикл
    while length > 0:
        win.image.setPixel(x, y, win.pen.color().rgb())
        x += dX
        y += dY
        length -= 1