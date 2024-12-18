# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector as mc
from PyQt5.QtWidgets import QTableWidgetItem


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(674, 600)

        # Layouts
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 141, 201))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        # Labels
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)

        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)

        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)

        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)

        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)

        # Input Fields
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(150, 20, 491, 201))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.lineNpm = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineNpm.setObjectName("lineNpm")
        self.verticalLayout_2.addWidget(self.lineNpm)

        self.lineNama = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineNama.setObjectName("lineNama")
        self.verticalLayout_2.addWidget(self.lineNama)

        self.lineKelas = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineKelas.setObjectName("lineKelas")
        self.verticalLayout_2.addWidget(self.lineKelas)

        self.lineJurusan = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineJurusan.setObjectName("lineJurusan")
        self.verticalLayout_2.addWidget(self.lineJurusan)

        self.lineTanggalLahir = QtWidgets.QDateEdit(self.verticalLayoutWidget_2)
        self.lineTanggalLahir.setCalendarPopup(True)
        self.lineTanggalLahir.setObjectName("lineTanggalLahir")
        self.verticalLayout_2.addWidget(self.lineTanggalLahir)

        # Buttons
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 270, 631, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.insertMahasiswa = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.insertMahasiswa.setObjectName("insertMahasiswa")
        self.horizontalLayout_2.addWidget(self.insertMahasiswa)

        self.DeleteMahasiswa = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.DeleteMahasiswa.setObjectName("DeleteMahasiswa")
        self.horizontalLayout_2.addWidget(self.DeleteMahasiswa)

        self.UpdateMahasiswa = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.UpdateMahasiswa.setObjectName("UpdateMahasiswa")
        self.horizontalLayout_2.addWidget(self.UpdateMahasiswa)

        self.LoadMahasiswa = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.LoadMahasiswa.setObjectName("LoadMahasiswa")
        self.horizontalLayout_2.addWidget(self.LoadMahasiswa)

        # Result Label
        self.labelResult = QtWidgets.QLabel(Form)
        self.labelResult.setGeometry(QtCore.QRect(150, 250, 300, 20))
        font.setPointSize(10)
        self.labelResult.setFont(font)
        self.labelResult.setObjectName("labelResult")

        # Table
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(10, 310, 631, 201))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tableWidget = QtWidgets.QTableWidget(self.verticalLayoutWidget_4)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderLabels(
            ["NPM", "NAMA", "KELAS", "JURUSAN", "TANGGAL LAHIR"]
        )
        self.verticalLayout_4.addWidget(self.tableWidget)

        # Search
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 520, 631, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        self.lineSearch = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineSearch.setObjectName("lineSearch")
        self.horizontalLayout_3.addWidget(self.lineSearch)

        self.SearchMahasiswa = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.SearchMahasiswa.setObjectName("SearchMahasiswa")
        self.horizontalLayout_3.addWidget(self.SearchMahasiswa)

        # Connect Buttons
        self.insertMahasiswa.clicked.connect(self.simpandata)
        self.LoadMahasiswa.clicked.connect(self.loadmahasiswa)
        self.DeleteMahasiswa.clicked.connect(self.deletemahasiswa)
        self.UpdateMahasiswa.clicked.connect(self.updatemahasiswa)
        self.SearchMahasiswa.clicked.connect(self.searchmahasiswa)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def simpandata(self):
        try:
            mydb = mc.connect(host="localhost", user="root", password="", database="db_kampus")
            cursor = mydb.cursor()

            lnpm = self.lineNpm.text()
            lnama = self.lineNama.text()
            lkelas = self.lineKelas.text()
            ljurusan = self.lineJurusan.text()
            ltgl = self.lineTanggalLahir.date().toString("yyyy-MM-dd")

            if not lnpm or not lnama or not lkelas or not ljurusan:
                self.labelResult.setText("All fields are required!")
                return

            sql = "INSERT INTO mahasiswa (npm, nama, kelas, jurusan, tanggal_lahir) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (lnpm, lnama, lkelas, ljurusan, ltgl))
            mydb.commit()

            self.labelResult.setText("Data Mahasiswa Berhasil Disimpan")
            self.lineNpm.clear()
            self.lineNama.clear()
            self.lineKelas.clear()
            self.lineJurusan.clear()
            self.lineTanggalLahir.setDate(QtCore.QDate.currentDate())

        except mc.Error as e:
            self.labelResult.setText(f"Error: {str(e)}")

    def loadmahasiswa(self):
        try:
            mydb = mc.connect(host="localhost", user="root", password="", database="db_kampus")
            cursor = mydb.cursor()
            cursor.execute("SELECT * FROM mahasiswa ORDER BY npm ASC")
            result = cursor.fetchall()

            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))

            self.labelResult.setText("Data Mahasiswa Berhasil Ditampilkan")

        except mc.Error as e:
            self.labelResult.setText(f"Error: {str(e)}")

    def deletemahasiswa(self):
        npm = self.lineNpm.text().strip()
        if not npm:
            self.labelResult.setText("NPM tidak boleh kosong!")
            return

        try:
            mydb = mc.connect(host="localhost", user="root", password="", database="db_kampus")
            cursor = mydb.cursor()
            sql = "DELETE FROM mahasiswa WHERE npm = %s"
            cursor.execute(sql, (npm,))
            mydb.commit()

            if cursor.rowcount > 0:
                self.labelResult.setText(f"Data dengan NPM {npm} berhasil dihapus!")
            else:
                self.labelResult.setText(f"Data dengan NPM {npm} tidak ditemukan!")

            self.loadmahasiswa()
            self.lineNpm.clear()

        except mc.Error as e:
            self.labelResult.setText(f"Error: {str(e)}")
        finally:
            if mydb.is_connected():
                cursor.close()
                mydb.close()

    def updatemahasiswa(self):
        npm = self.lineNpm.text().strip()
        nama = self.lineNama.text().strip()
        kelas = self.lineKelas.text().strip()
        jurusan = self.lineJurusan.text().strip()
        tanggal_lahir = self.lineTanggalLahir.date().toString("yyyy-MM-dd")

        if not npm or not nama or not kelas or not jurusan:
            self.labelResult.setText("All fields are required!")
            return

        try:
            mydb = mc.connect(host="localhost", user="root", password="", database="db_kampus")
            cursor = mydb.cursor()
            sql = """
                UPDATE mahasiswa 
                SET nama = %s, kelas = %s, jurusan = %s, tanggal_lahir = %s 
                WHERE npm = %s
            """
            cursor.execute(sql, (nama, kelas, jurusan, tanggal_lahir, npm))
            mydb.commit()

            self.labelResult.setText(f"Data Mahasiswa dengan NPM {npm} berhasil diperbarui!")
            self.loadmahasiswa()

        except mc.Error as e:
            self.labelResult.setText(f"Error: {str(e)}")
        finally:
            if mydb.is_connected():
                cursor.close()
                mydb.close()


    def searchmahasiswa(self):
        keyword = self.lineSearch.text().strip()
        if not keyword:
            self.labelResult.setText("Masukkan kata kunci pencarian!")
            return

        try:
            mydb = mc.connect(host="localhost", user="root", password="", database="db_kampus")
            cursor = mydb.cursor()

            search_pattern = f"%{keyword}%"
            sql = """
                SELECT * FROM mahasiswa 
                WHERE npm LIKE %s OR nama LIKE %s OR kelas LIKE %s 
                OR jurusan LIKE %s OR tanggal_lahir LIKE %s
            """
            cursor.execute(sql, (search_pattern, search_pattern, search_pattern, search_pattern, search_pattern))
            result = cursor.fetchall()

            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))

            if not result:
                self.labelResult.setText("Data tidak ditemukan!")
            else:
                self.labelResult.setText(f"{len(result)} data ditemukan!")

        except mc.Error as e:
            self.labelResult.setText(f"Error: {str(e)}")
        finally:
            if mydb.is_connected():
                cursor.close()
                mydb.close()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form Mahasiswa"))
        self.label_2.setText(_translate("Form", "NPM"))
        self.label.setText(_translate("Form", "NAMA"))
        self.label_4.setText(_translate("Form", "KELAS"))
        self.label_5.setText(_translate("Form", "JURUSAN"))
        self.label_3.setText(_translate("Form", "TANGGAL LAHIR"))
        self.insertMahasiswa.setText(_translate("Form", "INSERT"))
        self.DeleteMahasiswa.setText(_translate("Form", "DELETE"))
        self.UpdateMahasiswa.setText(_translate("Form", "UPDATE"))
        self.LoadMahasiswa.setText(_translate("Form", "LOAD"))
        self.SearchMahasiswa.setText(_translate("Form", "SEARCHING"))
        self.labelResult.setText(_translate("Form", "Status: Ready"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
