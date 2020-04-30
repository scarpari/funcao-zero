import math
import sys

def f(x):
    f = x**2 - 4*x + 3
    return f

def df(x):
    df = 2*x - 4
    return df

def phi(x):
    phi = (x**2 + 3)/4
    return phi

def bisseccao(a,b, epsilon1):
    k=0
    while k<1000:
        try:
            r = (a+b)/2
            k += 1
            if math.fabs(b - a) < epsilon1:
                r = (a + b) / 2
                break
            if f(a) * f(r) > 0:
                a = r
            else:
                b = r
        except:
            sys.stdout.write("O metodo nao foi capaz de achar uma solução....\n")
    sys.stdout.write("O valor da raiz aproximada é %.12f, obtido em %d iterações.\n" %(r,k))

def falsa_posicao(a, b, epsilon1, epsilon2):
    k = 0
    while k < 1000:
        try:
            r = (a*f(b)-b*f(a))/(f(b)-f(a))
            k += 1
            yr = f(r)
            if math.fabs(b - a) < epsilon1 or math.fabs(yr)<epsilon2:
                break
            if f(a)*yr > 0:
                a = r
            else:
                b = r
        except:
            sys.stdout.write("O metodo nao foi capaz de achar uma solução....\n")
    sys.stdout.write("O valor da raiz aproximada é %.12f, obtido em %d iterações.\n" % (r, k))

def ponto_fixo(epsilon1, epsilon2, x0):
    if math.fabs(f(x0))<epsilon1:
        k = 0
        r = x0
    else:
        k = 1
        r = x0
        tmp = r
        i = 0
        while math.fabs(f(r)) > epsilon1 or math.fabs(r - tmp) > epsilon2 or k < 1000:
            try:
                i+=1
                tmp = r
                r = phi(r)
                if math.fabs(f(r)) < epsilon1 or math.fabs(r - tmp) < epsilon2:
                    break
                k += 1
            except:
                sys.stdout.write("O metodo nao foi capaz de achar uma solução....\n")
    sys.stdout.write("O valor da raiz aproximada é %.12f, obtido em %d iterações.\n" % (r, k))

def newton_raphson(epsilon1, epsilon2, x0):
    k = 0
    r = x0
    if math.fabs(f(x0)) < epsilon1:
        r = x0
    else:
        while k < 1000:
            try:
                tmp = r
                r -= f(r)/df(r)
                k += 1
                if math.fabs(f(r))<epsilon1 or math.fabs(r - tmp)< epsilon2:
                    break
            except:
                sys.stdout.write("O metodo nao foi capaz de achar uma solução....\n")
    sys.stdout.write("O valor da raiz aproximada é %.12f, obtido em %d iterações.\n" % (r, k))

def secante (epsilon1, epsilon2, x0, x1):
    tmp = x0
    r = x1
    k = 0
    if math.fabs(f(tmp)) < epsilon1 or math.fabs(f(r)) < epsilon1 or math.fabs(r - tmp) < epsilon2:
        return
    while k < 1000:
        try:
            tmp2 = r
            r = r - (f(r) / (f(r) - f(tmp))) * (r - tmp)
            k += 1
            if math.fabs(f(r)) < epsilon1 or math.fabs(r - tmp) < epsilon2:
                break
            tmp = tmp2
        except:
            sys.stdout.write("O metodo nao foi capaz de achar uma solução....\n")
    sys.stdout.write("O valor da raiz aproximada é %.12f, obtido em %d iterações.\n" % (r, k))


if __name__ == "__main__":
    a = -1
    b = 1
    x0 = a
    x1 = b
    epsilon1 = 0.001
    epsilon2 = 0.001
    sys.stdout.write("\nPrograma de Metodos para a Obtencao de valores "
                     "aproximados do Zero da Funcao\n\n")
    opt = int(input("1 - Metodo da Bisseccao\n"
                    "2 - Metodo da Falsa Posicao\n"
                    "3 - Metodo do Ponto Fixo\n"
                    "4 - Metodo Newton-Raphson\n"
                    "5 - Metodo da Secante\n"
                    "6 - Todos os Metodos\n\n"
                    "Digite um numero de 1 a 6 referente ao metodo que gostaria de selecionar: "))
    sys.stdout.write("\n")
    if opt == 1:
        bisseccao(a, b, epsilon1)
    elif opt == 2:
        falsa_posicao(a, b, epsilon1, epsilon2)
    elif opt == 3:
        ponto_fixo(epsilon1, epsilon2, x0)
    elif opt == 4:
        newton_raphson(epsilon1, epsilon2, x0)
    elif opt == 5:
        secante(epsilon1, epsilon2, x0, x1)
    elif opt == 6:
        sys.stdout.write("1 - Metodo da Bisseccao: ")
        bisseccao(a, b, epsilon1)
        sys.stdout.write("2 - Metodo da Falsa Posicao: ")
        falsa_posicao(a, b, epsilon1, epsilon2)
        sys.stdout.write("3 - Metodo do Ponto Fixo: ")
        ponto_fixo(epsilon1, epsilon2, x0)
        sys.stdout.write("4 - Metodo Newton-Raphson: ")
        newton_raphson(epsilon1, epsilon2, x0)
        sys.stdout.write("5 - Metodo da Secante: ")
        secante(epsilon1, epsilon2, x0, x1)
    else:
        sys.stdout.write("\nO numero digitado eh invalido!\n"
                         "Digite um numero de 1 a 6 para verificar os Metodos.\n\n")

    sys.stdout.write("\n\n********************                  Tocha                  ********************\n\n")
