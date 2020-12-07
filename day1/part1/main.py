# one line method <!>(not the fastest way)<!>
main = lambda x : [
    i*j
    for i in list(map(int,x.split('\n')))
        for j in list(map(int,x.split('\n')))
            if j+i == 2020
][0]

if __name__ == "__main__":
    with open('input.txt','r') as f:
        inp = f.read()
    print(main(inp))

# this solution is better though :
def main_faster(inp):
    inp = list(map(int,inp.split('\n')))
    for i in inp:
        for j in inp:
            if j+i==2020:
                return i*j