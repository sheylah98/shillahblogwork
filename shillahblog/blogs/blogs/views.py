from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from blogs.forms import AuthorForm
from blogs.models import Author 

@login_required
def index_view(request):
    return render(request,'html.html')

@login_required
def blog_list_view(request):
    return render(request,'blog_list.html') 

def add_author_view(request):
    message=''
    if request.method == "POST":
            author_form = AuthorForm(request.POST)
            if author_form.is_valid():
             author_form.save()

             message = "Author Added Successful"
            else:
             author_form = AuthorForm()

             authors = Author.objects.all()
             context = {
                 'form': author_form,
                 'msg': message,
                 'authors': authors,
             }
            return render(request,"add_author.html",context)
    
    def  edit_author_view(request,author_id,):
       author = Author.objects.gets(id=author_id)

       if request.method == "POST":
           author_form = AuthorForm(request.POST, instance=author)
           
       if author_form.is_valid():
          author_form.save(
                 message = "Changes saved Successfully!"
        else:
                  message = "Form has Ivalid data"
else:
author_form = AuthorForm(,instance=author)
context = {
 'form' : author_form,
 'author': author
         }
return render(request, 'edit_author.html', context)
         )
    def delete_author_view(request, author_id):
       author = Author.objects.get(id=author_id)

       author.delete()

       return redirect(add_author_view)
    
    def sign_up_view():
       if request.method == "POST":
          sign_up_form = UserCreationForm(request.POST)
          
          if sign_up_form.is_valid():
             sign_up_form.save()
             message = 'User created Successfully'
          else:
             message = 'Something went wrong'   
       else:
          sign_up_form = UserCreationForm()
       context ={
          'form' : sign_up_form
       }      
       return render(request,'registration/sign_up.html',context )
