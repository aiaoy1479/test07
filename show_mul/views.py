from django.shortcuts import render

def show_num(request, num):
    return render(request, 'mul.html', {'show_num':num})
