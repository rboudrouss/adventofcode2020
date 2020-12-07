
def main(inp):
    for i in inp:
        for j in inp:
            for k in inp:
                if j+i+k==2020:
                    return i,j,k,i*j*k

if __name__ == "__main__":
    with open('input.txt','r') as f:
        inp = list(map(int,f.read().split('\n')))
    print(main(inp))