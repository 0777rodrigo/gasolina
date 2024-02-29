import customtkinter as ctkn

ctkn.set_appearance_mode('dark')
ctkn.set_default_color_theme('green')

janela = ctkn.CTk()
janela.geometry('500x400')
janela.iconbitmap('4213872-ecology-electric-energy-fuel-fuel-station-petrol-power_115441.ico')
janela.title('APP Combustivel 2024')


#funcoes


def calcular():
    
    global resultado
    
    d = int(distancia.get())
    c = int(consumo.get())
    p = float(preco.get())
    
    valor = (d/c)*p
    
    resultado.configure(text=f'O gasto total da viagem foi: R$ {valor:.2f}')
    

texto = ctkn.CTkLabel(janela, text = "APP calcular consumo em viagem",text_color='blue',font=('verdana',25,'bold'))
texto.pack(padx=10,pady=10)


distancia = ctkn.CTkEntry(janela,placeholder_text='digite a distancia da viagem',width=300,height=40,fg_color='white',
text_color='black',placeholder_text_color='gray')
distancia.pack(padx=10,pady=10)


consumo = ctkn.CTkEntry(janela,placeholder_text='digite a consumo da viagem',width=300,height=40,fg_color='white',
text_color='black',placeholder_text_color='gray')
consumo.pack(padx=10,pady=10)


preco = ctkn.CTkEntry(janela,placeholder_text='digite a preco da viagem',width=300,height=40,fg_color='white',text_color='black',
placeholder_text_color='gray')
preco.pack(padx=10,pady=10)


botao = ctkn.CTkButton(janela, text = 'calcule',font=('verdana',20,'bold'), fg_color='darkgreen',hover_color='darkred',
height=50,command=calcular)
botao.pack(padx=10,pad=10)


resultado = ctkn.CTkLabel(janela, text='',text_color='yellow',font=('verdana',18,'bold'))
resultado.pack(padx=10,pady=10)







janela.mainloop()