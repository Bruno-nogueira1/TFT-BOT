import tkinter as tk
import tftbot

root = tk.Tk()
root.geometry('500x300')
root.resizable(width=False,height=False)
root.title('TFT BOT v1.0')
root.configure(background='#e15f5f')

fontes = ('Calibri',17,'bold')

iniciar = tk.Button(root,command= tftbot.principal,text= 'Iniciar', background='#5fc9f8',font = fontes, width=12).place(x=175,y=75)


instrucoes = tk.Button(root,text= 'Instruções',background='#5fc9f8',font= fontes, width=12).place(x=175,y=150)


configuracoes = tk.Button(root,text= 'Configurações',background='#5fc9f8',font= fontes, width=12).place(x=175,y=225)


root.mainloop()
