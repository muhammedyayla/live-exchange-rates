import requests
import xml.etree.ElementTree as ET
import datetime
import time

def update_xml(data_list):
    try:
        tree = ET.parse('today.xml')
        root = tree.getroot()
        for data in data_list:
            currency_elem = root.find(f"./Currency[@Kod='{data['Kod']}']")
            if currency_elem is not None:
                for key, value in data.items():
                    if key == 'Kod':
                        continue  # Kod zaten Currency tag'inde
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
        tree.write('today.xml')
        print("Veriler güncellendi.")
    except Exception as e:
        print("XML güncellenirken bir hata oluştu:", e)

yenileme = 10  # Kaç saniyede bir yenilemesini söyler
tekrar = 5  # Kaç saniyede bir tekrar denemesini söyler

while True:
    try:
        # Veriyi URL'den çek
        response = requests.get('http://www.tcmb.gov.tr/kurlar/today.xml')
        if response.status_code == 200:
            xml_data = response.content
            root = ET.fromstring(xml_data)
            data_list = []
            for currency_elem in root.findall('Currency'):
                data = {'Kod': currency_elem.get('Kod')}
                for child in currency_elem:
                    data[child.tag] = child.text
                data_list.append(data)
            update_xml(data_list)
        else:
            print("Veri alınamadı. Tekrar deneniyor...")
            time.sleep(tekrar)
            continue

    except Exception as e:
        print("Döviz verileri alınırken hata oluştu:", e)

    time.sleep(yenileme)
