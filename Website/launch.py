from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for
from random import randint
import time
import fire
from firebase import firebase
import os
app = Flask(__name__)

@app.route('/JACBIS/')
def my_fosdvfavvvvxsxcxzcHdrm(arr=[], l = 0, numP = None,randL = 0):
	numP = ""
	print "f"
	numP = fire.getResp('NumOfPhrases')
	print "w"
	l = 0
	randL = fire.getRandLen()
	print "s"
	arr = [];
	arr = fire.getMe()
	print "t"
	l = len(arr)
	if len(arr) > 7:
		arr = arr[len(arr)-7:len(arr)]
	print "wtf"
	return render_template("JACBIS/home.html",arr=arr,l=l,numP = numP,randL=randL)

@app.route('/JACBIS/',methods=['POST'])
def my_fosasdasdaadvfavvvvxConvYo(arr=[], l = 0, numP = None,text = None,randL = 0):
	print "Hello"
	text = ""
	numP = ""
	randL = fire.getRandLen()
	numP = fire.getResp('NumOfPhrases')
	l = 0
	arr = [];
	
	print "YOHello"
	text = request.form['userText']
	print text
	print "Bro"
	fire.addToConvYou(text)
	print "done"
	arr = fire.getMe()
	if len(arr) > 7:
		arr = arr[len(arr)-7:len(arr)]
	l = len(arr)
	return render_template("JACBIS/home.html",arr=arr,l=l,numP = numP,randL = randL)


@app.route('/JACBIS/addPhraseToArtMenu/')
def addPhraseToArtMenu(numP = None,randL = 0):
	numP =""
	randL = fire.getRandLen()
	numP = fire.getResp('NumOfPhrases')
	return render_template("JACBIS/addPhraseMenu.html",numP = numP,randL = randL)



@app.route('/JACBIS/addPhraseToArtMenu/',methods=['POST'])
def  putInFireBro(phrase =None, resp = None, how = None,message = None, color = None, numP = None,randL = 0):
	numP =""
	randL = fire.getRandLen()
	print "YO)OOOOOOOOOOO"
	message = ""
	phrase = ""
	color = ""
	resp = ""
	how = ""
	phrase = request.form['phrase']
	resp = request.form['response']
	how = "Contain"
	print "2"
	resp = resp.lower()
	resp = resp.replace("(","")
	resp = resp.replace(")","")
	print "3"
	numP = fire.getResp('NumOfPhrases')
	message = "Congrats your response is 1 of "+str(fire.putInFirebase(phrase,resp))+" for this phrase!"
	color = "green"
	print "4"
	return render_template("JACBIS/addPhraseMenu.html",message=message,color =color,numP = numP,randL = randL)


@app.route('/JACBIS/Link/',methods=['POST'])
def putInFireBroPython(phrase =None, resp = None, how = None,message = None, color = None, numP = None,randL = 0):
	numP =""
	randL = fire.getRandLen()
	print "YO)OOOOOOOOOOO"
	message = ""
	phrase = ""
	color = ""
	resp = ""
	how = ""
	print "0000"
	phrase = request.form['phrase']
	print "1"
	resp = request.form['response']
	how = "Contain"
	print "2"
	print "3"
	resp = "r"+resp
	numP = fire.getResp('NumOfPhrases')
	message = "Congrats your response is 1 of "+str(fire.putInFirebasePython(phrase,resp))+" for this phrase!"
	color = "green"
	print "4"
	return render_template("JACBIS/addPhraseMenu.html",message=message,color =color,numP = numP,randL = randL)


@app.route('/JACBIS/addLink/')
def goToLinkMenu(numP = None, randL = 0):
	numP = ""
	randL = fire.getRandLen()
	numP = fire.getResp('NumOfPhrases')
	return render_template("JACBIS/python.html",numP = numP,randL = randL)

@app.route('/JACBIS/addRand/',methods=['POST'])
def aRandList(numP = None,randL = 0,color=None,message =None):
	print "1"
	numP = ""
	numP = fire.getResp('NumOfPhrases')
	print "2"
	message = ""
	color = ""
	color = request.form['rand']
	color = fire.addToRand(color)
	if color == 'green':
		message = 'You did it!'
	else:
		message = 'phrase is already in the system'
	randL = fire.getRandLen()
	print "3"
	return render_template("JACBIS/randMenu.html",numP=numP,randL = randL,color = color, message = message)



@app.route('/JACBIS/addRand/')
def aRandsdfsList(numP = None,randL = 0):
	numP = ""
	numP = fire.getResp('NumOfPhrases')
	randL = fire.getRandLen()
	return render_template("JACBIS/randMenu.html", numP = numP, randL = randL)
"""
firebase = firebase.FirebaseApplication('https://firstappabir.firebaseio.com/', None)
result = firebase.get('s', None)
print result
"""


if __name__ == '__main__':
    app.run()








