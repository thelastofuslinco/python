# Estilo (1=Negrito), Texto (32=Verde), Fundo (40=Preto)
import re


def ansi_center(text: str, width: int) -> str:
    # Calcula o tamanho visual (sem os escape codes)
    visible_len = len(re.sub(r'\033\[[0-9;]*m', '', text))
    total_padding = max(0, width - visible_len)
    left_pad = total_padding // 2
    right_pad = total_padding - left_pad
    return '_' * left_pad + text + '_' * right_pad


SEP = '\033[1;29;44m-\033[m' * 40
TITLE = '\033[4;29;44mSistema de suporte!\033[m'

print(SEP)
print(ansi_center(TITLE, 40))
print(SEP)

while True:
    entrada = input('Digite o nome da função: ').strip()

    if entrada.upper() == 'FIM':
        break
    help(entrada)
