import csv
import json
#shift-jis
#with open('sample_person_sjis.csv', 'r', encoding='shift_jis') as csvfile:
def readcsv(fileName):
    try:

        with open(fileName, 'r') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            for row in csv_reader:
                # print(row)
                print(','.join(row))
    except FileNotFoundError as e:
        print(e)
    except csv.Error as e:
        print(e)

#def jsonSet():

#csv_file = csv.DictReader('test.csv', dialect=csv.excel)
def csvToDic():
    jList = []
    jData = {}

    with open('test.csv') as csvfile:
        csv_reader  = csv.DictReader(csvfile)
        for line in csv_reader:
            jList.append(line)
        jData['music'] = jList
        #for row in csv_reader:
            #print(row)
    return jData
#print(type(csvToDic()),csvToDic())


with open('musin.json', 'w', encoding='utf-8') as f:
    # JSONへの書き込み
    json.dump(csvToDic(), f, ensure_ascii=False)
#json.dumps(list(csvToDic()))
