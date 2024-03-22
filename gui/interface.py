import pygame
import os
from gui.button import *
import source.utils as utils

SIZE = 540
PIECE = 32
N = 15
MARGIN = 23
GRID = (SIZE - 2 * MARGIN) / (N-1)

FPS = 30

class GameUI(object):
    def __init__(self, ai):
        self.ai = ai
        self.colorState = {}
        self.mapping = utils.create_mapping()
        
        # khởi tạo pygame
        pygame.init()
        self.screen = pygame.display.set_mode((SIZE, SIZE))
        pygame.display.set_caption('Chơi Caro XO!')

        self.board = pygame.image.load(os.path.join("assets", 'board.png')).convert()
        self.blackPiece = pygame.image.load(os.path.join("assets", 'black_piece.png')).convert_alpha()
        self.whitePiece = pygame.image.load(os.path.join("assets", 'white_piece.png')).convert_alpha()
        self.menuBoard = pygame.image.load(os.path.join("assets", "menu_board2.png")).convert_alpha()
        self.buttonSurf = pygame.image.load(os.path.join("assets", "button.png")).convert_alpha()
        self.buttonSurf = pygame.transform.scale(self.buttonSurf, (110, 60)) 
        self.screen.blit(self.board, (0,0))
        pygame.display.update()

    def drawMenu(self): 
        menu_board = pygame.transform.scale(self.menuBoard, (350,120))
        menu_board_rect = menu_board.get_rect(center = self.screen.get_rect().center)

        menu_font = pygame.font.SysFont("arial", 22)
        menu_text = menu_font.render('CHỌN MÀU CỦA BẠN: ', True, 'white')
        menu_board.blit(menu_text, (50,25))
        self.screen.blit(menu_board, menu_board_rect)

        pygame.display.update()
    
    def drawButtons(self, button1, button2, surface):
        button1.draw(surface)
        button2.draw(surface)
        pygame.display.update()
        

    # ktra ng chơi đã chọn màu nào
    def checkColorChoice(self, button_black, button_white, pos):
        if button_black.rect.collidepoint(pos):
            self.colorState[-1] = 'đen'
            self.colorState[1] = 'trắng'
            self.ai.turn = -1

        elif button_white.rect.collidepoint(pos):
            self.colorState[-1] = 'trắng'
            self.colorState[1] = 'đen'
            self.ai.turn = 1


    def drawPiece(self, state, i, j):
        x, y = self.mapping[(i,j)]
        x = x - PIECE/2
        y = y - PIECE/2

        if state == 'đen': 
            self.screen.blit(self.blackPiece, (x, y))
        elif state == 'trắng':
            self.screen.blit(self.whitePiece, (x, y))

        pygame.display.update()


    def drawResult(self, tie=False):
        menu_board = pygame.transform.scale(self.menuBoard, (400,190))
        width, height = menu_board.get_size()
        font = pygame.font.SysFont('arial', 25, True)
        
        if tie:
            text = "Đó là trận hòa! Ngu vc"
            render_text = font.render(str.upper(text), True, 'white')
            text_size = render_text.get_size()
            (x, y) = (width//2 - text_size[0]//2, height//4 - text_size[1]//2)
            menu_board.blit(render_text, (x, y))
            
        else:
            text = 'Ng chiến thắng là: '
            render_text = font.render(str.upper(text), True, 'white')
            size1 = render_text.get_size()
            (x1, y1) = (width//2 - size1[0]//2, 30)

            winner = self.ai.getWinner()
            render_winner = font.render(str.upper(winner), True, 'white')
            size2 = render_winner.get_size()
            (x2, y2) = (width//2 - size2[0]//2, 30 + size1[1])

            menu_board.blit(render_text, (x1, y1))
            menu_board.blit(render_winner, (x2, y2))
        
        restart_font = pygame.font.SysFont('arial', 18)
        restart_text = 'M ngu quá có muốn chơi lại k?'
        render_restart = restart_font.render(str.upper(restart_text), True, 'white')
        restart_size = render_restart.get_size()
        (x3, y3) = (width//2 - restart_size[0]//2, height//2) 
        menu_board.blit(render_restart, (x3, y3))

        self.screen.blit(menu_board, (SIZE//2 - width//2, MARGIN//2))
        pygame.display.update()
