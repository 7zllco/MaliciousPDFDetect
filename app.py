from flask import Flask,  render_template, request, session
#from werkzeug.utils import secure_filename
import os
app = Flask(__name__)
app.secret_key = "super secret key"
currentPath=os.getcwd()
app.config['UPLOAD_FOLDER'] = currentPath+'\\templates\\uploads'

def output():
    list_file = open('a.txt', 'r').read().split('\n')
    malicious_list=[]
    benign_list=[]
    for file in list_file:
        if (file.split(' ')[2]=="M"):
            malicious_list.append(file.split(' ')[0])
        else:
            benign_list.append(file.split(' ')[0])
    return(malicious_list,benign_list)


@app.route('/',methods=['GET'])
def a():
    if request.method=="GET":
        value=1
        return render_template('jsonTest.html',value=value)


@app.route('/upload')
def uploadfile():
    return render_template('upload.html')


@app.route('/uploader', methods=['POST'])
def uploader_file():
    if request.method=='POST':
        upload = request.files.getlist("file[]")
        for f in upload:
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))
        malicious,benign=output()
        return render_template('result.html',benign=benign,malicious=malicious)
        #test=True
        #if (test==False):
        #    return render_template('success.html')
        #else:
        #    return render_template('result.html',benign=benign,malicious=malicious)
            #return render_template('jsonTest.html',malicious=malicious)
        #return 'file uploaded successfully'
        #return render_template('malicious.html')

if __name__ == '__main__':
    app.debug = True
    app.run()