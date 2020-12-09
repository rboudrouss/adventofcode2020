if __name__ == "__main__":
    print((lambda x,r : [r:=r+1 for i in x.split('\n\n') if all(map(lambda x : x in i,['byr','iyr','eyr','hgt','hcl','ecl','pid']))][-1])(open("i").read(),0))

def main_debug(inp): # 204
    inp = inp.split('\n\n')
    rep = 0
    for i in inp:
        if all(map(lambda x : x in i,['byr','iyr','eyr','hgt','hcl','ecl','pid'])):
            rep += 1
    return rep
