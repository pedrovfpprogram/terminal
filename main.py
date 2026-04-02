from pathlib import Path
import shutil
from colorama import init
from datetime import datetime
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
def renomear(diretorio_atual,caminho_antigo,caminho_novo):
    origem = (diretorio_atual / caminho_antigo).resolve()
    destino = (diretorio_atual / caminho_novo).resolve()
    if not origem.exists():
        print('Arquivo/diretório não encotrado!')
        return
    if origem == destino:
        print('Coloque um nome direferente do atual')
    try:
        origem.rename(destino)
    except PermissionError:
        print('Você não tem permissão para renomear esse item')
    except FileExistsError:
        print('Já existe um item com esse nome')
    except OSError:
        print('Falha ao renomear esse item')
def remover_arquivo(caminho,nome):
    local = (caminho / nome).resolve()
    if not local.exists():
        print('Arquivo não encontrado.')
        return
    if local.is_file():
        try:
            local.unlink()
        except PermissionError:
            print('Você não tem permissão para excluir esse arquivo.')
        except OSError:
            print('O arquivo está aberto em outro programa.')
    else:
        print('O item deve ser um arquivo. Use rmdir para diretórios.')
        return
def ler_arquivo(caminho,nome):
    local = (caminho / nome).resolve()
    extensoes_texto = ['.txt', '.py', '.log', '.md', '.json', '.html', '.css']
    if not local.exists():
        print('O arquivo não existe.')
        return
    if local.is_file():
        if local.suffix.lower() not in extensoes_texto:
            confirmar = input(f"O arquivo '{local.suffix}' pode ser binário. Deseja tentar ler mesmo assim? (s/n): ").lower()
            if confirmar != 's':
                return
        try:
            conteudo = local.read_text(encoding='utf-8', errors='replace')
            print('='*50)
            print(conteudo)
            print('='*50)
        except PermissionError:
            print('Você não tem permissão para ler esse arquivo.')
        except UnicodeDecodeError:
            print('O arquivos contém binários e não pode ser lido.')
        except OSError:
            print('Não foi possível ler o arquivo.')
    else:
        print('O item deve ser um arquivo. Use md diretório para mudar de diretório ou ld para listar.')
def info(caminho,nome):
    local = (caminho / nome).resolve()
    if not local.exists():
        print('O arquivo/pasta não existe')
        return
    stats = local.stat()
    data_mod = datetime.fromtimestamp(stats.st_mtime).strftime('%d/%m/%Y %H:%M:%S')
    tamanho_bytes = stats.st_size
    tipo = "Diretório" if local.is_dir() else "Arquivo"
    if tamanho_bytes < 1024:
        tamanho = f'{tamanho_bytes} Bytes'
    elif tamanho_bytes < 1024**2:
        tamanho = f'{tamanho_bytes/ 1024:.2f} KB'
    elif tamanho_bytes < 1024**3:
        tamanho = f'{tamanho_bytes / (1024**2):.2f} MB'
    else:
        tamanho = f'{tamanho_bytes/ (1024**3):.2f} GB'
    print(f"\n--- Informações: {local.name} ---")
    print(f"Tipo: {tipo}")
    print(f"Tamanho: {tamanho}")
    print(f"Última modificação: {data_mod}")
    if local.is_file():
        print(f"Extensão: {local.suffix}")
    print("-" * 30)
print('Terminal para gerenciamento de arquivos totalmente feito em Português do Brasil.\nObrigado por usar!')
print("Digite --comandos para ver os comandos")
print('Versão 0.1.5')
while True:
    entrada = input(f'{caminho_atual}>').strip().split(maxsplit=1)
    match entrada:
        case []:
            continue
        case ['--comandos']:
            print('''Comandos:
1. Manipulação de arquivos e diretórios:
    dta - Mostra o diretório atual.
    md - Muda para o diretório fornecido. Ex.: md Documents.
    crdir - Cria um novo diretório usando o nome fornecido. Ex.: crdir nome_do_diretorio.
    rmdir - Remove o diretório especificado. Ex.: rmdir nome_do_diretorio.
    rnm - Renomeia um item espeicífico. Ex.: rnm nome_antigo nome_atual.
    rmarq - Remove um arquivo específico. Ex.: rmarq nome_arquivo.
    ler - Ler um arquivo específico. Ex.: ler arquivo.txt.
    info - Exibe as informações de um arquivo ou uma pasta. Ex.: info arquivo.txt.
2 - Utilitários:
    lp - Limpa a tela do terminal.
    sair - Sai do terminal.
    ld - Lista todos os arquivos e diretórios dentro do diretório atual.''')
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
        case ['rnm']:
            print('Sintaxe incorreta. Use rnm nome antigo nome atual')
        case ['rnm', argumentos]:
            lista = argumentos.split()
            if len(lista) == 2:
                renomear(caminho_atual,lista[0],lista[1])
            else:
                print('Sintaxe incorreta! O comando rnm precisa de dois nomes')
        case ['rmarq']:
            print('Sintaxe incorreta. Digite rmarq nome do arquivo')
        case ['rmarq', nome]:
            remover_arquivo(caminho_atual,nome)
        case ['ler']:
            print('Sintaxe incorreta. Use ler arquivo')
        case ['ler', nome]:
            ler_arquivo(caminho_atual,nome)
        case ['info']:
            print('Sintaxe incorreta. Tente info arquivo ou info pasta.')
        case ['info', nome]:
            info(caminho_atual,nome)
        case ['sair']:
            break
        case _:
            print('A sintaxe do comando está incorreta ou não existe esse comando. Digite --comandos para ver todos os comandos disponíveis')