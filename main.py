from pathlib import Path
import shutil
from colorama import init
init(autoreset=True)
caminho_atual = Path.home()
def listar_diretorio(caminho):
    for item in caminho.iterdir():
        tipo = "Diretório" if item.is_dir() else "Arquivo"
        print(f"[{tipo}] {item.name}")
def mudar_diretorio(diretorio_atual, destino):
    novo_caminho = (diretorio_atual / destino).resolve()
    if novo_caminho.exists() and novo_caminho.is_dir():
        return novo_caminho
    else:
        print("Erro: O diretório não existe.")
        return diretorio_atual
def limpar_tela():
    print("\033[H\033[J", end="")
print('Terminal para gerenciamento de arquivos totalmente feito em Português do Brasil.\nObrigado por usar!')
print("Digite --comandos para ver os comandos")
print('Versão 0.1.1')
while True:
    entrada = input(f'{caminho_atual}>').split()
    match entrada:
        case ['--comandos']:
            print('''Comandos:
1. Navegação e localização:
    dta - Mostra o diretório atual
    md - Muda para o diretório fornecido. Ex.: md Documents
2 - Utilitários:
    lp - Limpa a tela do terminal
    sair - Sai do terminal
    ld - Lista todos os arquivos e diretórios dentro do diretório atual''')
        case ['ld']:
            listar_diretorio(caminho_atual)
        case ['dta']:
            print(caminho_atual)
        case ['md', destino]:
            caminho_atual = mudar_diretorio(caminho_atual,destino)
        case ['lp']:
            limpar_tela()
        case ['sair']:
            break
        case _:
            print('Comando não encotrado')