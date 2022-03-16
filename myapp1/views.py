# from django.http import Http404
from django.http import HttpResponse
from django.http.response import HttpResponse
from myapp1.models import Stocks
from .models import Contact
from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import *
from django.contrib import messages
from .models import *
import mysql.connector
from operator import itemgetter

# Create your views here.
class MyIndexView(View):
    def get(self, request):

        return render(request,'index.html')

class MyIndexViewCustomer(View):
    def get(self, request):

        return render(request,'index Customer.html')

class MyDisplayView(View):
    def get(self, request):

        return render(request,'display.html')


class MyDashboardView(View):
    def get(self, request):
        book = Stocks.objects.all()
        context = {
            'books': book
        }

        return render(request,'dashboard.html',context)

    def post(self, request):
		
        if request.method == 'POST':
            
            if 'btnUpdate' in request.POST:	
                
                print('update profile button clicked')
                id = request.POST.get("id")
                BookTitle = request.POST.get("BookTitle")
                Author = request.POST.get("Author")
                Category = request.POST.get("Category")
                Price = request.POST.get("Price")
                
                update_book = Stocks.objects.filter(id = id).update(BookTitle = BookTitle, Author = Author, Category = Category, Price = Price)
                print(update_book)
                print('profile updated')
                
                return redirect('myapp1:my_dashboard_view')
            elif 'btnDelete' in request.POST:
                print('delete button clicked')
                id = request.POST.get("id")
                bookdel = Stocks.objects.filter(id=id).delete()
				# pers = Person.objects.filter(id = sid).delete()
                print('recorded deleted')
		        #return HttpResponse ('post')
                return redirect('myapp1:my_dashboard_view')

class MyDashboardViewBooks(View):
    def get(self, request):
        book = Stocks.objects.all()
        context = {
            'books': book
        }

        return render(request,'dashboardViewBooks.html',context)

    def post(self, request):
		
        if request.method == 'POST':
            
            if 'btnUpdate' in request.POST:	
               

                print('update profile button clicked')
                OrderId = request.POST.get("OrderId")
                BookId = request.POST.get("BookId")
                Quantity = request.POST.get("Quantity")
                Price = request.POST.get("Price")
                TotalAmount = request.POST.get("TotalAmount")

                total= int(Price)*int(Quantity)
                # values = { 'TotalAmount':total }
                
                
                update_book = Order(OrderId=OrderId, BookId = BookId, Quantity = Quantity, Price = Price, TotalAmount = total)
                print(update_book)
               
                update_book.save()
                return redirect('myapp1:my_dashboard_orderCustomer_view')
           



class MyDashboardCustomerView(View):
    def get(self, request):
        customers = Customer.objects.all()
        context = {
            'customer': customers
        }

        return render(request,'dashboardCustomer.html',context)

    def post(self, request):
        
        if request.method == 'POST':
            
            if 'btnUpdate' in request.POST:	
                print('update profile button clicked')
                id = request.POST.get("id")
                Fname = request.POST.get("Fname")
                Lname = request.POST.get("Lname")
                ContactNum = request.POST.get("ContactNum")
                Street = request.POST.get("Street")
                City_Municipality = request.POST.get("City_Municipality")
                Province = request.POST.get("Province")
                
                update_book = Customer.objects.filter(id = id).update(id = id, Fname = Fname, Lname = Lname, ContactNum = ContactNum, Street = Street, City_Municipality=City_Municipality,Province=Province)
                print(update_book)
                print('profile updated')
                return redirect('myapp1:my_dashboard_customer_view')
            elif 'btnDelete' in request.POST:
                print('delete button clicked')
                id = request.POST.get("id")
                bookdel = Customer.objects.filter(id=id).delete()
				# pers = Person.objects.filter(id = sid).delete()
                print('recorded deleted')
		        #return HttpResponse ('post')
                return redirect('myapp1:my_dashboard_customer_view')

class MyDashboardMainView(View):
    def get(self, request):

        return render(request,'dashboardmain.html')

class MySigninView(View):
    def get(self, request):

        return render(request,'signinBoard.html')

    # def post(self, request):
    #     form = LogInForm(request.POST)

    #     if form.is_valid():
    #         Username = request.POST.get("Username")
    #         Password = request.POST.get("Password")
			
    #         form = Customer( Username=Username, Password=Password)
    #         # Message_me = Stocks.objects.filter(BookId, status=0).count()
    #         # print (Message_me)
    #         # form.save()

    #         return redirect('myapp1:my_index_view')
        
    #     else:
    #         print(form.errors)
    #     return HttpResponse('not valid')


class MyLandingView(View):
    def get(self, request):

        return render(request,'landing.html')

class LoginChoices(View):
    def get(self, request):

        return render(request,'LoginChoices.html')

class MyDashboardSalesView(View):
    def get(self, request):
        sales = Sales.objects.all()
        context = {
            'sale': sales
        } 
        return render(request,'dashboardSales.html',context)

class MyDashboardOrderCustomerView(View):
    def get(self, request):
        orders = Order.objects.all()
        context = {
            'order': orders
        } 
        return render(request,'dashboardOrder Customer View.html',context)

    def post(self, request):
		
        if request.method == 'POST':
            
            if 'btnUpdate' in request.POST:	
                
                print('update profile button clicked')
                id = request.POST.get("id")
                BookId = request.POST.get("BookId")
                Quantity = request.POST.get("Quantity")
                Price = request.POST.get("Price")
                TotalAmount = request.POST.get("TotalAmount")
                
                update_book = Order.objects.filter(id = id).update(BookId = BookId, Quantity = Quantity, Price = Price, TotalAmount = TotalAmount)
                print(update_book)
                print('profile updated')
                return redirect('myapp1:my_dashboard_orderCustomer_view')
            elif 'btnDelete' in request.POST:
                print('delete button clicked')
                id = request.POST.get("id")
                bookdel = Order.objects.filter(id=id).delete()
				# pers = Person.objects.filter(id = sid).delete()
                print('recorded deleted')
		        #return HttpResponse ('post')
                return redirect('myapp1:my_dashboard_orderCustomer_view')


class MyDashboardOrderView(View):
    def get(self, request):
        orders = Order.objects.all()
        context = {
            'order': orders
        } 
        return render(request,'dashboardOrder.html',context)

    def post(self, request):
		
        if request.method == 'POST':
            
            if 'btnUpdate' in request.POST:	
                
                print('update profile button clicked')
                id = request.POST.get("id")
                BookId = request.POST.get("BookId")
                Quantity = request.POST.get("Quantity")
                Price = request.POST.get("Price")
                TotalAmount = request.POST.get("TotalAmount")
                
                update_book = Order.objects.filter(id = id).update(BookId = BookId, Quantity = Quantity, Price = Price, TotalAmount = TotalAmount)
                print(update_book)
                print('profile updated')
                return redirect('myapp1:my_dashboard_order_view')
            elif 'btnDelete' in request.POST:
                print('delete button clicked')
                id = request.POST.get("id")
                bookdel = Order.objects.filter(id=id).delete()
				# pers = Person.objects.filter(id = sid).delete()
                print('recorded deleted')
		        #return HttpResponse ('post')
                return redirect('myapp1:my_dashboard_order_view')


class MyDashboardAdminView(View):
    def get(self, request):
        admin = Admin.objects.all()
        context = {
            'admins': admin
        } 
        return render(request,'dashboardAdmin.html',context)

    def post(self, request):
        
        if request.method == 'POST':
            
            if 'btnUpdate' in request.POST:	
                print('update profile button clicked')
                id = request.POST.get("id")
                # AdminId = request.POST.get("AdminId")
                Fname = request.POST.get("Fname")
                Lname = request.POST.get("Lname")
                Username = request.POST.get("Username")
                Password = request.POST.get("Password")
                
                update_book = Admin.objects.filter(id = id).update(Fname = Fname, Lname = Lname, Username = Username, Password = Password)
                print(update_book)
                print('profile updated')
                return redirect('myapp1:my_dashboard_admin_view')
            elif 'btnDelete' in request.POST:
                print('delete button clicked')
                id = request.POST.get("id")
                bookdel = Admin.objects.filter(id=id).delete()
				# pers = Person.objects.filter(id = sid).delete()
                print('recorded deleted')
		        #return HttpResponse ('post')
                return redirect('myapp1:my_dashboard_admin_view')
        
class MyBookRegistrationView(View):
    def get(self, request):

        return render(request,'registration.html') 

    def post(self, request):
        form = BookForm(request.POST)

        if form.is_valid():
            BookId = request.POST.get("BookId")         
            BookTitle = request.POST.get("BookTitle")
            Author = request.POST.get("Author")
            Category = request.POST.get("Category")
            Price = request.POST.get("Price")
            
            form = Stocks(BookId=BookId, BookTitle=BookTitle, Author=Author, Category=Category, Price=Price)
            # Message_me = Stocks.objects.filter(BookId, status=0).count()
            # print (Message_me)
            form.save()

            return redirect('myapp1:my_dashboard_main_view')
        
        else:
            print(form.errors)
        return HttpResponse('not valid')

# class MyBookRegistrationView(View):
#     def get(self, request):

#         return render(request,'registration.html') 

#     def post(self, request):
#         form = BookForm(request.POST)

#         if request.method=="POST":
#             BookId = request.POST.get("BookId")         
#             BookTitle = request.POST.get("BookTitle")
#             Author = request.POST.get("Author")
#             Category = request.POST.get("Category")
#             Price = request.POST.get("Price")
#             empsearchobj=Stocks.objects.raw('select * from myapp1_stocks where BookTitle="'+BookTitle+'"')

#             return render(request,'dashboard.html',{"Stocks":empsearchobj})
            
#             # form = Stocks(BookId=BookId, BookTitle=BookTitle, Author=Author, Category=Category, Price=Price)
#             # form.save()

#            # return redirect('myapp1:my_dashboard_main_view')
        
#         else:
#         #     print(form.errors)
#         # return HttpResponse('not valid')
#             empobj=Stocks.objects.raw('select * from myapp1_stocks')
#             return render (request, 'dashboard.html', {"Stocks":empobj} )
class MyAdminRegistrationView(View):
    
    def get(self, request):

        return render(request,'registrationAdmin.html')

    def post(self, request):
        form = AdminForm(request.POST)

        if form.is_valid():
            AdminId = request.POST.get("AdminId")
            Fname = request.POST.get("Fname")			
            Lname = request.POST.get("Lname")
            Username = request.POST.get("Username")
            Password = request.POST.get("Password")
			
            form = Admin(AdminId=AdminId,Fname=Fname, Lname=Lname, Username=Username, Password=Password)
            form.save()

            return redirect('myapp1:my_dashboard_admin_view')
        
        else:
            print(form.errors)
        return HttpResponse('not valid')
        

class MyCustomerRegistrationView(View):
    def get(self, request):
        return render(request,'registrationCustomer.html')

    def post(self, request):
        form = CustomerForm(request.POST)

        if form.is_valid():
            # CostumerId = request.POST.get("CostumerId")
            Fname = request.POST.get("Fname")         
            Lname = request.POST.get("Lname")
            ContactNum = request.POST.get("ContactNum")
            Street = request.POST.get("Street")
            City_Municipality = request.POST.get("City_Municipality")
            Province = request.POST.get("Province")
            # Username = request.POST.get("Username")
            # Password = request.POST.get("Password")
            
            form = Customer( Fname=Fname, Lname=Lname, ContactNum=ContactNum, Street=Street,
                City_Municipality=City_Municipality, Province=Province)
            form.save()

            return redirect('myapp1:my_dashboard_main_view')
        
        else:
            print(form.errors)
            return HttpResponse('not valid')

class MyDashboardPracticalBookView(View):
    def get(self, request):
        book = Book.objects.all()
        context = {
            'book': book
        } 
        return render(request,'dashboardPracticalBook.html',context)

class MyRegistrationPracticalBookView(View):
    def get(self, request):

        return render(request,'registrationPracticalBook.html') 

    def post(self, request):
        form = PracticalBookForm(request.POST)

        if form.is_valid():
            isbn = request.POST.get("isbn")         
            title = request.POST.get("title")
            genre = request.POST.get("genre")
            year_published = request.POST.get("year_published")
            
            
            form = Book(isbn=isbn, title=title, genre=genre, year_published=year_published)
            form.save()

            return redirect('myapp1:my_dashboard_PracticalBook_view')
        
        else:
            print(form.errors)
        return HttpResponse('not valid')

class MyDashboardPracticalAuthorView(View):
    def get(self, request):
        book = Author.objects.all()
        context = {
            'book': book
        } 
        return render(request,'dashboardPracticalAuthor.html',context)

class MyRegistrationPracticalAuthorView(View):
    def get(self, request):

        return render(request,'registrationPracticalAuthor.html') 

    def post(self, request):
        form = PracticalAuthorForm(request.POST)

        if form.is_valid():
            author_Id = request.POST.get("author_Id")         
            name = request.POST.get("name")
            address = request.POST.get("address")
            birthdate = request.POST.get("birthdate")
            mobilenumber = request.POST.get("mobilenumber")
            
            
            form = Author(author_Id=author_Id, name=name, address=address, birthdate=birthdate, mobilenumber=mobilenumber)
            form.save()

            return redirect('myapp1:my_dashboard_PracticalAuthor_view')
        
        else:
            print(form.errors)
        return HttpResponse('not valid')



def login_page(request):
    form = forms.LoginForm()
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            pass
    return render(request, 'authentication/login.html', context={'form': form})


def feedback(request):
    
        if request.method=='POST':
            contact=Contact()
            name=request.POST.get("name")
            email=request.POST.get("email")
            subject=request.POST.get("subject")
            contact.name=name
            contact.email=email
            contact.subject=subject
            contact.save()
            return HttpResponse("<h1>Thanks For Contacting Us!</h1>")
        return render(request,'feedback.html')



def login(request):
    con = mysql.connector.connect(host="localhost",user="root",passwd="", database="onlinebookstore")
    cursor=con.cursor()
    con2 = mysql.connector.connect(host="localhost",user="root",passwd="", database="onlinebookstore")
    cursor2=con2.cursor()
    sqlcommand="SELECT Username from myapp1_customer"
    sqlcommand2="SELECT Password from myapp1_customer"
    cursor.execute(sqlcommand)
    cursor2.execute(sqlcommand2)
    u=[]
    p=[]

    for i in cursor:
        u.append(i)

    for j in cursor2:
        p.append(j)

    res= list(map(itemgetter(0),u))
    res2= list(map(itemgetter(0),p))


    if request.method=="POST":
        Username = request.POST.get("Username")
        Password = request.POST.get("Password")
        i=1
        k=len(res2)
        while i<k:
            if res[i]==Username and res2[i]==Password:
                return render(request,'index Customer.html',{'Username':Username})
                break
            i+=1
        else:
            messages.info(request,"*Check Username or Password*")
            # return redirect("login")
    

    return render(request,'login.html')

def loginAdmin(request):
    con = mysql.connector.connect(host="localhost",user="root",passwd="", database="onlinebookstore")
    cursor=con.cursor()
    con2 = mysql.connector.connect(host="localhost",user="root",passwd="", database="onlinebookstore")
    cursor2=con2.cursor()
    sqlcommand="SELECT Username from myapp1_admin"
    sqlcommand2="SELECT Password from myapp1_admin"
    cursor.execute(sqlcommand)
    cursor2.execute(sqlcommand2)
    u=[]
    p=[]

    for i in cursor:
        u.append(i)

    for j in cursor2:
        p.append(j)

    res= list(map(itemgetter(0),u))
    res2= list(map(itemgetter(0),p))


    if request.method=="POST":
        Username = request.POST.get("Username")
        Password = request.POST.get("Password")
        i=1
        k=len(res2)
        while i<k:
            if res[i]==Username and res2[i]==Password:
                return render(request,'index.html',{'Username':Username})
                break
            i+=1
        else:
            messages.info(request,"*Check Username or Password*")
            # return redirect("login")
    

    return render(request,'login Admin.html')

def register(request):
    if request.method=="POST":
        customer=Customer()

        CustomerId = request .POST.get("CustomerId")
        Fname = request.POST.get("Fname")         
        Lname = request.POST.get("Lname")
        ContactNum = request.POST.get("ContactNum")
        Street = request.POST.get("Street")
        City_Municipality = request.POST.get("City_Municipality")
        Province = request.POST.get("Province")
        Username = request.POST.get("Username")
        Password = request.POST.get("Password")
        repassword = request.POST.get("repassword")

        customer.CustomerId = CustomerId
        customer.Fname = Fname        
        customer.Lname = Lname
        customer.ContactNum = ContactNum
        customer.Street = Street
        customer.City_Municipality = City_Municipality
        customer.Province = Province
        customer.Username = Username
        customer.Password = Password
        customer.repassword = repassword
        
        if customer.Password != customer.repassword:
            messages.info(request,'*Password and Repassword are not the same!*')
            # return redirect("register")

        elif customer.CustomerId=="" or customer.Fname=="" or customer.Lname=="" or customer.ContactNum=="" or customer.Street=="" or customer.City_Municipality=="" or customer.Province=="" or customer.Username=="":
            messages.info(request,'*Some Fields are Empty*')
            # return redirect("register")

        else:
            customer.save()
            # return render(request,'login.html')
            
            

    return render(request,'register.html')
