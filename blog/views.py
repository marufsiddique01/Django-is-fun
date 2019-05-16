from django.shortcuts import render

#from django.http import HttpResponse

#dummy posts >>
posts = [
	{
	'author': 'Maruf',
	'title': 'Blog post 1',
	'content': 'First post content',
	'date_posted': 'August 27, 2018',
	},
	{
	'author': 'MarufS',
	'title': 'Blog post 2',
	'content': 'Second post content',
	'date_posted': 'August 28, 2018',
	}
]


#loading a template>>
def home(request):

	'''context = {
		'posts' : posts
		}'''

	return render(request, 'blog/home.html' , {'title' : 'Home'})
	#return HttpResponse('<h1>Blog Home</h1>')

def about(request):
	return render(request, 'blog/about.html', {'title' : 'About'})
	#return HttpResponse('<h1>About Us</h1>')

def post(request):
	#creating context dictionary >
	context = {
		'posts' : posts
		}
		#posts is accessible from template>>
	return render(request, 'blog/post.html', context , {'title' : 'Post'}) 


# blog -> templates -> blog -> template.html




