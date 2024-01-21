

def turnright():
    turnleft()
    turnleft()
    turnleft()

def jump():
    move()
    turnleft()
    move()
    turnright()
    move()
    turnright()
    move()
    turnleft()

for step in range(6):
    jump()   
    