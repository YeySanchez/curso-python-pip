import csv

def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    #leer el nombre de las columnas
    header = next(reader)
    data = []
     #crear un zip para que se unan los encabezados con los registros
    for row in reader:
      iterable = zip(header,row)
      #crera diccionario comprhension
      country_dict={ key: value for key, value in iterable}
      data.append(country_dict)
    return data

if __name__ == '__main__':
  data = read_csv('./app/data.csv')
  print(data[0])
