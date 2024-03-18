"""
Aplikasi gempa terkini
modularisasi dengan function
modularisasi dengan packge
"""
# from updategempa import ekstrasi_data, tampil_data
import updategempa
if __name__=='__main__':
    print('Aplikasi Utama')
    result=updategempa.ekstrasi_data()
    updategempa.tampil_data(result)


