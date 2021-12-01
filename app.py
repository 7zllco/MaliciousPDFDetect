from flask import Flask,  render_template, request, session
#from werkzeug.utils import secure_filename
import os
app = Flask(__name__)
app.secret_key = "super secret key"
currentPath=os.getcwd()
app.config['UPLOAD_FOLDER'] = currentPath+'\\templates\\uploads'



@app.route('/upload')
def uploadfile():
    return render_template('upload.html')


@app.route('/uploader', methods=['POST'])
def uploader_file():
    if request.method=='POST':
        upload = request.files.getlist("file[]")
        for f in upload:
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))
        test=True
        if (test==False):
            return render_template('success.html')
        else:
            return render_template('success.html')
        #return 'file uploaded successfully'
        #return render_template('malicious.html')

if __name__ == '__main__':
    app.debug = True
    app.run()