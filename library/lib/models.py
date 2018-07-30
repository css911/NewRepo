from __future__ import unicode_literals
#from datetime import datetime, timedelta
from django.db import models

# Create your models here.
class User(models.Model):
	userId = models.IntegerField(primary_key = True)
	name = models.CharField(max_length = 50)
	EmailId = models.EmailField(max_length = 50,blank = False)
	Password = models.CharField(max_length  = 50,blank = False)
	PhoneNo = models.CharField(max_length = 10)
	typee = models.CharField(max_length = 10,choices=[('Librarian', 'Librarian'), ('Student', 'Student')])
	bookIssued = models.IntegerField(default = 0)
	#used while querying the database.
	def __str__(self):
			return self.EmailId

class Table(models.Model):
	bookId = models.IntegerField(primary_key = True)
	bookName = models.CharField(max_length = 50)
	authorName = models.CharField(max_length = 50)
	subject = models.CharField(max_length = 50)
	starRating = models.CharField(max_length = 10)
	copies = models.IntegerField()
	summary = models.CharField(max_length = 256,default = "CHetan")
	def __str__(self):
			return self.bookName+" "+self.authorName+" "+self.subject

class Booked(models.Model):
	bookName = models.CharField(max_length = 50)
	name = models.CharField(max_length = 50)
	bookId1 = models.IntegerField()
	quantity1 = models.IntegerField(default = 1)
	IssuerId1 = models.IntegerField(primary_key =True)
	def __str__(self):
			return str(self.bookId1)+" "+str(self.quantity1)

class IssuedTable(models.Model):
	bookId2 = models.IntegerField()
	quantity2 = models.IntegerField()
	IssuerId2 = models.IntegerField(primary_key = True)
	IssuingDate2 = models.DateField()
	ReturnDate2 = models.DateField()
	def __str__(self):
			return str(self.IssuerId2)+" "+str(self.bookId2)+" "+str(self.IssuingDate2)



class ReturnTable(models.Model):
	ReturningNo3 = models.IntegerField()
	bookId3 = models.IntegerField()
	quantity3 = models.IntegerField()
	IssuerId3 = models.IntegerField(primary_key = True)
	def __str__(self):
			return self.ReturningNo3+" "+self.bookId3+" "+self.quantity3