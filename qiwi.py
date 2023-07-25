# http://www.cbr.ru/scripts/XML_daily.asp?date_req=02/03/2002 котировки на заданный день где date_req=ДАТА
# Для работы с таблицами данных использовал пандас :)
import pandas as pd

def getResult(day, month, year, charcode):
        # Если пользователь вводит число меньше 10, то преобразует его в подходящий для поиска формат
    if int(day) < 10:
        day = '0%s' % day
        # Если пользователь вводит число меньше 10, то преобразует его в подходящий для поиска формат
    if int(month) < 10:
        month = '0%s' % month
    #тут можно было бы написать еще и
    get_xml = 'http://www.cbr.ru/scripts/XML_daily.asp?date_req=%s/%s/%s' % (day, month, year) #url таблицы с курсами
    get_xml_name = 'https://www.cbr.ru/scripts/XML_valFull.asp' #url таблицы с названиями
    xml = pd.read_xml(get_xml, encoding='cp1251') #готовая таблица с курсами
    xml_name = pd.read_xml(get_xml_name, encoding='cp1251')#готовая таблица с названиями
    new_xml = xml[xml['CharCode'] == charcode] #Отдельная строка из которой мы берем value
    new_xml_name = xml_name[xml_name['ID'] == new_xml.iloc[0]['ID']] #Отсюда берем русское название валюты
    return (f"{new_xml.iloc[0]['CharCode']} ({new_xml_name.iloc[0]['Name']}) {new_xml.iloc[0]['Value']}")
        #я не стал округлять значение валюты, но вроде это и не нужно
        #{new_xml.iloc[0]['CharCode']}можно было бы не писать, а просто взять значение из charcode
    '''Программа может некоректно работать, если у ЦБ будут каким-то чудом разные значения либо код не будет описан
       у них в таблице с названиями XML_valFull.asp вот в этой'''

#Я не совсем понял пункт с интерфейсом, у меня дата и код как две переменные, которые вводятся пользователем по очереди
print("Программа принимает дату в формате день-месяц-год и код валюты по ISO 4217"
      "\nПример даты: 10-10-2022"
      "\nПривер кода валюты: USD"
      "\n")

date = input("Введите интересующую вас дату: ").split('-') # Создаем список из дня месяца и года
a = [int(x) for x in date] #преобразуем данные из str в int, ибо программа работает с int только :)
charcode = input('Введите код валюты в формате ISO 4217: ') #Получаем код валюты
print(getResult(*a, charcode)) #Вызываем метод c распакоукой в него нашей даты и кода