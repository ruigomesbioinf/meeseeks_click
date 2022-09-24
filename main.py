# imports
import pygame
import time
import os

# initialize pygame
pygame.init()
pygame.mixer.init()

# defining variables
clock = pygame.time.Clock()
display_width = 600
display_height = 800
RICK_MORTY = (15, 156, 66)
MR_BLUE = (116,226,243)
WHITE = (255, 255, 255)
DISABLED = (220, 220, 220)
coins = 0
auto_miner_add_coin = 0




# set display settings
screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("MeeseeksClicks")

# load images
meeseeks_box = pygame.image.load(os.path.join("assets", "box.png")).convert_alpha()
meeseeks_box = pygame.transform.scale(meeseeks_box, (183, 192))
box_rect = meeseeks_box.get_rect()
box_rect.center = (display_width // 2, display_height // 2)

# meeseeks sound
def meeseeks_sound():
    pygame.mixer.music.load(os.path.join("assets", "lookatme.mp3"))
    pygame.mixer.music.play()

def no_money():
    pygame.mixer.music.load(os.path.join("assets", "no_money.mp3"))
    pygame.mixer.music.play()
    
def main_theme():
    pygame.mixer.music.load(os.path.join("assets", "theme.mp3"))
    pygame.mixer.music.play(-1)
    
def auto_miner():
    global coins
    global auto_miner_add_coin
    time.sleep(0.5)
    coins += auto_miner_add_coin

def draw_text(text, text_color, x, y, font_size, rect_color = None):
    font = pygame.font.Font(os.path.join("assets", "04B_30__.TTF"), font_size)
    text = font.render(text, True, text_color, rect_color)
    text_rect = text.get_rect()
    text_rect.center = (x, y)
    screen.blit(text, text_rect)
    return text_rect

def mainloop():
    global coins
    global auto_miner_add_coin
    game_running = True
    add_coin = 1
    automining_costs = {0: 1000, 1: 2500, 2: 5000, 3: 10000, 4: 50000}
    # automining_costs = {0: 10, 1: 20, 2: 30, 3: 40} #testes
    automining_gain = {0: 0, 1: 4, 2: 16, 3: 48, 4: 158}
    automining = 0 # 0 for nothing, 1 for level 1, 2 for level 2, 3 for level 3 and 4 for level 4 autominer

    while game_running:
        # main_theme()
        if game_running:
            auto_miner()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if box_rect.collidepoint(x, y):
                    coins += add_coin
                elif autominer_rect.collidepoint(x, y):
                    if automining == 4:
                        break
                    if coins >= automining_costs[automining]:
                        coins -= automining_costs[automining]
                        automining += 1
                        auto_miner_add_coin = automining_gain[automining]
                        meeseeks_sound()
                    else:
                        no_money()
    



        
        screen.fill(MR_BLUE)
        draw_text("SCHMECKLES", RICK_MORTY, display_width // 2, 40, 30)
        draw_text(f"{coins}", RICK_MORTY, display_width // 2, 80, 40)

        if automining == 0:
            autominer_rect = draw_text("buy autominer (1000)", WHITE, display_width // 2, 700, 25, RICK_MORTY)
        elif automining == 1:
            autominer_rect = draw_text("upgrade autominer (3500)", WHITE, display_width // 2, 700, 25, RICK_MORTY)
        elif automining == 2:
            autominer_rect = draw_text("upgrade autominer (7000)", WHITE, display_width // 2, 700, 25, RICK_MORTY)
        elif automining == 3:
            autominer_rect = draw_text("upgrade autominer (10000)", WHITE, display_width // 2, 700, 25, RICK_MORTY)
        elif automining == 4:
            autominer_rect = draw_text("autominer max.", WHITE, display_width // 2, 700, 25, DISABLED)



        screen.blit(meeseeks_box, box_rect)
        pygame.display.update()
        clock.tick(60)


# exiting game
mainloop()
pygame.quit()
quit()

