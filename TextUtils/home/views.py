import string
from django.shortcuts import render ,HttpResponse

def index(request):
    return render(request,'index.html')
    

def analyzer(request):
    djtext=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    capfirst=request.POST.get('capfirst','off')
    newline_remove=request.POST.get('newline_remove','off')
    char_count=request.POST.get('char_count','off')
    if removepunc=='on':
        analyzed=''
        punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char  not in punctuations:
                analyzed=analyzed+char
        params={'purpose':'With no puntuations', 'analyzed_text':analyzed}
        djtext=analyzed
    if capfirst=='on':
        analyzed=''
        for char in djtext:
            char=char.upper()
            analyzed=analyzed+char
        params={'purpose':'Captilise each letter', 'analyzed_text':analyzed}
        djtext=analyzed
    if newline_remove=='on':
        analyzed=''.join(djtext.splitlines())
        params={'purpose':'Newline_remove', 'analyzed_text':analyzed} 
        djtext=analyzed
    elif char_count=='on':
        list=djtext.split(' ')
        analyzed=len(list)
        params={'purpose':'Char_count', 'analyzed_text':analyzed}
        djtext=analyzed 
    if removepunc=='off ' and capfirst=='off' and newline_remove=='off' and char_count=='off':
        return HttpResponse('Error')    
    return render(request,'analyzer.html',params) 
   
    