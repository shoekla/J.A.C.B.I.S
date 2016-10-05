import sys
import os
import Config
#import SPT
if sys.version_info < (3, 0):
    # Python 2
    import Tkinter as tk
else:
    # Python 3
    import tkinter as tk



"""root = tk.Tk()
root.title("J.A.C.B.I.S")
tk.Button(root, text="Activate J.A.C.B.I.S",command=SPT.convo).pack()

tk.mainloop()"""
#SPT.convo()
from datetime import datetime
"""
date_object = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')
print str(date_object)
print str(datetime.now())
"""
def getDate(user):
	user = user.lower()
	us = user.split(" ")
	now = str(datetime.now())
	res = now[:now.find(" ")].split("-")
	#print res
	#print now
	arr = user.split(" ")
	for i in arr:
		if "jan" in user:
			if int(res[1]) > 1:
				year = int(res[0])
				res[0] = str(year+1)	
			res[1] = '01'
		elif "feb" in user:
			if int(res[1]) > 2:
				year = int(res[0])
				res[0] = str(year+1)
			res[1] = '02'
		elif "mar" in user:
			if int(res[1]) > 3:
				year = int(res[0])
				res[0] = str(year+1)
			res[1] = '03'
		elif "april" in user:
			if int(res[1]) > 4:
				year = int(res[0])
				res[0] = str(year+1)
			res[1] = '04'
		elif "may" in user:
			if int(res[1]) > 5:
				year = int(res[0])
				res[0] = str(year+1)
			res[1] = '05'
		elif "jun" in user:
			if int(res[1]) > 6:
				year = int(res[0])
				res[0] = str(year+1)
			res[1] = '06'
		elif "jul" in user:
			if int(res[1]) > 7:
				year = int(res[0])
				res[0] = str(year+1)
			res[1] = '07'
		elif "aug" in user:
			if int(res[1]) > 8:
				year = int(res[0])
				res[0] = str(year+1)
			res[1] = '08'
		elif "sept" in user:
			if int(res[1]) > 9:
				year = int(res[0])
				res[0] = str(year+1)
			res[1] = '09'
		elif "oct" in user:
			if int(res[1]) > 10:
				year = int(res[0])
				res[0] = str(year+1)
			res[1] = '10'
		elif "nov" in user:
			if int(res[1]) > 11:
				year = int(res[0])
				res[0] = str(year+1)
			res[1] = '11'
		elif "dec" in user:
			if int(res[1]) > 12:
				year = int(res[0])
				res[0] = str(year+1)
			res[1] = '12'
		if "tommorow":
			res[2] = str(int(res[2])+1)
	for i in range(0,len(us)):
		if "next" in us[i] and i < len(user):
			if "week" in us[i+1]:
				res[2] = str(int(res[2])+7)
			elif "year" in us[i+1]:
				res[0] = str(int(res[0])+1)
			else:
				res[0] = str(int(res[0])+1)
	if int(res[2]) > 30 and (res[1] != '01' or res[1] != '03' or res[1] != '05' or res[1] != '07' or  res[1] != '08' or res[1] != '10' or res[1] != '12'):
		res[2] = str(int(res[2]) -30)
		res[1] = str(int(res[1])+1)
	if int(res[2]) > 31:
		if res[1] != '01' or res[1] != '03' or res[1] != '05' or res[1] != '07' or  res[1] != '08' or res[1] != '10' or res[1] != '12':
			res[2] = str(int(res[2]) -30)
			res[1] = str(int(res[1])+1)
		elif res[1] == '02' and int(res[0])%4 != 0:
			res[2] = str(int(res[2]) -28)
			res[1] = str(int(res[1])+1)
		elif res[1] == '02' and int(res[0])%4 == 0:
			res[2] = str(int(res[2]) -29)
			res[1] = str(int(res[1])+1)
		else:
			res[2] = str(int(res[2]) -31)
			res[1] = str(int(res[1])+1)
	if res[1] == '02' and res[2] == '29':
		if int(res[0])%4 != 0:
			res[2] = str(int(res[2]) -28)
			res[1] = str(int(res[1])+1)
	if int(res[1]) > 12:
		res[1] = str(int(res[1]) -12)
		res[0] = str(int(res[0])+1)


	return str(res)




print getDate("next october")

