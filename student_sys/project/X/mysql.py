'''
 mysql DB 
'''

# *args[]= procedureName + IN , write different SQL by dirrerent procedureName.
def mysql(*args): 
	import  cymysql
	con=cymysql.connect(host='localhost',passwd='root',db='yx',user='root')
	cur=con.cursor()

	# call procedure 
	if args[0]=='signin1':
		procedure_= "(%d)" % (args[1],) 

	if args[0]=='signin2':    #### '%s' must add the '' around %s
		procedure_= "(%d,'%s','%s')" % (args[1],args[2],args[3],) 		

	if args[0]=='login':  
		procedure_= "(%d,'%s')" % (args[1],args[2],) 		

	if args[0]=='search':  #get all student id , name
		procedure_= "()" 

	if args[0]=='student': 
		procedure_= "(%d)" % (args[1],)

	if args[0]=='score': 
		procedure_= "(%d)" % (args[1],)

	if args[0]=='delete_': 
		procedure_= "(%d)" % (args[1],)

	if args[0]=='id_check': 
		procedure_= "()" 		

	if args[0]=='insert_':  # id , name, sex, passwd, address
		procedure_= "(%d,'%s',%d,'%s','%s')" % (args[1],args[2],args[3],args[4],args[5],)		

	if args[0]=='update_': 
		procedure_= "(%d,'%s',%d,'%s','%s')" % (args[1],args[2],args[3],args[4],args[5],)

	procedure="call " + args[0] + procedure_
	cur.execute(procedure)

	# return res
	res=cur.fetchall()
	# commit SQL
	# close connection
	con.commit()
	cur.close()
	con.close()
	return res