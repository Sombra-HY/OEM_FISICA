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
        time.sleep(0.025)
def menu():
    write(bcolors.ENDC +"\nPara utilizar o programa escolha a opcao de acordo com o dado que voce possui:\n" + bcolors.OKCYAN)

    print_msg_box("""1 - Campo elétrico (Em)
2 - Campo magnético (Bm)
3 - Intensidade (I)
4 - Frequência (f)
5 - Comprimento de onda (λ)
6 - Número de ondas (k)
7 - Frequência angular (w)""")
    x = input(" R: ")

menu()