import os
from PIL import Image
from pillow_heif import register_heif_opener

# Mendaftarkan opener HEIF agar Pillow bisa mengenali .HEIC
register_heif_opener()

def convert_heic_to_jpg(source_folder):
    # Pastikan folder tujuan ada
    if not os.path.exists(source_folder):
        print(f"Folder {source_folder} tidak ditemukan.")
        return

    # Loop setiap file di folder
    for filename in os.listdir(source_folder):
        if filename.lower().endswith(".heic"):
            file_path = os.path.join(source_folder, filename)
            
            # Membuka gambar HEIC
            image = Image.open(file_path)
            
            # Membuat nama file baru dengan ekstensi .jpg
            target_path = os.path.join(source_folder, filename.replace(".HEIC", ".jpg").replace(".heic", ".jpg"))
            
            # Menyimpan sebagai JPG dengan kualitas 90%
            image.save(target_path, "JPEG", quality=90)
            print(f"Berhasil mengonversi: {filename} -> {os.path.basename(target_path)}")
            
            # Opsi: Hapus file HEIC asli agar tidak dobel (opsional)
            # os.remove(file_path)

if __name__ == "__main__":
    # Ganti 'DATASET' dengan nama folder Anda jika berbeda
    convert_heic_to_jpg('.')
    print("\nProses selesai!")