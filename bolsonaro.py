import pygame
import random

# Inicializa o Pygame
pygame.init()

# Configurações da tela
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bolsonaro vs Canos Lula")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Dimensões do jogador
BIRD_WIDTH, BIRD_HEIGHT = 50, 35
bird_x, bird_y = 50, HEIGHT // 2
bird_y_change = 0

# Função para desenhar o jogador (Bolsonaro)
def draw_bolsonaro(x, y):
    pygame.draw.rect(screen, RED, [x, y, BIRD_WIDTH, BIRD_HEIGHT])  # Desenha um retângulo vermelho como o jogador

# Função para desenhar os canos (Lula)
def draw_pipes(pipe_x, pipe_y, pipe_width, pipe_height, gap):
    pygame.draw.rect(screen, GREEN, [pipe_x, pipe_y, pipe_width, pipe_height])  # Cano superior
    pygame.draw.rect(screen, GREEN, [pipe_x, pipe_y + pipe_height + gap, pipe_width, HEIGHT - pipe_height - gap])  # Cano inferior

# Função principal do jogo
def game_loop():
    global bird_y, bird_y_change
    clock = pygame.time.Clock()
    score = 0

    # Posição dos canos
    pipe_x = WIDTH
    pipe_width = 70
    pipe_height = random.randint(150, 400)
    pipe_gap = 150
    pipe_speed = 3

    running = True
    while running:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird_y_change = -8  # Pulo
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    bird_y_change = 5  # Gravidade

        # Movimenta o jogador (Bolsonaro)
        bird_y += bird_y_change
        if bird_y < 0:
            bird_y = 0
        if bird_y > HEIGHT - BIRD_HEIGHT:
            bird_y = HEIGHT - BIRD_HEIGHT

        # Movimenta os canos (Lula)
        pipe_x -= pipe_speed
        if pipe_x < -pipe_width:
            pipe_x = WIDTH
            pipe_height = random.randint(150, 400)
            score += 1

        # Desenhar personagem Bolsonaro e canos Lula
        draw_bolsonaro(bird_x, bird_y)
        draw_pipes(pipe_x, 0, pipe_width, pipe_height, pipe_gap)

        # Verifica colisão
        if (bird_x + BIRD_WIDTH > pipe_x and bird_x < pipe_x + pipe_width):
            if bird_y < pipe_height or bird_y + BIRD_HEIGHT > pipe_height + pipe_gap:
                running = False  # Colisão com cano (fim de jogo)

        # Atualiza a tela
        pygame.display.update()
        clock.tick(30)

    # Exibe mensagem de game over
    font = pygame.font.SysFont(None, 55)
    game_over_text = font.render(f"Game Over! Pontos: {score}", True, BLACK)
    screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2))
    pygame.display.flip()
    pygame.time.wait(2000)

# Chama o loop do jogo
game_loop()

# Finaliza o Pygame
pygame.quit()
