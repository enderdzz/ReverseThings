#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import deque
from copy import deepcopy
trans_map = {' ': 0, 'r': 1, 'g': 2, 'b': 3}
re_trans_map = [' ', 'r', 'g', 'b']


def initial(constrain):
    color_map = [[0 for i in range(7)] for j in range(7)]
    k = 0
    for i in range(7):
        for j in range(7):
            color_map[i][j] = constrain[k]
            k += 1
    # print(constrain)
    return color_map

def check_idx(idx_i, idx_j):
    if idx_i >= 0 and idx_j >= 0 and idx_i < 7 and idx_j < 7:
        return True
    else:
        return False

def check_path_idx(idx_i, idx_j):
    if idx_i >= 0 and idx_j >= 0 and idx_i < 8 and idx_j < 8:
        return True
    else:
        return False

def getNeighbors(color_map, idx_i, idx_j):
    count = {' ': 0, 'r': 0, 'g': 0, 'b': 0}
    if check_idx(idx_i - 1, idx_j):    
        count[color_map[idx_j][idx_i - 1]] += 1
    if check_idx(idx_i + 1, idx_j):   
        count[color_map[idx_j][idx_i + 1]] += 1
    if check_idx(idx_i, idx_j - 1):    
        count[color_map[idx_j - 1][idx_i]] += 1
    if check_idx(idx_i, idx_j + 1):    
        count[color_map[idx_j + 1][idx_i]] += 1
    if check_idx(idx_i - 1, idx_j - 1):    
        count[color_map[idx_j - 1][idx_i - 1]] += 1
    if check_idx(idx_i + 1, idx_j + 1):   
        count[color_map[idx_j + 1][idx_i + 1]] += 1
    if check_idx(idx_i + 1, idx_j - 1):    
        count[color_map[idx_j - 1][idx_i + 1]] += 1
    if check_idx(idx_i - 1, idx_j + 1):    
        count[color_map[idx_j + 1][idx_i - 1]] += 1
    return count['r'], count['g'], count['b']

def chooseEmpty(r, g, b):
    if (-(g == 0) & -(b == 0)) == 0:
        if b < g:
            return 2
        else:
            return 3
    else:
        return 0

def chooseRed(r, g, b):
    if (-(r != 2) & -(r != 3)) == 0:
        if (-(b == 0) | -(g == 0)) == 0:
            return 1
        else:
            return 0
    else:
        return 0


def chooseGreen(r, g, b):
    if r < 5:
        if b < 5:
            if (-(r == 2) | -(r == 3)) == 0:
                return 2
            else:
                return 1
        else:
            return 3
    else:
        return 0

def chooseBlue(r, g, b):
    if r < 5:
        if g < 5:
            if (-(r == 2) | -(r == 3)) == 0:
                return 3
            else:
                return 1
        else:
            return 2
    else:
        return 0


def step_auto(color_map):
    new_color_map = [[0 for i in range(7)] for j in range(7)]

    for j in range(7):
        for i in range(7):
            r, g, b = getNeighbors(color_map, i, j)
            if color_map[j][i] == ' ':
                ret = chooseEmpty(r, g, b)
            elif color_map[j][i] == 'r':
                ret = chooseRed(r, g, b)
            elif color_map[j][i] == 'g':
                ret = chooseGreen(r, g, b)
            elif color_map[j][i] == 'b':
                ret = chooseBlue(r, g, b)
            new_color_map[j][i] = re_trans_map[ret]

    return new_color_map            


def print_color_map(color_map):
    for l in color_map:
        s = ''
        for c in l:
            if c == 'r':
                s += '\033[41;37mr \033[0m'
            elif c == 'b':
                s += '\033[44;37mb \033[0m'
            elif c == 'g':
                s += '\033[42;37mg \033[0m'
            else:
                s += '  '
        print(s)
    print("")

def is_red(x, y, m):
    if (x<0 or y<0 or x>6 or y>6) == 0:
        return m[y][x] == 'r'
    else:
        return False

def red_check(ci, cj, ni, nj, m):
    xmin = min(ci, ni)
    ymin = min(cj, nj)
    if ci == ni:
        return is_red(ci,ymin,m) | is_red(ci-1,ymin,m) 
    elif cj == nj:
        return is_red(xmin,cj,m) | is_red(xmin,cj-1,m) 

def BFS(_map):
    vis = [[0 for i in range(8)] for j in range(8)]
    sx = 0
    sy = 0
    ex = 7
    ey = 7
    xi = deque([])
    yi = deque([])
    mi = deque([])
    vi = deque([])
    pi = deque([])
    head = 0 
    tail = 0
    # 1,0 -> 2,0 -> 1,1 -> 0,0
    direction = {(0,1): "R", (1,0): "D", (0,-1): "L", (-1,0): "U",}
    next_step = [[0, 1],  # 向右走
             [1, 0],  # 向下走
             [0, -1],  # 向左走
             [-1, 0]]  # 向上走
    xi.append(sx)
    yi.append(sy)
    mi.append(_map)
    pi.append([])
    tail += 1

    vis[sx][sy] = 1
    vi.append(vis)
    
    flag = 0
    while head < tail:

        cur_m = mi[head]
        vis = vi[head]
        path = pi[head]
        for i in range(4):
            next_x = xi[head] + next_step[i][1]
            next_y = yi[head] + next_step[i][0]
            if not check_path_idx(next_x, next_y): continue
            #print(next_x, next_y)
            if red_check(xi[head], yi[head], next_x, next_y, cur_m) and vis[next_y][next_x] == 0:
                
                xi.append(next_x)
                yi.append(next_y)
                mi.append(step_auto(cur_m))
                
                new_vis = deepcopy(vis)
                new_vis[next_y][next_x] = 1
                vi.append(new_vis)
                
                new_path = deepcopy(path)
                new_path.append(direction[(next_step[i][0], next_step[i][1])])

                if next_x == ex and next_y == ey:
                    print(new_path)
                    return True

                pi.append(new_path)
                tail += 1

        head += 1
    return False
    #return True if flag == 1 else False
def main():
    
    constrain1 = "rbrr rgb rb  r brgrbrgb  grrgbbg grg bgrg  bbgrbg"
    constrain2 = "rbr  bbggrgrggb   bggbb b  b bbrbbgg gbrrbgrbbb g"
    constrain3 = "rrbrb rg g  bgrbgggr ggrgr gr rg brr  b  bggrbgbb"
    prob = [constrain1, constrain2, constrain3]
    
    color_map = initial(constrain1)
    print_color_map(color_map)
    # print(chooseEmpty(0,0,0))
    # print(getNeighbors(color_map, 1, 0))
    
    # for i in range(30):
    #     new_color_map = step_auto(color_map)
    #     print_color_map(new_color_map)
    #     color_map = new_color_map
    for i in prob:
        _m = initial(i)
        print(BFS(_m))

if __name__ == "__main__":
    main()


