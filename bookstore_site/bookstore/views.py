from django.shortcuts import render
from bookstore.models import books
from django.http import HttpResponseRedirect
# Create your views here.
def show_all_books(request):
    if request.method == 'GET':
        all_book = books.objects.all()
        return render(request,"get_all_book.html",locals())

def operate_storages(request,bookid):
    got_book = books.objects.get(id = bookid)
    if request.method == "GET":
        return render(request, "operate_book.html",locals())
    if request.method =="POST":
        got_book.price = request.POST["new_price"]
        got_book.market_price = request.POST["new_m_price"]
        got_book.save()
        return HttpResponseRedirect("/bookstore/all_books")

