import utils
import read_csv
import charts

def run():
  #data = read_csv.read_csv('./app/data.csv')
  data = read_csv.read_csv('./data/movies.csv')
  data = list(filter(lambda item : item['Year'] == '2009',data)) #2nd col

  countries = list(map(lambda x: x['Film'], data))                          #last col
  percentages = list(map(lambda x: x['Profitability'], data))
  charts.generate_pie_chart(countries, percentages)


if __name__ == '__main__':
  run()