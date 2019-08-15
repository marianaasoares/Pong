import pygame, sys
from pygame.locals import *

#CONSTANTES
#constantes para o tamanho da tela
LARGURA_TELA = 400
ALTURA_TELA = 300

# Será utilizado para a velocidade do jogo
FPS = 200


def main():
    pygame.init()
    global DISPLAYSURF
    
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption('PongNet')
    terminou = False
    while not terminou: # Loop principal do jogo
        for event in pygame.event.get():
            if event.type == QUIT:
                terminou = True
            
        pygame.display.update()
        FPSCLOCK.tick(FPS)
        
    # Finaliza a janela do jogo
    pygame.display.quit()

    # Finaliza o pygame
    pygame.quit()
    sys.exit()
    
if __name__ == 'main':
    main()