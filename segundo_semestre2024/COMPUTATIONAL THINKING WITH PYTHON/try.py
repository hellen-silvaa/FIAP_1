'''try:
    print(1/0)
except ZeroDivisionError:
    print('Divisao por zero')


#tratamento de exce��o
def divide(num1, num2):
    return num1/num2

try:
    resultado = divide(10,0)
except ZeroDivisionError as e:
    print(f"Erro: {e}")
else:
    print(f"Resultado da divis�o: {resultado}")
finally:
    print('Encerrando o programa...')


try:
    print(1 / 0)
except Exception as e:
    print(e)


class DivisaoPorZeroError(Exception):
    def __init__ (self, mensagem = "Divis�o por zero n�o permitida"):
        self.mensagem = mensagem
        super(). init (self.mensagem



with open('exemplo.txt', 'w') as arquivo:
    arquivo.write('Ol� este � um exemplo de escrita e leitura em arquivo.\n')
    arquivo.write('Python � poderoso e vers�til.\n')
    arquivo.write('Fechamendo o arquivo automaticamente com o bloco "with"\n')


with MeuContexto() as contexto:
    print("Executando código dentro do bloco 'with'")
    raise ValueError("Erro proposital")
print("Código fora do bloco 'with'")
'''


with open('exemplo.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

with open('exemplo.txt', 'a') as arquivo:
    arquivo.write('esta linha será adicionada ao conteúdo existente.\n')
    arquivo.write('Adicionando outra linha\n')

import logging

logging.basicConfig(filename='log.log', level=logging.DEBUG, format='%(asctime)s -%(levelname)s - %(message)s')

logging.debug("Isso é uma mensagem de depuração")
logging.info("Isso é uma mensagem de info")
logging.warning("Isso é uma mensagem de warning")
logging.error("Isso é uma mensagem de error")
logging.critical("Isso é uma mensagem de critical")
