import matplotlib.pyplot as plt

#grafica tipo barras
def generate_bar_chart(name, labels, values):
  #metodo subplots para cargar las graficas
  fig, ax = plt.subplots()
  #llamamos los valores de entrada
  ax.bar(labels,values)
  plt.savefig(f'./imgs/{name}bar.png')
  plt.close()

#grafica tipo torta
def generate_pie_charts(name,labels, values):
  #metodo subplots para cargar las graficas
  fig, ax = plt.subplots()
  #llamamos los valores de entrada
  ax.pie(values, labels=labels)
  ax.axis('equal')
  plt.savefig(f'./imgs/{name}pie.png')
  plt.close()

#mostrar grafica
if __name__ == '__main__':
  #valores de entrada del grafico
  labels =['a','b','c']
  values = [50,100,80]
  #generate_bar_chart(labels,values)
  generate_pie_charts(labels,values)
  
