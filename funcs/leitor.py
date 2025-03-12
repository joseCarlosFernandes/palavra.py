from pathlib import Path
import os
import subprocess
import sys
import tkinter as tk


def abrirArquivo(nome_arquivo):
	caminho = diretorio / nome_arquivo

	if sys.platform == "win32":
		os.startfile(caminho)
	elif sys.platform == "darwin":
		subprocess.run(["open", caminho])
	else:
		subprocess.run(["xdg-open", caminho])


diretorio = Path("arquivos")

leitor = tk.Tk()
leitor.title("Leitor")
leitor.geometry("500x500+500+200")

lableA = tk.Label(leitor, text="Arquivos Disponíveis para Leitura")
lableA.pack()

btn_sair = tk.Button(leitor, text="Sair", command=leitor.quit, width=20, height=3)
btn_sair.place(x=340, y=400)


arquivos = [arquivo.name for arquivo in diretorio.iterdir() if arquivo.is_file()]
if not arquivos:
	lableE = tk.Label(leitor, text="Erro, nenhum arquivo disponível")
	lableE.place(x=160, y=50)
	btn_sair = tk.Button(leitor, text="Sair", command=leitor.quit, width=20, height=3)
else:
	for i, arquivo in enumerate(arquivos):
		btn_abrir = tk.Button(leitor, text=arquivo, command=lambda nome=arquivo: abrirArquivo(nome), width=20, height=3)
		btn_abrir.place(x=180, y=60 + i * 40)
		
leitor.resizable(False, False)
leitor.mainloop()