import pygame
import random

# Inicializa o pygame
pygame.init()

# Configurações da tela
LARGURA = 800
ALTURA = 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Pegue o Objeto")

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)
AZUL = (0, 0, 255)

# Relógio para controlar o FPS
relogio = pygame.time.Clock()

# Variáveis do jogador
jogador_tamanho = 50
jogador_x = LARGURA // 2 - jogador_tamanho // 2
jogador_y = ALTURA - jogador_tamanho - 10
jogador_velocidade = 10

# Variáveis do objeto
objeto_tamanho = 30
objeto_x = random.randint(0, LARGURA - objeto_tamanho)
objeto_y = random.randint(0, ALTURA // 2)
objeto_velocidade = 5

# Pontuação
pontos = 0
fonte = pygame.font.SysFont(None, 55)

# Função para desenhar o jogador e o objeto
def desenhar_jogador(x, y):
    pygame.draw.rect(tela, AZUL, (x, y, jogador_tamanho, jogador_tamanho))

def desenhar_objeto(x, y):
    pygame.draw.rect(tela, VERMELHO, (x, y, objeto_tamanho, objeto_tamanho))

def mostrar_pontos(pontos):
    texto = fonte.render(f"Pontos: {pontos}", True, BRANCO)
    tela.blit(texto, (10, 10))

# Loop principal do jogo
executando = True
while executando:
    # Limpa a tela
    tela.fill(PRETO)

    # Verifica eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False

    # Movimentação do jogador
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]or teclas[pygame.K_a] and jogador_x > 0:
        jogador_x -= jogador_velocidade
    if teclas[pygame.K_RIGHT] or teclas[pygame.K_d] and jogador_x < LARGURA - jogador_tamanho:
        jogador_x += jogador_velocidade
    if teclas[pygame.K_UP] or teclas[pygame.K_w] and jogador_y > 0:
        jogador_y -= jogador_velocidade
    if teclas[pygame.K_DOWN] or teclas[pygame.K_s] and jogador_y < ALTURA - jogador_tamanho:
        jogador_y += jogador_velocidade

    # Movimentação do objeto (caindo)
    objeto_y += objeto_velocidade
    if objeto_y > ALTURA:
        objeto_x = random.randint(0, LARGURA - objeto_tamanho)
        objeto_y = 0

    # Verifica colisão entre jogador e objeto
    if (jogador_x < objeto_x + objeto_tamanho and
        jogador_x + jogador_tamanho > objeto_x and
        jogador_y < objeto_y + objeto_tamanho and
        jogador_y + jogador_tamanho > objeto_y):
        pontos += 1
        objeto_x = random.randint(0, LARGURA - objeto_tamanho)
        objeto_y = 0

    # Desenha o jogador, o objeto e a pontuação
    desenhar_jogador(jogador_x, jogador_y)
    desenhar_objeto(objeto_x, objeto_y)
    mostrar_pontos(pontos)

    # Atualiza a tela
    pygame.display.update()

    # Controla o FPS
    relogio.tick(30)

# Fecha o pygame
pygame.quit()