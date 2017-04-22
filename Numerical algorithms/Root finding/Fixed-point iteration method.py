from   math import sin, cos, e
import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return x**2-2
def fp(x):
    return 2*x

def iterationMethod(a, b, f, fp, eps_x, eps_y, max_n):
    #третий аргумент return - false , если корень не найден
    n = 0    
    for x0 in [a,b]:
        
        #подбираем lambd
        #lmbd == false => lambda = 1
        #lmbd == true  => lambda = 1/fp(x)
        lmbd = False
        x1 = x0 - f(x0)
        x2 = x1 - f(x1)

        if abs(x2 - x1) > abs(x1 - x0):
            lmbd = True 
            if (fp(x1) == 0) or (fp(x0) == 0)  :
                return x1, n, False
            x1 = x0 - f(x0)/fp(x0)
            x2 = x1 - f(x1)/fp(x1)
            if abs(x2 - x1) > abs(x1 - x0):
                return x1, n, False
            
        while True:
            n += 1     
            
            if not lmbd:
                x1 = x0 - f(x0)
            else:
                x1 = x0 - f(x0)/fp(x0)
            #условия завершения
            if eps_x > 0:
                if abs(x1 - x0) < eps_x:
                    return x1, n, True
            if eps_y > 0:
                if abs(f(x1) - f(x0)) < eps_y:
                    return x1, n, True
            if n >= max_n:
                return x1, n, True
            if  not (a<=x1<=b):                
                #если произошел выход за границы
                #обычно срабатывает при отстутсвии корня
                break
            
            x0 = x1
            
        #если не найдено корней, то
        return x1, n, False
        
            

def generateRootsData(a, b, h, eps_x, eps_y, max_n):
    ah = a
    bh = a + h
    roots_data = []
    step = 1
    while bh <= b:
        x, n, finded = iterationMethod(ah, bh, f, fp, eps_x, eps_y, max_n)
        if finded:            
            left_border  = ah
            right_border = bh
            root         = x
            value        = f(x)
            iteration_n  = n
            if n >= max_n:
                err_code = 1
            else:
                err_code = 0
            if not x in [i[2] for i in roots_data]:
                roots_data.append([left_border, right_border, root, value, iteration_n, err_code])

        step += 1            
        ah = a + h * (step - 1)
        bh = a + h * step
        if bh > b:
            if ah > b:
                break
            else:
                bh = b   
    return roots_data

def inputData():
    inp   = input('Введите интервал поиска [A,B] в формате "A,B":  ')
    a,b   = map(float, inp.split(','))
    inp   = input('Введите шаг h:                                  ')
    h     = float(inp)
    inp   = input('Введите ? по x, если требуется:                 ')
    if inp.strip() == '':
        eps_x = 0
    else:        
        eps_x = float(inp)
    inp   = input('Введите ? по y, если требуется:                 ')
    if inp.strip() == '':
        eps_y = 0
    else:        
        eps_y = float(inp)
    inp   = input('Введите предельное число итераций n_max >= 100: ')
    max_n = int(inp)
    if not (max_n>=100):
        print('Неверный ввод!')
        return 0
    return a, b, h, eps_x, eps_y, max_n
    
    
def printTable(data, max_n):    
    # расчет форматированной строки
    maxalen     = len( str(data[-1][0]) + str(data[-1][1]) )
    abrowlen    = maxalen + 5
    iterrowlen  = len('кол-во итераций') + 2
    errrowlen   =  len('код ошибки') + 2
    table_width = (1 + 9 + 1 + abrowlen + 1 
                  + 14 + 1 + 15 + 1 + iterrowlen + 1 + errrowlen+1)
    t_row  = ('|{:^9}|{:^'+str(abrowlen)+'}|{:^14}|{:^15}|{:^'+str(iterrowlen)
              +'}|{:^'+str(errrowlen)+'}|')
    t_head = t_row.format('№ корня','[А,B]','корень','f(x)','кол-во итераций',
                          'код ошибки')   

    print('-'*table_width)
    print(t_head)
    print('|','-'*(table_width-2),'|', sep='')
    n = 0
    for i in data:
        n += 1
        arg1 = n
        arg2 = ('['+'{:g}'.format(i[0])+','
                +'{:g}'.format(i[1])+']')
        arg3 = '{:g}'.format(i[2])
        arg4 = '{:.0e}'.format(i[3])
        arg5 = i[4]
        arg6 = i[5]
        if arg6 != 0:
            arg3 = arg4 = '-'
        print(t_row.format(arg1, arg2, arg3, arg4, arg5, arg6 ))
    print('-'*table_width)

    print('Коды ошибок: ')
    print('0 - нет ошибки')
    print('1 - достигнуто максимальное количество итераций')    


  
def drawPlot(data, a, b):
    x_f = np.linspace(a,b, 1000)
    y_f = list(map(f, x_f))
    x_roots = []
    y_roots = []
    point_text = []
    for row in range(len(data)):
        if data[row][5] == 0:
            x_roots.append(data[row][2])
            y_roots.append(data[row][3])
            point_text.append(row+1)
            
    bottom = min(y_f)
    top    = max(y_f)
    if bottom > 0:
        bottom*=0.9
    elif bottom < 0:
        bottom*=1.1
    #else:
    #    bottom = -top * 0.1
    if top > 0:
        top*=1.1
    elif top < 0:
        top*=0.9
    #else:
    #    top = -bottom * 0.1
    

    ax = plt.subplot()
     
    plt.axis([a,b, bottom, top])
    plt.title('Finding roots of f(x) with fixed-point iteration method')
    plt.xlabel('x')
    plt.ylabel('f(x)')   
    
    plt.plot(x_f,y_f, '-', color='blue', label='f(x)')    
    plt.plot(x_roots, y_roots, 'bo', color='red', label = 'finded roots')

    for i in range(len(x_roots)):
        ax.annotate('#'+str(point_text[i]), (x_roots[i],y_roots[i]))    
    plt.legend()   
    
    plt.plot([a,b], [0,0], '-', color='black')
    plt.plot([0,0], [bottom,top], '-', color='black')
    
    plt.show()


def main():   
    while 1:
        print('=== Уточнение корня методом подбора с итерацией ===')
        #ввод данных
        inp_data = inputData()
        if inp_data == 0:
            return
        else:
            a, b, h, eps_x, eps_y, max_n = inp_data

        #генерация и вывод таблицы
        print()
        print('               -  поиск корней  -                  ')
        roots_data = generateRootsData(a, b, h, eps_x, eps_y, max_n)
        if len(roots_data) == 0:
            print('Корней не найдено!')
        else:
            printTable(roots_data, max_n)
        drawPlot(roots_data, a, b)


        #просьба еще одного ввода
        print()
        inp = input('Введите 1, чтобы ввести новые данные: ')
        if inp!='1':
            break
        else:
            print()
            print()
        
    
    
main()

