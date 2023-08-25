import utils
import read
import charts
# funcion leer csv
def run ():
  #importar funcion leer csv
  data = read.read_csv('data.csv')
  #leer por escritorio la entrada del pais
  country = input('Escribe el Nombre del pais =>')
  #llamar funcion creada en utils 
  result = utils.population_by_country(data,country)
  #condicon para validar si la ciudad existe
  if len(result) > 0:
    #traer el pais encontrado
    country = result[0]
    print(country)
    labels, values = utils.get_population(country)
    charts.generate_pie_charts(country['Country/Territory'],labels, values)
    charts.generate_bar_chart(country['Country/Territory'],labels, values)
    
if __name__ == '__main__':
  run()