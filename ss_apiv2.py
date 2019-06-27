def read_cinfo():
    with open('cinfo.txt') as cinfo:
        lines = cinfo.readlines()
        return lines[0], lines[1]

lines[0], lines[1] = read_cinfo()

print("Username: {}".format(lines[0]))
