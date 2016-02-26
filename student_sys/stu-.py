'''
XXX stu sys
'''
# input-->python code-->print
def mysql(sql):
	import cymysql
	con=cymysql.connect(host='localhost',passwd='3306',db='yx',user='yx')
	cur=con.cursor()
	cur.execute(sql)
	res=cur.fetchall()
	con.commit()
	con.close()
	return res

def start():
	pass
	logORsign=input('****login[1] or signin[2]?****\n')
	if logORsign=='1':
		login()
	elif logORsign=='2':
		signin()
	else:
		start()
def login():
	pass
	id=input('id:\n')
	passwd=input('password:\n')
	id_=mysql("call a(%d,'%s')" % (int(id),passwd))
	if len(id_)==1:
		print('\nlogin OK..')
	elif len(id_)==0:
		print('\nyou have not signin..')

def signin():
	pass
	id=input('id:\n')
	name=input('name:\n')
	passwd=input('password:\n')
	id_=mysql("call b(%d)" % (int(id),))
	if len(id_)==1:
		print('\nid already exists')
	elif len(id_)==0:
		print('\nsignin OK..')
		mysql("call c(%d,'%s','%s')" % (int(id),name,passwd))


#start here:
print('******Welcome to stu sys******\n')
start()
