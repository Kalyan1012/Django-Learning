from django.http import HttpResponse
# Create your views here.
def showpost(request,post_id):
    return HttpResponse(f"Post ID is {post_id}")
def user_details(request,username):
    return HttpResponse(f"Username is {username}")
def article_details(request,year):
    return HttpResponse(f"Article year is {year}")
def article_use(request,**kwargs):
    return HttpResponse(f"Article year is {kwargs['year']}, month is {kwargs['month']}, day is {kwargs['day']}")
    #return HttpResponse(f"Data is {kwargs}")  both are same but the first one is more readable and easy to understand