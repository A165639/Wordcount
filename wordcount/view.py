from django.http import HttpResponse
from django.shortcuts import render
import operator
#rom django.http import HttpRequest
def homepage(request):
    return render(request,'home.html')
def count(request):
    data= request.GET['Fulltextarea']

    word_list=data.split()
    lenth = len(word_list)
    print(lenth)

    wordcount={}

    for word in word_list:
        if word in wordcount:
            wordcount[word] +=1

        else:
            wordcount[word]=1
    sorted_list = sorted(wordcount.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html', {'fulltext':data,'word':lenth,'wordcount':sorted_list})
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
