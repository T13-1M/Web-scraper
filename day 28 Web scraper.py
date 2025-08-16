import requests
from bs4 import BeautifulSoup


def ambil_judul_website():
    print("--- Pengambil Judul Artikel Website ---")
    url = input("Masukkan URL lengkap dari artikel website: ")

    try:
        print(f"\nMengunjungi {url}...")
        respons = requests.get(url)
        respons.raise_for_status()
        sup = BeautifulSoup(respons.text, 'html.parser')
        judul_tag = sup.find('h1')

        if judul_tag:
            judul = judul_tag.get_text(strip=True)
            print(f"\nJudul Artikel: {judul} ✨")
        else:
            print("\nWaduh, tidak bisa menemukan tag judul (<h1>) di halaman ini.")
            title_tag = sup.find('title')
            if title_tag:
                print(f"Judul dari tag <title>: {title_tag.get_text(strip=True)}")

    except requests.exceptions.RequestException as e:
        print(f"\nGagal mengunjungi website. Error: {e}")
    except Exception as e:
        print(f"\nTerjadi error: {e}")

if __name__ == "__main__":
    ambil_judul_website()