from sys import argv
from time import sleep as sl

clr = "\033[0;0m\033[H\033[2J\033[3J"

def ddp(x, y):
    return f"\033[{y+1};{x+1}H"

def dseg(seg, sym, x, y):
    result = ""

    if seg == 1:
      result += f"{ddp(x, y)}  {sym*12}   {ddp(x, y+1)} {sym*14}  {ddp(x, y+2)}{sym*14}  {ddp(x, y+3)}{sym*3}"
    
    elif seg == 2:
      y += 5
      result += f"{ddp(x, y)}{sym*2}{ddp(x, y+1)}{sym*3}{ddp(x, y+2)}{sym*3}{ddp(x, y+3)}{sym*3}{ddp(x, y+4)}{sym*3}{ddp(x, y+5)}{sym*3}{ddp(x, y+6)}{sym}"
      y -= 5
    
    elif seg == 3:
      y += 15
      result += f"{ddp(x, y)}{sym}{ddp(x, y+1)}{sym*3}{ddp(x, y+2)}{sym*3}{ddp(x, y+3)}{sym*3}{ddp(x, y+4)}{sym*3}{ddp(x, y+5)}{sym*3}{ddp(x, y+6)}{sym*2}"
      y -= 15

    elif seg == 4:
      y += 23
      result += f"{ddp(x, y)}{sym*3}{ddp(x, y+1)}{sym*14}{ddp(x, y+2)} {sym*14}{ddp(x, y+3)}  {sym*12}"
      y -= 23

    elif seg == 5:
      x += 14
      y += 15
      result += f"{ddp(x, y)}  {sym}{ddp(x, y+1)}{sym*3}{ddp(x, y+2)}{sym*3}{ddp(x, y+3)}{sym*3}{ddp(x, y+4)}{sym*3}{ddp(x, y+5)}{sym*3}{ddp(x, y+6)}{sym*3}{ddp(x, y+7)}{sym*3}{ddp(x, y+8)} {sym*2}{ddp(x, y+9)}  {sym*1}"
      x -= 14
      y -= 15

    elif seg == 6:
      x += 14
      y += 2
      result += f"{ddp(x, y)}  {sym}{ddp(x, y+1)} {sym*2}{ddp(x, y+2)}{sym*3}{ddp(x, y+3)}{sym*3}{ddp(x, y+4)}{sym*3}{ddp(x, y+5)}{sym*3}{ddp(x, y+6)}{sym*3}{ddp(x, y+7)}{sym*3}{ddp(x, y+8)}{sym*3}{ddp(x, y+9)}  {sym*1}"
      x -= 14
      y -= 2
    
    elif seg == 7:
      y += 12
      result += f"{ddp(x, y)}  {sym*13}{ddp(x, y+1)} {sym*15}{ddp(x, y+2)}  {sym*13}"
      y -= 12
    
    elif seg == 8:
      x += 20
      y += 24
      result += f"{ddp(x, y)}{sym*5}{ddp(x, y+1)}{sym*5}{ddp(x, y+2)}{sym*5}"
      x -= 20
      y -= 24
    
    elif seg == 9:
      x += 20
      y += 6
      result += f"{ddp(x, y)}{sym*5}{ddp(x, y+1)}{sym*5}{ddp(x, y+2)}{sym*5}"
      y += 12
      result += f"{ddp(x, y)}{sym*5}{ddp(x, y+1)}{sym*5}{ddp(x, y+2)}{sym*5}"
      x -= 20
      y -= 18
    
    elif seg == 10:
      x += 20
      result += f"{ddp(x, y)}{sym*5}{ddp(x, y+1)}{sym*5}{ddp(x, y+2)} {sym*4}{ddp(x, y+3)} {sym*4}"
      x -= 20
    
    return result + ddp(x, y+26)

def dnum(num, sym, x, y):
    if num == 0:
      return dseg(1, sym, x, y)+dseg(2, sym, x, y)+dseg(3, sym, x, y)+dseg(4, sym, x, y)+dseg(5, sym, x, y)+dseg(6, sym, x, y)
    
    elif num == 1:
      return dseg(5, sym, x, y)+dseg(6, sym, x, y)
    
    elif num == 2:
      return dseg(1, sym, x, y)+dseg(3, sym, x, y)+dseg(4, sym, x, y)+dseg(6, sym, x, y)+dseg(7, sym, x, y)

    elif num == 3:
      return dseg(1, sym, x, y)+dseg(4, sym, x, y)+dseg(5, sym, x, y)+dseg(6, sym, x, y)+dseg(7, sym, x, y)
    
    elif num == 4:
      return dseg(2, sym, x, y)+dseg(5, sym, x, y)+dseg(6, sym, x, y)+dseg(7, sym, x, y)
    
    elif num == 5:
      return dseg(1, sym, x, y)+dseg(2, sym, x, y)+dseg(4, sym, x, y)+dseg(5, sym, x, y)+dseg(7, sym, x, y)

    elif num == 6:
      return dseg(1, sym, x, y)+dseg(2, sym, x, y)+dseg(3, sym, x, y)+dseg(4, sym, x, y)+dseg(5, sym, x, y)+dseg(7, sym, x, y)
    
    elif num == 7:
      return dseg(1, sym, x, y)+dseg(5, sym, x, y)+dseg(6, sym, x, y)

    elif num == 8:
      return dseg(1, sym, x, y)+dseg(2, sym, x, y)+dseg(3, sym, x, y)+dseg(4, sym, x, y)+dseg(5, sym, x, y)+dseg(6, sym, x, y)+dseg(7, sym, x, y)
    
    elif num == 9:
      return dseg(1, sym, x, y)+dseg(2, sym, x, y)+dseg(4, sym, x, y)+dseg(5, sym, x, y)+dseg(6, sym, x, y)+dseg(7, sym, x, y)

def main():
  while True:
    print(clr, end="")
    for n in range(0, 10):
      x, y = 16, 5
      print(dnum(n, "#", x, y))
      x += 28
      print(dnum(n, "#", x, y))
      print(dseg(9, "*", x, y))
      x += 28
      print(dnum(n, "#", x, y))
      x += 28
      print(dnum(n, "#", x, y))
      sl(1)
      print(clr, end="")

if __name__ == "__main__":
    main()
