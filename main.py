from pathlib import Path
import shutil
from colorama import init
init(autoreset=True)
caminho_atual = Path.home()
def listar_diretorio(caminho):
    try:
        for item in caminho.iterdir():
            tipo = "Diretório" if item.is_dir() else "Arquivo"
            print(f"[{tipo}] {item.name}")
    except PermissionError:
        print("Você não tem permissão pra acessar essa pasta")
def mudar_diretorio(diretorio_atual, destino):
    novo_caminho = (diretorio_atual / destino).resolve()
    if novo_caminho.exists() and novo_caminho.is_dir():
        return novo_caminho
    elif novo_caminho.exists() and not novo_caminho.is_dir():
        print('O destino especificado é um arquivo')
        return diretorio_atual
    else:
        print("Erro: O diretório não existe.")
        return diretorio_atual
def limpar_tela():
    print("\033[H\033[J", end="")
def criar_diretorio(caminho,nome):
    local = (caminho / nome).resolve()
    if local.exists():
        print("O diretório já existe")
        return
    try:
        local.mkdir(parents=True, exist_ok=True)
    except PermissionError:
        print('Você não tem permissão para criar a pasta no diretório atual')
def remover_diretorio(caminho,nome):
    local = (caminho / nome).resolve()
    if local.exists() and local.is_dir():
        try:
            local.rmdir()
        except OSError:
            valor = input('O diretório não está vazio. Continuar operação(s/n): ').lower()
            if valor == 's':
                try:
                    shutil.rmtree(local)
                except PermissionError:
                    print('Você não tem permissão para excluir esse diretório')
                except OSError:
                    print("Há um arquivo dentro do diretório aberto em outro local")
            else:
                return
        except PermissionError:
            print('Você não tem permissão para excluir esse diretório')
    else:
        print('Diretório não encotrado')
        return
print('Terminal para gerenciamento de arquivos totalmente feito em Português do Brasil.\nObrigado por usar!')
print("Digite --comandos para ver os comandos")
print('Versão 0.1.3')
while True:
    entrada = input(f'{caminho_atual}>').strip().split(maxsplit=1)
    match entrada:
        case []:
            continue
        case ['--comandos']:
            print('''Comandos:
1. Manipulação de arquivos e diretórios:
    dta - Mostra o diretório atual
    md - Muda para o diretório fornecido. Ex.: md Documents
    crdir - Cria um novo diretório usando o nome fornecido. Ex.: crdir nome_do_diretorio
    rmdir - Remove o diretório especificado. Ex.: rmdir nome_do_diretorio.
2 - Utilitários:
    lp - Limpa a tela do terminal
    sair - Sai do terminal
    ld - Lista todos os arquivos e diretórios dentro do diretório atual''')
        case ['ld']:
            listar_diretorio(caminho_atual)
        case ['dta']:
            print(caminho_atual)
        case ['md']:
            print('Sintaxe incorreta. Digite o destino. Ex.: md Documents')
        case ['md', destino]:
            caminho_atual = mudar_diretorio(caminho_atual,destino)
        case ['lp']:
            limpar_tela()
        case ['crdir']:
            print('Digite o nome do diretório')
        case ['crdir', nome]:
            criar_diretorio(caminho_atual,nome)
        case ['rmdir']:
            print('Digite o nome do diretório')
        case ['rmdir', nome]:
            remover_diretorio(caminho_atual,nome)
        case ['sair']:
            break
        case _:
            print('A sintaxe do comando está incorreta ou não existe esse comando. Digite --comandos para ver todos os comandos disponíveis')