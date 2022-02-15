def add_block(x, r, c):
    rows, cols = x.shape
    x[r%rows,c%cols] = 1
    x[(r+1)%rows,c%cols] = 1
    x[(r+1)%rows,(c+1)%cols] = 1
    x[(r)%rows,(c+1)%cols] = 1
    return x

def add_beehive(x, r, c):
    rows, cols = x.shape
    x[r%rows,c%cols] = 1
    x[(r+1)%rows,(c-1)%cols] = 1
    x[(r+2)%rows,(c-1)%cols] = 1
    x[(r+1)%rows,(c+1)%cols] = 1
    x[(r+2)%rows,(c+1)%cols] = 1
    x[(r+3)%rows,c%cols] = 1
    return x
    
def add_pond(x, r, c):
    rows, cols = x.shape
    x[r%rows,c%cols] = 1
    x[(r+1)%rows,(c-1)%cols] = 1
    x[(r+2)%rows,(c-1)%cols] = 1
    x[(r)%rows,(c+1)%cols] = 1
    x[(r+1)%rows,(c+2)%cols] = 1
    x[(r+2)%rows,(c+2)%cols] = 1
    x[(r+3)%rows,c%cols] = 1
    x[(r+3)%rows,(c+1)%cols] = 1
    return x    
    
def add_blinker(x, r, c):
    rows, cols = x.shape
    x[r%rows,c%cols] = 1
    x[(r+1)%rows,c%cols] = 1
    x[(r-1)%rows,c%cols] = 1
    return x

def add_glider(x, r, c):
    rows, cols = x.shape
    x[r%rows,c%cols] = 1
    x[(r+1)%rows,(c+1)%cols] = 1
    x[(r+2)%rows,(c-1)%cols] = 1
    x[(r+2)%rows,c%cols] = 1
    x[(r+2)%rows,(c+1)%cols] = 1
    return x

def add_eater(x, r, c):
    rows, cols = x.shape
    x[r%rows,c%cols] = 1
    x[r%rows,(c+1)%cols] = 1
    x[(r+1)%rows,c%cols] = 1
    x[(r+2)%rows,(c+1)%cols] = 1
    x[(r+2)%rows,(c+2)%cols] = 1
    x[(r+2)%rows,(c+3)%cols] = 1
    x[(r+3)%rows,(c+3)%cols] = 1
    return x

def add_glider_gun(x, r, c):
    rows, cols = x.shape
    x = add_block(x, r, c)
    x = add_block(x, r-2,c+34)
    c = (c+10)%cols
    r = (r+1)%rows
    x[r%rows, c%cols] = 1
    x[(r-1)%rows, c%cols] = 1
    x[(r+1)%rows, c%cols] = 1
    x[(r-2)%rows, (c+1)%cols] = 1
    x[(r+2)%rows, (c+1)%cols] = 1
    x[(r-3)%rows, (c+2)%cols] = 1
    x[(r-3)%rows, (c+3)%cols] = 1
    x[(r+3)%rows, (c+2)%cols] = 1
    x[(r+3)%rows, (c+3)%cols] = 1
    c = (c+4)%cols
    x[r%rows, c%cols] = 1
    x[(r-2)%rows, (c+1)%cols] = 1
    x[(r+2)%rows, (c+1)%cols] = 1
    c = (c+2)%cols
    x[r%rows, c%cols] = 1
    x[(r-1)%rows, c%cols] = 1
    x[(r+1)%rows, c%cols] = 1
    c = (c+1)%cols
    x[r%rows, c%cols] = 1
    r = (r-2)%rows
    c = (c+3)%cols
    x[r%rows, c%cols] = 1
    x[(r-1)%rows, c%cols] = 1
    x[(r+1)%rows, c%cols] = 1
    c = (c+1)%cols
    x[r%rows, c%cols] = 1
    x[(r-1)%rows, c%cols] = 1
    x[(r+1)%rows, c%cols] = 1
    x[(r-2)%rows, (c+1)%cols] = 1
    x[(r+2)%rows, (c+1)%cols] = 1
    
    x[(r-2)%rows, (c+3)%cols] = 1
    x[(r-3)%rows, (c+3)%cols] = 1
    
    x[(r+2)%rows, (c+3)%cols] = 1
    x[(r+3)%rows, (c+3)%cols] = 1
    
    return x
