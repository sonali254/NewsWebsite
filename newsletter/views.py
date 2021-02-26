from django.shortcuts import render, redirect
from .models import Newsletter
# Create your views here.
def newsletter_add(request):
    if request.method == 'POST':

        txt = request.POST.get('txt')

        res = txt.find('@')

        if int(res) != -1:
            b = Newsletter(txt=txt, status=1)
            b.save()
        else:

            try:

                int(txt)
                b = Newsletter(txt=txt, status=2)
                b.save()

            except:

                return redirect('home')

    return redirect('home')

def email(request):
    # login check start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # login check end

    email=Newsletter.objects.filter(status=1)
    return render(request, 'back/email.html', {'email':email})


def phone(request):
    # login check start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # login check end

    phone = Newsletter.objects.filter(status=2)

    return render(request, 'back/phone.html', {'phone': phone})


def news_txt_del(request, pk, num):
    # login check start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # login check end

    b = Newsletter.objects.get(pk=pk)
    b.delete()

    if int(num) == 2:
        return redirect('phone')

    return redirect('email')