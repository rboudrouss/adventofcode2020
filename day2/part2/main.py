main = lambda x : len(
    [
        1 for i in [
            [
                *map(int,i.split(': ')[0].split(' ')[0].split('-')),
                i.split(': ')[0].split(' ')[-1],
                i.split(': ')[-1]
            ] for i in x.split('\n')
        ] if (
            (
                i[3][i[1]-1] == i[2]
            ) and (
                i[3][i[0]-1] != i[2]
            )
        ) or (
            (
                i[3][i[0]-1] == i[2]
            ) and (
                i[3][i[1]-1] != i[2]
            )
        )
    ]
)

if __name__ == "__main__":
    with open('input.txt','r') as f:
        inp = f.read()
    print(main(inp))