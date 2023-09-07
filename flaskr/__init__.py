#import aplikasi flask untuk di pakai di web
from flask import Flask
#mengatur nama aplikasi
app = Flask(__name__)
#mengatur uri (universal resource identifier), dan apa yang ditampilkan jika uri tersebut diakses 
@app.route('/')#ketika alamat http://127.0.0.1:5000/ dipanggil, maka server akan mengeksekusi fungsi hello() 
def hello(): #function dengan nama hello
    return 'HELLO, WORLD!'

#mengatur URI ke http://127.0.0.1:5000/login, dan mengeksekusi fungsi lokal() jika diakses di alamat URI http://127.0.0.1:5000/login
@app.route("/login")
def login():
    return 'halaman login'