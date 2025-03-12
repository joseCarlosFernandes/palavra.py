import tkinter as tk
import subprocess
import sys

def abreBusca():
    subprocess.run([sys.executable, "funcs/buscador.py"])

def abreBuscaDocx():
	subprocess.run([sys.executable, "funcs/buscadorD.py"])

def abreCriador():
	subprocess.run([sys.executable, "funcs/criador.py"])

def abreLeitor():
	subprocess.run([sys.executable, "funcs/leitor.py"])

janela = tk.Tk()
janela.title("Palavra - Menu Principal")
janela.geometry("500x500+200+200")

label = tk.Label(janela, text="Palavra - Menu de Ações")
label.pack()

# botão buscar txt
botao_buscar = tk.Button(janela, text="Buscar", command=abreBusca, width = 20, height= 3)
botao_buscar.place(x=80, y=50)

#botão buscar docx
botao_docx = tk.Button(janela, text="Buscar em Docx", command=abreBuscaDocx, width=20, height=3)
botao_docx.place(x=80, y=120)


#botão ler
botao_ler = tk.Button(janela, text="Ler/Editar", command=abreLeitor, width = 20, height= 3)
botao_ler.place(x=280, y=120)

#botão criar
botao_criar = tk.Button(janela, text="Criar", command=abreCriador, width = 20, height= 3)
botao_criar.place(x=280, y=50)

#botão sair
botao_sair = tk.Button(janela, text="Sair", command=janela.quit, width = 20, height= 3)
botao_sair.place(x=180, y=190)

#imagem
imagem = tk.PhotoImage(file="imagens/palavra.png")
label_imagem = tk.Label(janela, image=imagem)
label_imagem.place(x=150, y=280)

janela.resizable(False, False) #impede o redimensionamento da janela
janela.mainloop() #Executar a interface