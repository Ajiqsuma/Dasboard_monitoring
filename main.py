"""
Aplikasi gempa terkini
modularisasi dengan function
modularisasi dengan packge
"""


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
    hasil= dict()
    hasil['tanggal']= '01 Maret 2024'
    hasil['waktu']= '20:59:36 WIB'
    hasil['magnitudo']= '3,2'
    hasil['kedalaman']= '5 km'
    hasil['lokasi']= {'ls':2.88,'bt':119.48}
    hasil['pusat'] ='Pusat gempa berada di darat 17 km TimurLaut Mamasa'
    hasil['dirasakan']='Dirasakan (Skala MMI): III Mamasa'

    return hasil


def tampil_data(result):
    print('Tampilkan gempa terkini dari bmkg')
    print(f"Tanggal {result['tanggal']}")
    print(f"Waktu {result['waktu']}")
    print(f"Magnitudo {result['magnitudo']}")
    print(f"Kedalaman {result['kedalaman']}")
    print(f"Lokasi : {result['lokasi']['ls']} LS, {result['lokasi']['bt']} BT")
    print(f"Pusat {result['pusat']}")
    print(f"Dirasakan {result['dirasakan']}")

if __name__=='__main__':
    print('Aplikasi Utama')
    result=ekstrasi_data()
    tampil_data(result)

