# Simple pygame program

# Import and initialize the pygame library
import pygame
import numpy as np
import random
dims=3

up = np.zeros(dims**2).reshape(dims,dims).astype(int)
left = np.zeros(dims**2).reshape(dims,dims).astype(int)+5
front = np.zeros(dims**2).reshape(dims,dims).astype(int)+4
right = np.zeros(dims**2).reshape(dims,dims).astype(int)+2
back = np.zeros(dims**2).reshape(dims,dims).astype(int)+1
down = np.zeros(dims**2).reshape(dims,dims).astype(int)+3
temp = np.zeros(dims).astype(int)




pygame.init()
WHITE = (255,255,255)
BLUE = (0,95,237)
RED = (212,2,2)
YELLOW = (247,247,45)
GREEN = (52,247,35)
ORANGE = (237,166,100)
colors = {0:WHITE,1:BLUE,2:RED,3:YELLOW,4:GREEN,5:ORANGE}

# Set up the drawing window
screen = pygame.display.set_mode([790, 600])
screen.fill((0,0,0))
clock = pygame.time.Clock()
font = pygame.font.Font(None,25)
frame_count = 0
frame_rate = 60


def display_time():
    pygame.draw.rect(screen,(0,0,0),pygame.Rect(600,50,100,30))
    total_seconds = frame_count//frame_rate
    output_string = "{}".format(total_seconds)
    text = font.render(output_string,True,(255,255,255))
    screen.blit(text,[600,50])
def timer_init():
    global frame_count
    global timer_on
    pygame.draw.rect(screen,(0,0,0),pygame.Rect(600,100,100,30))
    frame_count = 0
    display_time()
    timer_on = False
def timer_tick():
    global frame_count
    frame_count += 1
    clock.tick(frame_rate)
    
def check_solve():
    for i in range(3):
        for j in range(3):
            if up[i,j] != up[1,1]:
                return False
            if left[i,j] != left[1,1]:
                return False
            if front[i,j] != front[1,1]:
                return False
            if right[i,j] != right[1,1]:
                return False
            if back[i,j] != back[1,1]:
                return False
            #if down[i,j] != down[1,1]:
             #   return False
    return True

def win():
    global total_seconds
    #pygame.draw.rect(screen,(0,0,0),pygame.Rect(600,50,100,30))
    text = font.render("YOU WIN!",True,(255,255,255))
    screen.blit(text,[600,100])
# Run until the user asks to quit

def draw_face(face_array,x0,y0,cubie_width):
    
    for i in range(3):
        for j in range(3):
            pygame.draw.rect(screen,colors[face_array[i,j]],pygame.Rect(x0+1+60*j,y0+1+60*i,cubie_width-2,cubie_width-2))
            
    #pygame.draw.rect(screen,colors[top_array[0,0]],pygame.Rect(211,21,58,58))
    #pygame.draw.rect(screen,colors[top_array[0,0]],pygame.Rect(271,21,58,58))
    #pygame.draw.rect(screen,colors[top_array[0,0]],pygame.Rect(331,21,58,58))
    #pygame.draw.rect(screen,colors[top_array[0,0]],pygame.Rect(211,81,58,58))
    #pygame.draw.rect(screen,colors[top_array[0,0]],pygame.Rect(271,81,58,58))
    #pygame.draw.rect(screen,colors[top_array[0,0]],pygame.Rect(331,81,58,58))
    #pygame.draw.rect(screen,colors[top_array[0,0]],pygame.Rect(211,141,58,58))
    #pygame.draw.rect(screen,colors[top_array[0,0]],pygame.Rect(271,141,58,58))
    #ygame.draw.rect(screen,colors[top_array[0,0]],pygame.Rect(331,141,58,58))


# (x0,y0) values:
# TOP: (210,20)
# LEFT: (20,210)
# FRONT: (210,210)
# RIGHT: (400,210)
# BACK: (590,210)
# DOWN: (210,400)
def draw_cube():
    draw_face(up,210,20,60)
    draw_face(left, 20, 210, 60)
    draw_face(front, 210, 210, 60)
    draw_face(right, 400, 210, 60)
    draw_face(back, 590, 210, 60)
    draw_face(down, 210, 400, 60)
    
def u():
    # adjust u face
    temp[:] = up[0,:]
    up[0,:] = np.flip(up[:,0])
    up[:,0] = up[2,:]
    up[2,:] = np.flip(up[:,2])
    up[:,2] = temp
    # adjust l,f,r,b faces
    temp[:] = front[0,:]
    front[0,:] = right[0,:]
    right[0,:] = back[0,:]
    back[0,:] = left[0,:]
    left[0,:] = temp
def f():
    # adjust u face
    temp[:] = front[0,:]
    front[0,:] = np.flip(front[:,0])
    front[:,0] = front[2,:]
    front[2,:] = np.flip(front[:,2])
    front[:,2] = temp
    # adjust l,f,r,b faces
    temp[:] = up[2,:]
    up[2,:] = np.flip(left[:,2])
    left[:,2]=down[0,:]
    down[0,:] = np.flip(right[:,0])
    right[:,0] = temp
def r():
    # adjust u face
    temp[:] = right[0,:]
    right[0,:] = np.flip(right[:,0])
    right[:,0] = right[2,:]
    right[2,:] = np.flip(right[:,2])
    right[:,2] = temp
    # adjust l,f,r,b faces
    temp[:] = up[:,2]
    up[:,2] = front[:,2]
    front[:,2] = down[:,2]
    down[:,2] = np.flip(back[:,0])
    back[:,0] = np.flip(temp)
def l():
    # adjust u face
    temp[:] = left[0,:]
    left[0,:] = np.flip(left[:,0])
    left[:,0] = left[2,:]
    left[2,:] = np.flip(left[:,2])
    left[:,2] = temp
    # adjust l,f,r,b faces
    temp[:] = up[:,0]
    up[:,0] = np.flip(back[:,2])
    back[:,2] = np.flip(down[:,0])
    down[:,0] = front[:,0]
    front[:,0] = temp
def d():
    # adjust u face
    temp[:] = down[0,:]
    down[0,:] = np.flip(down[:,0])
    down[:,0] = down[2,:]
    down[2,:] = np.flip(down[:,2])
    down[:,2] = temp
    # adjust l,f,r,b faces
    temp[:] = front[2,:]
    front[2,:] = left[2,:]
    left[2,:] = back[2,:]
    back[2,:] = right[2,:]
    right[2,:] = temp
def b():
    # adjust u face
    temp[:] = back[0,:]
    back[0,:] = np.flip(back[:,0])
    back[:,0] = back[2,:]
    back[2,:] = np.flip(back[:,2])
    back[:,2] = temp
    # adjust l,f,r,b faces
    temp[:] = up[0,:]
    up[0,:] = right[:,2]
    right[:,2] = np.flip(down[2,:])
    down[2,:] = left[:,0]
    left[:,0] = np.flip(temp)

def ui():
    u();u();u()
def li():
    l();l();l()
def fi():
    f();f();f()
def ri():
    r();r();r()
def bi():
    b();b();b()
def di():
    d();d();d()
    
def u2():
    u();u();
def l2():
    l();l();
def f2():
    f();
    f();
def r2():
    r();r()
def b2():
    b();b()
def d2():
    d();d()
    
#cube rotations
def y():
    temp[:] = up[0,:] # need this [:]??
    up[0,:] = np.flip(up[:,0])
    up[:,0] = up[2,:]
    up[2,:] = np.flip(up[:,2])
    up[:,2] = temp
    
    temp[:] = down[0,:]
    down[0,:] = down[:,2]
    down[:,2] = np.flip(down[2,:])
    down[2,:] = down[:,0]
    down[:,0] = np.flip(temp)
    
    for i in range(3):
        for j in range(3):
            tempcell = front[i,j]
            front[i,j] = right[i,j]
            right[i,j] = back[i,j]
            back[i,j] = left[i,j]
            left[i,j] = tempcell
    
def yi():
    y();y();y();
def x():
    temp[:] = right[0,:]
    right[0,:] = np.flip(right[:,0])
    right[:,0] = right[2,:]
    right[2,:] = np.flip(right[:,2])
    right[:,2] = temp
    
    temp[:] = left[0,:]
    left[0,:] = left[:,2]
    left[:,2] = np.flip(left[2,:])
    left[2,:] = left[:,0]
    left[:,0] = np.flip(temp)
    
    
    for i in range(3):
        for j in range(3):
            tempcell = front[i,j]
            front[i,j] = down[i,j]
            down[i,j] = back[2-i,2-j]
            back[2-i,2-j] = up[i,j]
            up[i,j] = tempcell
            
def xi():
    x();x();x()
    
possible_moves= [r,ri,r2,u,ui,u2,l,li,l2,d,di,d2,f,fi,f2,b,bi,b2]
def scramble_cube(scramble_length):
    for i in range(scramble_length):
        possible_moves[random.randrange(len(possible_moves))]()
        
        
running = True
timer_on = False
while running:
    
    for event in pygame.event.get():
         if event.type == pygame.QUIT:
             running = False
         if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                scramble_cube(30)
                draw_cube()
                timer_init()
            if event.key == pygame.K_j:
                if timer_on == False:
                    timer_on = True
                u()
                draw_cube()
            if event.key == pygame.K_f:
                if timer_on == False:
                    timer_on = True
                ui()
                draw_cube()
            if event.key == pygame.K_i:
                if timer_on == False:
                    timer_on = True
                r()
                draw_cube()
            if event.key == pygame.K_k:
                if timer_on == False:
                    timer_on = True
                ri()
                draw_cube()
            if event.key == pygame.K_e:
                if timer_on == False:
                    timer_on = True
                li()
                draw_cube()
            if event.key == pygame.K_d:
                if timer_on == False:
                    timer_on = True
                l()
                draw_cube()
            if event.key == pygame.K_s:
                if timer_on == False:
                    timer_on = True
                d()
                draw_cube()
            if event.key == pygame.K_l:
                if timer_on == False:
                    timer_on = True
                di()
                draw_cube()
            if event.key == pygame.K_h:
                if timer_on == False:
                    timer_on = True
                f()
                draw_cube()
            if event.key == pygame.K_g:
                if timer_on == False:
                    timer_on = True
                fi()
                draw_cube()
            if event.key == pygame.K_o:
                if timer_on == False:
                    timer_on = True
                bi()
                draw_cube()
            if event.key == pygame.K_w:
                if timer_on == False:
                    timer_on = True
                b()
                draw_cube()
            if event.key == pygame.K_SEMICOLON:
                y()
                draw_cube()
            if event.key == pygame.K_a:
                yi()
                draw_cube()
            if event.key == pygame.K_y:
                x()
                draw_cube()
            if event.key == pygame.K_n:
                xi()
                draw_cube()
    if timer_on:
        timer_tick()
        display_time()
        if check_solve():
            timer_on = False
            win()
            
                
                
                
    
    
    

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()