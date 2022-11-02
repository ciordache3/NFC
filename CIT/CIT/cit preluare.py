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
app.secret_key="12345"






@app.route('/CIT')
def SAFT():    
	return render_template('CIT.html')
@app.route('/CIT', methods=['POST', 'GET'])
def cit_process():
    if request.method=="POST":
        q1=request.form['selectq1']
        print(q1)
        if(q1=="yes"):
            q11=request.form.get('selectq1.1')
            print(q11)
            if(q11=="yes"):
                q12=request.form.get('selectq1.2')
                if(q12=="yes"):
                    q12n=request.form.get('selectq1.2Yes')

            else:
                q11n=request.form.get('q1.1No')
                print(q11n)
        q2=request.form['selectq2']
        if(q2=="yes"):
            q21=request.form['selectq2.1']
            if(q21=="no"):
                q21n=request.form['selectq2.1No']
        q3=request.form['selectq3']
        if(q3=="yes"):
            q3n=request.form['q31yes']
        q4=request.form['selectq4']
        if(q4=="yes"):
            q4n=request.form['q41yes']
        q5=request.form['selectq5']
        if(q5=="yes"):
            q5n=request.form['q51yes']
        q6=request.form['selectq6']
        if(q6=="yes"):
            q61=request.form['q61']
            if(q61=="yes"):
                q61n=request.form['q61yes']
        selectq7=request.form['selectq7']
        if(selectq7=="yes"):
            selectq71=request.form['selectq7.1']
            if(selectq71=="yes"):
                inputq71=request.form['inputq71']
                selectq72=request.form['selectq7.2']
                if(selectq72=="yes"):
                    inputq72=request.form['inputq72']
                    selectq73=request.form['selectq7.3']
                    if(selectq73=="yes"):
                        inputq73=request.form['inputq73']
        selectq8=request.form['selectq8']        
        if(selectq8=="yes"):
            selectq81=request.form['selectq81']
            if(selectq81=="yes"):
                selectq81n=request.form['inputq81']        
        q10=request.form['selectq10']
        if(q10=="yes"):
            q10n=request.form['q10yes']
        selectq11=request.form['selectq11']
        if(selectq11=="yes"):
            selectq11n=request.form['q11yes']
        selectq12=request.form['selectq12']
        if(selectq12=="no"):
            selectq121=request.form['selectq12.1']
            if(selectq121=="yes"):
                selectq12n=request.form['selectq12yes']
        selectq13=request.form['selectq13']
        if(selectq13=="yes"):
            selectq13n=request.form['inputq13']                
        selectq14=request.form['selectq14']
        if(selectq14=="yes"):
            selectq14n=request.form['inputq14']
        selectq15=request.form['selectq15']
        if(selectq15=="yes"):
            selectq15n=request.form['inputq15']
        selectq16=request.form['selectq16']
        if(selectq16=="yes"):
            selectq16n=request.form['inputq16'] 
        selectq17=request.form['selectq17']
        if(selectq17=="no"):
            selectq17n=request.form['inputq17']
        else:
            selectq171=request.form['selectq17Yes']
            if(selectq171=="yes"):
                selectq171n=request.form['inputq171']    
        selectq18=request.form['selectq18']
        if(selectq18=="yes"):
            selectq18n=request.form['inputq18']
        selectq19=request.form['selectq19']
        if(selectq19=="yes"):
            selectq19n=request.form['inputq19']
        selectq20=request.form['selectq20']
        if(selectq20=="yes"):
            selectq20n=request.form['inputq21']
        selectq21=request.form['selectq21']
        if(selectq21=="yes"):
            selectq21n=request.form['inputq21']
        selectq23=request.form['selectq23']            
        if(selectq23=="yes"):
            selectq231=request.form['selectq231']
            if(selectq231=="yes"):
                selectq231n=request.form['inputq23']
        selectq24=request.form['selectq24']
        if(selectq24=="yes"):
            selectq241=request.form['selectq241']
            if(selectq241=="yes"):
                selectq241n=request.form['inputq241']                
        selectq25=request.form['selectq25']
        if(selectq25=="yes"):
            selectq251=request.form['selectq251']
        selectq26=request.form['selectq26']
        if(selectq26=="yes"):
            selectq261=request.form['selectq261']            
        print(q2)
        selectq27=request.form['selectq27']
        if(selectq27=="yes"):
            selectq21n=request.form['inputq27']
        selectq28=request.form['selectq28']
        if(selectq28=="yes"):
            selectq28n=request.form['inputq28']
        selectq29=request.form['selectq29']
        if(selectq29=="yes"):
            selectq29n=request.form['inputq29']                        
        return render_template('CIT.html')
    

app.run(debug="True",host="0.0.0.0", port=3000)
