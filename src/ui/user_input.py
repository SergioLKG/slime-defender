import pygame

import src.controls.mouse as mouseconf
import src.util.gameconf as conf


def open():
    screen = conf.__sizescreen__()
    input_rect = pygame.Rect(200, 200, 400, 40)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    font = pygame.font.Font(None,36)
    custom_cursor = mouseconf.Cursor()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = not active
            else: 
                active = False
            color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        return text
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode

        screen.fill((200, 255, 200, 0))  # Color del fondo
       

        txt_surface = font.render(text, True, color)
        width = max(200, txt_surface.get_width()+10)
        input_rect.w = width
        screen.blit(txt_surface, (input_rect.x, input_rect.y))
        pygame.draw.rect(screen, color, input_rect, 2)

        custom_cursor.update()
        custom_cursor.draw()
        
        pygame.display.flip()