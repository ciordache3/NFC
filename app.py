from flask import Flask, render_template, redirect, request

app=Flask(__name__)
app.secret_key="1234"

@app.route('/')
def login():
    if request.method == 'POST':
        ans1 = request.form['ans1']
        ans2 = request.form['ans2']
        ans3 = request.form['ans3']
        ans4 = request.form['ans4']

        print(ans1)
    
    return render_template('page.html')

app.run(debug="True",host="0.0.0.0", port=3000)
