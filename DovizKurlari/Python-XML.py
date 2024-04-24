from requests import get
from bs4 import BeautifulSoup
from time import sleep
import xml.etree.ElementTree as ET
import datetime

def clean_price(price_str):
    return price_str.replace(".", "").replace(",", ".")

def update_xml(data_list):
    try:
        tree = ET.parse('exchange_rates.xml')
        root = tree.getroot()
        for data in data_list:
            currency_elem = root.find(f"./currency[@name='{data['Currency']}']")
            if currency_elem is not None:
                for key, value in data.items():
                    if key == 'Currency':
                        continue  # Currency zaten Currency tag'inde
                    elem = currency_elem.find(key)
                    if elem is not None:
                        elem.text = str(value)
                    else:
                        new_elem = ET.SubElement(currency_elem, key)
                        new_elem.text = str(value)
                # Güncelleme tarihini ve saati ekleyelim
                now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                updated_at_elem = currency_elem.find('UpdatedAt')
                if updated_at_elem is not None:
                    updated_at_elem.text = now
                else:
                    updated_at = ET.SubElement(currency_elem, 'UpdatedAt')
                    updated_at.text = now
        tree.write('exchange_rates.xml')
        print("Veriler güncellendi.")
    except Exception as e:
        print("XML güncellenirken bir hata oluştu:", e)

yenileme = 10  # Kaç saniyede bir yenilemesini söyler
tekrar = 5  # Kaç saniyede bir tekrar denemesini söyler

while True:
    try:
        #kaynak
        site = get("https://www.bloomberght.com/piyasalar")
        icerik = BeautifulSoup(site.content, "html.parser")
        liste0 = icerik.find_all("small", {"class": "value LastPrice"})
        liste1 = icerik.find_all("span", {"class": "value"})
        liste2 = icerik.find_all("small", {"data-type": "yuzde_degisim"})

        #bist
        bistlast = clean_price((liste0[0].text))
        bistprevclose = clean_price((liste1[0].text))
        bistmin = clean_price((liste1[1].text))
        bistmax = clean_price((liste1[2].text))
        bistpercentage = clean_price((liste2[0].text))
        #dolar
        dolarlast = clean_price((liste0[1].text))
        dolarbuy = clean_price((liste1[3].text))
        dolarsell = clean_price((liste1[4].text))
        dolarprevclose = clean_price((liste1[5].text))
        dolarmin = clean_price((liste1[6].text))
        dolarmax = clean_price((liste1[7].text))
        dolarpercentage = clean_price((liste2[1].text))
        # euro
        eurolast = clean_price((liste0[2].text))
        eurobuy = clean_price((liste1[8].text))
        eurosell = clean_price((liste1[9].text))
        europrevclose = clean_price((liste1[10].text))
        euromin = clean_price((liste1[11].text))
        euromax = clean_price((liste1[12].text))
        europercentage = clean_price((liste2[2].text))
        # eurusd
        eurusdlast = clean_price((liste0[3].text))
        eurodolarbuy = clean_price((liste1[13].text))
        eurodolarsell = clean_price((liste1[14].text))
        eurusdprevclose = clean_price((liste1[15].text))
        eurusdmin = clean_price((liste1[16].text))
        eurusdmax = clean_price((liste1[17].text))
        eurusdpercentage = clean_price((liste2[3].text))


        # Güncellenen verileri bir liste olarak oluşturalım
        data_list = [
            {
                'Currency': 'Bist100',
                'Last': bistlast,
                'DisplayName': 'Bist100',
                'Description': 'Borsa İstanbul ilk 100',
                'Exchange': 'SPOT',
                'PrevClose': bistprevclose,
                'DailyPercentage': bistpercentage,
                'Low': bistmin,
                'Max': bistmax,
            },
            {
                'Currency': 'Dolar',
                'Last': dolarlast,
                'Buy': dolarbuy,
                'Sell': dolarsell,
                'DisplayName': 'Dolar',
                'Description': 'Dolar TL',
                'Exchange': 'SPOT',
                'PrevClose': dolarprevclose,
                'DailyPercentage': dolarpercentage,
                'Low': dolarmin,
                'Max': dolarmax,

            },
            {
                'Currency': 'Euro',
                'Last': eurolast,
                'Buy': eurobuy,
                'Sell': eurosell,
                'DisplayName': 'Euro',
                'Description': 'Euro TL',
                'Exchange': 'SPOT',
                'PrevClose': europrevclose,
                'DailyPercentage': europercentage,
                'Low': euromin,
                'Max': euromax,
            },
            {
                'Currency': 'EurUsd',
                'Last': eurusdlast,
                'Buy': eurodolarbuy,
                'Sell': eurodolarsell,
                'DisplayName': 'EurUsd',
                'Description': 'Euro Dolar',
                'Exchange': 'SPOT',
                'PrevClose': eurusdprevclose,
                'DailyPercentage': eurusdpercentage,
                'Low': eurusdmin,
                'Max': eurusdmax,
            },

        ]
        update_xml(data_list)
    except Exception as e:



        print("Döviz verileri alınırken hata oluştu:", e)

    sleep(yenileme)
