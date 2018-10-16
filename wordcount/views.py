from django.http import HttpResponse
from django.shortcuts import render
import operator
def about(request):
    return render(request,'wordcount\\about.html')

def home(request):
    # return HttpResponse("HELLO")
    return render(request,'wordcount\home.html')

# def eggs(request):
#     return render(request,'wordcount\home.html',{'hi_there':'EGGS'})

def count(request):
    fulltext = request.GET['fulltext']
    # print(fulltext)
    wordlist = fulltext.split()
    worddictionary={}
    for word in wordlist:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1
    sorted_Word=sorted(worddictionary.items(),key=operator.itemgetter(1),reverse=True)

    return render(request,'wordcount\count.html',{'fulltext':fulltext,'wordcount':len(wordlist),'wordDic':sorted_Word})
