'''
select delete update insert  Student Info System
'''

# need mysql DB + PROCEDURE SQL

class Student:
	studentNumber=0
	name=''
	grade=0
	def __init__(self,studentnumber,name,grade):
		self.studentNumber=studentnumber
		self.name=name
		self.grade=grade

def mysql(flag,*args):
	import cymysql
	con=cymysql.connect(host='localhost',passwd='root',db='yx',user='root')
	cur=con.cursor()
	try:		
		if flag=='select': #
			cur.execute("call selectStudent('%s')" % (args[0],))
			res=cur.fetchall()
		elif flag=='delete':
			cur.execute("call deleteStudent('%s')" % (args[0],))
			res='*delete ok*'
		elif flag=='update':
			cur.execute("call updateStudent('%s')" % (args[0],))
			res='*update ok*'
		elif flag=='insert':
			cur.execute("call insertStudent(%d,'%s',%d)" % (args[0],args[1],args[2]))
			res='*insert ok*'
	except:
		print('**ERROR HAPPEN**')
	finally:
		cur.close()
		con.commit()
		con.close()
	return res
	
def select():
	name=number=None
	selectmessage=input('choose one:\n1=>name \n2=>studentNumber\n\n')
	if selectmessage=='1':
		name=input("put the student's name:\n\n")

	elif selectmessage=='2':
		number=input("put the student's number:")
	else:
		('please choose one above.')
	if name!=None:
		nameORnumber=name+'0' #replace flag2
		#flag2=0 #flag2 for select by name or number4
	else:
		nameORnumber=number+'1'
		#flag2=1
	res=mysql('select',nameORnumber) #in->sql->out
	print("\nthe student'info here:")
	for x in res:
		print("**********************\n["+'number->'+str(x[0])+"][name->"+x[1]+"]"+"\n**********************")
		
	nextoperation=input('\n\nFINISHED!!\ndo u want another operation?([y/n])')
	if nextoperation=='y':
		start()
	else:
		print('Byebye.')

def insert():
	number=input('put the studentnumber:\n')
	name=input('put the name:\n')
	res=mysql('insert',int(number),name,1)
	print(res)

def delete():
	name=input('put the name:')
	res=mysql('delete',name)
	print(res)




def update():
	name=input()

	







def start():
	operation=input('choose one[enter number]:\n1=>insert\n2=>delete\n3=>update\n4=>select\n\n')

	if operation=='1':#insert
		insert()
	elif operation=='2':#delete
		delete()
	elif operation=='3':#update
		update()
	elif operation=='4':#select
		select()

#ENTRY  HERE:
print('*************************\n*Welcome to student info*\n*************************\n')
start()











