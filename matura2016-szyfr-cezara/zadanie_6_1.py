datafile = open("dane_6_1.txt")
writefile = open("wyniki_6_1.txt", "w")

data = datafile.readlines()
key = 107
for line in data:
    line = line.strip()
    for letter in line:
        letternum = ord(letter) + key
        while letternum > ord('Z'):
            letternum -= ord('Z') - ord('A') + 1
        writefile.write(chr(letternum))
    writefile.write('\n')

