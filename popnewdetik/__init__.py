"""
Mengekstraksi data populer dari detik.com

"""
import requests
from bs4 import BeautifulSoup


def ekstrak_data():
    """
      Berita Terpopuler
      #1   Prediksi Ranking FIFA Indonesia Usai Kalahkan Vietnam Sepakbola | 1 jam yang lalu
      #2   Shin Tae-yong Sebut Indonesia Sedikit Beruntung Sepakbola | 1 jam yang lalu
      #3   Jadwal Imsak Hari Ini 27 Maret di Bogor, Depok, Bekasi, Tangerang detikNews | 1 jam yang lalu
      #4   Jadwal Imsak Hari Ini di Jakarta dan Sekitarnya, Rabu 27 Maret 2024 detikNews | 1 jam yang lalu
      #5   Ganjar Gugat Suara Prabowo Nol, Muzani: Yang ke TPS Nggak Dihargai? detikNews | 2 jam yang lalu
      :return:
    """
    url = 'https://detik.com'
    content = requests.get(url)
    if content.status_code == 200:
        soup = BeautifulSoup(content.text, 'html.parser')
        result = soup.find('div', {'class': 'box cb-mostpop'})
        judul= result.find('h2')
        print(judul.text)

        result = soup.find('div', {'class': 'box cb-mostpop'})
        # tag= result.find_all('div',{'class':'list-content'})
        tag= result.text

        print(tag)

        view = dict()
        view['satu'] = 'Prediksi Ranking FIFA Indonesia Usai Kalahkan Vietnam, Sepakbola | 1 jam yang lalu'
        view['dua'] = 'Shin Tae-yong Sebut Indonesia Sedikit Beruntung,  Sepakbola | 1 jam yang lalu'
        view['tiga'] = 'Jadwal Imsak Hari Ini 27 Maret di Bogor, Depok, Bekasi, Tangerang, detikNews | 1 jam yang lalu'
        view[
            'empat'] = 'Jadwal Imsak Hari Ini di Jakarta dan Sekitarnya, Rabu 27 Maret 2024,  detikNews | 1 jam yang lalu'
        view[
            'lima'] = 'Ganjar Gugat Suara Prabowo Nol, Muzani: Yang ke TPS Nggak Dihargai? ,   detikNews | 2 jam yang lalu'

        return view
    else:
        return None


def tampilkan_data(result):
    print('\nBerita terpopuler dari detik.com, Indonesia')
    print(f"#1 {result['satu']}")
    print(f"#2 {result['dua']}")
    print(f"#3 {result['tiga']}")
    print(f"#4 {result['empat']}")
    print(f"#5 {result['lima']}")

# if __name__='__main__':
#     print('hai')
