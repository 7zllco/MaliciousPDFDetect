from flask import Flask,  render_template, request, session

import os
app = Flask(__name__)
app.secret_key = "super secret key"
currentPath=os.getcwd()

#pdf의 파일을 받아온 뒤, 업로드 되는 경로 설정
app.config['UPLOAD_FOLDER'] = currentPath+'/templates/uploads'

#머신러닝을 통해 나온 텍스트파일을 malicious, benign으로 분리해서 pdf 이름 저장
#malicious, benign 리스트 리턴
def output():
    list_file = open('output/out.txt', 'r').read().split('\n')
    list_file=list_file[:-1]
    malicious_list=[]
    benign_list=[]
    for file in list_file:
        if (file.split(' ')[2]=="Malicious"):
            malicious_list.append(file.split(' ')[0])
        else:
            benign_list.append(file.split(' ')[0])
    return(malicious_list,benign_list)

#사용자가 pdf 파일 업로드
@app.route('/upload')
def uploadfile():
    return render_template('upload.html')

#pdf 파싱 결과 리턴
@app.route('/uploader', methods=['POST'])
def uploader_file():
    if request.method=='POST':
        upload = request.files.getlist("file[]")
        for f in upload:
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))
        os.system("sh output/code.sh")
        malicious,benign=output()
        return render_template('result.html',benign=benign,malicious=malicious)
        
if __name__ == '__main__':
    app.debug = True
    app.run()