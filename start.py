from gui.interface import *
from source.Bot import *
from gui.button import Button
import source.utils as utils
import source.caro as caro
import pygame

pygame.init()

def startGame():
    pygame.init()
    # khởi tạo
    bot = CaroAI()
    game = GameUI(bot)
    button_black = Button(game.buttonSurf, 200, 290, "X", 22)
    button_white = Button(game.buttonSurf, 340, 290, "O", 22)

    # menu bắt đầu
    game.drawMenu()
    game.drawButtons(button_black, button_white, game.screen)
    
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN\
                    and pygame.mouse.get_pressed()[0]:
                mouse_pos = pygame.mouse.get_pos()
                # Ktra màu ng chơi đã chọn và đặt trạng thái
                game.checkColorChoice(button_black, button_white, mouse_pos)
                game.screen.blit(game.board, (0,0))
                pygame.display.update()
                
                if game.ai.turn == 1:
                    game.ai.firstMove()
                    game.drawPiece('đen', game.ai.currentI, game.ai.currentJ)
                    pygame.display.update()
                    game.ai.turn *= -1
                
                main(game)

                # Khi trò chơi kết thúc và có ng chiến thắng, tạo bảng kết quả
                if game.ai.checkResult() != None:
                    last_screen = game.screen.copy()
                    game.screen.blit(last_screen, (0,0))
                    #endMenu(game, last_screen)
                    game.drawResult()

                    # cái này cài đặt để hỏi ng chơi có muốn khởi động lại trò chơi hay không
                    yes_button = Button(game.buttonSurf, 200, 155, "CÓ", 18)
                    no_button = Button(game.buttonSurf, 350, 155, "KHÔNG", 18)
                    game.drawButtons(yes_button, no_button, game.screen)
                    mouse_pos = pygame.mouse.get_pos()
                    if yes_button.rect.collidepoint(mouse_pos):
                        # khởi động lại trò chơi
                        game.screen.blit(game.board, (0,0))
                        pygame.display.update()
                        game.ai.turn = 0
                        startGame()
                    if no_button.rect.collidepoint(mouse_pos):
                        # kết thúc trò chơi
                        pygame.quit()
        pygame.display.update()   

    pygame.quit()

def endMenu(game, last_screen):
    pygame.init()
    game.screen.blit(last_screen, (0,0))
    pygame.display.update()
    run = True
    while run:
        for event in pygame.event.get():
            game.drawResult()
            yes_button = Button(game.buttonSurf, 200, 155, "CÓ", 18)
            no_button = Button(game.buttonSurf, 350, 155, "KHÔNG", 18)
            game.drawButtons(yes_button, no_button, game.screen)
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN\
                    and pygame.mouse.get_pressed()[0]:
                mouse_pos = pygame.mouse.get_pos()
                if yes_button.rect.collidepoint(mouse_pos):
                    print('Chọn CÓ')
                    game.screen.blit(game.board, (0,0))
                    pygame.display.update()
                    startGame()
                if no_button.rect.collidepoint(mouse_pos):
                    print('Chọn KHÔNG')
                    run = False
    pygame.quit()


# vòng lặp chính của trò chơi
def main(game):
    pygame.init()
    end = False
    result = game.ai.checkResult()

    while not end:
        turn = game.ai.turn
        color = game.colorState[turn]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            # lượt bot
            if turn == 1:
                move_i, move_j = caro.ai_move(game.ai)
                # thực hiện nước đi và cập nhật bảng zobrist
                game.ai.setState(move_i, move_j, turn)
                game.ai.rollingHash ^= game.ai.zobristTable[move_i][move_j][0]
                game.ai.emptyCells -= 1

                game.drawPiece(color, move_i, move_j)
                result = game.ai.checkResult()
                # chuyển lượt
                game.ai.turn *= -1

            # lượt của ng chơi
            if turn == -1:
                if event.type == pygame.MOUSEBUTTONDOWN\
                        and pygame.mouse.get_pressed()[0]:
                    # nhận nước đi của ng chơi
                    mouse_pos = pygame.mouse.get_pos()
                    human_move = utils.pos_pixel2map(mouse_pos[0], mouse_pos[1])
                    move_i = human_move[0]
                    move_j = human_move[1]
                    #print(mouse_pos, move_i, move_j)

                    # ktra tính hợp lệ của nước đi của ng chơi
                    if game.ai.isValid(move_i, move_j):
                        game.ai.boardValue = game.ai.evaluate(move_i, move_j, game.ai.boardValue, -1, game.ai.nextBound)
                        game.ai.updateBound(move_i, move_j, game.ai.nextBound)
                        game.ai.currentI, game.ai.currentJ = move_i, move_j
                        # thực hiện nước đi và cập nhật bảng zobrist
                        game.ai.setState(move_i, move_j, turn)
                        game.ai.rollingHash ^= game.ai.zobristTable[move_i][move_j][1]
                        game.ai.emptyCells -= 1
                        
                        game.drawPiece(color, move_i, move_j)
                        result =  game.ai.checkResult()
                        game.ai.turn *= -1
            
            if result != None:
                # hết game =))
                end = True



if __name__ == '__main__':
    startGame()
