import tkinter

janela = tkinter.Tk()
janela.geometry('500x300')

def ola():
    print('oi, tudo bem')

titulo = tkinter.Label(janela,text = 'bem vindo ao app')
titulo.pack(padx=10,pady=10)

botao = tkinter.Button(janela,text = 'calcular', command=ola)
botao.pack(padx=10,pady=10)






janela.mainloop()
