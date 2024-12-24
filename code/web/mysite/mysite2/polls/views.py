from django.shortcuts import render

# Create your views here.
def index(request):
    
    args = {
        'name':'John',
        'age':'11',
        'vip':'true',
        
        'dc':{
        'a':10,
        'b':20
        },

        'loops':[1,2,3,4]
    }



    return render(request,'./polls/index.html',args)