<p align="center">
  <img src="https://github.com/Icon11-community.png?size=250" alt="logo"/>
</p>

> Ikon mungkin mengandung merek dagang, merek dagang terdaftar, atau logo merek. Anda diperbolehkan menggunakan ikon ini hanya untuk tujuan pribadi. Anda tidak diperbolehkan menggunakannya untuk tujuan lain, termasuk tetapi tidak terbatas pada penggunaan komersial, tanpa izin tertulis dari pemegang hak cipta merek dagang, merek dagang terdaftar, atau logo merek.

[![English](https://img.shields.io/badge/-English-E4405F?style=for-the-badge)
](/README.md)
[![Bahasa](https://img.shields.io/badge/-Bahasa%20Indonesia-E4405F?style=for-the-badge)
](/README.id.md)
[![简体中文](https://img.shields.io/badge/Chinese%20Simplified-E4405F?style=for-the-badge)
](/README.zh_cn.md)

Folder11 ikon direktori khusus yang dibuat mirip dengan gaya ikon pada Windows 11.

## Daftar Isi

- [Daftar Isi](#daftar-isi)
- [Panduan Kontribusi](#panduan-kontribusi)
  - [Speifikasi Ikon](#spesifikasi-ikon)
  - [Penamaan Berkas](#penamaan-berkas)
  - [Penamaan Commit](#penamaan-commit)

## Panduan Kontribusi

Kontribusi Anda diapresiasi, tapi Anda harus megikuti panduan kontribusi. Adapun panduannya antara lain sebagai berikut.

### Spesifikasi Ikon

Kami menyediakan template dalam format fig, ai, dan svg. Adapun spesifikasinya sebagai berikut:
- Kami tidak memaksakan pada penggunaan pada program vektor tertentu.
- Ikon harus berupa vektor berformat svg.
- Ikon semestinya tidak memuat gambar raster.
- Anda tidak semestinya menipa ikon yang sudah ada.
- Kanvas berasio 1:1.
- Diasumsikan kanvas memiliki panjang 246px, maka marginnya adalah sebagai berikut:
  - Margin kiri adalah 17px (0.06640625vh).
  - Margin kanan adalah 15px (0.05859375vh).
  - Margin bawah adalah 46px (0.1796875vh).
  - Margin atas untuk "back" adalah 34px (0.1328125vh).
  - Margin atas untuk "front" adalah 62px (0.2421875vh).

### Varian Ikon Kecil

- Folder `small` adalah opsional dan berisi versi kecil dari ikon.
- Ikon ini dioptimalkan untuk ukuran piksel kecil yang umum digunakan pada ikon folder Windows, seperti 32px, 24px, 20px, dan 16px.
- Kontributor diharapkan untuk menyediakan varian kecil ini untuk memastikan konsistensi di berbagai ukuran ikon.
- Penamaan dan struktur folder `small` harus mengikuti struktur folder `svg` untuk memudahkan pemeliharaan dan pembaruan.

### Penamaan Berkas

- Penamaan berkas dimulai dengan nama ikon dan diakhiri dengan nomor varian yang dipisahkan dengan tanda hubung.
- Nama ikon harus ditulis dengan penulisan snake case.
- Karena kita tidak semestinya mengubah ikon yang ada, ikon baru haruslah memiliki nomor yang dimulai dengan 1.
- Ikon pertama tidak boleh memiliki nomor.

```
Folder11
├──📁 svg/
│   ├──📄 my_folder.svg
│   ├──📄 my_folder-1.svg
│   └──📄 my_folder-2.svg
└──📁 small/
    ├──📄 my_folder.svg
    ├──📄 my_folder-1.svg
    └──📄 my_folder-2.svg
```

### Penamaan Commit

- `feat:`  
  Jenis commit `feat` merupakan penambahan/perubahan ikon.
- `docs:`  
  Jenis commit `docs` merupakan penambahan/perubahan dokumentasi.
- `chore:`  
  Jenis commit `chore` merupakan perubahan yang tidak terlihat pengguna, misalnya: `.gitkeep` dan `.gitignore`.
- `ci:`  
  Jenis commit `ci` merupakan perubahan yang meliputi workflow action.

Perubahan besar harus menggunakan tanda seru sebagai sufiks dari jenis commit, misalnya: `feat!: changes existing icon`. Dan pesan commit haruslah berbahasa inggris.
