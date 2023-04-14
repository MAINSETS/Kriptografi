<a name="readme-top"></a>
<h1 align="center">Digital Signature</h1>
<!-- TABLE OF CONTENTS -->
Daftar Isi
  <ol>
    <li><a href="#penjelasan-aplikasi">Penjelasan Aplikasi</a></li>
    <li><a href="#cara-menjalankan-aplikasi">Cara Menjalankan Aplikasi</a></li>
  </ol>

<!-- Penjelasan Aplikasi -->
## Penjelasan Aplikasi

**Digital Signature**

Aplikasi desktop 'Digital Signature' mengimplementasikan algoritma RSA + SHA-3 (Keccak) untuk memberi tanda-tangan digital pada dokumen (file) elektronis. Dalam hal ini, pengguna sebagai pemilik dokumen mempunyai sepasang kunci, yaitu kunci publik dan kunci privat yang digunakan untuk menandatangani dokumen dan memverifikasi keaslian dokumen. 

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- Cara Menjalankan Aplikasi -->
## Cara Menjalankan Aplikasi

**Prerequisites**
1. Download folder tugas 2 dan jalankan pada IDE visual studio code atau IDE lainnya yang mendukung
2. Saat akan menjalankan program, apabila belum memiliki library tkinter, lakukan instalasi tkinter pada terminal.
  ```sh
  pip install tkinter
  ```
3. Lakukan instalasi library Crypto pada terminal
  ```sh
  pip install Crypto
  ```
4. Run program main.py

apabila terjadi error *ModuleNotFoundError: No module named 'Crypto'*, biasanya terjadi karena os windows tidak sengaja me-lowercase-kan folder library Crypto. Solusinya, cek library Crypto pada direktori site-packages python,
biasanya terdapat pada C:\Users\NamaUser\AppData\Roaming\Python\Python38\site-packages. Ubah folder yang bernama "crypto" menjadi uppercase "Crypto", dan jalankan kembali main.py

<p align="right">(<a href="#readme-top">back to top</a>)</p>
