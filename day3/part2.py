steps = [(1,1),(3,1),(5,1),(7,1),(1,2)]

main = lambda x : x

def main_debug(inp):
    rep = []
    inp = inp.split('\n')
    for R,D in steps:
        nb=x=y=0
        maxx = len(inp[0])
        while y<len(inp):
            print(inp[y][x])
            if inp[y][x]=='#':
                nb+=1
            x=(R+x)%maxx
            y+=D
        rep.append(nb)
    rep_ = 1
    for i in rep:
        rep_ *= i
    return rep_


if __name__ == "__main__":
    with open('input.txt','r') as f:
        inp = f.read()
    print(main_debug(inp))