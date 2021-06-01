import time
def getLastSismo():
    import requests
    from bs4 import BeautifulSoup

    urlSlackError = "https://hooks.slack.com/services/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"
    url = 'http://www.sismologia.cl/links/tabla.html'
    response = requests.get(url)
    y = []

    for row in BeautifulSoup(response.text, 'lxml').findChildren('table')[0].findChildren(['th', 'tr']):
        x = []
        for cell in row.findChildren('td'):
            x.append(cell.string)
        y.append(x)

    data = [x for x in y if x != []]

    if float(data[0][2][0:3]) >= 4.5:
        mensajeSlackError = 'Sismo!\nFecha: %s \nSe registro un sismo a %s con una magnitud de %s' % (data[0][0] , data[0][1] , data[0][2])
        payloadSlackError="{\"text\": \"" + mensajeSlackError + "\"}"
        headersSlackError = {
            'Content-Type': 'application/json'
        }
        r = requests.request("POST", urlSlackError, headers=headersSlackError, data=payloadSlackError)
        print(r.status_code, r.reason)

while True:
    getLastSismo()
    time.sleep(1)