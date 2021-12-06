<p align="center">
  <img src="https://user-images.githubusercontent.com/46255322/144792780-db2a2947-2a69-4788-ba15-6ae0b6a49a7d.png"  style="width:300px;height:300px;"/>
</p>

[![English](https://img.shields.io/badge/-English-blue)
](/README.md)
[![Bahasa](https://img.shields.io/badge/-Bahasa%20Indonesia-blue)
](/README.id.md)
[![Facebook](https://img.shields.io/badge/Facebook%20Group-Sun%20Valley%20Indonesia-blue?logo=facebook)
](https://www.facebook.com/groups/sunvalleyindonesia/)

Folder11 ikon direktori khusus yang dibuat mirip dengan gaya ikon pada Windows 11.

> Kami tidak berafiliasi dengan Microsoft.

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

### Penamaan Berkas

- Penamaan berkas dimulai dengan nama ikon dan diakhiri dengan nomor varian yang dipisahkan dengan tanda hubung.
- Nama ikon harus ditulis dengan penulisan snake case.
- Karena kita tidak semestinya mengubah ikon yang ada, ikon baru haruslah memiliki nomor yang dimulai dengan 1.
- Ikon pertama tidak boleh memiliki nomor.

```
Folder11
└──📁 svg/
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
  Jenis commit `chore` merupakan perubahan yang tidak terlihat pengguna, misalnya: action workflow, `.gitkeep`, dan `.gitignore`.

Perubahan besar harus menggunakan tanda seru sebagai sufiks dari jenis commit, misalnya: `feat!: changes existing icon`. Dan pesan commit haruslah berbahasa inggris.
