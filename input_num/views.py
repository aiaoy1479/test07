from django.shortcuts import render

def input(request):
    input_num = ""
    if request.POST:
        input_num = request.POST['name']
        try:
            if float(input_num)*0 == 0:
                pass
        except ValueError:
            input_num = "It's not number."
        return render(request, 'input.html', {'out_num': input_num})
    return render(request, 'input.html')
