# Import necessary modules from PyQt5
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QRadioButton, QMessageBox, QGroupBox, QButtonGroup, QLineEdit, QComboBox, QFileDialog, QTextEdit, QInputDialog

import time

# Initialize the application and main window
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('restaurant')
main_win.resize(400, 200)

# Get current timestamp for billing purposes
timestamp = time.time()
current_date = time.ctime(timestamp)

# Global variables for order details and billing
textmakan = '' 
textminum = ''
promotext = ''
qty_makantext = ''
qty_minumtext = ''
total = 0
file_content_drink = ''
file_content_food = ''
total_makan = 0
total_minum = 0
buyer =''
promo = 0
promonotif =''
totalbills = 0
tax = 0

# Widgets initialization
labelminum = QLabel('Pilih minuman')
labelmakan = QLabel('Pilih makanan')
promolabel = QLabel('Masukkan kode promo di sini:')
promocode = QLineEdit('')
label_qty_makan = QLabel('Qty: (0 jika tidak memesan)')
qty_makan = QLineEdit('')
label_qty_minum = QLabel('Qty: (0 jika tidak memesan)')
qty_minum = QLineEdit('')
input_makanan = QComboBox()
input_minum = QComboBox()
buyer_name = QLabel('Nama pembeli:')
buyer_input = QLineEdit('')
button = QPushButton('Pesan')
button2 = QPushButton('Bayar')

# List for menu items
makanan = ['Bubur Ayam', 'Bakmie kuah', 'Bakmie goreng', 'Nasigoreng Seafood', 'Ayam nangking', 'Bihun Goreng', 'Kwetiaw Goreng', 'Bakpao', 'Siomay', 'Gyoza']
minum = ['chinese tea', 'Jeruk es/panas', 'Teh tawar es/panas', 'Teh manis es/panas', 'jus semangka', 'Lemon Tea', 'Coconut Milk', 'Mineral Water', 'Soda', 'jus melon']
input_makanan.addItems(makanan)
input_minum.addItems(minum)

# Layout setup
layout = QVBoxLayout()
hbox_nama = QHBoxLayout()
hbox_makanan = QHBoxLayout()
hbox_minuman = QHBoxLayout()

hbox_nama.addWidget(buyer_name)
hbox_nama.addWidget(buyer_input)
layout.addLayout(hbox_nama)

hbox_makanan.addWidget(labelmakan)
hbox_makanan.addWidget(input_makanan)
hbox_makanan.addWidget(label_qty_makan)
hbox_makanan.addWidget(qty_makan)
layout.addLayout(hbox_makanan)

hbox_minuman.addWidget(labelminum)
hbox_minuman.addWidget(input_minum)
hbox_minuman.addWidget(label_qty_minum)
hbox_minuman.addWidget(qty_minum)
layout.addLayout(hbox_minuman)

layout.addWidget(promolabel)
layout.addWidget(promocode)
layout.addWidget(button)
layout.addWidget(button2)
main_win.setLayout(layout)

# Function to handle ordering of food items
def pesan():
    global textmakan, textminum, promotext, qty_makantext, qty_minumtext, total_makan, total_minum, total, file_content_food, file_content_drink, promo, promonotif, totalbills, tax
    
    textmakan = input_makanan.currentText()
    textminum = input_minum.currentText()
    promotext = promocode.text()
    qty_makantext = int(qty_makan.text())
    qty_minumtext = int(qty_minum.text())

    # Calculate total for food items ordered
    if qty_makantext != 0:
        subtotal_makan = 0
        if textmakan == 'Bubur Ayam':
            subtotal_makan += 25500
        elif textmakan == 'Bakmie kuah': 
            subtotal_makan += 20000
        elif textmakan == 'Bakmie goreng':
            subtotal_makan += 22000
        elif textmakan == 'Nasigoreng Seafood':
            subtotal_makan += 22000
        elif textmakan == 'Ayam nangking':
            subtotal_makan += 30000
        elif textmakan == 'Bihun Goreng':
            subtotal_makan += 22000
        elif textmakan == 'Kwetiaw Goreng':
            subtotal_makan += 22000
        elif textmakan == 'Bakpao':
            subtotal_makan += 8000
        elif textmakan == 'Siomay':
            subtotal_makan += 5500
        elif textmakan == 'Gyoza':
            subtotal_makan += 5000
        else:
            QMessageBox.information(main_win, 'Input error', 'Error')
        
        total_makan = subtotal_makan * qty_makantext
        combined_food = '\n' + textmakan + ' x ' + str(qty_makantext) + '=' + str(subtotal_makan * qty_makantext)
    else:
        combined_food = ''

    # Write food order details to file
    with open('food.txt', 'a') as file:
        file.write(combined_food)

    # Calculate total for drink items ordered
    if qty_minumtext != 0:
        if qty_minumtext != '':
            subtotal_minum = 0
            if textminum == 'chinese tea':
                subtotal_minum += 15800
            elif textminum == 'Jeruk es/panas':
                subtotal_minum += 5000
            elif textminum == 'Teh tawar es/panas':
                subtotal_minum += 3000
            elif textminum == 'Teh manis es/panas':
                subtotal_minum += 4000
            elif textminum == 'jus semangka':
                subtotal_minum += 10000
            elif textminum == 'Lemon Tea':
                subtotal_minum += 6000
            elif textminum == 'Coconut Milk':
                subtotal_minum += 12300
            elif textminum == 'Mineral Water':
                subtotal_minum += 5000
            elif textminum == 'Soda':
                subtotal_minum += 13000
            elif textminum == 'jus melon':
                subtotal_minum += 13200
            else:
                QMessageBox.information(main_win, 'Input error', 'Error')
            
            total_minum = subtotal_minum * qty_minumtext
            combined_drink = '\n' + textminum + ' x ' + str(qty_minumtext) + '=' + str(subtotal_minum * qty_minumtext)
    else:
        combined_drink = ''
    
    # Write drink order details to file
    with open('drink.txt', 'a') as file:
        file.write(combined_drink)

    # Calculate total bill including tax and apply promo code if valid
    total += total_makan + total_minum
    tax = total * 0.11
    totalbills = total + tax

    if promotext == 'promo2102':
        totalbills -= 2000
        promonotif = 'Potongan diskon 2000 rupiah'
        QMessageBox.information(main_win, 'Promo', 'Kode promo Anda valid! ' + promonotif + ' diterapkan.')
        promo = 1
    elif promotext == '':
        QMessageBox.information(main_win, 'Notifikasi', 'Berhasil')
    else:
        QMessageBox.information(main_win, 'Promo', 'Kode promo Anda tidak valid!')

# Function to handle payment and generate bill
def bayar():
    global textmakan, textminum, promotext, qty_makantext, qty_minumtext, total_makan, total_minum, total, file_content_drink, file_content_food, buyer_input, promo, promonotif, current_date, totalbills, tax
    buyer = buyer_input.text()
    with open('food.txt', 'r') as file:
        file_content_food = file.read()

    with open('drink.txt', 'r') as file:
        file_content_drink = file.read()
    
    # Input cash amount and calculate change
    cash, ok = QInputDialog.getDouble(main_win, "Masukkan uang tunai", "Total: " + str(totalbills), 0, 0, 1000000000, 2)
    
    if ok:
        if cash >= total:
            change = cash - totalbills
            if promo == 1:
                hasil = (
                    "********************* Tagihan *********************\n"
                    "Tanggal: " + current_date + '   ' + buyer + "\n"
                    "=============================\n"
                    "Makanan: " + file_content_food +  "\n"
                    "Minuman: " + file_content_drink + "\n"
                    "Diskon: " + promonotif + "\n"
                    "----------------------------------------------\n"
                    "Subtotal: " + str(total) + " Rupiah\n" 
                    'Pajak: ' + str(tax) + ' Rupiah\n'
                    'Total: ' + str(totalbills) + ' Rupiah\n'
                    "Uang Tunai: " + str(cash) + " Rupiah\n"
                    "Kembalian: " + str(change) + " Rupiah\n"
                    "***********************************************"
                )
            else:
                hasil = (
                    "********************* Tagihan *********************\n"
                    "Tanggal: " + current_date + '   ' + buyer + "\n"
                    "=============================\n"
                    "Makanan: " + file_content_food +  "\n"
                    "Minuman: " + file_content_drink + "\n"
                    "----------------------------------------------\n"
                    "Subtotal: " + str(total) + " Rupiah\n"
                    'Pajak: ' + str(tax) + ' Rupiah\n'
                    'Total: ' + str(totalbills) + ' Rupiah\n'
                    "Uang Tunai: " + str(cash) + " Rupiah\n"
                    "Kembalian: " + str(change) + " Rupiah\n"
                    "***********************************************"
                )
            with open('history.txt', 'a') as file:
                file.write('\n' + hasil)
            with open('food.txt', 'w') as file:
                file.write('')
            with open('drink.txt', 'w') as file:
                file.write('')
            
            with open('profit.txt', 'r') as file:
                total_history = file.read()
                total_history = int(total_history)
                total_history += total

            with open('profit.txt', 'w') as file:
                file.write(str(total_history))

            QMessageBox.information(main_win, 'Berhasil', hasil)
            app.quit()
        else:
            QMessageBox.information(main_win, 'Error', 'Uang tunai tidak mencukupi!')

# Connect buttons to their respective functions
button.clicked.connect(pesan)
button2.clicked.connect(bayar)

# Display the main window and start the application event loop
main_win.show()
app.exec_()
