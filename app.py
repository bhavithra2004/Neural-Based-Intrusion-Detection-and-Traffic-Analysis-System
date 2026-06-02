from flask import Flask, render_template, flash, request, session, send_file,url_for, request
import sys

import pickle

import numpy as np

import mysql.connector

app = Flask(__name__)
app.config['DEBUG']
app.config['SECRET_KEY'] = '789546321452145a'

@app.route("/")
def home():
    return render_template('index.html')
@app.route("/adminlogin")

@app.route("/adminlogin")
def adminlogin():
    return render_template('Adminlogin.html')

@app.route("/ADMINLOGIN", methods=['GET', 'POST'])
def ADMINLOGIN():
    if request.method == 'POST':
        if request.form['username'] == 'admin' and request.form['password'] == 'admin':
            conn = mysql.connector.connect(user='root', password='', host='localhost', database='1intrusionandmalwareimagedb')
            cur = conn.cursor()
            cur.execute("SELECT * FROM regtb ")
            data = cur.fetchall()
            flash("Your are Logged In...!")
            return render_template('AdminHome.html',data=data)
        else:
            flash("Username or Password is wrong")
            return render_template('Adminlogin.html')

@app.route("/userlogin")
def userlogin():
    return render_template('Userlogin.html')

@app.route("/USERLOGIN", methods=['GET', 'POST'])
def USERLOGIN():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        session['username'] = request.form['username']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1intrusionandmalwareimagedb')
        cursor = conn.cursor()
        cursor.execute("SELECT * from regtb where UserName='" + username + "' and Password='" + password + "'")
        data = cursor.fetchone()
        if data is None:
            flash("Username or Password is wrong...!")
            return render_template('UserLogin.html')
        else:
            session['email'] = data[3]
            conn = mysql.connector.connect(user='root', password='', host='localhost', database='1intrusionandmalwareimagedb')
            cur = conn.cursor()
            cur.execute("SELECT * FROM regtb where UserName='" + username + "' and Password='" + password + "'")

            data = cur.fetchall()
            flash("Your are Logged In...!")
            return render_template('UserHome.html',data=data)



@app.route("/newuser")
def newuser():
    return render_template('NewUser.html')

@app.route("/NEWUSER", methods=['GET', 'POST'])
def NEWUSER():
    if request.method == 'POST':
        name = request.form['name']
        mobile = request.form['mobile']
        email = request.form['email']
        address = request.form['address']
        username = request.form['username']
        password = request.form['Password']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='1intrusionandmalwareimagedb')
        cursor = conn.cursor()
        cursor.execute("SELECT * from regtb where UserName='" + username + "' and Password='" + password + "'")
        data = cursor.fetchone()
        if data is None:
            conn = mysql.connector.connect(user='root', password='', host='localhost',
                                           database='1intrusionandmalwareimagedb')
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO regtb VALUES ('','" + name + "','" + mobile + "','" + email + "','" + address + "','" + username + "','" + password + "')")
            conn.commit()
            conn.close()
            flash('New User register successfully')
            return render_template('Userlogin.html')
        else:
            flash('Already registered')
            return render_template('NewUser.html')



@app.route("/UserHome")

def UserHome():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1intrusionandmalwareimagedb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM regtb")
    data = cur.fetchall()
    return render_template('UserHome.html', data=data)



@app.route("/AdminHome")
def AdminHome():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1intrusionandmalwareimagedb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM regtb")
    data = cur.fetchall()
    return render_template('AdminHome.html', data=data)



@app.route("/predict")
def predict():
    return render_template('home.html')


@app.route("/result", methods=['GET', 'POST'])
def result():
    if request.method == 'POST':
        import tensorflow as tf
        import numpy as np

        t1 = request.form['t1']
        t2 = request.form['t2']
        t22 = request.form['t22']
        t23 = request.form['t23']
        t24 = request.form['t24']
        t25 = request.form['t25']
        t26 = request.form['t26']
        t27 = request.form['t27']
        t28 = request.form['t28']
        t29 = request.form['t29']
        t210 = request.form['t210']
        t211 = request.form['t211']
        t212 = request.form['t213']
        t213 = request.form['t213']
        t214 = request.form['t214']
        t215 = request.form['t215']
        t216 = request.form['t216']
        t217 = request.form['t217']
        t218 = request.form['t218']
        t219 = request.form['t219']
        t220 = request.form['t220']
        t221 = request.form['t221']
        t222 = request.form['t222']
        t223 = request.form['t223']
        t224 = request.form['t224']
        t225 = request.form['t225']
        t226 = request.form['t226']
        t227 = request.form['t227']
        t228 = request.form['t228']
        t229 = request.form['t229']
        t230 = request.form['t230']
        t231 = request.form['t231']
        t232 = request.form['t232']
        t233 = request.form['t233']
        t234 = request.form['t234']
        t235 = request.form['t235']
        t236 = request.form['t236']
        t237 = request.form['t237']

        t1 = float(t1)
        t2 = float(t2)
        t22 = float(t22)
        t23 = float(t23)
        t24 = float(t24)
        t25 = float(t25)
        t26 = float(t26)
        t27 = float(t27)
        t28 = float(t28)
        t29 = float(t29)
        t210 = float(t210)
        t211 = float(t211)
        t212 = float(t213)
        t213 = float(t213)
        t214 = float(t214)
        t215 = float(t215)
        t216 = float(t216)
        t217 = float(t217)
        t218 = float(t218)
        t219 = float(t219)
        t220 = float(t220)
        t221 = float(t221)
        t222 = float(t222)
        t223 = float(t223)
        t224 = float(t224)
        t225 = float(t225)
        t226 = float(t226)
        t227 = float(t227)
        t228 = float(t228)
        t229 = float(t229)
        t230 = float(t230)
        t231 = float(t231)
        t232 = float(t232)
        t233 = float(t233)
        t234 = float(t234)
        t235 = float(t235)
        t236 = float(t236)
        t237 = float(t237)

        model = tf.keras.models.load_model('model.h5')
        data = np.array([[t1, t2, t22, t23, t24, t25, t26, t27, t28, t29, t210,
                          t211,
                          t212,
                          t213,
                          t214,
                          t215,
                          t216,
                          t217,
                          t218,
                          t219,
                          t220,
                          t221, t222, t223, t224, t225, t226, t227, t228, t229, t230,
                          t231, t232, t233, t234, t235, t236, t237
                          ]])

        my_prediction1 = model.predict(data, batch_size=64)

        my_prediction = np.argmax(my_prediction1)
        print(my_prediction)

        print(my_prediction)
        Answer = ''

        if my_prediction == 0:
            Answer = 'back'

        elif my_prediction == 1:
            Answer = 'ftp_write'
        elif my_prediction == 2:
            Answer = 'R2L'
        elif my_prediction == 3:
            Answer = 'smurf'
        elif my_prediction == 4:
            Answer = 'normal'
        elif my_prediction == 5:
            Answer = 'multihop'
        elif my_prediction == 6:
            Answer = 'probing'
        elif my_prediction == 7:
            Answer = 'Accident'
        sendmail(session['email'],"Predicted Info-"+Answer)
        return render_template('home.html', res=Answer)


@app.route("/ImagePredict")
def ImagePredict():
    return render_template('ImagePredict.html')


@app.route("/imagepredict", methods=['GET', 'POST'])
def imagepredict():
    if request.method == 'POST':

        import tensorflow as tf
        import numpy as np
        import cv2
        import os

        # Load trained model
        model = tf.keras.models.load_model('malwaremodel.h5')

        # Get uploaded file
        file = request.files['file']

        # Save file
        filepath = os.path.join("static/upload", file.filename)
        file.save(filepath)

        # Read image using OpenCV
        img = cv2.imread(filepath)

        # Resize to match training size
        img = cv2.resize(img, (200, 200))

        # Normalize (same as training rescale=1/255)
        img = img / 255.0

        # Convert to numpy array
        img = np.array(img)

        # Expand dimensions (1, 200, 200, 3)
        img = np.expand_dims(img, axis=0)

        # Prediction
        prediction = model.predict(img)
        ind = np.argmax(prediction)

        classes = [
            "Adposhel","Agent","BrowseFox","Dinwod","Elex",
            "Fakerean","Hlux","Injector","Neshta","Stantinko"
        ]

        result = classes[ind]
        sendmail(session['email'], "Predicted Info-" + result)
        confidence = round(np.max(prediction) * 100, 2)

        return render_template("ImagePredict.html",
                               res=result,
                               conf=confidence,
                               img_path=filepath)



def sendmail(Mailid, message):
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders

    fromaddr = "projectmailm@gmail.com"
    toaddr = Mailid

    # instance of MIMEMultipart
    msg = MIMEMultipart()

    # storing the senders email address
    msg['From'] = fromaddr

    # storing the receivers email address
    msg['To'] = toaddr

    # storing the subject
    msg['Subject'] = "Alert"

    # string to store the body of the mail
    body = message

    # attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))

    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login(fromaddr, "tdyr kebi hnyr yzyh")

    # Converts the Multipart msg into a string
    text = msg.as_string()

    # sending the mail
    s.sendmail(fromaddr, toaddr, text)

    # terminating the session
    s.quit()



if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
