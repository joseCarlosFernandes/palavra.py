from pathlib import Path
from docx import Document
import os

os.system('cls' if os.name == 'nt' else 'clear')
print("Buscador de Palavras - Apenas .DOCX")

busca = input("Qual palavra você quer buscar? ").strip().lower()
pastaArquivos = Path("arquivos_docx")

# Verifica se a pasta "arquivos" existe
if not pastaArquivos.exists():
    print("Erro: A pasta 'arquivos_docx' não foi encontrada. Certifique-se de que ela existe no mesmo diretório do script.")
    input("Pressione Enter para sair")
    exit()

# Lista arquivos .docx na pasta
arquivos_docx = sorted([arq for arq in pastaArquivos.iterdir() if arq.is_file() and arq.suffix == ".docx"])

# Se não houver arquivos .docx, exibe uma mensagem
if not arquivos_docx:
    print("Erro: Nenhum arquivo .docx foi encontrado na pasta 'arquivos'.")
    input("Pressione Enter para sair")
    exit()

# Percorre apenas os arquivos .docx
for arquivo in arquivos_docx:
    try:
        print(f"Lendo arquivo DOCX: {arquivo.name}")
        doc = Document(arquivo)
        conteudo = "\n".join([p.text for p in doc.paragraphs if p.text.strip()])  # Junta os textos dos parágrafos

        # Verifica se a palavra está no conteúdo
        if busca in conteudo.lower():
            print(f"✅ A palavra '{busca}' foi encontrada no arquivo {arquivo.name}")
        else:
            print(f"❌ A palavra '{busca}' NÃO foi encontrada no arquivo {arquivo.name}")

    except Exception as e:
        print(f"Erro ao processar {arquivo.name}: {e}")

input("Pressione Enter para sair")
os.system('cls' if os.name == 'nt' else 'clear')
print("Volte para o Menu para selecionar outa opção")
