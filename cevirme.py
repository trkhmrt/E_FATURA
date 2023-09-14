from PyQt6 import uic

with open("Login_Sayfasi.py","w", encoding="utf-8") as fout:
    uic.compileUi("Login_Sayfasi.ui", fout)
