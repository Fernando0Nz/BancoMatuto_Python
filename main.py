from tkinter import *
from PIL import Image,ImageTk
import os

#Definindo a janela
root = Tk()

#Definindo o tamanho da janela
root.geometry('600x600')

#Definindo o título da página
root.title('Banco Matuto')

#Definindo o ícone da página
root.iconbitmap('img/icone_cacto.ico')

#Definindo a cor inicial da página
root.config(bg='black')

#timer1=5000
#timer2=4000
#timer3=6000
#timer4=13000

timer1 = 4000
timer2 = 4000
timer3 = 5500
timer4 = 12000

#Lista com o nome de todas as imagens
banco_de_imagens = ['logo_banco_matuto.png','logo_matuto.png','logo_nome_matuto.png']

#Dicionario com os imagens carregadas
imagens_carregadas = {}

#Função para abrir as imagens e transformar em objetos que podem ser usados pelas labels
def carregar_imagens(imagem):
    for imgs in banco_de_imagens:
        if imgs is imagem:
            caminho_para_imagem = os.path.join('img/',imgs)
            objeto_imagem = ImageTk.PhotoImage(Image.open(caminho_para_imagem))
            imagens_carregadas[imgs] = objeto_imagem
            break
    return objeto_imagem

#Função para criar as labels
def criar_label_imagem(indice_imagem):
    label_criada = Label(image=carregar_imagens(banco_de_imagens[indice_imagem]),borderwidth=0,highlightthickness=0)
    return label_criada

#Função para posicionar as labels
def posicionar_label(label,posx,posy):
    label.place(relx=posx,rely=posy,anchor=CENTER)

#Função para deletar as labels
def deletar_label(label):
    label.destroy()

#Função para inicialização - Fim
def boot():
    root.config(bg='#1b1b1b')
    root.after(timer2,lambda: root.config(bg='white'))
    label_logo_boot = criar_label_imagem(0)
    label_logo_boot
    root.after(timer3,lambda: posicionar_label(label_logo_boot,0.5,0.5))
    root.after(timer4,lambda: deletar_label(label_logo_boot))
    
#Delay de 1 segundo para executar a função boot() - Inicio
root.after(timer1,boot)

#Loop principal da janela
root.mainloop()