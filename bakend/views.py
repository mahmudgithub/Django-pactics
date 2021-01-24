from django.shortcuts import render

lol=[
    {
        'name':'mahmud'
    

    }
]

def one(request):
    # context='mahmiud'
    return render(request,'home.html',{'data':lol})

def two(request):
    if request.method=='POST':
        number1=request.POST['number1']
        number2=request.POST['number2']
        context={ 'num1': number1 , 'num2': number2 ,'sum': (int(number1)+int(number2))}
        return render(request,'base.html',{'data':context})
    return render(request,'home.html')