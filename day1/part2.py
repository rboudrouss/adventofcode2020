# one line method <!>(not the fastest way)<!>
main = lambda x : [
    i*j*k
    for i in list(map(int,x.split('\n')))
        for j in list(map(int,x.split('\n')))
            for k in list(map(int,x.split('\n')))
                if j+i+k == 2020
][0]

if __name__ == "__main__":
    with open('input.txt','r') as f:
        inp = list(map(int,f.read().split('\n')))
    print(main(inp))

# this solution is better though :
def main_faster(inp):
    inp = list(map(int,inp.split('\n')))
    for i in inp:
        for j in inp:
            for k in inp:
                if j+i+k==2020:
                    return i,j,k,i*j*k