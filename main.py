from pathlib import Path
import shutil
caminho_atual = Path.home()
def listar_diretorio(caminho):
    # Listar TUDO (arquivos e pastas)
    for item in caminho.iterdir():
        tipo = "Diretório" if item.is_dir() else "Arquivo"
        print(f"[{tipo}] {item.name}")
def mudar_diretorio(diretorio_atual, destino):
    # O operador / da pathlib junta caminhos de forma inteligente
    novo_caminho = (diretorio_atual / destino).resolve()
    if novo_caminho.exists() and novo_caminho.is_dir():
        return novo_caminho
    else:
        print("Erro: O diretório não existe.")
        return diretorio_atual
print('Terminal para gerenciamento de arquivos totalmente feito em Português do Brasil.\nObrigado por usar!')
print("Digite --comandos para ver os comandos")
print('Versão 0.1.1')
while True:
    entrada = input(f'{caminho_atual}>').split()
    match entrada:
        case ['--comandos']:
            print('''Comandos:
1. Navegação e localização:
    ld - Lista todos os arquivos e diretórios dentro do diretório atual
    dta - Mostra o diretório atual
    md - Muda para o diretório fornecido. Ex.: md Documents''')
        case ['ld']:
            listar_diretorio(caminho_atual)
        case ['dta']:
            print(caminho_atual)
        case ['md', destino]:
            caminho_atual = mudar_diretorio(caminho_atual,destino)
        case ['.']:
            break
        case _:
            print('Comando não encotrado')