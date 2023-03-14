from django.shortcuts import render

# Create your views here.
def home(request): 
    author = 'Wallium Ladrian'
    age = 49
    address = 'The Citadel'
    ctx = {'athr':author, 'age':age, 'addr':address}
    return render (request, 'home.html', context=ctx)


def categories(request):
    cats = ['python','Django','web development','programing']
    return render (request,'categories.html',
                   context={'categories':cats})

def articles(request):
    data = [
        
         {'title':'first article',
         'author':'waxllium ladrian',
         'date':'2023-01-2' },
          {'title':'second article',
         'author':'waxllium ladrian',
         'date':'2023-01-2' },
          {'title':'third article',
         'author':'waxllium ladrian',
         'date':'2023-01-2' },
    ]
    return render (request,'articles.html',
                  context={'articles':data})