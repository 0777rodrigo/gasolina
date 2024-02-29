import customtkinter as ctkn

ctkn.set_appearance_mode('dark')

janela = ctkn.CTk()
janela.geometry('500x300')

titulo = ctkn.CTkLabel(janela, text='Bem vindo ao aplicativo', text_color='red', font=('Verdana', 28))
titulo.pack(padx=10, pady=10)

login = ctkn.CTkEntry(janela, placeholder_text='faca seu login',width=250)
login.pack(padx=10,pady=10)

senha = ctkn.CTkEntry(janela, placeholder_text='digite sua senha',width=250,show='*')
senha.pack(padx=10,pady=10)

botao = ctkn.CTkButton(janela, text='Entrar', text_color = 'blue', command='clique')
botao.pack(padx=10,pady=10)


janela.mainloop()