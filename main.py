def p(x): return x ** 4


def q(x): return 1 - x ** 3


def f(x): return x ** 3 + 8


alf0 = -1
alf1 = 1
A = 1
a = 0
B = 0
b = 1
be0 = 0
be1 = 1

for n in [10, 20]:
    print('n =', n)
    print('n   x_i    y_i      m_i     r_i     fi_i     c_i      d_i')
    h = 1 / n
    X = []
    x_0 = 0
    for i in range(n + 1):
        X.append(round(x_0 + h * i, 2))
    c0 = -1 / (h + 1)
    d0 = -h
    M = []
    R = []
    FI = []
    C = []
    D = []
    Y = []
    for i in range(n + 1):
        m_i = (2 * h * h * (1 - X[i] ** 3) - 4) / (2 + h * X[i] ** 4)
        M.append(m_i)
        r_i = (2 - h * (X[i] ** 4)) / (2 + h * (X[i] ** 4))
        R.append(r_i)
        fi_i = (2 * h * h * (X[i] ** 3 + 8)) / (2 + h * (X[i] ** 4))
        FI.append(fi_i)
        if i != 0:
            c_i = 1 / (M[i] - R[i] * C[i - 1])
        else:
            c_i = c0
        C.append(c_i)
        if i != 0:
            d_i = FI[i] - R[i] * C[i-1] * D[i-1]
        else:
            d_i = d0
        D.append(d_i)
    for i in range(n, -1, -1):
        if i == n:
            y_i = (B * h + be0*C[n-1]*D[n-1]) / (be0*(C[n-1]+1)+be1*h)
        else:
            y_i = C[i] * (D[i] - Y[0])
        Y = [y_i] + Y
    for i in range(n + 1):
        if i == 0:
            print('{}   {:.2f}  {:.4f}   {}   {}  {}  {:.4f}  {:.4f}'.format(i, X[i], Y[i], '      ', '      ',
                                                                             '     ', C[i], D[i]))
        elif i == n:
            print('{}  {:.2f}  {:.4f}   {}  {}  {}  {}  {}'.format(i, X[i], Y[i], '   ', '   ',
                                                                   '   ', '   ', '   '))
        elif i >= 10 and n == 20:
            print('{}  {:.2f}  {:.4f}   {:.4f}  {:.4f}  {:.4f}  {:.4f}  {:.4f}'.format(i, X[i], Y[i], M[i], R[i],
                                                                                       FI[i], C[i], D[i]))
        elif i >= 10 and n == 10:
            print('{}  {:.2f}  {:.4f}  {:.4f}  {:.4f}  {:.4f}  {:.4f}  {:.4f}'.format(i, X[i], Y[i], M[i], R[i], FI[i],
                                                                                      C[i], D[i]))
        else:
            if i >= 1 and n == 20:
                print('{}   {:.2f}  {:.4f}   {:.4f}  {:.4f}  {:.4f}  {:.4f}  {:.4f}'.format(i, X[i], Y[i], M[i], R[i],
                                                                                            FI[i], C[i], D[i]))
            else:
                print('{}   {:.2f}  {:.4f}  {:.4f}  {:.4f}  {:.4f}  {:.4f}  {:.4f}'.format(i, X[i], Y[i], M[i], R[i],
                                                                                           FI[i], C[i], D[i]))
    y_0 = (A * h - alf0 * Y[1]) / (h * alf1 - alf0)
    print('|{:.6f} - {:.6f}| = {:.4f}'.format(y_0, Y[0], (y_0 - Y[0])))
