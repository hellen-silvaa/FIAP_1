
'''numero=10
texto='o valor é: %d' % numero
print(texto)
print ('Agora são %02d:%02d.' % (16, 30))
print ('Percentagem: %.1f%%, Exponencial:%.2e' % (5.333, 0.00314))
print ('Decimal: %d, Octal: %o, Hexadecimal: %x' % (10, 10, 10))

#---------------------------------------------------------------------------------------------

nome = 'Thon'
sobre = 'de Souza'
print("{} {}".format(nome, sobre))
nome = 'Thon'
sobre = 'de Souza'
print("{:>20} {}".format(nome, sobre))

s = "Olá, mundo!"
# Tamanho de uma string.
number = len(s)
print(number)

#---------------------------------------------------------------------------------------------

s = "Olá, mundo!"
# Substitui uma substring por alguma outra coisa.
s1 = s.replace("mundo", "inferno")
print(s1)

#---------------------------------------------------------------------------------------------

s = "Olá, mundo abacate abacate!"
# A string s começa com "Olá"?
print(s.startswith("Olá"))
# A string s termina com "mundo!"?
print(s.endswith("mundo!"))
# Quantas ocorrências da palavra "abacate" a string s1 possui?
print(s.count("abacate"))


#---------------------------------------------------------------------------------------------

# Como "capitalizar" (transformar a primeira letra da primeira
#palavra em maiúscula).
s = "ordem e progresso"
print(s.capitalize())
print(s)

# Como verificar se uma string só possui números.
print('12345'.isdigit())
print('12345abc'.isdigit())

# Como verificar se uma string é alfanumérica (só possui letras e
#números).
print('12345abc'.isalnum())


#---------------------------------------------------------------------------------------------

#String.find: procura uma substring em uma string e retorna o
#índice:
s = "Pedro, Paulo e Maria"
print(s.find("a"))

#Além disso, ela recebe um argumento adicional que especifica o
#índice pelo qual ela deve começar sua procura:
print(s.find("a", 10))

#Ord: Retorna o valor decimal de um caractere
print(ord('a'))

#chr: retorna o caractere de um valor decimal.
print(chr(97))

nome= 'Alexia'
print(nome[-2])
'''
#---------------------------------------------------------------------------------------------

'''s='Isso é um texto'
print(s.title())
print(s.lower())
print(s.upper())

Isso É Um Texto
isso é um texto
ISSO É UM TEXTO

#---------------------------------------------------------------------------------------------

texto='isso é '
texto2=' um texto'
print(texto+texto2)
texto=texto.rstrip()
texto2=texto2.lstrip()
print(texto+texto2)


#TABELA https://unicode.org/emoji/charts/full-emoji-list.html
print('\U0001F600')
print('\U0001F911')
print('\U0001F60F')
print('\U0001F40D')
'''

s = "Olá, alunos bobocas!"
print(s[0:3])
print(s[5:10])
print(s[12:20])

print(s[0:len(s):2])
print(s[-1::-1])

