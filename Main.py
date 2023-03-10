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
    # Função do quadro do menu
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
# Função que mostra o texto de maneira assíncrona
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(5E-5)

def tranf(x):
    # Trata os dados do input, no caso o (3.44E10)
    # Notação Científica

    a = x.split("E")
    return (float(a[0]) * (10 ** int(a[len(a)-1])))



def menu():
    # Função que mostra o menu para o usuário escolher a entrada que ele possui
    var = 1
    write(
        bcolors.ENDC + "\nOndas eletromagnéticas: são oscilações produzidas por campos elétricos e magnéticos, que se propagam através do vácuo ou de meios materiais, transportando energia."
                       "\nCampo elétrico: é uma importante grandeza física definida como o módulo da força elétrica produzida em cada unidade de carga elétrica."
                       "\nCampo magnético: é a região do espaço em que as cargas em movimento sofrem a ação de uma força magnética; é responsável pela atração e repulsão dos polos magnéticos."
                       "\nIntensidade: ela mede a quantidade de energia que passa por unidade de tempo e por unidade de área em um determinado ponto do espaço."
                       "\nFrequência: diz respeito ao número de oscilações que o seu campo elétrico realiza a cada segundo."
                       "\nComprimento de onda: é o espaço pelo qual a onda propaga-se até que se forme uma oscilação completa."
                       "\nNúmero de onda: é proporcional à frequência e à energia do fóton."
                       "\nFrequência angular: representa uma taxa de variação de uma grandeza angular, nem sempre relacionada ao movimento de rotação." + bcolors.OKBLUE
    )
    # Recursão para o programa nao finalizar com apenas uma execução
    while(var !=0 ):
        write(
            bcolors.ENDC + "\n\n\nPara utilizar o programa escolha a opcao de acordo com o dado que voce possui."
                           "\nPara a entrada de dados sempre coloque 'E' para notação científica (ex:. 22Hz: 22E0)\n" + bcolors.OKCYAN)

        print_msg_box("""    1 - Campo elétrico (Em) [V/m]
    2 - Campo magnético (Bm) [T]
    3 - Intensidade (I) [W/m²]
    4 - Frequência (f) [Hz]
    5 - Comprimento de onda (λ) [m]
    6 - Número de ondas (k) [rad/m]
    7 - Frequência angular (w) [rad/s]""")

        x = int(input(" R: "))
        valor = input("Valor: ")
        valor = tranf(valor)

        # chamada de funcoes
        for fun in [Em, Bm, I, f, k, compr, w]:
            fun(x,valor )
        var = int(input("\n\nSe deseja continuar digite 1 (SIM) ou 0 (NAO):"))

def round_it(x):
    # Função que arredonda o resultado para três algarismos significativos
    return round(x, 3- int(floor(log10(abs(x))))-1)

# FÓRMULAS_____________________________________

C_velocidadeLuz = 3E8
u0 = 4E-7*pi

# O usuário escolhe no menu o dado com qual ele deseja entrar. Após escolher a entrada,
# todas as funções serão executadas, porém é repassada uma variável de controle (o 'x')
# onde a fórmula só será calculada nas funções onde o 'x' for compatível.
# Por exemplo, no caso da intensidade (parâmetro de saída), os únicos valores
# de entrada possíveis para que a função seja executada, são o Em (1) e o Bm (2).
# Então, a variável (x) enviada na linha 88 controla os tipos de saída.

def Em(x, valor):
    # Cálculo do Campo Elétrico
    if x == 2:
        Em_Bm = valor*C_velocidadeLuz
        print('Em (Campo elétrico) = {:.2e} V/m'.format(round_it(Em_Bm)))
    elif x == 3:
        Em_I = sqrt(2*u0 * C_velocidadeLuz * valor)
        print('Em (Campo elétrico) = {:.2e} V/m'.format(round_it(Em_I)))
def Bm(x, valor):
    # Cálculo do Campo Magnético
    if x == 1:
        Bm_Em = valor/C_velocidadeLuz
        print('Bm (Campo Magnetico) = {:.2e} T'.format(round_it(Bm_Em)))
    elif x == 3:
        Bm_I = sqrt((valor*2*u0)/C_velocidadeLuz)
        print('Bm (Campo Magnetico) = {:.2e} T'.format(round_it(Bm_I)))
def I(x,valor):
    # Cálculo da Intensidade
    if x == 1:
        I_Em = (valor)**2/(2*u0*C_velocidadeLuz)
        print('Itensidade (I) = {:.2e} W/m²'.format(round_it(I_Em)))
    elif x == 2:
        I_Bm = (C_velocidadeLuz*valor**2)/(2*u0)
        print('Itensidade (I) = {:.2e} W/m²'.format(round_it(I_Bm)))

def f(x, valor):
    # Cálculo da Frequência
    if x == 5:
        f_compr = C_velocidadeLuz/valor
        print('f (Frequência) = {:.2e} Hz'.format(round_it(f_compr)))
    elif x == 6:
        compr = (2*pi)/valor
        f_k = C_velocidadeLuz/compr
        print('f (Frequência) = {:.2e} Hz'.format(round_it(f_k)))
    elif x == 7:
        f_w = valor/(2*pi)
        print('f (Frequência) = {:.2e} Hz'.format(round_it(f_w)))
def k(x, valor):
    # Cálculo do Número de Onda
    if x == 4:
        T = 1/valor
        compr = C_velocidadeLuz*T
        k_f = (2*pi)/compr
        print('k (Número de onda) = {:.2e} rad/m'.format(round_it(k_f)))
    elif x == 5:
        k_compr = (2*pi)/valor
        print('k (Número de onda) = {:.2e} rad/m'.format(round_it(k_compr)))
    elif x == 7:
        k_w = valor/C_velocidadeLuz
        print('k (Número de onda) = {:.2e} rad/m'.format(round_it(k_w)))
def compr(x, valor):
    # Cálculo de Comprimento da Onda
    if x == 4:
        compr_f = C_velocidadeLuz/valor
        print('λ (Comprimento de Onda) = {:.2e} m'.format(round_it(compr_f)))
    elif x == 6:
        compr_k = (2*pi)/valor
        print('λ (Comprimento de Onda) = {:.2e} m'.format(round_it(compr_k)))
    elif x == 7:
        T = (2*pi)/valor
        compr_w =C_velocidadeLuz*T
        print('λ (Comprimento de Onda) = {:.2e} m'.format(round_it(compr_w)))
def w(x, valor):
    # Cálculo do Frequência Angular
    if x == 4:
        w_f = 2*pi*valor
        print('Frequência Angular ( W ) = {:.2e} rad/s'.format(round_it(w_f)))
    elif x == 5:
        T = valor/C_velocidadeLuz
        w_compr = (2*pi)/T
        print('Frequência Angular ( W ) = {:.2e} rad/s'.format(round_it(w_compr)))
    elif x == 6:
        w_k = C_velocidadeLuz * valor
        print('Frequência Angular ( W ) = {:.2e} rad/s'.format(round_it(w_k)))

menu()