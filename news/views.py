from django.shortcuts import render, redirect

from trending.models import Trending
from .models import News
from main.models import Main
from django.core.files.storage import FileSystemStorage
import datetime
from subcat.models import Subcat
from cat.models import Cat
from comment.models import Comment
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

# Create your views here.
def news_details(request, word):
    site = Main.objects.get
    shownews=News.objects.filter(name=word)
    news = News.objects.all().order_by('-pk')
    cat = Cat.objects.all()
    subcat = Subcat.objects.all()
    lastnews = News.objects.all().order_by('-pk')[:3]
    popnews = News.objects.all().order_by('-show')
    popnews2 = News.objects.all().order_by('-show')[:3]
    trending = Trending.objects.all().order_by('-pk')[:5]

    try:
        mynews = News.objects.get(name=word)
        mynews.show = mynews.show + 1
        mynews.save()

    except:
        print("can't add show")
    code = News.objects.get(name=word).pk
    comment = Comment.objects.filter(news_id=code, status=1).order_by('-pk')[:3]
    cmcount = len(comment)

    return render(request, 'font/news_details.html', {'site':site, 'news':news, 'cat':cat, 'subcat':subcat, 'lastnews':lastnews, 'code':code, 'shownews':shownews,'popnews':popnews, 'popnews2':popnews2, ' trending': trending, 'comment':comment, 'cmcount':cmcount })

def newslist(request):
    # login start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # login end
    perm = 0
    for i in request.user.groups.all():
        if i.name == "masteruser": perm = 1

    if perm == 0:
        news = News.objects.filter(writer=request.user)
    elif perm == 1:
        newss = News.objects.all()
        paginator = Paginator(newss, 3)
        page = request.GET.get('page')

        try:
            news = paginator.page(page)

        except EmptyPage:
            news = paginator.page(paginator.num_page)

        except PageNotAnInteger:
            news = paginator.page(1)

    #news= News.objects.all()
    return render(request, 'back/newslist.html', {'news':news})

def newsadd (request):
    # login start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # login end
    now=datetime.datetime.now()
    year=now.year
    day=now.day
    month=now.month
    if len(str(day)) == 1:
        day="0" + str(day)
    if len(str(month)) ==1:
        month="0"+str(month)
    today=(str(year) + "/" + str(month) + "/" + str(day))
    time=str(now.hour)+ ":" + str(now.minute) + ":" +str(now.second)

    cat=Subcat.objects.all()


    if request.method=='POST':
        newstitle = request.POST.get('newstitle')
        showtxt = request.POST.get('showtxt')
        bodytxt = request.POST.get('bodytxt')
        newscat = request.POST.get('newscat')
        newsid = request.POST.get('newscat')
        if newstitle == '' or showtxt == '' or bodytxt == '' or newscat == '':
            error = "All field requried"
            return render(request, 'back/error.html', {'error': error})
        try:
            myfile=request.FILES['myfile']
            fs=FileSystemStorage()
            filename=fs.save(myfile.name, myfile)
            url=fs.url(filename)
            if str(myfile.content_type).startswith("image"):
                if myfile.size<5000000:
                    newsname=Subcat.objects.get(pk=newsid).name
                    ocat_id=Subcat.objects.get(pk=newsid).cat_id
                    b = News(name=newstitle, show_txt=showtxt, body_txt=bodytxt, cat_name=newsname, date=today, writer=request.user, cat_id=0, ocat_id=ocat_id, picname=filename, picurl=url, time=time, show=0)
                    b.save()
                    count=len(News.objects.filter(ocat_id=ocat_id))
                    b=Cat.objects.get(pk=ocat_id)
                    b.count=count
                    b.save()
                    return redirect('newslist')
                else:
                    fs = FileSystemStorage()
                    fs.delete(filename)
                    error = "image size must be less than 5mb"
                    return render(request, 'back/error.html', {'error': error})
            else:
                fs = FileSystemStorage()
                fs.delete(filename)
                error = "your file is not image file"
                return render(request, 'back/error.html', {'error': error})

        except:
            error = "please input your image"
            return render(request, 'back/error.html', {'error': error})





    return render(request, 'back/newsadd.html', {'cat':cat})

def news_delete(request, pk):
    # login start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # login end
    try:
        b=News.objects.get(pk=pk)
        fs=FileSystemStorage()
        fs.delete(b.picname)
        ocat_id=News.objects.get(pk=pk).ocat_id
        count = len(News.objects.filter(ocat_id=ocat_id))
        m = Cat.objects.get(pk=ocat_id)
        m.count = count
        m.save()
        b.delete()
    except:
        error = "something went wrong"
        return render(request, 'back/error.html', {'error': error})

    return redirect('newslist')

def news_edit(request, pk):
    # login start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # login end
    if len(News.objects.filter(pk=pk))==0 :
        error = "news not found"
        return render(request, 'back/error.html', {'error': error})

    news=News.objects.get(pk=pk)
    cat = Subcat.objects.all()

    if request.method == 'POST':
        newstitle = request.POST.get('newstitle')
        showtxt = request.POST.get('showtxt')
        bodytxt = request.POST.get('bodytxt')
        newscat = request.POST.get('newscat')
        newsid = request.POST.get('newscat')
        if newstitle == '' or showtxt == '' or bodytxt == '' or newscat == '':
            error = "All field requried"
            return render(request, 'back/error.html', {'error': error})
        try:
            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            url = fs.url(filename)
            if str(myfile.content_type).startswith("image"):
                if myfile.size < 5000000:
                    newsname = Subcat.objects.get(pk=newsid).name

                    b =News.objects.get(pk=pk)
                    fss = FileSystemStorage()
                    fss.delete(b.picname)

                    b.show_txt=showtxt
                    b.body_txt=bodytxt
                    b.name=newstitle
                    b.picname=filename
                    b.picurl=url
                    b.writer="-"
                    b.cat_name=newsname
                    b.cat_id=newsid
                    b.save()
                    return redirect('newslist')
                else:
                    fs = FileSystemStorage()
                    fs.delete(filename)
                    error = "image size must be less than 5mb"
                    return render(request, 'back/error.html', {'error': error})
            else:
                fs = FileSystemStorage()
                fs.delete(filename)
                error = "your file is not image file"
                return render(request, 'back/error.html', {'error': error})

        except:
            newsname = Subcat.objects.get(pk=newsid).name

            b = News.objects.get(pk=pk)

            b.show_txt = showtxt
            b.body_txt = bodytxt
            b.name = newstitle
            b.cat_name = newsname
            b.cat_id = newsid
            b.save()
            return redirect('newslist')
    return render(request, 'back/news_edit.html', {'pk':pk, 'news':news, 'cat':cat } )
def news_publish(request, pk):
    news=News.objects.get(pk=pk)
    news.act=1
    news.save()
    return redirect('newslist')

def news_all_show(request,word):

    catid = Cat.objects.get(name=word).pk
    allnews = News.objects.filter(ocatid=catid)

    site = Main.objects.get(pk=2)
    news = News.objects.filter(act=1).order_by('-pk')
    cat = Cat.objects.all()
    subcat = Subcat.objects.all()
    lastnews = News.objects.filter(act=1).order_by('-pk')[:3]
    popnews = News.objects.filter(act=1).order_by('-show')
    popnews2 = News.objects.filter(act=1).order_by('-show')[:3]
    trending = Trending.objects.all().order_by('-pk')[:5]
    lastnews2 = News.objects.filter(act=1).order_by('-pk')[:4]

    return render(request, 'front/all_news.html', {'site':site, 'news':news, 'cat':cat, 'subcat':subcat, 'lastnews':lastnews, 'popnews':popnews, 'popnews2':popnews2, 'trending':trending, 'lastnews2':lastnews2, 'allnews':allnews})
