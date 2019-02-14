from django.shortcuts import render
from .models import Total_input

def input(request):
    num_input = ""
    if request.POST:
        num_input = request.POST['name']
        mul = []
        show_total = Total_input.objects.all()
        try:
            totals = Total_input.objects.get(num=num_input)
            totals.total += 1
            totals.save()
        except Total_input.DoesNotExist:
            totals = Total_input(num = num_input, total = 1)
            totals.save()

        try:
            number = int(float(num_input))
            for i in range(1,13,1):
                mul.append(str(number) + " X " + str(i) + " = " + str(number*i))
        except ValueError:
            mul.append("It's not number.")
        return render(request, 'input.html', {'mul_list':mul, 'total': show_total})
    return render(request, 'input.html')
