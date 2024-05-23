sequencia = [0,1,1,0,1,0,0,1,1,1,0,1,0,1,1]
#sub_seq = [0,1,1]
#sub_seq = [1,0,1]
#sub_seq = [0,1,0]
indices = []
for i in range(len(sequencia)):
    if sequencia[i] == sub_seq[0] and i <= len(sequencia) - 3: #-> indice é 0
        indices.append(i)
print(indices)
j=0
novo_indices = indices[:]
for i in novo_indices:
    if sequencia[i+1] != sub_seq[1]:
        indices.remove(i)

for i in indices:
    if sequencia[i+2] == sub_seq[2]:
        indices.remove(i)
print(len(indices))

#.pop remove o indice que passa e o .remove remove o conteudo do indice
# flag -> marcação, nome de variavel comum

sequencia = [0,1,1,0,1,0,0,1,1,1,0,1,0,1,1]
#sub_seq = [0,1,1]
sub_seq = [1,0,1]
#sub_seq = [0,1,0]

qtd = 0
for i in range (len(sequencia) - len(sub_seq) + 1):
    flag = False
    for j in range(len(sub_seq)):
        if sequencia[i+j] != sub_seq[j]:
            flag = True
            break
    if flag:
        continue
    qtd += 1
print(qtd)

