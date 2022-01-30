import cx_Oracle
from django.http import HttpResponse
from django.contrib import messages
#from .forms import UserRegisterForm
from django.shortcuts import render,redirect
# Create your views here.
def home(request):
	if request.method=='POST':
		dsn_tns = cx_Oracle.makedsn('Revanth', '1521', service_name='orcl') 
		conn = cx_Oracle.connect(user='c##rath', password='bigpika', dsn=dsn_tns) 
		c = conn.cursor()
		product={}
		for i in ['names','rollno','department','gender','course','mobile','email']:
			product[i] = request.POST.get(i)
		product['mobile']=int(product['mobile'])
		c.prepare('insert into login values(:names,:rollno,:department,:gender,:course,userid.nextval,:mobile,:email)')
		c.execute(None,product)
		conn.commit()	
		c.prepare('select userid from login where rollno=:rollno')
		c.execute(None,{'rollno':product['rollno']})
		userid=int
		for i in c:
			userid=i[0]	
		product={}
		for i in ['rollno','pass']:
			product[i] = request.POST.get(i)
		product['userx']=userid
		c.prepare('insert into userdetail values(:rollno,:userx,:pass)')
		c.execute(None,product)
		product={}
		for i in ['prozone','inkling','incognito','fuzzlebuzzle','gamoholix']:
			if request.POST.get(i) !=None:
				c.prepare('insert into eventdetail values(:userx,:event)')
				c.execute(None,{'userx':userid,'event':i})
		conn.commit()
		conn.close()
		return render(request,'infinity/home.html')
	else:	
		return render(request,'infinity/home.html')

def admin(request):
	if request.method=='POST':
		dsn_tns = cx_Oracle.makedsn('Revanth', '1521', service_name='orcl') 
		conn = cx_Oracle.connect(user='c##rath', password='bigpika', dsn=dsn_tns) 
		c = conn.cursor()
		d={}
		given=[]
		for i in ['userid','pass']:
			d[i]=request.POST.get(i)
		c.execute('select * from administrator')
		for i in c:
			for j in i:
				given.append(j)
		c.prepare('select * from userdetail where rollno=:rollno')
		c.execute(None,{'rollno':d['userid']})
		pas=str
		usr=int
		for i in c:
			usr=i[1]
			pas=i[2]
		if d['userid']==given[0] and d['pass']==given[1]:
			dsn_tns = cx_Oracle.makedsn('Revanth', '1521', service_name='orcl') 
			conn = cx_Oracle.connect(user='c##rath', password='bigpika', dsn=dsn_tns) 
			c = conn.cursor()
			c.execute('select distinct(event) from eventdetail')
			event=[]
			for i in c:
				event.append(i)
			c.execute('select L.Names,L.gender,L.rollno,L.department,L.course,L.mobile,L.email,L.userid,U.pass from login L join userdetail U on(L.rollno=U.rollno)')
			userdet=[]
			for i in c:
				userdet.append(i)
			c.execute('select * from eventdetail')
			eventdet=[]
			for i in c:
				eventdet.append(i)
			return render(request,'infinity/admin.html',{'event':event,'user':userdet,'eventdet':eventdet})
		elif pas==d['pass']:
			dsn_tns = cx_Oracle.makedsn('Revanth', '1521', service_name='orcl') 
			conn = cx_Oracle.connect(user='c##rath', password='bigpika', dsn=dsn_tns) 
			c = conn.cursor()
			c.prepare('select * from eventdetail where userid=:urs')
			c.execute(None,{'urs':usr})
			event=[]
			for i in c:
				event.append(i)
			return render(request,'infinity/user.html',{'event':event})
			conn.commit()
			conn.close()
		else:
			return render(request,'infinity/user.html')
	else:	
		return render(request,'infinity/login.html')

def del_usr(request):
	if request.method=='POST':
		usrid=request.POST.get('userid')
		dsn_tns = cx_Oracle.makedsn('Revanth', '1521', service_name='orcl') 
		conn = cx_Oracle.connect(user='c##rath', password='bigpika', dsn=dsn_tns) 
		c = conn.cursor()
		c.prepare('delete from userdetail where userid=:usrid')
		c.execute(None,{'usrid':usrid})
		c.prepare('delete from eventdetail where userid=:usrid')
		c.execute(None,{'usrid':usrid})
		c.prepare('delete from login where userid=:usrid')
		c.execute(None,{'usrid':usrid})
		conn.commit()
		conn.close()
		return redirect('login')
	else:
		return render(request,'infinity/del_usr.html')

def del_eve(request):
	if request.method=='POST':
		ename=request.POST.get('eventname')
		dsn_tns = cx_Oracle.makedsn('Revanth', '1521', service_name='orcl') 
		conn = cx_Oracle.connect(user='c##rath', password='bigpika', dsn=dsn_tns) 
		c = conn.cursor()
		c.prepare('delete from eventdetail where event=:eventname')
		c.execute(None,{'eventname':ename})
		conn.commit()
		conn.close()
		return redirect('login')
	else:
		return render(request,'infinity/del_eve.html')

def find_usr(request):
	if request.method=='POST':
		usrid=request.POST.get('userid')
		dsn_tns = cx_Oracle.makedsn('Revanth', '1521', service_name='orcl') 
		conn = cx_Oracle.connect(user='c##rath', password='bigpika', dsn=dsn_tns) 
		c = conn.cursor()
		c.prepare('select * from login where userid=:usrid')
		c.execute(None,{'usrid':usrid})
		userdet=[]
		for i in c:
			userdet.append(i)
		c.prepare('select * from eventdetail where userid=:usrid')
		c.execute(None,{'usrid':usrid})
		eventdet=[]
		for i in c:
			eventdet.append(i)
		return render(request,'infinity/disp_user.html',{'user':userdet,'eventdet':eventdet})
		conn.commit()
		conn.close()
	else:
		return render(request,'infinity/find_usr.html')

def syslog(request):
	dsn_tns = cx_Oracle.makedsn('Revanth', '1521', service_name='orcl') 
	conn = cx_Oracle.connect(user='c##rath', password='bigpika', dsn=dsn_tns) 
	c = conn.cursor()
	c.execute('select * from sys_log')
	logdata=[]
	for i in c:
		logdata.append(i)
	return render(request,'infinity/syslog.html',{'logdata':logdata})
	conn.commit()
	conn.close()

def updatedata(request):
	if request.method=='POST':
		dsn_tns = cx_Oracle.makedsn('Revanth', '1521', service_name='orcl') 
		conn = cx_Oracle.connect(user='c##rath', password='bigpika', dsn=dsn_tns) 
		c = conn.cursor()
		product={}
		for i in ['names','rollno','mobile','userid']:
			product[i] = request.POST.get(i)
		product['mobile']=int(product['mobile'])
		c.prepare('update login set names=:names, rollno=:rollno, mobile=:mobile where userid=:userid')
		c.execute(None,product)
		conn.commit()	
		c.prepare('select userid from login where rollno=:rollno')
		c.execute(None,{'rollno':product['rollno']})
		userid=int
		for i in c:
			userid=i[0]
		c.prepare('delete from eventdetail where userid=:userid')
		c.execute(None,{'userid':userid})
		product={}
		for i in ['prozone','inkling','incognito','fuzzlebuzzle','gamoholix']:
			if request.POST.get(i) !=None:
				c.prepare('insert into eventdetail values(:userx,:event)')
				c.execute(None,{'userx':userid,'event':i})
		rollno=request.POST.get('rollno')
		c.prepare('update userdetail set rollno=:rollno where userid=:userid')
		c.execute(None,{'userid':userid,'rollno':rollno})
		conn.commit()
		conn.close()
		return render(request,'infinity/updatedata.html')
	else:	
		return render(request,'infinity/updatedata.html')

def updatepass(request):
	if request.method=='POST':
		userid=request.POST.get('userid')
		passw=request.POST.get('pass')
		dsn_tns = cx_Oracle.makedsn('Revanth', '1521', service_name='orcl') 
		conn = cx_Oracle.connect(user='c##rath', password='bigpika', dsn=dsn_tns) 
		c = conn.cursor()
		c.prepare('update userdetail set pass=:passw where userid=:userid')
		c.execute(None,{'userid':userid,'passw':passw})
		conn.commit()
		conn.close()
		return redirect('login')
	else:
		return render(request,'infinity/updatepass.html')