import os
from PIL import Image

def check_and_remove_invalid_images(directory):
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)
        try:
            # Membuka gambar untuk memastikan file dapat dibaca
            with Image.open(file_path) as img:
                img.verify()  # Memverifikasi bahwa file tersebut adalah gambar yang valid
                if img.format not in ['JPEG', 'PNG', 'GIF', 'BMP']:  # Format yang didukung
                    print(f"Format tidak didukung, menghapus file: {file_path}")
                    os.remove(file_path)  # Menghapus jika format tidak didukung
        except (IOError, SyntaxError) as e:
            # Menghapus file jika file rusak atau tidak dapat dibaca
            print(f"Gambar tidak valid atau rusak, menghapus file: {file_path}")
            os.remove(file_path)

# Ganti path di bawah dengan lokasi folder Jahe Anda
check_and_remove_invalid_images(r"E:\BANGKIT\Project Capstone\ML-side\data\Lengkuas")

