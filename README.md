# WannnSion Scanner

Port scanner sederhana dengan threading dan banner grabbing, dibuat oleh **Wannn Sion**.

## Fitur
- Scan banyak port sekaligus pakai threading
- Deteksi nama service (HTTP, PostgreSQL, dll)
- Ambil banner/header dari service yang terbuka

## Install
\`\`\`bash
git clone https://github.com/wannn-sion95/wannnsion-scanner.git
cd wannnsion-scanner
python3 wannnsion_scanner.py <target> -p 1-1000
\`\`\`

## Contoh
\`\`\`bash
python3 wannnsion_scanner.py 127.0.0.1 -p 1-1000
\`\`\`

## Disclaimer
Tool ini dibuat untuk tujuan edukasi. Hanya gunakan pada sistem milik sendiri atau yang sudah mendapat izin eksplisit. Penyalahgunaan adalah tanggung jawab pengguna.
