# Arjawinangun Racing — proyek APK Android

Isi: game web 3D (www/index.html) dibungkus Capacitor menjadi aplikasi Android (landscape, layar penuh, offline).

## Cara 1 — Tanpa instal apa pun (GitHub, gratis)
1. Buat akun di github.com, lalu buat repositori baru (private boleh).
2. Upload SELURUH isi folder ini (termasuk folder .github) ke repositori.
3. Buka tab Actions, pilih "Build APK", klik Run workflow (atau otomatis berjalan setelah upload).
4. Setelah centang hijau (sekitar 5-8 menit), buka run tersebut dan unduh artifact "ArjawinangunRacing-apk".
5. Ekstrak zip-nya, kirim app-debug.apk ke HP, buka, izinkan "instal dari sumber tidak dikenal".

## Cara 2 — Di komputer (Android Studio)
Butuh Node 20, JDK 17, Android Studio.
npm install
npm install three@0.128.0 --no-save
cp node_modules/three/build/three.min.js www/three.min.js   (lalu ganti src script three di www/index.html menjadi three.min.js)
npx cap add android
npx capacitor-assets generate --android
python3 scripts/patch_android.py
npx cap sync android
cd android && ./gradlew assembleDebug
APK ada di android/app/build/outputs/apk/debug/app-debug.apk

## Ikon aplikasi
Ikon diambil dari folder assets/ (icon-only.png, icon-foreground.png, icon-background.png). Untuk mengganti ikon, timpa file-file itu (1024x1024 px) lalu jalankan ulang build.

## Catatan
- APK ini versi debug (cukup untuk dipasang di HP). Untuk Google Play perlu build release yang ditandatangani (keystore).
- Progres dan koin disimpan di penyimpanan lokal aplikasi.
- Belum ada pengaturan grafis; di HP lemah bisa terasa berat.

## Cara membuat APK (otomatis di GitHub)
1. Buat repository baru di GitHub, upload seluruh isi folder ini (termasuk folder `.github`).
2. Buka tab **Actions** → workflow **Build APK** akan berjalan sendiri (atau klik *Run workflow*).
3. Setelah selesai (±5–8 menit), unduh artifact **ArjawinangunRacing-apk** → di dalamnya `app-debug.apk`.
4. Pindahkan ke HP Android, izinkan "install dari sumber tidak dikenal", lalu install.
Ikon aplikasi dan splash sudah memakai gambar logo Arjawinangun Racing.
