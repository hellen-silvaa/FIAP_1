'''from matplotlib import pyplot as plt
import numpy as np

#criando arranjo de 0 a 10 que vai de 0.2 em 0.2 (igual o range)
x = np.arange(0,10,0.2)
y = np.sin(x)
#tem que instalar o numpy e o matplotlib
#plot -> cria grafico com as codernadas x e y
plt.plot(x,y)

# show -> ele mostra o grafico
plt.show()
#print(x)
#print(y)'''

#---------------------------------------------------------------------

'''x = np.arange(0,10,0.2)
y = np.sin(x)
fig, ax = plt.subplots()

ax.plot(x,y)

ax.set_title("Título")
ax.set_xlabel("x")
ax.set_ylabel("y")

plt.show()'''

#---------------------------------------------------------------------

'''x = np.arange(0, 14, 0.2)
y = np.sin(x)
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title('Título')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_xlim([0, 15])
ax.xaxis.set_ticks_position('top')
ax.yaxis.set_ticks_position('right')
plt.show()'''

#----------------------------------------------------------------

'''from matplotlib import pyplot as plt
import numpy as np
# cria uma amostragem entre 0 e 2 e ele oega 100 numeros entra 0 e 2
x = np.linspace(0, 2, 100)

#print x x
plt.plot(x, x, label='linear')
plt.plot(x, x**2, label='quadrático')
plt.plot(x, x**3, label='cúbico')
plt.xlabel('x label')
plt.ylabel('y label')
plt.title("Gráfico simples")

#legend é a legenda ele pega o "label" e assume
#da para colocar varias curvas em um grafico como uma matriz x y
plt.legend()
plt.show()'''
#----------------------------------------------------------------

#O mesmo gráfico usando a interface orientada a objetos:
'''from matplotlib import pyplot as plt
import numpy as np
x = np.linspace(0, 2, 100)
fig, ax = plt.subplots()
ax.plot(x, x, label='linear')
ax.plot(x, x**2, label='quadrático')
ax.plot(x, x**3, label='cúbico')
ax.set_xlabel('x label')
ax.set_ylabel('y label')
ax.set_title("Gráfico simples")
ax.legend()
plt.show()'''

#----------------------------------------------------------------
'''from matplotlib import pyplot as plt
import numpy as np

plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
plt.axis([0, 6, 0, 20])
plt.show()
'''
#----------------------------------------------
'''from matplotlib import pyplot as plt
import numpy as np
t = np.arange(0., 5., 0.2)
# red dashes, blue squares and green triangles
plt.plot(
t, t, 'r--',
t, t**2, 'bs',
t, t**3, 'g^'
)
plt.show()'''
#----------------------------------------------

'''import matplotlib.pyplot as plt
# Dados de exemplo
x = [0, 1, 2, 3, 4]
y = [10, 20, 25, 30, 35]
# Gráfico com várias formatações de linha e marcador
plt.plot(x, y, color='blue', marker='x', linestyle=':', linewidth=4,
markersize=10, markerfacecolor='yellow', markeredgecolor='pink',
markeredgewidth=2)
plt.title("Exemplo de Formatação de Linha e Marcadores")
plt.show()'''

#----------------------------------------------

'''Scatter'''
'''import matplotlib.pyplot as plt
import numpy as np
# Dados de exemplo para os gráficos
x = np.random.randn(1000)
y = np.random.randn(1000)
plt.scatter(x, y, alpha=0.5, color='b')
plt.title('Scatter Plot')
plt.show()'''

'''Histograma'''
'''import matplotlib.pyplot as plt
import numpy as np
# Dados de exemplo para os gráficos
x = np.random.randn(1000)
y = np.random.randn(1000)
plt.hist(x, bins=50, color='g', alpha=0.7)
plt.title('Histograma')
plt.show()'''

'''BARRAS'''

'''import matplotlib.pyplot as plt
import numpy as np
categories = ['A', 'B', 'C', 'D']
values = [15, 25, 35, 45]
plt.bar(categories, values, color=['r', 'g', 'b', 'y'])
plt.title('Gráfico de Barras')
plt.show()'''

'''Pizza'''
'''import matplotlib.pyplot as plt
categories = ['A', 'B', 'C', 'D']
values = [15, 25, 35, 45]
plt.pie(values, labels=categories, autopct='%1.1f%%',
colors=['r', 'g', 'b', 'y'], startangle=140)
plt.title('Gráfico de Pizza')
plt.show()'''
'''
Estilos'''
'''import numpy as np
import matplotlib.pyplot as plt
# creating an array of data for plot
data = np.random.randn(50)
# using the style for the plot
plt.style.use('Solarize_Light2')
# creating a plot
plt.plot(data)
# show plot
plt.show()'''
'''
import numpy as np
import matplotlib.pyplot as plt
# creating an array of data for plot
data = np.random.randn(50)
# using the style for the plot
plt.style.use('dark_background')

# creating a plot
plt.plot(data)
# show plot
plt.show()
'''
#SABER OS ESTILOS
'''print(plt.style.available)'''

#---------------------------------------
#0 é branco
#1 é vermelho porque to usando um vermelho claro e escuro
import matplotlib.pyplot as plt
import numpy as np
# Criar uma matriz de exemplo que represente um coração em pixel art
heart_pixel_art = np.array([
[0, 0, 1, 1, 0, 0, 1, 1, 0, 0],
[0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
[0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
[0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
[0, 0, 0, 0, 1, 1, 0, 0, 0, 0]
])
# Definir as cores: 0 será branco e 1 será vermelho
cmap = plt.get_cmap('Reds')
# Visualizar o coração em pixel art
plt.imshow(heart_pixel_art, cmap=cmap, interpolation='none')
# Remover os eixos
plt.axis('off')
# Título
plt.title('Coração em Pixel Art')
# Mostrar o gráfico
plt.show()
