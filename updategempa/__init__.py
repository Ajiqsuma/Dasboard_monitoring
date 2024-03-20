import requests
from bs4 import BeautifulSoup


def ekstrasi_data():
    """
    Tanggal   :01 Maret 2024,
    Waktu     :20:59:36 WIB
    magnitud0 : 3.2
    Kedalaman :5 km
    Lokasi    :2.88 LS - 119.48 BT
    Pusat     :Pusat gempa berada di darat 17 km TimurLaut Mamasa
    Dirasakan :Dirasakan (Skala MMI): III Mamasa
    :return:
    """

    url= "https://bmkg.go.id/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
    }

    try :
        content= requests.get(url, headers=headers)
    except Exception:
        return None

    if content.status_code == 200:
        soup = BeautifulSoup(content.text,'html.parser')
        result = soup.find('span', {'class':'waktu'})
        result = result.text.split(', ')
        tanggal = result[0]
        waktu = result[1]
        result = soup.find('div', {'class': 'col-md-6 col-xs-6 gempabumi-detail no-padding'})
        result = result.findChildren('li')

        i = 0
        magnitudo = None
        kedalaman = None
        ls = None
        bt = None
        lokasi =None
        dirasakan =None
        for res in result:
            # print(i, res)
            if i == 1:
                magnitudo = res.text
            elif i == 2:
                kedalaman = res.text
            elif i == 3:
                koordinat = res.text.split(' - ')
                ls = koordinat[0]
                bt = koordinat[1]
            elif i == 4:
                lokasi = res.text
            elif i == 5:
                dirasakan = res.text
            i = i + 1

        hasil= dict()
        hasil['tanggal']= tanggal   #'01 Maret 2024'
        hasil['waktu']= waktu #'20:59:36 WIB'
        hasil['magnitudo']= magnitudo #'3,2'
        hasil['kedalaman']= kedalaman #'5 km'
        hasil['koordinat']= {'ls':ls, 'bt':bt}
        hasil['lokasi'] = lokasi #Pusat gempa berada di darat 17 km TimurLaut Mamasa
        hasil['dirasakan']= dirasakan #'Dirasakan (Skala MMI): III Mamasa'
        return hasil
    else:
        return None

def tampil_data(result):
    if result is None:
        print('data gempa terkni tidak di temukan')
        return

    print('Tampilkan gempa terkini dari bmkg')
    print(f"Tanggal {result['tanggal']}")
    print(f"Waktu {result['waktu']}")
    print(f"Magnitudo {result['magnitudo']}")
    print(f"Kedalaman {result['kedalaman']}")
    print(f"Koordinat : {result['koordinat']['ls']}, {result['koordinat']['bt']}")
    print(f"Lokasi {result['lokasi']}")
    print(f"Getaran {result['dirasakan']}")

