# one line method <!>(not the fastest way)<!>
if __name__ == "__main__":
    print((lambda x : [i*j*k for i in x for j in x for k in x if j+i+k == 2020][0])(list(map(int,open('i').readlines()))))

# this solution is better though :
def main_faster(inp):
    inp = list(map(int,inp.split('\n')))
    for i in inp:
        for j in inp:
            for k in inp:
                if j+i+k==2020:
                    return i,j,k,i*j*k