import pygame


def keycontrols(ctx, event):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            ctx.click()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Botón izquierdo del ratón
                ctx.click()
    if event.type == pygame.KEYUP:
        pass
