from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from .models import Main
from news.models import News
from cat.models import Cat
from subcat.models import Subcat
from django.contrib.auth import authenticate, login, logout
from trending.models import Trending
from django.contrib.auth.models import User
from manager.models import Manager
from ipware import get_client_ip
from ip2geotools.databases.noncommercial import DbIpCity




# Create your views here.
def home(request):
    site = Main.objects.get(pk=1)
    news = News.objects.filter(act=1).order_by('-pk')
    cat = Cat.objects.all()
    subcat = Subcat.objects.all()
    lastnews = News.objects.filter(act=1).order_by('-pk')[:3]
    popnews = News.objects.filter(act=1).order_by('-show')
    popnews2 = News.objects.filter(act=1).order_by('-show')[:3]
    trending = Trending.objects.all()
    return render(request, 'font/home.html',
                  {'site': site, 'news': news, 'cat': cat, 'subcat': subcat, 'lastnews': lastnews, 'popnews': popnews,
                   'trending': trending, 'popnews2':popnews2})


def about(request):
    site = Main.objects.get(pk=1)
    return render(request, 'font/about.html', {'site': site})


def panel(request):
    # login start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # login end
    return render(request, 'back/home.html')


def register(request):
    if request.method == 'POST':

        name = request.POST.get('name')
        uname = request.POST.get('uname')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if name == "":
            msg = "Input Your Name"
            return render(request, 'font/msgbox.html', {'msg': msg})

        if password1 != password2:
            msg = "Your Pass Didn't Match"
            return render(request, 'font/msgbox.html', {'msg': msg})

        count1 = 0
        count2 = 0
        count3 = 0
        # count4 = 0

        for i in password1:

            if i > "0" and i < "9":
                count1 = 1
            if i > "A" and i < "Z":
                count2 = 1
            if i > 'a' and i < 'z':
                count3 = 1
            # if i > "!" and i < "(":
            #     count4 = 1

        if count1 == 0 or count2 == 0 or count3 == 0:
            msg = "Your Pass Is Not Strong"
            return render(request, 'font/msgbox.html', {'msg': msg})

        if len(password1) < 8:
            msg = "Your Pass Most Be 8 Character"
            return render(request, 'font/msgbox.html', {'msg': msg})
        if len(User.objects.filter(username=uname)) == 0 and len(User.objects.filter(email=email)) == 0:
            ip, is_routable = get_client_ip(request)
            if ip is None:
                ip = "0.0.0.0"
            try:

                response = DbIpCity.get(ip, api_key='free')
                country = response.country + " | " + response.city

            except:

                country = "Unknown"

            user = User.objects.create_user(username=uname, email=email, password=password1)
            user.save()

            b = Manager(name=name, utxt=uname, email=email, ip=ip, country=country)

            b.save()

    return render(request, 'font/mylogin.html')


def mylogin(request):
    if request.method == "POST":
        utxt = request.POST.get('username')
        ptxt = request.POST.get('password')
        if utxt != "" and ptxt != "":
            user = authenticate(username=utxt, password=ptxt)
        if user != None:
            login(request, user)
            return redirect('panel')

    return render(request, 'font/mylogin.html')


def mylogout(request):
    logout(request)
    return redirect('mylogin')


def changepass(request):
    # login check start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # login check end

    if request.method == 'POST':

        oldpass = request.POST.get('oldpass')
        newpass = request.POST.get('newpass')

        if oldpass == "" or newpass == "":
            error = "All Fields Requirded"
            return render(request, 'back/error.html', {'error': error})

        user = authenticate(username=request.user, password=oldpass)

        if user != None:

            if len(newpass) < 8:
                error = "Your Password Most Be At Less 8 Character"
                return render(request, 'back/error.html', {'error': error})

            count1 = 0
            count2 = 0
            count3 = 0
            # count4 = 0

            for i in newpass:

                if i > "0" and i < "9":
                    count1 = 1
                if i > "A" and i < "Z":
                    count2 = 1
                if i > "a" and i < "z":
                    count3 = 1
                # if i > "`" and i < "-" :
                #     count4 = 1

            if count1 == 1 and count2 == 1 and count3 == 1:
                user = User.objects.get(username=request.user)
                user.set_password(newpass)
                user.save()

                return redirect('mylogout')

        else:

            error = "Your Password Is Not Correct"
            return render(request, 'back/error.html', {'error': error})

    return render(request, 'back/changepass.html')


def site_settings(request):
    # login check start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # login check end

    perm = 0
    for i in request.user.groups.all():
        if i.name == "masteruser": perm = 1

    if perm == 0:
        error = "Access Denied"
        return render(request, 'back/error.html', {'error': error})

    if request.method == 'POST':

        name = request.POST.get('name')
        tell = request.POST.get('tell')
        fb = request.POST.get('fb')
        tw = request.POST.get('tw')
        yt = request.POST.get('yt')
        link = request.POST.get('link')
        txt = request.POST.get('txt')

        if fb == "": fb = "#"
        if tw == "": tw = "#"
        if yt == "": yt = "#"
        if link == "": link = "#"

        if name == "" or tell == "" or txt == "":
            error = "All Fields Requirded"
            return render(request, 'back/error.html', {'error': error})

        try:

            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            url = fs.url(filename)

            picurl = url
            picname = filename

        except:

            picurl = "-"
            picname = "-"

        try:

            myfile2 = request.FILES['myfile2']
            fs2 = FileSystemStorage()
            filename2 = fs2.save(myfile2.name, myfile2)
            url2 = fs2.url(filename2)

            picurl2 = url2
            picname2 = filename2

        except:

            picurl2 = "-"
            picname2 = "-"

        b = Main.objects.get(pk=1)
        b.name = name
        b.tell = tell
        b.fb = fb
        b.tw = tw
        b.yt = yt
        b.link = link
        b.about = txt

        if picurl != "-": b.picurl = picurl
        if picname != "-": b.picname = picname
        if picurl2 != "-":  b.picurl2 = picurl2
        if picname2 != "-": b.picname2 = picname2

        b.save()

    site = Main.objects.get(pk=1)

    return render(request, 'back/site_settings.html', {'site': site})


def aboutsettings(request):
    if request.method == 'POST':

        txt = request.POST.get('txt')

        if txt == "":
            error = "All Fields Required"
            return render(request, 'back/error.html', {'error': error})

        b = Main.objects.get(pk=1)
        b.abouttxt = txt
        b.save()

    about = Main.objects.get(pk=1).abouttxt

    return render(request, 'back/aboutsettings.html', {'about': about})
