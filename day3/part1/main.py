D = 1
R = 3

main = lambda x : x

def main_debug(inp):
    nb=x=y=0
    inp = inp.split('\n')
    maxx = len(inp[0])
    while y<len(inp):
        print(inp[y][x])
        if inp[y][x]=='#':
            nb+=1
        x=(R+x)%maxx
        y+=D
    return nb
    

if __name__ == "__main__":
    with open('input.txt','r') as f:
        inp = f.read()
    print(main_debug(inp))