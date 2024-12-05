@echo off
:: Yönetici olarak cmd açılması için komut
:: Bu komutun çalışması için bat dosyasının, yönetici yetkisiyle çalıştırılması gerekiyor
setlocal enabledelayedexpansion

:: Yönetici olarak çalıştırma
:: Scriptin yönetici olarak çalışıp çalışmadığını kontrol et
NET SESSION >nul 2>&1
if %errorlevel% NEQ 0 (
    echo Bu dosya yönetici olarak calistirilmalidir.
    pause
    exit /b
)

:: DS_Helper paketini kaldırma
echo DS_Helper paketini kaldırmak istiyorsunuz. Devam etmek icin "y" tusuna basın...
pip uninstall DS_Helper -y

:: DS_Helper paketini GitHub'dan yükleme
echo DS_Helper paketini GitHub'dan yükluyoruz...
pip install git+https://github.com/csinangin/DS_Helper.git

echo Islemler tamamlandi.
pause
