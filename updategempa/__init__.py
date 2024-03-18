import requests
# from bs4 import BeautifulSoup
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
        title= soup.find('title')
        print(title.string)

        hasil= dict()
        hasil['tanggal']= '01 Maret 2024'
        hasil['waktu']= '20:59:36 WIB'
        hasil['magnitudo']= '3,2'
        hasil['kedalaman']= '5 km'
        hasil['lokasi']= {'ls':2.88,'bt':119.48}
        hasil['pusat'] ='Pusat gempa berada di darat 17 km TimurLaut Mamasa'
        hasil['dirasakan']='Dirasakan (Skala MMI): III Mamasa'
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
    print(f"Lokasi : {result['lokasi']['ls']} LS, {result['lokasi']['bt']} BT")
    print(f"Pusat {result['pusat']}")
    print(f"Dirasakan {result['dirasakan']}")

