from math import sqrt, pi
from math import log10 , floor

import time
import sys

ra = "\nNathalia Saori Shimokawa..................22.122.052-8\n\
Guilherme Ferreira de Souza...............22.122.061-9\n\
Lucas Sombra do Nascimento................22.122.112-0\n\
Rafael Augusto Feliciano Assembleia.......22.122.103-9\n\n"

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_msg_box(msg, indent=1, width=None, title=None):
    """Print message-box with optional title."""
    lines = msg.split('\n')
    space = " " * indent
    if not width:
        width = max(map(len, lines))
    box = f'╔{"═" * (width + indent * 2)}╗\n'  # upper_border
    if title:
        box += f'║{space}{title:<{width}}{space}║\n'  # title
        box += f'║{space}{"-" * len(title):<{width}}{space}║\n'  # underscore
    box += ''.join([f'║{space}{line:<{width}}{space}║\n' for line in lines])
    box += f'╚{"═" * (width + indent * 2)}╝'  # lower_border
    print(box)
print(bcolors.WARNING + ra)

def write(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0)

def tranf(x):
    a = x.split("e")
    return (float(a[0]) * (10 ** int(a[1])))


def menu():
    var = 1
    while(var !=0 ):
        write(
            bcolors.ENDC + "\nPara utilizar o programa escolha a opcao de acordo com o dado que voce possui:\n" + bcolors.OKCYAN)

        print_msg_box("""1 - Campo elétrico (Em)
    2 - Campo magnético (Bm)
    3 - Intensidade (I)
    4 - Frequência (f)
    5 - Comprimento de onda (λ)
    6 - Número de ondas (k)
    7 - Frequência angular (w)""")

        x = int(input(" R: "))
        valor = input("Valor: ")
        valor= tranf(valor)

        funcoes = [Em, Bm, I, f, k, compr, w]
        for fun in funcoes:
            fun(x,valor )
        var = int(input("\n\nSe deseja continuar digite 1 (SIM) ou 0 (NAO):"))






def round_it(x):
    return round(x, 3- int(floor(log10(abs(x))))-1)

# FORMULAS_____________________________________

C_velocidadeLuz = 2.998*10**8
u0 = 4 * pi  * 10 ** -7

def Em(x, valor):
    if x == 2:
        Em_Bm = valor*C_velocidadeLuz
        print('Em (Campo elétrico) = {:.2e}'.format(round_it(Em_Bm)))
    if x == 3:
        Em_I = sqrt(2*u0 * C_velocidadeLuz * valor)
        print('Em (Campo elétrico) = {:.2e}'.format(round_it(Em_I)))
def Bm(x, valor):
    if x == 1:
        Bm_Em = valor/C_velocidadeLuz
        print('Bm (Campo Magnetico) = {:.2e}'.format(round_it(Bm_Em)))
    if x == 3:#errado
        Bm_I = (1/(2 * u0 * C_velocidadeLuz )) * (C_velocidadeLuz * valor)
        print('Bm (Campo Magnetico) = {:.2e}'.format(round_it(Bm_I)))

def I(x,valor):
    if x == 1:#errado
        I_Em = (valor)**2/(2*u0*C_velocidadeLuz)
        print('Itensidade (I) = {:.2e}'.format(round_it(I_Em)))
    if x == 2:#errado
        I_Em = sqrt(valor * 2 * u0 * C_velocidadeLuz)
        I_Bm = I_Em / C_velocidadeLuz
        print('Itensidade (I) = {:.2e}'.format(round_it(I_Bm)))
def f(x, valor):
    if x == 5:
        f_compr = C_velocidadeLuz/valor
        print('f (Frequência) = {:.2e}'.format(round_it(f_compr)))
    if x == 6:
        compr = (2*pi)/valor
        f_k = C_velocidadeLuz/compr
        print('f (Frequência) = {:.2e}'.format(round_it(f_k)))
    if x == 7:
        f_w = valor/(2*pi)
        print('f (Frequência) = {:.2e}'.format(round_it(f_w)))
def k(x, valor):
    if x == 4:
        T = 1/valor
        compr = C_velocidadeLuz*T
        k_f = (2*pi)/compr
        print('k (Número de onda) = {:.2e}'.format(round_it(k_f)))
    if x == 5:
        k_compr = (2*pi)/valor
        print('k (Número de onda) = {:.2e}'.format(round_it(k_compr)))
    if x == 7:
        k_w = valor/C_velocidadeLuz
        print('k (Número de onda) = {:.2e}'.format(round_it(k_w)))
def compr(x, valor):
    if x == 4:
        compr_f = C_velocidadeLuz/valor
        print('λ (Comprimento de Onda) = {:.2e}'.format(round_it(compr_f)))
    if x == 6:
        compr_k = (2*pi)/valor
        print('λ (Comprimento de Onda) = {:.2e}'.format(round_it(compr_k)))
    if x == 7:
        T = (2*pi)/valor
        compr_w =C_velocidadeLuz*T
        print('λ (Comprimento de Onda) = {:.2e}'.format(round_it(compr_w)))
def w(x, valor):
    if x == 4:
        w_f = 2*pi*valor
        print('Frequencia Angular ( W ) = {:.2e}'.format(round_it(w_f)))
    if x == 5:
        T = valor/C_velocidadeLuz
        w_compr = (2*pi)/T
        print('Frequencia Angular ( W ) = {:.2e}'.format(round_it(w_compr)))
    if x == 6:
        w_k = C_velocidadeLuz * valor
        print('Frequencia Angular ( W ) = {:.2e}'.format(round_it(w_k)))

menu()