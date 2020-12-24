from flask import Flask, render_template,send_file

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/download')
def download ():
    path = "C:/Users/Dell/PycharmProject/Virtual-RealTime-Model/apk/vrm.apk"
    return send_file(path, as_attachment=True)

@app.route('/sample1')
def sample1 ():
    path = "C:/Users/Dell/PycharmProject/Virtual-RealTime-Model/apk/sample1.png"
    return send_file(path, as_attachment=True)

@app.route('/sample2')
def sample2 ():
    path = "C:/Users/Dell/PycharmProject/Virtual-RealTime-Model/apk/sample2.png"
    return send_file(path, as_attachment=True)

if __name__ == '__main__':
    app.run()

