from django.db import models


# Create your models here.

class Customer(models.Model):
	CustomerId = models.CharField(max_length=10)
	Fname = models.CharField(max_length=20)
	Lname = models.CharField(max_length=20)
	ContactNum = models.IntegerField()
	Street = models.CharField(max_length=20)
	City_Municipality = models.CharField(max_length=20)
	Province = models.CharField(max_length=20)
	Username = models.CharField(max_length=50)
	Password = models.CharField(max_length=20)
	repassword = models.CharField(max_length=20)

	def __str__(self):
		return self.Fname

class Order(models.Model):
	OrderId = models.CharField(max_length=10)
	BookId = models.CharField(max_length=10)
	Quantity = models.IntegerField()
	Price = models.IntegerField()
	TotalAmount = models.IntegerField()

	# class meta:
	# 	db_table = 'myapp1_order'

class Admin(models.Model):
	AdminId = models.CharField(max_length=10)
	Fname = models.CharField(max_length=20)
	Lname = models.CharField(max_length=20)
	Username = models.CharField(max_length=50)
	Password = models.CharField(max_length=20)

	def __str__(self):
		return self.Fname

	# class meta:
	# 	db_table = 'myapp1_admin'
	
class Stocks(models.Model):
	BookId = models.CharField(max_length=10)
	BookTitle = models.CharField(max_length=100)
	Author = models.CharField(max_length=50)
	Category = models.CharField(max_length=50)
	Price = models.IntegerField()

	class meta:
		db_table = 'myapp1_stocks'

	# class meta:
	# 	db_table = 'myapp1_sales'

class Book(models.Model):
	isbn = models.IntegerField()
	title = models.CharField(max_length=100)
	genre = models.CharField(max_length=50)
	year_published = models.IntegerField()

	# class meta:
	# 	db_table = 'myapp1_stocks'

class Author(models.Model):
	author_Id = models.CharField(max_length=10)
	name = models.CharField(max_length=100)
	address = models.CharField(max_length=50)
	birthdate = models.CharField(max_length=10)
	mobilenumber = models.IntegerField()

	# class meta:
	# 	db_table = 'myapp1_stocks'

class Contact(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField()
	subject = models.TextField()

	def __str__(self):
		return self.name

	# class meta:
	# 	db_table = 'myapp1_stocks'
