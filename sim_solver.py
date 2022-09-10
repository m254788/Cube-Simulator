import numpy as np
import random
import pygame

def init(): # solve cube, reset scramble and solution
    global cube
    global temp
    global scramble
    global solution
    cube = np.zeros(6*3*3).reshape(6,3,3).astype(int)
    for face in range(6):
        cube[face,:,:] = face
    temp = np.zeros(3).astype(int)
    scramble = []
    solution = []


pygame.init()
WHITE = (255,255,255)
BLUE = (0,95,237)
RED = (212,2,2)
YELLOW = (247,247,45)
GREEN = (52,247,35)
ORANGE = (237,166,100)
GREY = (50,50,50)
HIGHLIGHTED = (100,100,100)
colors = {0:WHITE,1:ORANGE,2:GREEN,3:RED,4:BLUE,5:YELLOW,6:GREY,7:HIGHLIGHTED}

screen = pygame.display.set_mode([790, 600])
screen.fill((0,0,0))
clock = pygame.time.Clock()
font = pygame.font.Font(None,25)
frame_count = 0
frame_rate = 60

tps = 6

def draw_face(face_array,x0,y0,cubie_width):
    for i in range(3):
        for j in range(3):
            pygame.draw.rect(screen,colors[face_array[i,j]],pygame.Rect(x0+1+60*j,y0+1+60*i,cubie_width-2,cubie_width-2))

def drawcube(my_cube,delay):
    draw_face(my_cube[0],210,20,60)
    draw_face(my_cube[1], 20, 210, 60)
    draw_face(my_cube[2], 210, 210, 60)
    draw_face(my_cube[3], 400, 210, 60)
    draw_face(my_cube[4], 590, 210, 60)
    draw_face(my_cube[5], 210, 400, 60)
    pygame.time.delay(delay)
    pygame.display.flip()


def simplifymoves(sol):
    facedict = {0:'U',1:'L',2:'F',3:'R',4:'B',5:'D'}
    magdict = {1:'',2:'2',3:'i'}
    i = 0
    simplified_solution = []
    while i < len(sol):
        chain = 0
        j = i
        while j < len(sol) and sol[j][0]==sol[i][0]:
            chain += sol[j][1]
            j += 1
        if chain%4 >0:
            simplified_solution.append(facedict[sol[i][0]]+magdict[chain%4])
        i = j
    return simplified_solution


def u(solstep,animate=True):
    global solution
    if solstep:
        solution.append([0,1])
    ##print('u')
    global cube
    # adjust u face
    temp[:] = cube[0,0,:]
    cube[0,0,:] = np.flip(cube[0,:,0])
    cube[0,:,0] = cube[0,2,:]
    cube[0,2,:] = np.flip(cube[0,:,2])
    cube[0,:,2] = temp
    # adjust l,f,r,b faces
    temp[:] = cube[2,0,:]
    cube[2,0,:] = cube[3,0,:]
    cube[3,0,:] = cube[4,0,:]
    cube[4,0,:] = cube[1,0,:]
    cube[1,0,:] = temp

    if animate:
        drawcube(cube,int(1000/tps))
        
def f(solstep,animate=True):
    global solution
    if solstep:
        solution.append([2,1])
    ##print('f')
    global cube
    # adjust u face
    temp[:] = cube[2,0,:]
    cube[2,0,:] = np.flip(cube[2,:,0])
    cube[2,:,0] = cube[2,2,:]
    cube[2,2,:] = np.flip(cube[2,:,2])
    cube[2,:,2] = temp
    # adjust l,f,r,b faces
    temp[:] = cube[0,2,:]
    cube[0,2,:] = np.flip(cube[1,:,2])
    cube[1,:,2]=cube[5,0,:]
    cube[5,0,:] = np.flip(cube[3,:,0])
    cube[3,:,0] = temp

    if animate:
        
        drawcube(cube,int(1000/tps))
        
def r(solstep,animate=True):
    global solution
    if solstep:
        solution.append([3,1])
    ##print('r')
    global cube
    # adjust u face
    temp[:] = cube[3,0,:]
    cube[3,0,:] = np.flip(cube[3,:,0])
    cube[3,:,0] = cube[3,2,:]
    cube[3,2,:] = np.flip(cube[3,:,2])
    cube[3,:,2] = temp
    # adjust l,f,r,b faces
    temp[:] = cube[0,:,2]
    cube[0,:,2] = cube[2,:,2]
    cube[2,:,2] = cube[5,:,2]
    cube[5,:,2] = np.flip(cube[4,:,0])
    cube[4,:,0] = np.flip(temp)

    if animate:
        drawcube(cube,int(1000/tps))
        
def l(solstep,animate=True):
    global solution
    if solstep:
        solution.append([1,1])
    ##print('l')
    global cube
    # adjust u face
    temp[:] = cube[1,0,:]
    cube[1,0,:] = np.flip(cube[1,:,0])
    cube[1,:,0] = cube[1,2,:]
    cube[1,2,:] = np.flip(cube[1,:,2])
    cube[1,:,2] = temp
    # adjust l,f,r,b faces
    temp[:] = cube[0,:,0]
    cube[0,:,0] = np.flip(cube[4,:,2])
    cube[4,:,2] = np.flip(cube[5,:,0])
    cube[5,:,0] = cube[2,:,0]
    cube[2,:,0] = temp

    if animate:
        
        drawcube(cube,int(1000/tps))
def d(solstep,animate=True):
    global solution
    if solstep:
        solution.append([5,1])
    ##print('d')
    global cube
    # adjust u face
    temp[:] = cube[5,0,:]
    cube[5,0,:] = np.flip(cube[5,:,0])
    cube[5,:,0] = cube[5,2,:]
    cube[5,2,:] = np.flip(cube[5,:,2])
    cube[5,:,2] = temp
    # adjust l,f,r,b faces
    temp[:] = cube[2,2,:]
    cube[2,2,:] = cube[1,2,:]
    cube[1,2,:] = cube[4,2,:]
    cube[4,2,:] = cube[3,2,:]
    cube[3,2,:] = temp

    if animate:
        
        drawcube(cube,int(1000/tps))
def b(solstep,animate=True):
    global solution
    if solstep:
        solution.append([4,1])
    ##print('b')
    global cube
    # adjust u face
    temp[:] = cube[4,0,:]
    cube[4,0,:] = np.flip(cube[4,:,0])
    cube[4,:,0] = cube[4,2,:]
    cube[4,2,:] = np.flip(cube[4,:,2])
    cube[4,:,2] = temp
    # adjust l,f,r,b faces
    temp[:] = cube[0,0,:]
    cube[0,0,:] = cube[3,:,2]
    cube[3,:,2] = np.flip(cube[5,2,:])
    cube[5,2,:] = cube[1,:,0]
    cube[1,:,0] = np.flip(temp)

    if animate:
       
        drawcube(cube,int(1000/tps))
def ui(solstep,animate=True):
    u(solstep,False);u(solstep,animate=False);u(solstep,animate)

def li(solstep,animate=True):
    l(solstep,False);l(solstep,False);l(solstep,animate)

def fi(solstep,animate=True):
    f(solstep,False);f(solstep,False);f(solstep,animate)

def ri(solstep,animate=True):
    r(solstep,False);r(solstep,False);r(solstep,animate)

def bi(solstep,animate=True):
    b(solstep,False);b(solstep,False);b(solstep,animate)

def di(solstep,animate=True):
    d(solstep,False);d(solstep,False);d(solstep,animate)

    
def u2(solstep,animate=True):
    u(solstep,False);u(solstep,animate);

def l2(solstep,animate=True):
    l(solstep,False);l(solstep,animate);

def f2(solstep,animate=True):
    f(solstep,False);
    f(solstep,animate);

def r2(solstep,animate=True):
    r(solstep,False);r(solstep,animate)

def b2(solstep,animate=True):
    b(solstep,False);b(solstep,animate)

def d2(solstep,animate=True):
    d(solstep,False);d(solstep,animate)

def donothing(solstep):
    pass

def scramble_cube(scramble_length,printout):
    possible_moves= [u,l,f,r,b,d,ui,li,fi,ri,bi,di,u2,l2,f2,r2,b2,d2]
    possible_move_names=[[0,1],[1,1],[2,1],[3,1],[4,1],[5,1],[0,-1],[1,-1],[2,-1],[3,-1],[4,-1],[5,-1],[0,2],[1,2],[2,2],[3,2],[4,2],[5,2]]
    global scramble
    for index in range(scramble_length):
        i = random.randrange(len(possible_moves))#
        possible_moves[i](False,animate=False)
        scramble.append(possible_move_names[i])#
    scramble = simplifymoves(scramble)
    if printout:
        print(scramble)
        print(cube)

def user_input_scramble():
    global cube
    init()
    for f in range(6):
        for r in range(3):
            for c in range(3):
                cube[f,r,c] = 6 #GREY
    drawcube(cube,0)


    index = 0
    while index < 6*3*3:
        f = index//9
        r = (index-f*9)//3
        c = index-f*9-r*3
        highlighted = True
        while highlighted:
            cube[f,r,c] = 7
            drawcube(cube,0)
            for event in pygame.event.get():
                 if event.type == pygame.QUIT:
                     pygame.quit()
                 if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        cube[f,r,c] = 0
                        drawcube(cube,0)
                        highlighted = False
                        index += 1
                    if event.key == pygame.K_o:
                        cube[f,r,c] = 1
                        drawcube(cube,0)
                        highlighted = False
                        index += 1
                    if event.key == pygame.K_g:
                        cube[f,r,c] = 2
                        drawcube(cube,0)
                        highlighted = False
                        index += 1
                    if event.key == pygame.K_r:
                        cube[f,r,c] = 3
                        drawcube(cube,0)
                        highlighted = False
                        index += 1
                    if event.key == pygame.K_b:
                        cube[f,r,c] = 4
                        drawcube(cube,0)
                        highlighted = False
                        index += 1
                    if event.key == pygame.K_y:
                        cube[f,r,c] = 5
                        drawcube(cube,0)
                        highlighted = False
                        index += 1
                    if event.key == pygame.K_BACKSPACE:
                        cube[f,r,c] = 6
                        index -= 1
                        highlighted = False
            

    
## START OF SOLVING ALGORITHM


edge_positions = [[0,1],[1,0],[1,2],[2,1]]
corner_positions = [[0,0],[0,2],[2,0],[2,2]]

#TRIGGER DEFINITIONS

def sexy(solstep):
    r(solstep);u(solstep);ri(solstep);ui(solstep)
def sledgehammer(solstep):
    ri(solstep);f(solstep);r(solstep);fi(solstep)

#corresponding_edge = {_3d_to_1d_indexing([0,0,1]):_3d_to_1d_indexing([4,0,1]),_3d_to_1d_indexing([0,1,0]):_3d_to_1d_indexing([1,0,1]),_3d_to_1d_indexing([0,1,2]):_3d_to_1d_indexing([3,0,1]),_3d_to_1d_indexing([0,2,1]):_3d_to_1d_indexing([2,0,1]),_3d_to_1d_indexing([1,1,2]):_3d_to_1d_indexing([2,1,0]),_3d_to_1d_indexing([2,1,2]):_3d_to_1d_indexing([3,1,0]),_3d_to_1d_indexing([3,1,2]):_3d_to_1d_indexing([4,1,0]),_3d_to_1d_indexing([4,1,2]):_3d_to_1d_indexing([1,1,0]),_3d_to_1d_indexing([5,0,1]):_3d_to_1d_indexing([2,2,1]),_3d_to_1d_indexing([5,1,0]):_3d_to_1d_indexing([1,2,1]),_3d_to_1d_indexing([5,1,2]):_3d_to_1d_indexing([3,2,1]),_3d_to_1d_indexing([5,2,1]):_3d_to_1d_indexing([4,2,1])}
corresponding_edge = {
 1: 37,
 3: 10,
 5: 28,
 7: 19,
 14: 21,
 23: 30,
 32: 39,
 41: 12,
 46: 25,
 48: 16,
 50: 34,
 52: 43,
 37: 1,
 10: 3,
 28: 5,
 19: 7,
 21: 14,
 30: 23,
 39: 32,
 12: 41,
 25: 46,
 16: 48,
 34: 50,
 43: 52}

def _3d_to_1d_indexing(_3d_index):
    return 9*_3d_index[0]+3*_3d_index[1]+_3d_index[2]
def _1d_to_3d_indexing(_1d_index):
    face = _1d_index//9
    row = (_1d_index-face*9)//3
    col = _1d_index-face*9-row*3
    return [face,row,col]
def name_edge_piece(_2_colors): # want to assign a single 
        #2d edge names {[0,4],[0,1],[0,2],[0,3]    , [1,4],[1,2],[2,3],[3,4]    ,    [2,5],[1,5],[4,5],[3,5]   }
        return 6*_2_colors[0]+_2_colors[1]

#FLOWER
def solve_flower(printout):
    global cube
    goal_position_flower = {1:[2,1],2:[1,2],3:[2,1],4:[1,2],5:[1,2]} # puts yellow into position to be sent to white side
    adjustment_move_flower = {1:l,2:f,3:r,4:b,5:d}
    goal_queue_flower = {1:[1,2],2:[1,2],3:[1,0],4:[1,0],5:[1,2]}
    keyhole_u_flower = {1:[1,0],2:[2,1],3:[1,2],4:[0,1],5:[1,1]} #5 doesn't matter, [1,1] will never be yellow
    insert_flower = {1:f,2:r,3:fi,4:ri,5:r2}
    while (cube[0,0,1] != 5) or (cube[0,1,0] != 5) or (cube[0,1,2] != 5) or (cube[0,2,1] != 5): # if any edges on white side are not yellow, execute
        for face in range(1,6):
            for edge in edge_positions:
                if cube[face,edge[0],edge[1]] == 5: # yellow targeted
                    ##print(f'yellow targeted: face {face} row {edge[0]} col {edge[1]}')
                    while cube[face,goal_queue_flower[face][0],goal_queue_flower[face][1]] != 5: #while its not in the queue
                        while cube[0,keyhole_u_flower[face][0],keyhole_u_flower[face][1]] == 5: #while keyhole not open
                            ##print('adjust u face to make keyhole open:')
                            u(True) #make keyhole open
                        # now keyhole is open, ready to adjust face to put yellow into queue
                        ##print('adjust face to put yellow in queue:')
                        adjustment_move_flower[face](True) # turn face until queued up properly
                        # now queued up\
                    while cube[0,goal_position_flower[face][0],goal_position_flower[face][1]] == 5: # adjust u to put non-yellow in goal pos
                        ##print('adjust u face to open goal position')
                        u(True)
                    ##print('insert yellow to white side')
                    insert_flower[face](True) 
    if printout:
        print(f'flower: {simplifymoves(solution)}')
        print(cube)    

#CROSS
def solve_cross(printout):
    global cube
    cross_adjust = {1:u,2:donothing,3:ui,4:u2}
    cross_insert = {1:l2,2:f2,3:r2,4:b2}
    while (cube[5,0,1] != 5) or (cube[5,1,0] != 5) or (cube[5,1,2] != 5) or (cube[5,2,1] != 5):
        while cube[0,2,1]!=5: #put yellow in front
            u(True)
        other_color = cube[2,0,1]
        cross_adjust[other_color](True)
        cross_insert[other_color](True)
    if printout:
        print(f'cross: {simplifymoves(solution)}')
        print(cube)

# FIRST LAYER CORNERS
def solve_flc(printout):
    global cube
    
    def first_layer_solved(check_cube):
        if np.sum(check_cube[5,:,:]) != 9*5:
            return False
        # side solved at least
        for face in range(1,5):
            for col in [0,2]:
                if check_cube[face,2,col] != check_cube[face,2,1]:
                    return False
                    print('not solved')
        return True
    
    
    #still prototyping below function
    def keyhole_prepared(check_cube): ## need to double check layer is correct not just face
        global keyhole
        solved_corners = 0
        for corner in corner_positions:
            if cube[5,corner[0],corner[1]] == 5:
                solved_corners += 1
            else:
                keyhole = corner
        if solved_corners >= 3:
            if solved_corners == 4:
                keyhole = [0,2]
            return True
        return False
        

    #BELOW IS TO FIX INABILITY TO ASSIGN A LIST OBJECT A KEY IN A DICTIONARY
    #def _3d_to_1d_indexing(_3d_index):
        #return 9*_3d_index[0]+3*_3d_index[1]+_3d_index[2]
    

    adjustment_algorithm_flc = {_3d_to_1d_indexing([0,0,0]):[u2],_3d_to_1d_indexing([0,0,2]):[u],_3d_to_1d_indexing([0,2,0]):[ui],_3d_to_1d_indexing([0,2,2]):[donothing],_3d_to_1d_indexing([1,0,0]):[u2],_3d_to_1d_indexing([1,0,2]):[ui],_3d_to_1d_indexing([1,2,0]):[l,u2,li],_3d_to_1d_indexing([1,2,2]):[li,ui,l],_3d_to_1d_indexing([2,0,0]):[ui],_3d_to_1d_indexing([2,0,2]):[donothing],_3d_to_1d_indexing([2,2,0]):[li,u,l,ui],_3d_to_1d_indexing([2,2,2]):[r,ui,ri],_3d_to_1d_indexing([3,0,0]):[donothing],_3d_to_1d_indexing([3,0,2]):[u],_3d_to_1d_indexing([3,2,0]):[r,u,ri,ui],_3d_to_1d_indexing([3,2,2]):[ri,ui,r,u2],_3d_to_1d_indexing([4,0,0]):[u],_3d_to_1d_indexing([4,0,2]):[u2],_3d_to_1d_indexing([4,2,0]):[ri,u,r,u],_3d_to_1d_indexing([4,2,2]):[l,ui,li,u2]}
    d_setup_move_flc = {name_edge_piece([1,2]):d,name_edge_piece([2,3]):donothing,name_edge_piece([3,4]):di,name_edge_piece([1,4]):d2}
    while not first_layer_solved(cube):
        if np.sum(cube[5,:,:]) == 9*5: # face solved but side not solved
            if cube[2,2,2] != cube[2,1,1]:
                r(True);ui(True);ri(True)
            elif cube[3,2,2] != cube[3,1,1]:
                ri(True);ui(True);r(True)
            elif cube[4,2,2] != cube[4,1,1]:
                l(True);u(True);li(True)
            elif cube[1,2,2] != cube[1,1,1]:
                li(True);ui(True);l(True)
        for face in [1,2,3,4,0]: # want to check 0 last because longest to solve when yellow on top (triple sexy)
            for corner in corner_positions:
                if cube[face,corner[0],corner[1]] == 5:# yellow corner targeted
                    for turn in adjustment_algorithm_flc[_3d_to_1d_indexing([face,corner[0],corner[1]])]:
                        turn(True)
                    # now it is queued
                    if cube[0,2,2] == 5: # yellow pointed up
                        d_setup_move_flc[name_edge_piece(sorted([cube[2,0,2],cube[3,0,0]]))](True)
                        r(True);u(True);ri(True);ui(True);r(True);u(True);ri(True);ui(True);r(True);u(True);ri(True);ui(True); # triple sexy
                        while cube[2,2,1] != cube[2,1,1]: #undo d setup move
                            d(True)
                    elif cube[2,0,2] == 5: # yellow pointed front
                        d_setup_move_flc[name_edge_piece(sorted([cube[0,2,2],cube[3,0,0]]))](True)
                        u(True);r(True);ui(True);ri(True);
                        while cube[2,2,1] != cube[2,1,1]: #undo d setup move
                            d(True)
                    elif cube[3,0,0]==5: #yellow pointed right
                        d_setup_move_flc[name_edge_piece(sorted([cube[0,2,2],cube[2,0,2]]))](True)
                        r(True);u(True);ri(True)
                        while cube[2,2,1] != cube[2,1,1]: #undo d setup move
                            d(True)
    if printout:
        print(f'first layer: {simplifymoves(solution)}')
        print(cube)

def solve_middle_layer(printout):
    global cube
    
    def middle_layer_solved(check_cube):
        for face in range(1,5):
            if (check_cube[face,1,0]!=check_cube[face,1,1]) or (check_cube[face,1,2]!=check_cube[face,1,1]):
                return False
        return True # maybe change this to use name_edge_piece syntax
    
    
    top_edges = [1,3,5,7] #edges in top layer
    
    def is_white_edge(single_edge_sticker):
        if cube.reshape(-1)[single_edge_sticker] == 0:
            return True
        if cube.reshape(-1)[corresponding_edge[single_edge_sticker]] == 0:
            return True
        return False
    
    while not middle_layer_solved(cube):
        white_edge_list = [is_white_edge(e) for e in top_edges]
        #IF ALL ARE TRUE (NONE ARE FALSE / ALL ARE WHITE) 
        if min(white_edge_list) == True:
            for middle_layer_edge in [12,21,30,39]:
                if cube.reshape(-1)[middle_layer_edge] != cube.reshape(-1)[middle_layer_edge+1]: #bad edge COMPARED TO CENTER PIECE
                    if middle_layer_edge == 12:
                        d2(True);l(True);u(True);li(True);d2(True)
                    if middle_layer_edge == 21:
                        di(True);li(True);ui(True);l(True);d(True)
                    if middle_layer_edge == 30:
                        r(True);ui(True);ri(True)
                    if middle_layer_edge == 39:
                        d(True);ri(True);ui(True);r(True);di(True)
        for edge in top_edges:
            if cube.reshape(-1)[edge] != 0 and cube.reshape(-1)[corresponding_edge[edge]]!=0: # 'edge' is middle layer edge
                topcolor = cube.reshape(-1)[edge] #either 1, 2, 3, or 4. where edge needs to go
                sidecolor = cube.reshape(-1)[corresponding_edge[edge]]
                edgecolors = sorted([topcolor,sidecolor])
                #goal_position = name_edge_piece(edgecolors) # gives 1 of 4 indicies for middle layer edges
                if edge == 5:
                    edge = 7
                elif edge == 7:
                    edge = 5
                d_setup_keyhole = {name_edge_piece([1,2]):di,name_edge_piece([2,3]):donothing,name_edge_piece([3,4]):d,name_edge_piece([1,4]):d2}
                d_setup_keyhole[name_edge_piece(edgecolors)](True)
                # now d layer setup
                x = (edge//2-topcolor)%4
                for i in range(x):
                    u(True)
                # now edge queued
                if topcolor == 1:
                    if sidecolor == 4:
                        bi(True);u(True);b(True)
                    else:
                        f(True);ui(True);fi(True)
                if topcolor == 2:
                    if sidecolor == 1:
                        li(True);u(True);l(True)
                    else:
                        r(True);ui(True);ri(True)
                if topcolor == 3:
                    if sidecolor == 2:
                        fi(True);u(True);f(True)
                    else:
                        b(True);ui(True);bi(True)
                if topcolor == 4:
                    if sidecolor == 3:
                        ri(True);u(True);r(True)
                    else:
                        l(True);ui(True);li(True)
                while cube[2,2,1] != cube[2,1,1]: #undo d setup move
                    d(True)
        
    if printout:
        print(simplifymoves(solution))
        print(cube)

def correct_keyhole(printout):
    global cube
    if np.sum(cube[5,:,:]) == 9*5:
        pass
    else:
        corners_to_check = [0,2,6,8,9,11,18,20,27,29,36,38,26,33]
        for corner in corners_to_check:
            if cube.reshape(-1)[corner] == 5:
                if corner == 0:
                    u(True);sexy(True);r(True);u(True);r2(True);f(True);r(True);fi(True)
                elif corner == 2:
                    sexy(True);r(True);u(True);r2(True);f(True);r(True);fi(True)
                elif corner == 6:
                    r(True);ui(True);ri(True);u(True);r(True);ui(True);r2(True);f(True);r(True);fi(True)
                elif corner == 8:
                    sexy(True);sexy(True);sexy(True)
                elif corner == 9:
                    ui(True);sexy(True);ui(True);r(True);u(True);ri(True)
                elif corner == 18:
                    sexy(True);ui(True);r(True);u(True);ri(True)
                elif corner == 27:
                    u(True);sexy(True);ui(True);r(True);u(True);ri(True)
                elif corner == 36:
                    u2(True);sexy(True);ui(True);r(True);u(True);ri(True)
                elif corner == 11:
                    u2(True);r(True);ui(True);ri(True);u2(True);r(True);ui(True);ri(True)
                elif corner == 20:
                    ui(True);r(True);ui(True);ri(True);u2(True);r(True);ui(True);ri(True)
                elif corner == 29:
                    r(True);ui(True);ri(True);u2(True);r(True);ui(True);ri(True)
                elif corner == 38:
                    u(True);r(True);ui(True);ri(True);u2(True);r(True);ui(True);ri(True)
                elif corner == 26:
                    sexy(True);r(True);u2(True);ri(True);ui(True);r(True);u(True);ri(True)
                elif corner == 33:
                    sexy(True);ui(True);r(True);ui(True);ri(True);u(True);r(True);u(True);ri(True)
                    
    if printout:
        print(simplifymoves(solution))
        print(cube)

def find_headlights(color_check_list):
    global cube
    results = {0:[],1:[],2:[],3:[],4:[]}
    for c in color_check_list:
        c_locations = []
        for i in range(1,5):
            if (cube[i,0,0] == cube[i,0,2]) and (cube[i,0,0] == c):
                c_locations.append(i) # assign side to specific color
        results[c] = c_locations
    return results

def orient_edges_ll(printout):
    global cube
    def get_cross_state():
        cross_state = np.zeros(4).astype(int)
        cross_state[0] = cube[0,0,1]==0
        cross_state[1] = cube[0,1,0]==0
        cross_state[2] = cube[0,2,1]==0
        cross_state[3] = cube[0,1,2]==0
        if np.sum(cross_state) == 0:
            return 'empty' # no solved
        if np.sum(cross_state) == 4:
            return 'solved' # cross solved
        locations = np.where(cross_state==0)[0]
        dif = locations[1]-locations[0]
        if (dif%2) == 1: #adjascent AKA L-shape
            return 'l' # L
        if (dif%2) == 0: #across AKA I-shape
            return 'bar'
    
    if get_cross_state() == 'solved':
        pass
    elif get_cross_state()=='empty':
        f(True);sexy(True);fi(True);u2(True);f(True);u(True);r(True);ui(True);ri(True);fi(True)
    elif get_cross_state() == 'bar':
        while cube[0,1,0] != 0:
            u(True)
        f(True);sexy(True);fi(True)
    elif get_cross_state() == 'l':
        while not (cube[0,0,1]==0 and cube[0,1,0]==0):
            u(True)
        f(True);u(True);r(True);ui(True);ri(True);fi(True)
    
    if printout:
        print(simplifymoves(solution))
        print(cube)

def orient_corners_ll(printout):
    
    
    def find_white_headlights(): #INPUT: none. OUTPUT: LIST of FACES where white headlights are
        global cube
        results = []
        for i in range(1,5):
            if (cube[i,0,0] == cube[i,0,2]) and (cube[i,0,0] == 0):
                results.append(i)
        return results
    
    corner_state = np.zeros(4).astype(int)
    corner_state[0] = cube[0,0,0]==0
    corner_state[1] = cube[0,0,2]==0
    corner_state[2] = cube[0,2,2]==0
    corner_state[3] = cube[0,2,0]==0
    if np.sum(corner_state) == 4:
        pass
    elif np.sum(corner_state) == 1:
        while cube[0,2,0] != 0:
            u(True)
        if cube[2,0,2] == 0: #SUNE
            r(True);u(True);ri(True);u(True);r(True);u2(True);ri(True)
        else: # ANTI SUNE
            u(True);ri(True);ui(True);r(True);ui(True);ri(True);u2(True);r(True)
    elif np.sum(corner_state) == 0:
        headlight_locations = find_white_headlights()
        print(headlight_locations)
        if len(headlight_locations) == 2:
            while cube[2,0,0] != 0:
                u(True)
            r(True); u2(True); ri(True); ui(True); r(True); u(True); ri(True); ui(True); r(True); ui(True); ri(True);
        else:
            while (cube[1,0,0] != cube[1,0,2]) or (cube[1,0,0] != 0):
                u(True)
            r(True);u2(True);r2(True);ui(True);r2(True);ui(True);r2(True);u2(True);r(True)
    else: # two whites up
        locations = np.where(corner_state==0)[0]
        dif = locations[1]-locations[0]
        if (dif%2) == 1: #adjascent corners
            if len(find_white_headlights()) == 0: #no headlights
                while cube[2,0,0] != 0:
                    u(True)
                l(True);f(True);ri(True);fi(True);li(True);f(True);r(True);fi(True)
            else:
                while (cube[4,0,0] != cube[4,0,2]) or (cube[4,0,0] != 0):
                    u(True)
                r2(True);di(True);r(True);u2(True);ri(True);d(True);r(True);u2(True);r(True)
        elif (dif%2) == 0: #bowtie
            while cube[2,0,0] != 0:
                u(True)
            ri(True);f(True);r(True);bi(True);ri(True);fi(True);r(True);b(True)
        
    if printout:
        print(simplifymoves(solution))
        print(cube)

def pll(printout):
    #CORNERS
    global cube
    def find_headlights():
        results = []
        for i in range(1,5):
            if cube[i,0,0] == cube[i,0,2]:
                results.append(i)
        return results
    headlight_locations = find_headlights()
    if len(headlight_locations) == 0:
        # y perm
        f(True); r(True); ui(True); ri(True); ui(True); r(True); u(True); ri(True); fi(True); sexy(True); sledgehammer(True)
    elif len(headlight_locations) == 1:
        # a perm
        while cube[4,0,0] != cube[4,0,2]:
            u(True)
        ri(True); f(True); ri(True); b2(True); r(True); fi(True); ri(True); b2(True); r2(True)
    # else (more than two headlights) do nothing bc corners already solved
    def find_solved_sides():
        results = []
        for i in range(1,5):
            if cube[i,0,1] == cube[i,0,0]:
                results.append(i)
        return results
    
    if len(find_solved_sides()) == 1:
        while cube[4,0,0] != cube[4,0,1]:
            u(True) #put bar in back
        if abs(cube[1,0,0]-cube[1,0,1]) == 2: #opposite on left
            r2(True); u(True); r(True); u(True); ri(True); ui(True); ri(True); ui(True); ri(True); u(True); ri(True) 
        else:
            r(True); ui(True); r(True); u(True); r(True); u(True); r(True); ui(True); ri(True); ui(True); r2(True)
    elif len(find_solved_sides()) == 0:
        if abs(cube[1,0,1]-cube[1,0,0])==2: # opposite = H Perm
            r2(True);l2(True);d(True);r2(True);l2(True);u2(True);r2(True);l2(True);d(True);r2(True);l2(True)
        else:
            while cube[1,0,2] != cube[2,0,1]:
                u(True) 
            ri(True);ui(True); r(True); ui(True); r(True); u(True); r(True); ui(True); ri(True); u(True); r(True); u(True); r2(True); ui(True); ri(True)
    
    #AUF
    while cube[1,0,0] != cube[1,1,1]:
        u(True)
                
    if printout:
        print(simplifymoves(solution))
        print(cube)


def solve_cube():
    solve_flower(False)
    solve_cross(False)
    solve_flc(False)
    solve_middle_layer(False)
    correct_keyhole(False)
    orient_edges_ll(False)
    orient_corners_ll(False)
    pll(False)
    
##END OF SOLVING ALGORITHM



running = True
while running:
    
    for event in pygame.event.get():
         if event.type == pygame.QUIT:
             running = False
         if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                init()
                scramble_cube(30, False)
                drawcube(cube,0)
            if event.key == pygame.K_i:
                user_input_scramble()
            if event.key == pygame.K_RETURN:
                solve_cube()
        
            


    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()