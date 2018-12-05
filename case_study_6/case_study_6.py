"""Case-study 6
   Developers:
   A. Zelenskaya, M. Zolotych, A. Sherubneva"""

from turtle import *

width(1)


def color_choice():
    cc = str('')
    while cc != 'красный' and cc != 'синий' and cc != 'зеленый' and cc != 'желтый' and cc != 'оранжевый' and cc != 'пурпурный' and cc != 'розовый':
        cc = textinput('COLOR', 'Пожалуйста, введите цвет. Допустимые цвета: красный, синий, зеленый, желтый, оранжевый, пурпурный, розовый.').lower()
    return cc


def d(n):
    p = 500 / int(n)
    return p


def h(p):
    d1 = p / 2
    s = d1 / ((3**0.5) / 2)
    return s


def figure(s, p, n, col_1, col_2):
    speed(500)
    x = -350
    y = 300
    n = int(n)
    r = n // 2
    penup()
    goto(x, y)
    pendown()
    pp = 1
    for l in range(r):
        color('black')
        if col_1 == 'красный':
            color_1 = 'red'
        if col_1 == 'синий':
            color_1 = 'blue'
        if col_1 == 'зеленый':
            color_1 = 'green'
        if col_1 == 'желтый':
            color_1 = 'yellow'
        if col_1 == 'оранжевый':
            color_1 = 'orange'
        if col_1 == 'пурпурный':
            color_1 = 0.83,0.26,0.8
        if col_1 == 'розовый':
            color_1 = 'pink'

        if col_2 == 'красный':
            color_2 = 'red'
        if col_2 == 'синий':
            color_2 = 'blue'
        if col_2 == 'зеленый':
            color_2 = 'green'
        if col_2 == 'желтый':
            color_2 = 'yellow'
        if col_2 == 'оранжевый':
            color_2 = 'orange'
        if col_2 == 'пурпурный':
            color_2 = 0.83,0.26,0.8
        if col_2 == 'розовый':
            color_2 = 'pink'


        nn = 1
        n = int(n)
        if pp % 2 == 0:
            color_1, color_2 = color_1, color_2
        else:
            color_1, color_2 = color_2, color_1
        for i in range(n):
            if nn % 2 == 0:
                fillcolor(color_2)
            else:
                fillcolor(color_1)
            begin_fill()
            right(-30)
            forward(s)
            for q in range(5):
                right(60)
                forward(s)
            end_fill()
            right(90)
            penup()
            forward(p)
            pendown()
            nn += 1
            continue
        right(90)
        penup()
        forward(s)
        forward(s)
        left(-60)
        forward(s)
        pendown()
        left(-30)
        nn = 1
        for i in range(n):
            if nn % 2 == 0:
                fillcolor(color_1)
            else:
                fillcolor(color_2)
            begin_fill()
            right(-30)
            forward(s)
            for q in range(5):
                right(60)
                forward(s)
            end_fill()
            right(90)
            penup()
            forward(p)
            pendown()
            nn += 1
            continue
        pp += 1
        right(90)
        penup()
        forward(s)
        forward(s)
        left(-60)
        forward(s)
        left(-30)
        right(90)
        forward(3 * s)
        right(-90)
        pendown()
    mainloop()


def main():
    # Selection of colors.

    col_1 = color_choice()
    col_2 = color_choice()

    # Selection of the number of figures.

    n = numinput('n', 'Пожалуйста, введите количество шестиугольников, располагаемых в ряд. Допустимые значения - от 4 до 20.', 0, minval=4, maxval=20)

    # Drawing of shapes.

    p = d(n)
    a = h(p)
    figure(a, p, n, col_1, col_2)


if __name__ == '__main__':
    main()