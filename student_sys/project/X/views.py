from django.shortcuts import render
from . import mysql

# Create your views here.
'''
the essence of develop software :

IN===>> python code ===>>OUT (show Model is .html)
'''

# start here + login , or signin
def start(request):
	return render(request,'start.html',{'flag':1})

# to login page, show student sys main page
def login(request):
	id=int(request.GET['id'])
	passwd=request.GET['passwd']

	res=mysql.mysql('signin1',id)
	if len(res)==1: # id exists
		res2=mysql.mysql('login',id,passwd)
		if len(res2)==1: # id + passwd all right
			return render(request,'login_ok.html',{'id':id,'passwd':passwd})	
		else:  # passwd not right
			return render(request,'start.html',{'flag':0})
	elif len(res)==0: # id not exists
		return render(request,'to_signin.html',)
	
# to signin page
def signin(request):	
	return render(request,'signin.html')
# sign ok page
def signin_ok(request):	
	id=int(request.GET['id'])
	passwd=request.GET['passwd']
	
	res=mysql.mysql('signin1',id)
	print(res)
	if len(res)==1: # id already exists
		return render(request,'signin_fail.html',{'id':id})
	elif len(res)==0:
		mysql.mysql('signin2',id,'test',passwd)
		return render(request,'signin_ok.html',{'id':id,'passwd':passwd})

def search(request):
	pass
	res=mysql.mysql('search')
	total=len(res)
	
	return render(request,'search.html',{ 'res':res,'total':total})
	
def student(request):
	id=int(request.GET['id'])
	try:
		flag=request.GET['flag']
	except:
		flag=''
	res=mysql.mysql('student',id)		
	return render(request,'student.html',{'res':res,'flag':flag})

def score(request):
	pass
	id=int(request.GET['id'])
	res=mysql.mysql('score',id)
	print(res)
	return render(request,'score.html',{'res':res })