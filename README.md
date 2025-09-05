# 🍢 Angkringan Cyberpunk

## 🛠️ Setup Git dan GitHub
1. Buat repo di GitHub dan folder project lokal  
2. Inisialisasi Git:
   ```bash
   git init
   git remote add origin <link>
   git branch -M main
   git add .
   git commit -m "Initial commit"
   git push -u origin main
3. Tambahkan '.gitignore' dan 'README.md'

## 🐍 Setup Virtual Environment dan Django
1. Buat virtual environment dan aktifkan
    ```bash
    python -m venv env
    .\\env\\Scripts\\activate
2. Install dependencies dengan `pip install -r requirements.txt`
3. Buat project Django dan file `/env` dan `.env.prod`
4. Sesuaikan `settings.py` (ALLOWED_HOSTS, database)
5 Jalankan migrasi dengan `python manage.py migrate`

## Setup Aplikasi `main`
1. Buat aplikasi 
    ```bash
    python manage.py startapp main
2. Tambahkan main ke dalam INSTALLED_APPS di settings.py
3. Buat folder `template` di direktori main
4. Buat file `main.html` di direktori template
5. Tambahkan model di models.py dan jalankan migrasi

## 🌐 URL Routing
1. Buat `urls.py` di app `main`
2. Import `include` di `angkringan_cyberpunk/urls.py` dan tambahkan
    ```bash
    path('', include('main.urls'))
