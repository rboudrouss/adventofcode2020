# one line method <!>(not the fastest way)<!>
if __name__ == "__main__":
    print((lambda i:[a*b for a in i for b in i if a+b==2020][0])(list(map(int,open('i').readlines()))))

# this solution is better though :
def main_faster(inp):
    inp = list(map(int,inp.split('\n')))
    for i in inp:
        for j in inp:
            if j+i==2020:
                return i*j