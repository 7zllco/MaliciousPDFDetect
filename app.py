from flask import Flask, flash, redirect, render_template, request, url_for, send_from_directory, session
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.secret_key = "super secret key"
currentPath=os.getcwd()
app.config['UPLOAD_FOLDER'] = currentPath+'\\templates\\uploads'

@app.route('/')
def a():
    return render_template('test.html')

@app.route('/upload')
def uploadfile():
    return render_template('upload.html')


@app.route('/uploader', methods=['GET', 'POST'])
def uploader_file():
    if request.method=='POST':
        upload = request.files.getlist("file[]")
        for f in upload:
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))
        
        return 'file uploaded successfully'
        #return render_template('success.html')

if __name__ == '__main__':
    app.debug = True
    app.run()