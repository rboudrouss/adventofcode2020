# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID)

def main_debug(inp):
    inp = inp.split('\n\n')
    rep = 0
    for i in inp:
        if all(map(lambda x : x in i,['byr','iyr','eyr','hgt','hcl','ecl','pid'])):
            rep += 1
    return rep

if __name__ == "__main__":
    with open('input.txt','r') as f:
        inp = f.read()
    print(main_debug(inp))