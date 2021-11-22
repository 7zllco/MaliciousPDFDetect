from flask import Flask, request,abort,jsonify
app = Flask(__name__)

@app.errorhandler(500)
def error500(error):
    return jsonify({
        'success':False,
        'message': error.description,
        'status':500
    })

@app.route('/')
def hello_pybo():
    return 'Hello, Pybo!'

@app.route('/upload')
def upload_file():
    if request.method=='POST':
        try:
            file_name=request.form['pdf_name']
            f=request.files['pdf']
        except:
            abort(500,"something wrong")
