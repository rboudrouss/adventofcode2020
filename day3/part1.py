if __name__ == "__main__":
    (lambda i,n,x:[n:=n+1 for y in range(1,len(i))if(x:=(3+x)%len(i[0]))+1 and i[y][x]=='#'][-1])(open("./day3/input.txt",'r').read().split('\n'),0,0)

# 
def main_debug(inp,D=1,R=3):
    nb=x=y=0
    inp = inp.split('\n')
    maxx = len(inp[0])
    for y in range(0,len(inp),D):
        if inp[y][x]=='#':
            nb+=1
            yield nb,x,y
        x=(R+x)%maxx
    
