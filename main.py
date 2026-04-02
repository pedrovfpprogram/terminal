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
    local.mkdir(parents=True, exist_ok=True)
def remover_diretorio(caminho,nome):
    if not nome:
        print("Insira o nome do diretório logo após o comando. Ex.: crdir nome_do_diretorio")
        return
    local = (caminho / nome).resolve()
    if local.exists() and local.is_dir():
        try:
            Path.rmdir(local)
        except:
            valor = input('O diretório não está vazio. Continuar operação(s/n): ').lower()
            if valor == 's':
                shutil.rmtree(local)
            else:
                return
    else:
        print('Diretório não encotrado')
        return
print('Terminal para gerenciamento de arquivos totalmente feito em Português do Brasil.\nObrigado por usar!')
print("Digite --comandos para ver os comandos")
print('Versão 0.1.1')
while True:
    entrada = input(f'{caminho_atual}>').split(maxsplit=1)
    match entrada:
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
        case ['md', destino]:
            caminho_atual = mudar_diretorio(caminho_atual,destino)
        case ['lp']:
            limpar_tela()
        case ['crdir', nome]:
            criar_diretorio(caminho_atual,nome)
        case ['rmdir', nome]:
            remover_diretorio(caminho_atual,nome)
        case ['sair']:
            break
        case _:
            print('A sintaxe do comando está incorreta ou não existe esse comando. Digite --comandos para ver todos os comandos disponíveis')