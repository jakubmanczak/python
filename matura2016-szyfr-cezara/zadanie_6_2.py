datafile = open("dane_6_2.txt")
writefile = open("wyniki_6_2.txt", "w")

data = datafile.readlines()
for index, line in enumerate(data):
    if index == 700:
        break

    splits = line.strip().split()
    word = splits[0]
    key = int(splits[1])
    for letter in word:
        num = ord(letter) - key
        while num < ord('A'):
            num += ord('Z') - ord('A') + 1
        writefile.write(chr(num))
    writefile.write('\n')
