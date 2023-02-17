<a name="readme-top"></a>
<h1 align="center">MyFood</h1>
<!-- TABLE OF CONTENTS -->
Daftar Isi
  <ol>
    <li><a href="#penjelasan-aplikasi">Penjelasan Aplikasi</a></li>
    <li><a href="#cara-menjalankan-aplikasi">Cara Menjalankan Aplikasi</a></li>
    <li>
      <a href="#daftar-modul">Daftar Modul</a>
      <ul>
        <li><a href="#modul-menu">Modul Menu</a></li>
      </ul>
      <ul>
        <li><a href="#modul-produk">Modul Produk</a></li>
      </ul>
      <ul>
        <li><a href="#modul-keranjang">Modul Keranjang</a></li>
      </ul>
    </li>
    <li>
      <a href="#daftar-tabel-basis-data">Daftar Tabel Basis Data</a>
      <ul>
        <li><a href="#tabel-data-menu-restoran">Tabel Data Menu Restoran</a></li>
      </ul>
      <ul>
        <li><a href="#tabel-data-pesanan-customer">Tabel Data Pesanan Customer</a></li>
      </ul>
    </li>
  </ol>

<!-- Penjelasan Aplikasi -->
## Penjelasan Aplikasi

**MyFood**

MyFood merupakan aplikasi pemesanan makanan di restoran yang bertujuan untuk membantu customer yang hendak melakukan pemesanan makanan melalui dekstop app yang tersedia pada restoran. Dengan adanya aplikasi ini, customer akan dimudahkan dalam melihat daftar menu, harga, dan dapat memesan makanan dan minuman sendiri melalui fitur keranjang dan checkout. Makanan yang telah dipesan customer otomatis masuk ke database milik restoran sehingga mempermudah koki dalam menyiapkan menu makanan.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- Cara Menjalankan Aplikasi -->
## Cara Menjalankan Aplikasi

**Prerequisites**
1. Mengunduh file [DataRestoran.sql](https://github.com/salimashockbgt/TubesRPL/tree/master/src/db) yang tersedia pada folder src/db
2. Membuat database yang bernama DataRestoran pada postgreSQL, lalu mengimport file DataRestoran.sql pada database DataRestoran
3. Mengubah pengaturan server postgreSQL menjadi sebagai berikut:
          
          user="postgres",
          password="123",
          host="127.0.0.1",
          port=5432
4. Membuka folder src pada master branch lalu run program melalui file Main.py

Saat akan menjalankan program, lakukan instalasi pycoporg2 pada terminal.
  ```sh
  pip install psycopg2-binary
  ```
<p align="right">(<a href="#readme-top">back to top</a>)</p>
