from django.shortcuts import render

def show_num(request, num):
    mul = []
    for i in range(1,13,1):
        mul.append(str(num*i))
    return render(request, 'mul.html', {'show_num':num, 'mul_list':mul})
