from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for
from random import randint
import time
import fireJA
from firebase import firebase
import os
app = Flask(__name__)

@app.route('/JACBIS/')
def my_fosdJACKIBISvfavvvvxsxcxzcHdrm(arr=[], l = 0, numP = None,randL = 0):
	numP = ""
	print "f"
	numP = fireJA.getResp('NumOfPhrases')
	print "w"
	l = 0
	randL = fireJA.getRandLen()
	print "s"
	arr = [];
	arr = fireJA.getMe()
	print "t"
	l = len(arr)
	if len(arr) > 7:
		arr = arr[len(arr)-7:len(arr)]
	print "wtf"
	return render_template("JACBIS/home.html",arr=arr,l=l,numP = numP,randL=randL)

@app.route('/JACBIS/',methods=['POST'])
def my_fosasdaSBJSKDsdaadvfavvvvxConvYo(arr=[], l = 0, numP = None,text = None,randL = 0):
	print "Hello"
	text = ""
	numP = ""
	randL = fireJA.getRandLen()
	numP = fireJA.getResp('NumOfPhrases')
	l = 0
	arr = [];
	
	print "YOHello"
	text = request.form['userText']
	print text
	print "Bro"
	fireJA.addToConvYou(text)
	print "done"
	arr = fireJA.getMe()
	if len(arr) > 7:
		arr = arr[len(arr)-7:len(arr)]
	l = len(arr)
	return render_template("JACBIS/home.html",arr=arr,l=l,numP = numP,randL = randL)


@app.route('/JACBIS/addPhraseToArtMenu/')
def addPhraseTfsdfoArtMenu(numP = None,randL = 0):
	numP =""
	randL = fireJA.getRandLen()
	numP = fireJA.getResp('NumOfPhrases')
	return render_template("JACBIS/addPhraseMenu.html",numP = numP,randL = randL)



@app.route('/JACBIS/addPhraseToArtMenu/',methods=['POST'])
def  putIsadfnfireJABro(phrase =None, resp = None, how = None,message = None, color = None, numP = None,randL = 0):
	numP =""
	randL = fireJA.getRandLen()
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
	numP = fireJA.getResp('NumOfPhrases')
	print "3.5"
	message = "Congrats your response is 1 of "+str(fireJA.putInFirebase(phrase,resp))+" for this phrase!"
	color = "green"
	print "4"
	return render_template("JACBIS/addPhraseMenu.html",message=message,color =color,numP = numP,randL = randL)


@app.route('/JACBIS/Link/',methods=['POST'])
def putInfireJasdfasdABroPython(phrase =None, resp = None, how = None,message = None, color = None, numP = None,randL = 0):
	numP =""
	randL = fireJA.getRandLen()
	print "YO)OOOOOOOOOOO"
	message = ""
	phrase = ""
	color = ""
	resp = ""
	how = ""
	print "0000"
	phrase = request.form['phrase']
	print "1"
	phrase = phrase.lower()
	phrase = phrase.strip()
	resp = request.form['response']
	how = "Contain"
	print "2"
	print "3"
	resp = "r"+resp
	numP = fireJA.getResp('NumOfPhrases')
	print "2"
	message = "Congrats your response is 1 of "+str(fireJA.putInFirebasePython(phrase,resp))+" for this phrase!"
	color = "green"
	print "4"
	return render_template("JACBIS/python.html",message=message,color =color,numP = numP,randL = randL)


@app.route('/JACBIS/addLink/')
def goToLasdfasdfasdfinkMenu(numP = None, randL = 0):
	numP = ""
	randL = fireJA.getRandLen()
	numP = fireJA.getResp('NumOfPhrases')
	return render_template("JACBIS/python.html",numP = numP,randL = randL)

@app.route('/JACBIS/addRand/',methods=['POST'])
def aRandasdfasdfList(numP = None,randL = 0,color=None,message =None):
	print "1"
	numP = ""
	numP = fireJA.getResp('NumOfPhrases')
	print "2"
	message = ""
	color = ""
	color = request.form['rand']
	color = fireJA.addToRand(color)
	if color == 'green':
		message = 'You did it!'
	else:
		message = 'phrase is already in the system'
	randL = fireJA.getRandLen()
	print "3"
	return render_template("JACBIS/randMenu.html",numP=numP,randL = randL,color = color, message = message)



@app.route('/JACBIS/addRand/')
def aRandsdsdfasdfasdffsList(numP = None,randL = 0):
	numP = ""
	numP = fireJA.getResp('NumOfPhrases')
	randL = fireJA.getRandLen()
	return render_template("JACBIS/randMenu.html", numP = numP, randL = randL)
"""
firebase = firebase.firebaseApplication('https://firstappabir.firebaseio.com/', None)
result = firebase.get('s', None)
print result
"""


if __name__ == '__main__':
    app.run()








