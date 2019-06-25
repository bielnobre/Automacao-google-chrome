from Pyautomators.desk import Desk
from Pyautomators.mouse_teclado import Teclado
from Pyautomators.mouse_teclado import Mouse
from Pyautomators.Verifica import Valida

class Chrome():

    def __init__(self,app):
        self.app = app
    
    def validacao_tela(self,imagem):
        tentativas=50
        for tentativas in range(tentativas):
            if(self.app.verifica_tela(imagem, 80, similaridade=50) != None):
                break
            time.sleep(2)
    
    def valida_abertura(self):
        self.validacao_tela(imagem=r'data\images\passo1.png')
        self.app.clica_imagem(r'data\images\passo1.png', similar=70)
 
    def navega_menu_sobre(self):
        self.app.clica_imagem(r'data\images\passo2.png', similar=70)
        self.app.clica_imagem(r'data\images\passo3.png', similar=70)
        self.app.clica_imagem(r'data\images\passo4.png', similar=70)

    def valida_tela_final(self):
        self.app.clica_imagem(r'data\images\passo_final.png', similar=70)


 