from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from models import User
from models import Table
from models import IssuedTable
from models import ReturnTable
from models import Booked
from django.db.models import Sum
from django.db.models import Q

context = {}

# Create your views here.

def books(request):
	context = {}
	pq = Table.objects.get(bookId =request.GET['book_id'])
	context['summary'] = pq.summary
	return render(request,'book_summary.html',context)



def ren(request):
	if 'username' in request.session:
		if "Librarian" == request.session['typee']:
		    return render (request,'library.html',{})
		else:
			return redirect('/retrivelist')
	return render(request,"login.html",{})


def ren1(request):
	return render(request,"register.html",{})

def retrivelist(request):
	if 'username' in request.session:
		
		if "Librarian" == request.session['typee']:
			infolist = [] 
			
			copies = Table.objects.aggregate(value=Sum('copies'))
			copies['name'] ="No of Copies"
			
			booksIssued = IssuedTable.objects.aggregate(value=Sum('quantity2'))
			booksIssued['name'] ="No of BooksIssued"

			booksReturned = ReturnTable.objects.aggregate(value=Sum('quantity3'))
		   	booksReturned['name'] = "No of booksReturned"

		   	booked = Booked.objects.aggregate(value=Sum('quantity1'))
		   	booked['name'] = "No of books booked"

		   	#appending to the list
		   	infolist.append(copies)
		   	infolist.append(booksIssued)
		   	infolist.append(booksReturned)
		   	infolist.append(booked)
		   	#adding the list to the dictionary
		   	print infolist
		   	context['list2'] = infolist

		   	return render(request,'library.html',context)
		else:
			context[list] = ""
			context['list1'] = Table.objects.all()
			return render(request,"student.html",context)
	return render(request,'login.html',{'message':"Your are not login"})		


@csrf_exempt
def issueit(request):
#	IssueingNo2
#bookId2
#quantity2
#IssuerId2
#IssuingDate2
#ReturnDate2

	context['list2'] = Booked.objects.all()
	return render(request,'issue_a_book.html',context)	







@csrf_exempt
def book_a_book(request):
	count = Table.objects.get(bookId=request.GET['book_id'])
	p=Booked(bookId1=request.GET['book_id'],quantity1="1",IssuerId1=request.session['UserId'],name=User.objects.get(userId=request.session['UserId']).name,bookName=count.bookName)
	try:
		if count.copies > 0:
			count.copies = count.copies-1
			p.save(force_insert = True)
			count.save()
			
		else:
			raise Exception('No book left')  	
	except Exception as e:
		context = {}
		context['list1'] =Table.objects.all()
		context['message'] = "You have already booked a book"
		print str(e) +"chetan"+str(request.GET['book_id'])+"kaka"
		return render(request,'student.html',context)
	context = {}
	context['list1'] =Table.objects.all()
	context['message'] ="The book is been booked"
	return render(request,'student.html',context)


@csrf_exempt
def issuedBook(request):
	context= {}
	context['list1'] = IssuedTable.objects.filter(IssuerId2=request.session['UserId'])
	return render(request,'booked.html',context)




@csrf_exempt
def enterregister(request):
	context = {}
	name = request.POST['name']
	email = request.POST['email']
	password = request.POST['Password']
	typee = request.POST['pro']		
	phone_number = request.POST['PhoneNumber']
	


	if User.objects.filter(EmailId = email).exists():
		print "The user already exists"
	else:
		user_obj = User(name = name,EmailId = email,Password=password,PhoneNo=phone_number,typee = typee)
		user_obj.save()
	return render(request,"login.html",{})

def profile(request):
	context = {}
	usernm=request.session['username']
	usr_obj=User.objects.get(EmailId = usernm)
	context['message'] = usr_obj.EmailId +" "+ usr_obj.name+" "+usr_obj.PhoneNo
	return render(request,'user_profile.html',context)

@csrf_exempt
def search(request):
	search = request.POST['book_name']
	usr_obj = Table.objects.filter(Q(bookName =search)|Q(authorName = search)|Q(subject = search))
	context['list'] = usr_obj 
	return render(request,"student.html",context)

@csrf_exempt
def issuebook(request):
	context={}
	context['list2'] = Booked.objects.all()
	return render(request,"issue_a_book.html",context)




@csrf_exempt	
def check(request):
	
	message = ''
	name = request.POST['email']
	password = request.POST['password']
	if User.objects.filter(EmailId=name).exists():
		#print 'User name exists'
		if User.objects.filter(EmailId=name,Password=password).exists():
			user_obj=User.objects.get(EmailId=name,Password=password)
			request.session['username'] = name
			request.session['typee'] = user_obj.typee
			request.session['UserId'] = User.objects.get(EmailId=name).userId
			#print request.session['UserId']+"dhfjsdhfjdhfsjdfhdjfhdjfhdjfdfjdhfjdhfj"
			if user_obj.typee == "Student":
				return redirect('/retrivelist')
 			else:
 				context ={}
 				context['name']= name
 				context['userid'] =user_obj.userId 
 				return render(request,'library.html',context)
		else:
			message = "Wrong Details"

	else:
		message = 'User not exists'
	context={}	
	context["message"] = message
	return render(request,'login.html',{'message':"error in loging"})


@csrf_exempt
def logout(request):
	if "username" in request.session:
		del request.session['username']
	return redirect('/login')