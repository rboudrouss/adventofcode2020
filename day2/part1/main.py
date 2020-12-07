main = lambda x : len(
    [
        1 for i in [
            [
                *map(int,i.split(': ')[0].split(' ')[0].split('-')),
                i.split(': ')[0].split(' ')[-1],
                i.split(': ')[-1]
            ] for i in x.split('\n')
        ] if i[0]<=i[3].count(i[2])<=i[1]
    ]
)

if __name__ == "__main__":
    with open('input.txt','r') as f:
        inp = f.read()
    print(main(inp))