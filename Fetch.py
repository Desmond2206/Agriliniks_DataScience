from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://agmarknet.gov.in/SearchCmmMkt.aspx?Tx_Commodity=24&Tx_State=UP&Tx_District=1&Tx_Market=0&DateFrom=01-Jan-2011&DateTo=31-Mar-2022&Fr_Date=01-Jan-2011&To_Date=31-Mar-2022&Tx_Trend=0&Tx_CommodityHead=Potato&Tx_StateHead=Uttar+Pradesh&Tx_DistrictHead=Agra&Tx_MarketHead=--Select--'

row_data = []

months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
days = [31,28,31,30,31,30,31,31,30,31,30,31]
market_id=[2551,314,2550,2555,2553,2554,2552,2556]
market=['Achnera','Agra','Fatehabad','Fatehpur+Sikri','Jagnair','Jarar','Khairagarh','Samsabad']

for i in range(2011,2023):
    if i%4==0:
        days[1]=29
    else:
        days[1]=28
    for j in range(12):
        for k in range(8):
            url= 'https://agmarknet.gov.in/SearchCmmMkt.aspx?Tx_Commodity=24&Tx_State=UP&Tx_District=1&Tx_Market=' +str(market_id[k])+ '&DateFrom=01-' +months[j]+ '-' +str(i)+ '&DateTo=' +str(days[j])+ '-' +months[j]+ '-' +str(i)+ '&Fr_Date=01-' +months[j]+ '-' +str(i)+ '&To_Date=' +str(days[j])+ '-' +months[j]+ '-' +str(i)+ '&Tx_Trend=0&Tx_CommodityHead=Potato&Tx_StateHead=Uttar+Pradesh&Tx_DistrictHead=Agra&Tx_MarketHead=' + market[k]
            html_text=requests.get(url).text
            soup = BeautifulSoup(html_text, 'lxml')

            table = soup.find('table', class_="tableagmark_new")

            for row in table.find_all('tr')[1:]:
                data = row.find_all('td')
                col = [td.text.strip() for td in data]
                if col[0]!='No Data Found':
                    row_data.append(col)
        if i==2022 and j==2:
            break


    


headers = []
for i in table.find_all('th'):
    title = i.text
    headers.append(title)

df = pd.DataFrame(row_data, columns = headers)

df.to_csv('Data.csv')