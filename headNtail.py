def headNtail(aux):
    for i in range(len(aux)):
        if aux[i] != aux[0-i-1]:
            return False
    return True


print("Please enter the sequence of characters: ")
seq = input()
print(headNtail(seq))
