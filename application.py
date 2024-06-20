from flask import Flask
FAI=Flask(__name__)
@FAI.route('/errorhari')
def errorhari():
    return 'Errorhari Is Best'
FAI.run (debug=True)
