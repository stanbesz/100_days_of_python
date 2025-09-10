enemies = 1

if 4>2:
    enemies = 16 # if, for and else are in the same scope as the code execution level, they are not a different level

def increase_enemies():
    #enemies += 2 referenced before assignment without global
    global enemies # one way to directly reference global variable, however error prone, it is also "not clean" e.g. it modifies
    enemies += 2
    print(f"Enemies inside function: {enemies}")

def increase_enemies_2():
    print(f"Enemies inside function: {enemies}")
    return enemies + 2

enemies = increase_enemies_2()
print(f"Enemies outside function: {enemies}")