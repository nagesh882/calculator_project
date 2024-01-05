from django.shortcuts import render


def homePage(request):
    op = {}
    try:
        if request.method=="POST":
            n1 = eval(request.POST.get('num1'))
            n2 = eval(request.POST.get('num2'))
            opr = request.POST.get('opr')

            if opr=="+":
                op = n1 + n2
            elif opr=="-":
                op = n1 - n2
            elif opr=="*":
                op = n1 * n2
            elif opr =="/":
                op = n1 / n2
            
            op = {
                "op":op,
                "n1":n1,
                "n2":n2,
                "opr":opr,
            }
    except:
        print("Invalid Operation......")

        
    return render(request, "calculator.html", op)