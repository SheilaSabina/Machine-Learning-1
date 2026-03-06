import cv2
import os
import numpy as np

# 1. Konfigurasi Jalur Folder
folder_asal = r'D:\FILE SELA\SEMESTER 6\ML 1\PREPROSESING\Machine-Learning-1\dataset_mentah'
folder_tujuan = r'D:\FILE SELA\SEMESTER 6\ML 1\PREPROSESING\Machine-Learning-1\dataset fix'

if not os.path.exists(folder_tujuan):
    os.makedirs(folder_tujuan)

# 2. Proses Preprocessing
print("Sedang memproses gambar...")
for nama_file in os.listdir(folder_asal):
    if nama_file.endswith(('.jpg', '.jpeg', '.png')):
        path_file = os.path.join(folder_asal, nama_file)
        img = cv2.imread(path_file)

        if img is not None:
            # Resize 224x224
            img_resized = cv2.resize(img, (224, 224), interpolation=cv2.INTER_LINEAR)
            
            # Simpan hasil
            path_simpan = os.path.join(folder_tujuan, nama_file)
            cv2.imwrite(path_simpan, img_resized)

print(f"Proses selesai di: {folder_tujuan}")

# --- BAGIAN 2: KODE VERIFIKASI ---
print("\n=== MEMULAI AUDIT DATA ===")

# Tentukan sub-folder mana yang ingin diaudit (misal: folder Clean)
sub_folder_audit = os.path.join(folder_tujuan, 'Clean')

# Pastikan folder tersebut ada dan tidak kosong
if os.path.exists(sub_folder_audit) and len(os.listdir(sub_folder_audit)) > 0:
    # Mengambil file pertama di dalam folder Clean
    nama_file_asli = os.listdir(sub_folder_audit)[0]
    path_sampel = os.path.join(sub_folder_audit, nama_file_asli)
    
    img_cek = cv2.imread(path_sampel)

    if img_cek is not None:
        # Simulasi normalisasi (0-1)
        img_norm = img_cek.astype('float32') / 255.0

        # CETAK BUKTI
        print(f"Audit Berhasil pada file: {nama_file_asli}") 
        print(f"Ukuran Piksel: {img_cek.shape[1]} x {img_cek.shape[0]}")
        print(f"Nilai Maksimum: {np.max(img_norm):.4f}")
    else:
        print(f"Gagal membaca file: {nama_file_asli}")
else:
    print("Folder audit tidak ditemukan atau kosong. Pastikan foto sudah ada di dalam sub-folder.")

print("===========================")
