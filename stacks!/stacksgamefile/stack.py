import msvcrt
import os
import time

map = []
block_loc = []
x = 15
width = 5
i = 10
i_clear = 10
clocks = 0.2
current = -1
old = -2
real_width = 5
xp = 0
map_end = 10
LEFT_RIGHT_FLAG = 0

def initialize_map():
    for ym in range(10):
        row = []
        for xm in range(20):
            row.append("-")
        map.append(row)

def generate_map():
    for y in range(10):
        for xa in range(20):
            print(f"{map[y][xa]}", end="")
        print("")

def update_block():              
    for y_map in range(i):
        for p in range(real_width):
          if(y_map == i - 1): 
            map[y_map][x + p] = "#"
            
def clear_old_blocks():
    for y in range(i_clear):
        for xs in range(20):
            if(map[y][xs] == '#'):
                map[y][xs] = "-"
            


def place():
    global x, width, i, i_clear, clocks,old,current,real_width,xp, map_end
    if msvcrt.kbhit():
        last_input = msvcrt.getch().decode()
        print(f"pressed: {last_input}")
        if(last_input == " "):
          block_loc.append([x,real_width])
          i_clear -= 1
          current += 1
          old += 1
          i -= 1
          x=15
          map_end -= 1
          if(clocks <= 0):
           clocks = 0.2
          else:
           clocks -= 0.005
          if(old >= 0):
            if(block_loc[current][0] != block_loc[old][0]):
                real_width-=1
                xp+=1
                x = 15 + xp
            elif(block_loc[current][0] == block_loc[old][0]):
                real_width += 0
                x = 15 + xp
            
        
 
initialize_map()
print("TUTORIAL:\nPRESS SPACE TO STACK/PLACE THE BLOCK!")
time.sleep(1)
while True:
 oldx = x
 time.sleep(clocks)
 os.system("cls")
 clear_old_blocks()
 update_block()
 generate_map()
 print(x,real_width)
 print(f"old = {old} current = {current}")
 print(f"real width: {real_width}")
 if(old >= 0):
  print(f"old = {block_loc[old][0]} current = {x}")
 print(f"oldx => {oldx}")
 print(block_loc)
 if(x <= 0 or real_width <= 0):
  os.system("cls")
  print("YOU LOSE! dont get to the left edge!... or dont lose your blocks!....")
  break
 if(map_end <= 0):
     os.system("cls")
     print("YOU WIN! CONGRATULATIONS!!!")
     time.sleep(2)
     break
 x-=1
 place()