import pygame
import numpy as np

grid_width, grid_height = 220, 100
cell_size = 8

grid = np.zeros((grid_width, grid_height), dtype = int)

center = grid_width//2
start_cell = (center, 1)
#start_cell_2 = (center + 3, 2)
#grid[start_cell] = 63
#grid[start_cell] = 15
grid[start_cell] = 52
#grid[start_cell] = 60
#grid[start_cell] = 7

pygame.init()

screen_width = grid_width * cell_size
screen_height = grid_height * cell_size
screen = pygame.display.set_mode((screen_width, screen_height))

white = (255, 255, 255)
black = (0, 0, 0)

f = lambda x: (x//16, (x % 16)//4, x % 4)
#f = lambda x: (x//4, (x % 4)//2, x % 2)

def rule(a, b, c):
    a1, a2, a3 = f(a)
    b1, b2, b3 = f(b)
    c1, c2, c3 = f(c)
    res = (a1^a2^a1)*16 + (b1^b2^b3)*4 + (c1^c2^c3)*1
    #res = (a1^a2^a1)*18 + (b1^b2^b3)*22 + (c1^c2^c3)*6
    #res = (a1^a2^a1)*16 + (b1^b2^b3)*3 + (c1^c2^c3)*1
    #res = (a1^a2^a1)*4 + (b1^b2^b3)*2 + (c1^c2^c3)*1
    return res % 64
    #return res % 8

def update_grid(current_grid):
    new_grid = np.zeros_like(current_grid)
    for i in range(1, grid_height - 1):
        for j in range(center - i, center + i + 1):
            if current_grid[j, i]:
                new_grid[j, i] = current_grid[j, i]
            else:
                new_grid[j, i] = rule(current_grid[j - 1, i - 1], current_grid[j, i - 1], current_grid[j + 1, i - 1])
                #new_grid[j, i] = rule(current_grid[j - 1, i - 1], current_grid[j, i], current_grid[j + 1, i - 1])
                #new_grid[j, i] = rule(current_grid[j - 1, i - 1], current_grid[j, i - 1], current_grid[j + 2, i - 1])
    return new_grid

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    grid = update_grid(grid)

    screen.fill(black)
    for i in range(grid_width):
        for j in range(grid_height):
            g = grid[i, j]
            a, b, c = f(g)
            color = (85*a, 85*b, 85*c)
            #color = (255*a, 255*b, 255*c)
            pygame.draw.rect(screen, color, (i * cell_size, j * cell_size, cell_size, cell_size))

    pygame.display.flip()

#pygame.quit()
