from pathlib import Path
import shutil
caminho_atual = Path('C:/')
def listar_diretorio(caminho):
    # Listar TUDO (arquivos e pastas)
    for item in caminho.iterdir():
        tipo = "Diretório" if item.is_dir() else "Arquivo"
        print(f"[{tipo}] {item.name}")
while True:
    print('Terminal para gerenciamento de arquivos totalmente feito em Português do Brasil.\nObrigado por usar!')
    print("Digite --comandos para ver os comandos")
    print('Versão 0.1')
    comando = input(f'{caminho_atual}>')
    match comando:
        case '--comandos':
            print('''Comandos:
1. Navegação e localização:
    ld - Lista todos os arquivos e diretórios dentro do diretório atual
    dta - Mostra o diretório atual''')
        case 'ld':
            listar_diretorio(caminho_atual)
        case 'dta':
            print(caminho_atual)
        case _:
            print('Comando não encotrado')
    break