from django.shortcuts import render
from datetime import datetime

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
def home(request):
    context = {
        "name": "John Doe",
        "age": 30,
        "skills": ["Python", "Django", "JavaScript"],
        "user": User("Jane Smith", 25),
        "blog":{
            "title": "My First Blog Post",
            "content": "This is the content of my first blog post.",
            "created_at": datetime.now(),
        },
        "empty_value": None,

    }
    return render(request, 'blog/home.html', context)


# Create your views here.
