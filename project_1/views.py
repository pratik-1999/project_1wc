from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request,'homepage.html')

def count(request):
    Text=request.GET['Text']

    wordlist= Text.split()
    wordict ={}
    for word in wordlist:
        if word in wordict:
            wordict[word] += 1
        else:
            wordict[word] = 1

    sortword= sorted(wordict.items(), key = operator.itemgetter(1), reverse=True)



    return render(request,'count.html',{'Text':Text,'count':len(wordlist),'sortword':sortword})

def info(request):
    return render(request,'info.html')
