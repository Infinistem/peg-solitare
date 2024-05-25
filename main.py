import pygame, sys, math # super duper easy pygame tile map project, but i like this game so i made it while sitting around waiting
W_WIDTH = 570
W_HEIGHT = 570
WIDTH = W_WIDTH/10
HEIGHT = W_HEIGHT/10
FPS = 240
board = []
game = True
selectedPeg, selectedDest = None, None
rects = []
def reset():
    global board
    board = [
[-1,-1, 1, 1, 1,-1,-1],
[-1,-1, 1, 1, 1,-1,-1],
[1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 0, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1],
[-1,-1, 1, 1, 1,-1,-1],
[-1,-1, 1, 1, 1,-1,-1],
]
    draw()
def clicked(pos):
    global selectedDest, selectedPeg
    for i,x in enumerate(rects):
        if x.collidepoint(pos):
            col = i % 7
            row = math.floor(i/7)
            if board[row][col] == 1:
                selectedPeg = [row, col]
            elif board[row][col] == 0:
                selectedDest = [row, col]
            if selectedPeg and selectedDest:
                dx = selectedDest[0] - selectedPeg[0]
                dy = selectedDest[1] - selectedPeg[1]
                if (dx == 0 or dy == 0) and ((abs(dx) == 2) or (abs(dy) == 2)):
                    board[selectedPeg[0]][selectedPeg[1]] = 0
                    board[selectedDest[0]][selectedDest[1]] = 1
                    mx = (selectedPeg[0] + selectedDest[0]) / 2
                    my = (selectedPeg[1] + selectedDest[1]) / 2
                    board[int(mx)][int(my)] = 0
                    draw()
                selectedDest, selectedPeg = None, None
            break
def render(cell, row, col):
    if cell == -1:
        rect = pygame.Rect((col+1)*WIDTH+25, (row+1)*HEIGHT+25, WIDTH-1, HEIGHT-1)
        rects.append(rect)
        pygame.draw.rect(screen, (25, 222, 50), rect)
    elif cell == 0:
        rect = pygame.Rect((col+1)*WIDTH+25, (row+1)*HEIGHT+25, WIDTH-1, HEIGHT-1)
        pygame.draw.rect(screen, (25, 222, 50), rect)
        rects.append(rect)
        pygame.draw.circle(screen, (60,222,200), ((col+1)*WIDTH+53, (row+1)*HEIGHT+53), WIDTH/2)
    elif cell == 1:
        rect = pygame.Rect((col+1)*WIDTH+25, (row+1)*HEIGHT+25, WIDTH-1, HEIGHT-1)
        pygame.draw.rect(screen, (25, 222, 50), rect)
        rects.append(rect)
        pygame.draw.circle(screen, (60,22,200), ((col+1)*WIDTH+53, (row+1)*HEIGHT+53), WIDTH/2.2)
def draw():
    for i in range(7):
        for j in range(7):
            render(board[i][j], i, j)
pygame.init()
mainClock = pygame.time.Clock()
pygame.display.set_caption('Peg Solitare')
screen = pygame.display.set_mode((W_WIDTH, W_HEIGHT),0,32)
font = pygame.font.SysFont(None, 30)
reset()
while game:
    screen.fill((255, 255, 255))
    textobj = font.render("Simple Peg Solitare", 1, (0, 0, 255))
    textrect = textobj.get_rect()
    textrect.topleft = (WIDTH/3, 10)
    screen.blit(textobj, textrect)
    button = pygame.Rect(400, 10, 160, 40)
    pygame.draw.rect(screen, (25, 222, 50), button)
    textobj = font.render("Reset", 1, (88, 222, 255))
    textrect = textobj.get_rect()
    textrect.topleft = (400, 10)
    screen.blit(textobj, textrect)
    draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pos = pygame.mouse.get_pos()
                if button.collidepoint(pos):
                    reset()
                    continue
                clicked(pos)
    pygame.display.update()
    mainClock.tick(FPS)
