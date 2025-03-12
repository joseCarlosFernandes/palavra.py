from pathlib import Path
import os
import subprocess
import sys
import tkinter as tk

pastaArquivos = Path("arquivos")

def abrirArquivo(nome_arquivo):
	caminho = pastaArquivos / nome_arquivo

	if sys.platform == "win32":
		os.startfile(caminho)
	elif sys.platform == "darwin":
		subprocess.run(["open", caminho])
	else:
		subprocess.run(["xdg-open", caminho])


def buscaArquivo():
	busca = busca_user.get().strip().lower()
	encontrou = 0
	for arquivo in sorted(pastaArquivos.iterdir()):
		if arquivo.is_file():
			with arquivo.open("r") as a:
				conteudo = a.read()

				if busca in conteudo.lower():
					labelR.config(text=f"A palavra {busca} foi encontrada no arquivo {arquivo.name}")
					encontrou = 1

					buscador.geometry("500x500+500+200")
					btn_abrir.config(text=f"Abrir {arquivo.name}")
					btn_abrir.config(command= lambda nome=arquivo.name: abrirArquivo(nome))
					btn_abrir.config(width=20, height=3)
	if encontrou != 1:
		labelR.config(text=f"A palavra {busca} NÃO foi encontrada")
		btn_abrir.config(width=0, height=0)
		btn_abrir.config(text="")
		buscador.geometry("500x200+500+300")




buscador = tk.Tk()
buscador.title("Buscador")
buscador.geometry("500x200+500+300")

labelP = tk.Label(buscador, text="Qual Palavra Você Deseja Buscar?")
labelP.place(x=160,y=30)

busca_user = tk.Entry(buscador, width=50)
busca_user.place(x=100, y=50)

btn_sair = tk.Button(buscador, text="Sair", command=buscador.quit, width=20, height=3)
btn_sair.place(x=255, y=90)

btn_busca = tk.Button(buscador, text="Buscar", command=buscaArquivo, width = 20, height= 3)
btn_busca.place(x=99, y=90)

labelR = tk.Label(buscador, text="")
labelR.place(x=130, y=150)

btn_abrir = tk.Button(buscador, width=0, height=0)
btn_abrir.place(x=160, y=280)

buscador.mainloop()

