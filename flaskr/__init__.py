#import aplikasi flask , os, flash, jsonify, redirect, dan render_template untuk dipakai di web kita
import os 
#import SQL untuk akses database
from cs50 import SQL
#import flash untuk notifikasi pada web
#import jsonify untuk mengformat data
#import redirect dan render_template untuk berpidah halaman web
#import request dan session untuk mengakses data
from flask import Flask, flash , jsonify, redirect, render_template, request, session
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