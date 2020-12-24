from flask import Flask, render_template,send_file

APK = 'apk/'

app = Flask(__name__)
app.config['APK'] = APK

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/sample1')
def sample1 ():
    path = APK + sample1
    return send_file(path, as_attachment=True)

@app.route('/sample2')
def sample2 ():
    path = APK + sample2
    return send_file(path, as_attachment=True)

if __name__ == '__main__':
    app.run()

