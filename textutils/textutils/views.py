from django.http import  HttpResponse
from django.shortcuts import  render
def index(request):
    # return HttpResponse("Home <a href='/removepunc'>remove punc</a> <a href='/capital'>capitalize</a> "
    #                     " <a href='/newlineremove'>New line remove</a> <a href='/spaceremove'>spaceremove</a> "
    #                     "<a href='/charcount'>character count</a>")
    param={'name':'santu','place':'basrur'}
    return render(request,'index.html',param)
def analyze(request):
    djtext=request.POST.get('text','null')
    removepunc=request.POST.get('removepunc','off')
    capitalize=request.POST.get('capitalize','off')
    newlineremove=request.POST.get('newlineremove','off')
    spaceremove=request.POST.get('spaceremove','off')
    purpose=""
    if removepunc=='on':
        analyzed=""
        punct='''!@#$%^&*()-_{}[];:'",.<>/?\|~`'''
        for char in djtext:
            if char not in punct:
                analyzed+=char
        purpose+="||Remove Punctuation|"
        djtext=analyzed
    if capitalize=='on':
        analyzed = ""
        for char in djtext:
            analyzed += char.upper()
        purpose+="|Capitalize|"
        djtext=analyzed
    if newlineremove=='on':
        analyzed = ""
        for char in djtext:
            if char!='\n':
                analyzed += char
        purpose+="|New line remove|"
        djtext=analyzed
    if spaceremove=='on':
        analyzed = ""
        for i,char in enumerate(djtext):
            if not(djtext[i]==" " and djtext[i+1]==" "):
                 analyzed += char

        purpose+="|Remoove Punctuation||"

    if(removepunc!='on' and capitalize!='on' and newlineremove!='on' and spaceremove!='on'):
        return HttpResponse("EROOR")
    param={'purpose':purpose,'analyze':analyzed}
    return render(request, 'analyze.html', param)