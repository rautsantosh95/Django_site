#I have created this file - Santosh
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def Analyze(request):
    #Get the text

    Dtext =request.POST.get('text', 'default')
    #check checkbox value

    removepunc =request.POST.get('removepunc', 'off')
    fullcaps =request.POST.get('fullcaps', 'off')
    newlineremover =request.POST.get('newlineremover', 'off')
    extraspaceremover =request.POST.get('extraspaceremover', 'off')

    #check the checkbox
    if removepunc == "on":
        punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in Dtext:
            if char not in punctuation:
                analyzed = analyzed + char
        params = {'purpose':'Remove Punctuations', 'analyzed_text':analyzed}
        return render(request, 'Analyze.html', params)

    #check the checkbox
    elif (fullcaps == "on"):
        analyzed = ""
        for char in Dtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}

        return render(request, 'analyze.html', params)
    elif(newlineremover == 'on'):
        analyzed = ""
        for char in Dtext:
            if char !="\n" and char !="\r":
                analyzed = analyzed + char

        params = {'purpose': 'Removed New Line', 'analyzed_text': analyzed}

        return render(request, 'analyze.html', params)
    elif(extraspaceremover == 'on'):
        analyzed = ""
        for index, char in enumerate(Dtext):
            if not(Dtext[index] == " " and Dtext[index+1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed space', 'analyzed_text': analyzed}

        return render(request, 'analyze.html', params)

    else:
        return HttpResponse("Error")
