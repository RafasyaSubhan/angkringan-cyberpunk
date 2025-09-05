# 🚀 Setup Project Django + GitHub

Langkah-langkah awal setup project ini:

1. Buat repo di Github  
2. Buat folder  
3. Setelah masuk ke dalam folder, ketik `git init` di terminal untuk initialized  
4. Buat `README.md` untuk mencatat progress  
5. Tambahkan `.gitignore` agar file tertentu tidak terpush ke github  
6. Menambahkan remote ke repo Github dengan `git remote add origin link`  
7. Ubah nama branch menjadi `main` dengan `git branch -M main`  
8. Tambahkan semua file ke stage commit  
9. Commit  
10. Lalu push dengan `git push -u origin main`, yaitu agar Github tau bahwa code ini akan dipush ke remote origin dan nama branch main  
11. Buat virtual environment untuk menyiapkan dependencies dan membuat proyek django  
12. Lalu install dependencies yang dibutuhkan  
13. Buat Proyek django  
14. Buat `.env` dan `.env.prod` untuk konfigurasi environment variables dan proyek  
15. Modifikasi `settings.py` supaya dapat menggunakan environment variables  
16. Tambahkan `localhost` di allowed host agar dapat develop di jaringan lokal  
17. Tambahkan konfigurasi production  
18. Ubah konfigurasi databases  
19. Migrate  