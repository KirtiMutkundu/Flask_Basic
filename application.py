from flask import Flask,render_template
FAI=Flask(__name__)
@FAI.route('/errorhari')
def errorhari():
    return 'Errorhari Is Best'

@FAI.route('/hai')
def hai():
    return render_template('hai.html',name='kirti',age=21)
FAI.run (debug=True,host='192.168.16.13',port=8000)
