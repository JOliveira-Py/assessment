def capicua(aux):
    for i in range(len(aux)):
        if aux[i] != aux[0-i-1]:
            return False
    return True


print("Introduza a sequência de caractéres: ")
seq = input()
print(capicua(seq))
