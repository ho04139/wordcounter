from django.shortcuts import render

# Create your views here.

def home(req):
    return render(req, 'home.html' )

def about(req):
    return render(req, 'about.html')

def result(req):
    text = req.GET['fulltext']
    words = text.split()
    word_dic = {}

    for word in words:
        if word in word_dic:
            #increase
            word_dic[word] += 1
        else:
             #add to dic
             word_dic[word] = 1
    return render(req, 'result.html', {'full': text, 'total' : len(words), 'dic' : word_dic.items})