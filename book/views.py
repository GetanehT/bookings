from django.http import HttpResponse

def my_book(request):
    return HttpResponse("This is the book page.")
