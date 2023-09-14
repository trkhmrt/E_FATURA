import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.mime.text import MIMEText

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox
from Login_Sayfasi import *
from Fatura_Ekrani import *
from Menu_Ekrani import *
from Fatura_Listeleme_Ekrani import *

import sqlite3

con=sqlite3.connect("E_FATURA.db")
cursor=con.cursor()
class LoginSayfasi(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.girisyap.clicked.connect(self.kontrol)

        self.con = sqlite3.connect("E_FATURA.db")
        self.cursor = self.con.cursor()

    def kontrol(self):
        kod = self.ui.kaadi.text()
        sifre = self.ui.sifre.text()

        self.cursor.execute(f"SELECT * FROM Esnaf WHERE EsnafKod = '{sifre}' AND EsnafSifre ='{kod}'")
        kullanici = self.cursor.fetchone()


        if kullanici:
            QMessageBox.information(None, "Bilgi", "Giriş Başarılı!!!")
            self.hide()

            self.menu=MenuEkrani()
            self.menu.show()


        else:
            QMessageBox.critical(None, "Uyarı", "Kullanıcı adı veya şifre hatalı!!!.")

class FaturaEkrani(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Fature_Ekrani()
        self.ui.setupUi(self)
        self.ui.btn_Ekle.clicked.connect(self.FaturaEkle)
        self.ui.btn_Temizle.clicked.connect(self.Temizle)
        self.ui.btnHesapla.clicked.connect(self.UrunToplamTutar)
    def FaturaEkle(self):
        try:
            tarih=self.ui.tarih.date().toString("yyyy-MM-dd")
            saat=self.ui.saat.time().toString("hh:mm")
            parabirimi=self.ui.cmbParaBirimi.currentText()
            kur=self.ui.txtDovizKuru.text()
            fatura=self.ui.cmbFaturaTipi.currentText()
            kimlikno=self.ui.txttc.text()
            aliciunvan=self.ui.txtunvan.text()
            aliciad=self.ui.txtad.text()
            alicisoyad=self.ui.txtsoyad.text()
            vergidairesi=self.ui.txtvergidairesi.text()
            aliciulke=self.ui.cmbulke.currentText()
            aliciadres=self.ui.txtadres.toPlainText()
            urunbilgisi=self.ui.txtUrunBilgisi.text()
            urunadet=self.ui.txtUrunAdet.text()
            urunbirimfiyat=self.ui.txtBirimFiyati.text()
            toplam=self.ui.lblTutar.text()
            if self.ui.lblTutar.text().strip()=="":
                QMessageBox.critical(None, "Bilgi", "Önce Toplam Tutar Hesaplanmalı!")
            else:
                cursor.execute(
                    f"Insert into Fatura (DuzenlemeTarihi,DuzenlemeSaati,ParaBirimi,DovizKuru,FaturaTipi,Tc,Unvan,Ad,Soyad,VergiDairesi,Ulke,Adres,UrunBilgisi,UrunAdet,UrunKdv,UrunToplamTutar,UrunBirimFiyatı)values('{tarih}','{saat}','{parabirimi}','{kur}','{fatura}','{kimlikno}','{aliciunvan}','{aliciad}','{alicisoyad}','{vergidairesi}','{aliciulke}','{aliciadres}','{urunbilgisi}','{urunadet}','18','{toplam}','{urunbirimfiyat}')")
                con.commit()
                QMessageBox.information(None, "Bilgi", "Fatura Kaydedildi!")
        except:
            QMessageBox.critical(None, "Bilgi", "Fatura Kaydedilmedi!\nEksik veya Hatalı Giriş")

    def Temizle(self):
        self.ui.tarih.setDate(self.ui.tarih.minimumDate())
        self.ui.saat.setTime(self.ui.saat.minimumTime())
        self.ui.cmbParaBirimi.setCurrentIndex(0)
        self.ui.txtDovizKuru.clear()
        self.ui.cmbFaturaTipi.setCurrentIndex(0)
        self.ui.txttc.clear()
        self.ui.txtunvan.clear()
        self.ui.txtad.clear()
        self.ui.txtsoyad.clear()
        self.ui.txtvergidairesi.clear()
        self.ui.cmbulke.setCurrentIndex(0)
        self.ui.txtadres.clear()
        self.ui.txtUrunBilgisi.clear()
        self.ui.txtUrunAdet.clear()
        self.ui.txtBirimFiyati.clear()
        self.ui.lblTutar.clear()
    def UrunToplamTutar(self):
        try:
            toplam = (int(self.ui.txtUrunAdet.text()) * int(self.ui.txtBirimFiyati.text())) + (
                        int(self.ui.txtUrunAdet.text()) * int(self.ui.txtBirimFiyati.text())) * 18 / 100
            self.ui.lblTutar.setText(str(toplam))
        except:
            QMessageBox.critical(None, "Bilgi", "Eksik veya Hatalı Giriş")


class FaturaListeleme(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_Form()
        self.ui.setupUi(self)
        self.ui.btn_eposta.clicked.connect(self.MailGonder2)
        self.ui.btnPdf.clicked.connect(self.PdfDonustur)
        self.ui.FaturaTablosu.itemClicked.connect(self.HucredenVeriAl)
        self.ui.btn_faturasil.clicked.connect(self.FaturaSil)
        self.ui.btnAra.clicked.connect(self.FaturaAra)

        cursor.execute(
            "SELECT * FROM Fatura")
        veriler = cursor.fetchall()
        basliklar = [desc[0] for desc in cursor.description]  ##Başlıkları veri tabanından aldım.
        self.ui.FaturaTablosu.setHorizontalHeaderLabels(basliklar)
        self.ui.FaturaTablosu.verticalHeader().setVisible(False)#Y eksenindeki rakamları yok etmek için

        self.ui.FaturaTablosu.setWindowTitle("Fatura Tablosu")
        self.ui.FaturaTablosu.setRowCount(len(veriler))
        self.ui.FaturaTablosu.setColumnCount(len(veriler[0]))

        for column, baslik in enumerate(basliklar):
            item = QTableWidgetItem(baslik)
            self.ui.FaturaTablosu.setHorizontalHeaderItem(column, item)

        for row, veri_satiri in enumerate(veriler):
            for column, veri in enumerate(veri_satiri):
                item = QTableWidgetItem(str(veri))
                self.ui.FaturaTablosu.setItem(row, column, item)
        self.ui.FaturaTablosu.show()
    def PdfDonustur(self):
        if self.ui.txtFaturaID.text().strip()=="":
            QMessageBox.critical(None, "Uyarı", "Dönüştürülecek Fatura'nın ID bilgisi girilmeli!")
        else:
            id = self.ui.txtFaturaID.text()
            cursor.execute(
                f"SELECT FaturaID,DuzenlemeTarihi, DuzenlemeSaati, ParaBirimi, DovizKuru, FaturaTipi, Tc, Unvan, Ad, Soyad, VergiDairesi, Ulke, Adres,UrunBilgisi,UrunAdet,UrunKdv,UrunToplamTutar,UrunBirimFiyatı FROM Fatura where FaturaID='{id}'")
            veriler = cursor.fetchall()
            id = veriler[0][0]
            id=str(id)
            id += ".pdf"

            pdf = canvas.Canvas(id, pagesize=letter)
            pdf.setFont("Helvetica-Bold", 12)
            yatay_bosluk = 50  # Yatay boşluk miktarı
            dikey_bosluk = 20  # Dikey boşluk miktarı

            for veri in veriler:
                fatura_id = str(veri[0])
                duzenleme_tarihi = veri[1]
                duzenleme_saati = veri[2]
                para_birimi = veri[3]
                doviz_kuru = veri[4]
                fatura_tipi = veri[5]
                tc = veri[6]
                unvan = veri[7]
                ad = veri[8]
                soyad = veri[9]
                vergi_dairesi = veri[10]
                ulke = veri[11]
                adres = veri[12]

                # Fatura ID
                pdf.drawString(yatay_bosluk, pdf._pagesize[1] - dikey_bosluk, f"Fatura ID: {fatura_id}")
                dikey_bosluk += 20

                # Düzenleme Tarihi
                pdf.drawString(yatay_bosluk, pdf._pagesize[1] - dikey_bosluk, f"Düzenleme Tarihi: {duzenleme_tarihi}")
                dikey_bosluk += 20

                # Düzenleme Saati
                pdf.drawString(yatay_bosluk, pdf._pagesize[1] - dikey_bosluk, f"Düzenleme Saati: {duzenleme_saati}")
                dikey_bosluk += 20

                # Para Birimi
                pdf.drawString(yatay_bosluk, pdf._pagesize[1] - dikey_bosluk, f"Para Birimi: {para_birimi}")
                dikey_bosluk += 20

                # Döviz Kuru
                pdf.drawString(yatay_bosluk, pdf._pagesize[1] - dikey_bosluk, f"Döviz Kuru: {doviz_kuru}")
                dikey_bosluk += 20

                # Fatura Tipi
                pdf.drawString(yatay_bosluk, pdf._pagesize[1] - dikey_bosluk, f"Fatura Tipi: {fatura_tipi}")
                dikey_bosluk += 20

                # TC
                pdf.drawString(yatay_bosluk, pdf._pagesize[1] - dikey_bosluk, f"TC: {tc}")
                dikey_bosluk += 20

                # Unvan
                pdf.drawString(yatay_bosluk, pdf._pagesize[1] - dikey_bosluk, f"Unvan: {unvan}")
                dikey_bosluk += 20

                # Ad
                pdf.drawString(yatay_bosluk, pdf._pagesize[1] - dikey_bosluk, f"Ad: {ad}")
                dikey_bosluk += 20

                # Soyad
                pdf.drawString(yatay_bosluk, pdf._pagesize[1] - dikey_bosluk, f"Soyad: {soyad}")
                dikey_bosluk += 20

                # Vergi Dairesi
                pdf.drawString(yatay_bosluk, pdf._pagesize[1] - dikey_bosluk, f"Vergi Dairesi: {vergi_dairesi}")
                dikey_bosluk += 20

                # Ülke
                pdf.drawString(yatay_bosluk, pdf._pagesize[1] - dikey_bosluk, f"Ülke: {ulke}")
                dikey_bosluk += 20

                # Adres
                pdf.drawString(yatay_bosluk, pdf._pagesize[1] - dikey_bosluk, f"Adres: {adres}")
                dikey_bosluk += 20

                # Urun Bilgisi
                pdf.drawString(yatay_bosluk, pdf._pagesize[1] - dikey_bosluk, f"Ürün Bilgisi: {veri[13]}")
                dikey_bosluk += 20

                # Urun Adet
                pdf.drawString(yatay_bosluk, pdf._pagesize[1] - dikey_bosluk, f"Ürün Adet: {veri[14]}")
                dikey_bosluk += 20

                # Urun KDV
                pdf.drawString(yatay_bosluk, pdf._pagesize[1] - dikey_bosluk, f"Ürün KDV: {veri[15]}")
                dikey_bosluk += 20

                # Urun Toplam Tutar
                pdf.drawString(yatay_bosluk, pdf._pagesize[1] - dikey_bosluk, f"Ürün Toplam Tutar: {veri[16]}")
                dikey_bosluk += 20

                # Urun Birim Fiyatı
                pdf.drawString(yatay_bosluk, pdf._pagesize[1] - dikey_bosluk, f"Ürün Birim Fiyatı: {veri[17]}")
                dikey_bosluk += 20

                dikey_bosluk += 20  # Bir sonraki veri seti için dikey boşluk ekle

            pdf.save()
            QMessageBox.information(None, "Uyarı", "Dönüştürüldü")




    def MailGonder2(self):
        if  self.ui.txtFaturaIDEposta.text().strip()=="" or self.ui.txtGonderen.text().strip()=="" or self.ui.txtAlici.text().strip()=="":
            QMessageBox.warning(None, "Uyarı", "Bilgiler Boş Bırakılamaz!")
        else:
            id = self.ui.txtFaturaIDEposta.text()
            cursor.execute(f"SELECT FaturaID,Ad,Soyad from Fatura where FaturaID='{id}'")
            veri = cursor.fetchone()
            print(veri)
            dosyaadi = str(id)
            dosyaadi += ".pdf"
            msg = MIMEMultipart()
            msg['From'] = self.ui.txtGonderen.text()
            msg['To'] = self.ui.txtAlici.text()
            msg['Subject'] = self.ui.txtKonu.text()

            # E-posta mesajını ekleyin
            msg.attach(MIMEText(f"Sayın {veri[1]} {veri[2]} faturanız ektedir.İyi Günler Dileriz. ", 'plain'))

            # Dosya ekleyin

            with open(dosyaadi, 'rb') as attachment:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)

                part.add_header('Content-Disposition', f'attachment; filename="{dosyaadi}"')
                msg.attach(part)

            # SMTP sunucusuna bağlanarak e-postayı gönderin
            try:
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login("trkhamarat@gmail.com", "gjpcoewfuskozyyr")
                server.send_message(msg)
                server.quit()
                QMessageBox.information(None, "Uyarı", "E-Posta İletildi!")
            except Exception as e:
                print("E-posta gönderme hatası:", str(e))
                QMessageBox.information(None, "Uyarı", "E-Posta İletilmedi!")

    def HucredenVeriAl(self,item):
        column = 0  # İstenilen sütun indeksi
        row = item.row()
        cell_text = self.ui.FaturaTablosu.item(row, column).text()
        self.ui.txtFaturAraSil.setText(cell_text)
        self.ui.txtFaturaID.setText(cell_text)
        self.ui.txtFaturaIDEposta.setText(cell_text)


    def FaturaSil(self):
        id=self.ui.txtFaturAraSil.text()
        cursor.execute(f"Delete from Fatura Where FaturaID='{id}'")
        con.commit()
        QMessageBox.critical(None, "Uyarı", "Fatura Silindi")
        cursor.execute(
            "SELECT * FROM Fatura")
        veriler = cursor.fetchall()
        basliklar = [desc[0] for desc in cursor.description]  ##Başlıkları veri tabanından aldım.
        self.ui.FaturaTablosu.setHorizontalHeaderLabels(basliklar)
        self.ui.FaturaTablosu.verticalHeader().setVisible(False)  # Y eksenindeki rakamları yok etmek için

        self.ui.FaturaTablosu.setWindowTitle("Fatura Tablosu")
        self.ui.FaturaTablosu.setRowCount(len(veriler))
        self.ui.FaturaTablosu.setColumnCount(len(veriler[0]))

        for column, baslik in enumerate(basliklar):
            item = QTableWidgetItem(baslik)
            self.ui.FaturaTablosu.setHorizontalHeaderItem(column, item)

        for row, veri_satiri in enumerate(veriler):
            for column, veri in enumerate(veri_satiri):
                item = QTableWidgetItem(str(veri))
                self.ui.FaturaTablosu.setItem(row, column, item)
        self.ui.FaturaTablosu.show()
    def FaturaAra(self):
        if self.ui.txtFaturAraSil.text().strip()=="":
            cursor.execute(f"Select * from Fatura")
            veriler = cursor.fetchall()
            basliklar = [desc[0] for desc in cursor.description]  ##Başlıkları veri tabanından aldım.
            self.ui.FaturaTablosu.setHorizontalHeaderLabels(basliklar)
            self.ui.FaturaTablosu.verticalHeader().setVisible(False)  # Y eksenindeki rakamları yok etmek için

            self.ui.FaturaTablosu.setWindowTitle("Fatura Tablosu")
            self.ui.FaturaTablosu.setRowCount(len(veriler))
            self.ui.FaturaTablosu.setColumnCount(len(veriler[0]))

            for column, baslik in enumerate(basliklar):
                item = QTableWidgetItem(baslik)
                self.ui.FaturaTablosu.setHorizontalHeaderItem(column, item)

            for row, veri_satiri in enumerate(veriler):
                for column, veri in enumerate(veri_satiri):
                    item = QTableWidgetItem(str(veri))
                    self.ui.FaturaTablosu.setItem(row, column, item)
            self.ui.FaturaTablosu.show()
        else:
            id = self.ui.txtFaturAraSil.text()
            cursor.execute(f"Select * from Fatura Where FaturaID='{id}'")
            veriler = cursor.fetchall()
            basliklar = [desc[0] for desc in cursor.description]  ##Başlıkları veri tabanından aldım.
            self.ui.FaturaTablosu.setHorizontalHeaderLabels(basliklar)
            self.ui.FaturaTablosu.verticalHeader().setVisible(False)  # Y eksenindeki rakamları yok etmek için

            self.ui.FaturaTablosu.setWindowTitle("Fatura Tablosu")
            self.ui.FaturaTablosu.setRowCount(len(veriler))
            self.ui.FaturaTablosu.setColumnCount(len(veriler[0]))

            for column, baslik in enumerate(basliklar):
                item = QTableWidgetItem(baslik)
                self.ui.FaturaTablosu.setHorizontalHeaderItem(column, item)

            for row, veri_satiri in enumerate(veriler):
                for column, veri in enumerate(veri_satiri):
                    item = QTableWidgetItem(str(veri))
                    self.ui.FaturaTablosu.setItem(row, column, item)
            self.ui.FaturaTablosu.show()













class MenuEkrani(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_Menu()
        self.ui.setupUi(self)
        self.ui.btn_faturaolustur.clicked.connect(self.FaturaEkraniAc)
        self.ui.btn_faturagoruntule.clicked.connect(self.FaturaGoruntuleEkrani)
        self.ui.btn_cikis.clicked.connect(self.CikisYap)

    def CikisYap(self, event):
        reply = QMessageBox.question(self, 'Çıkış', 'Çıkmak istediğinize emin misiniz?',
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            self.hide()
            self.loginekrani=LoginSayfasi()
            self.loginekrani.show()
        else:
            pass
    def FaturaEkraniAc(self):
        self.faturaekrani=FaturaEkrani()
        self.faturaekrani.show()
    def FaturaGoruntuleEkrani(self):
        self.faturagoruntule=FaturaListeleme()
        self.faturagoruntule.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)

    login_sayfasi = LoginSayfasi()
    login_sayfasi.show()

    sys.exit(app.exec())
