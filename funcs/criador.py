from pathlib import Path
import os
import tkinter as tk

def salvaArquivo():
	nome = entradaNome.get()
	conteudo = entradaTexto.get("1.0", tk.END)
	nomeTipo = nome + ".txt"

	pastaArquivos = Path("arquivos")
	novoArquivo = pastaArquivos / nomeTipo

	novoArquivo.write_text(conteudo)
	criador.title("ARQUIVO CRIADO")

criador = tk.Tk()
criador.title("Criador")
criador.geometry("500x500+500+200")

labelN = tk.Label(criador, text="Digite o nome do Arquivo:")
labelN.place(x=50, y=30)

entradaNome = tk.Entry(criador, width=40)
entradaNome.place(x=50, y=50)

entradaTexto = tk.Text(criador, width=50, height=20)
entradaTexto.insert("1.0", "Insira o texto do Arquivo")
entradaTexto.place(x=50, y=100)

botao_salvar = tk.Button(criador, text="Salvar", command=salvaArquivo, width = 20, height= 3)
botao_salvar.place(x=50, y=430)

botao_sair = tk.Button(criador, text="Sair", command=criador.quit, width = 20, height= 3)
botao_sair.place(x=305, y=430)

criador.mainloop()
