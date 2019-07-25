import csv

def nome():
    csv.register_dialect('myDialect',
    delimiter = ';',
    skipinitialspace=True)

    with open('documento_emails.csv', 'rU') as csvFile:
        reader = csv.reader(csvFile, dialect='myDialect')
        for row in reader:
            yield row[0]

    csvFile.close()


    
def email():
    csv.register_dialect('myDialect',
    delimiter = ';',
    skipinitialspace=True)

    with open('documento_emails.csv', 'rU') as csvFile:
        reader = csv.reader(csvFile, dialect='myDialect')
        for row in reader:
            yield row[1]

    csvFile.close()