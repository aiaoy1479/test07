from django.shortcuts import render, get_object_or_404
from .models import Total_input

def input(request):
    num_input = ""
    number = []
    if request.POST:
        num_input = request.POST['name']
        mul = []
        total = Total_input(num = num_input, total = 1)
        total.save()
        show_total = Total_input.objects.all()

        try:
            number = int(float(num_input))
            for i in range(1,13,1):
                mul.append(str(number) + " X " + str(i) + " = " + str(number*i))
        except ValueError:
            mul.append("It's not number.")
        return render(request, 'input.html', {'mul_list':mul, 'total': show_total})
    return render(request, 'input.html')
