lista = []
for i in range(6):
    print("podaj liczbe")
    a = input()
    a = int(a)
    lista.append(a)

print(lista)

for i in range(6):
    if lista[i] == 3:
        print("3 znajduje sie na " + str(i+1) + " miejscu w liscie")
    else:
        print("nie ma 3 na " + str(i+1) + " miejscu w liscie")
