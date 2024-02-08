from _tkinter import *
from dbm import whichdb
from tkinter import Label, PhotoImage, Tk


janela = Tk()
janela.title('cadastro')
janela.geometry('300x300')


nome_label = Label(janela, width=10, height=2, text='Nome', font=('Arial 10 bold'), fg='red', bg='black')
nome_label.place(x=10,y=20) # ONDE VAI FICAR A TAG COM ESCRITA NOME

nome = Label(janela, width=10, height=2, text='Harison', font=('Arial 10 bold'), fg='red', bg='black')
nome.place(x=100, y=20) # ONDE VAI FICAR A TAG COM O NOME DA PESSOA NO CASO => HARISON

idade_label =Label(janela, width=10, height=2, text='idade', font=('Arial 10 bold'), fg='red', bg='green')
idade_label.place(x=10, y=65) # ONDE VAI FICAR A TAG COM A ESCRIA IDADE

idade = Label(janela, width=10, height=2, text='45', font=('Arial 10 bold'), fg='gray', bg='orange')
idade.place(x=100,y=65) # ONDE VAI FICAR TAG COM O VALOR IDADE, NO CASO => 45

janela.mainloop()