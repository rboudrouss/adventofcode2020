# one line method <!>(not the fastest way)<!>
if __name__ == "__main__":
    print((lambda x : len([1 for i in [[*map(int,i.split(': ')[0].split(' ')[0].split('-')),i.split(': ')[0].split(' ')[-1],i.split(': ')[-1]] for i in x] if ((i[3][i[1]-1] == i[2]) and (i[3][i[0]-1] != i[2])) or ((i[3][i[0]-1] == i[2]) and (i[3][i[1]-1] != i[2]))]))(open('i').readlines()))