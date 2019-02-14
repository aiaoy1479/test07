from django.shortcuts import render

def input(request):
    input_num = ""
    if request.POST:
        input_num = request.POST['name']
        mul = []
        try:
            num = int(float(input_num))
            for i in range(1,13,1):
                mul.append(str(num) + " X " + str(i) + " = " + str(num*i))
        except ValueError:
            mul.append("It's not number.")
        return render(request, 'input.html', {'mul_list':mul})
    return render(request, 'input.html')
