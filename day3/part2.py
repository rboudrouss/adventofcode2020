steps = [(1,1),(3,1),(5,1),(7,1),(1,2)]
main = lambda x : x

def main_debug(inp):
    rep = []
    inp = inp.split('\n')
    for R,D in steps:
        nb=x=y=0
        maxx = len(inp[0])
        while y<len(inp):
            if inp[y][x]=='#':
                nb+=1
            x=(R+x)%maxx
            y+=D
        rep.append(nb)
    rep_ = 1
    for i in rep:
        rep_ *= i
    return rep_


if __name__ == "__main__": # FIXME 2983070376
    print((lambda i,s,n,x,r:[r:=[n:=n+1 for y in range(1,len(i))if(x:=(R+x)%len(i[0]))+1 and i[y][x]=='#'][-1]*r for R,D in s][-1])(open("i").readlines(),[(1,1),(3,1),(5,1),(7,1),(1,2)],0,0,1))