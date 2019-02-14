from django.shortcuts import render, get_object_or_404
from .models import Number, Total_input

def input(request):
    input_num = ""
    if request.POST:
        num = request.POST['name']
        mul = []
        number = Number()
        number.num_input = num
        number.save()
        show_num = 
        try:
            num = int(float(num))
            for i in range(1,13,1):
                mul.append(str(num) + " X " + str(i) + " = " + str(num*i))
        except ValueError:
            mul.append("It's not number.")
        return render(request, 'input.html', {'mul_list':mul, 'show_num': show_num})
    return render(request, 'input.html')
