import warnings
warnings.filterwarnings('ignore')

from flask import Flask,render_template,url_for,request,redirect
app = Flask(__name__)
@app.route('/')
def host():
    return render_template('index.html')
@app.route('/pre',methods=['GET', 'POST'])
def pre():
    if request.method == 'POST':
        text = request.form['message']
        re = int(text)+1
    return render_template('index.html',url=re)
if __name__ == '__main__':
	app.run(debug=True)
