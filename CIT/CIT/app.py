from flask import Flask, render_template, request, send_from_directory, after_this_request, flash, redirect, url_for
from datetime import datetime
from werkzeug.utils import secure_filename
import openpyxl
import tkinter
import shutil
import pandas as pd

from time import sleep
# import PIL
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from openpyxl.styles.borders import Border, Side
from openpyxl import Workbook
from openpyxl.cell import cell
from openpyxl.chart import LineChart, Reference
import xml.etree.ElementTree as ET
import smtplib
from os.path import exists
from openpyxl.descriptors import (
    String,
    Sequence,
    Integer,
    )
from openpyxl.descriptors.serialisable import Serialisable
from openpyxl.styles import Color, PatternFill, Font, Border
from openpyxl.styles import colors
from openpyxl.styles import Alignment, alignment
from tkinter import filedialog
from string import ascii_uppercase
import os


app=Flask(__name__)
app.secret_key="1234"






@app.route('/CIT')
def SAFT():

    
	return render_template('CIT.html')

@app.route('/Loading')
def loading():
   
    return render_template('loadingPage.html')
@app.route('/Feedback/')
def ageing():
    
    return render_template('Ageing.html')
@app.route('/Feedback/<ticketno>')
def ageing_procc(ticketno="T0005"):
    ticketno=ticketno
    # ticketno=request.args.get('ticketno')
    print(request.args.get('ticketno'))
    print(ticketno)
    
    return render_template('Ageing.html', value=ticketno)
 


@app.route('/Loading', methods=['POST', 'GET'])
def loading_proc():
    # print("DADCSD")

    ok=1
    path_to_file="D:\\Projects\\9. VAT-depunere si semnare\\Submitted\\D394_AFT_February_2022_42937074.xml"
    while ok==1:
        print("abc")
        if exists(path_to_file):
            print(exists(path_to_file))
            ok=0
            return redirect('/CIT')
        else:
            print(exists(path_to_file))
            ok=1
    render_template('loadingPage.html')

    print("a iesit")  



    

app.run(debug="True",host="0.0.0.0", port=3000)
