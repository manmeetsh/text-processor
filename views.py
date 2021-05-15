 #khud bnayi ye file

from django.shortcuts import render
from django.http import HttpResponse

# def favsites(request):
# 	return HttpResponse('''<title>TOP 3 SITES </title>
# 		<h1>Hi these are my fav sites!</h1>
# 		<a  href="https://web.whatsapp.com/"> WHATSAPP</a><br>
# 		<a  href="https://www.youtube.com/"> YOUTUBE</a><br>
# 		<a  href="http://www.linkedin.com/jobs"> LINKEDIN</a>''')
	
# def home(request):
# 	# return HttpResponse('''<a href="http://127.0.0.1:8000/rempunc">REMOVE PUNC</a>
# 	# 	<a href="http://127.0.0.1:8000/cap">Capitalize</a>
# 	# 	<a href="http://127.0.0.1:8000/linrem">Remove line</a>
# 	# 	<a href="http://127.0.0.1:8000/spacrem">Space remover</a>
# 	# 	<a href="http://127.0.0.1:8000/charcount">Char counter</a>''')	
# 	params={'name':'manny', 'place':'jupiter'}
# 	return render(request, 'home.html', params)
def index(request):
 	return render(request, 'index.html')

def analyze(request):
	
	#get the text
	djtext = request.GET.get('text','default_text')
	
	rempuncCheckBox=request.GET.get('rempuncCheckBox', 'off')
	capCheckBox=request.GET.get('capCheckBox')
	linremCheckBox=request.GET.get('linremCheckBox')
	spacremCheckBox=request.GET.get('spacremCheckBox')
	charcountCheckBox=request.GET.get('charcountCheckBox')
	
	punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
	analyzed=""

	if rempuncCheckBox=="on":
		#remove puncs
		for char in djtext:
			if(char not in punctuations):
				analyzed+=char
		djtext=analyzed		
		params={'analyzed_text': analyzed}
		#return render(request, 'analyze.html', params)

	if capCheckBox=="on" :
		#capitalize all
		analyzed= djtext.upper()
		djtext=analyzed
		params={'analyzed_text':analyzed}
		#return render(request, 'analyze.html', params)
	

	if linremCheckBox == "on":
		for char in djtext:
			if char !="\n":
				analyzed+=char
		djtext=analyzed		
		params={'analyzed_text': analyzed}
		#return render(request, 'analyze.html', params)


	if spacremCheckBox == "on":
		for char in djtext:
			if char !=" ":
				analyzed+=char
		djtext=analyzed		
		params={'analyzed_text': analyzed}
		#return render(request, 'analyze.html', params)

	if charcountCheckBox == "on": 	
		cnt=0
		for char in djtext:
			cnt+=1
		params={'analyzed_text': cnt}
		#return render(request, 'analyze.html', params)

		
	else:
		return HttpResponse('''<title>ERR!!!!</title><h1>you forgot to checkbox</h1><br>
							<a href="/">Back</a>''')

# def cap(request):
# 	return HttpResponse('capitalize')
# def linrem(request):
# 	return HttpResponse('line remove')
# def spacrem(request):
# 	return HttpResponse('space remove')
# def charcount(request):
# 	return HttpResponse('charcount ')

