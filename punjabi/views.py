from django.shortcuts import render, redirect
from .models import Room, Booking, Order,Gallery,Restaurant,Contact
from django.contrib.auth.models import User, auth
from datetime import date
from django.db.models import Q
import requests
from datetime import date
# Create your views here.
today = date.today()


def login(request):
    if request.method=='POST':
        unm=request.POST['unm']
        ps=request.POST['ps']
        user = auth.authenticate(username=unm,password=ps)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return render(request,'login.html',{'error':'User Name Not Exits..!'})

    else:
        return render(request,'login.html')



def reg(request):
    if request.method=='POST':
        nm = request.POST['nm']
        no = request.POST['no']
        add = request.POST['add']
        uid = request.POST['uid']
        ps = request.POST['ps']
        cps = request.POST['cps']
        if ps!=cps:
            return render(request,'register.html',{'error':'Password Not Matched..!'})
        else:
            if User.objects.filter(username=no).exists():
                return render(request,'register.html',{'error':'User Name Exits..!'})
            else:
                user = User.objects.create_user(username=no,password=ps,email=add,first_name=nm,last_name=uid)
                user.save()
                auth.login(request, user)
                return render(request,'register.html',{'success':'success'})

    else:
        return render(request,'register.html')


def index(request):
    gallery=Gallery.objects.all()
    return render(request,'index.html',{'gallery':gallery})


def room(request):
    if request.method =='POST':
        sdate = request.POST.get('sdate')
        edate = request.POST.get('edate')
        # date correct filter section
        print(sdate)
        print(edate)

        c1=sdate[3:5]
        c2=edate[3:5]
        month=edate[0:2]
        month1=sdate[0:2]
        # working on today datetime
        d2 = today.strftime("%m/%d/%Y")
        todayc1=d2[3:5]
        todaym=d2[0:2]

        # end section
        if c1>c2 and month1==month:
            return render(request,'index.html',{'msg':'You enter wrong date..!'})
        elif c1<todayc1 and month1==todaym:
            return render(request,'index.html',{'msg':'You enter wrong date..!'})
        # end
        if c1==str(31) and month1==str(12):
           edate=sdate
           order=Order.objects.filter(startdate__range=(sdate, edate))
        else:
           order=Order.objects.filter(startdate__range=(sdate, edate))



        order_count=order.count()
        print(order_count)
        a=[]

        for i in order:
            room_id=i.room_id

            a.append(room_id)
            values = a
            queries = [Q(pk=value) for value in values]
            query = queries.pop()
            for item in queries:
                query |= item

        if order_count>0:
            data = Room.objects.filter(~Q(query))
            dist={'data':data,'sdate':sdate,'edate':edate}
            return render(request, 'room.html',dist)
        else:
             data = Room.objects.all()
             dist={'data':data,'sdate':sdate,'edate':edate}
             return render(request, 'room.html',dist)

    else:
        data = Room.objects.all()
        return redirect('/')



def roomview(request, id):

    data = Room.objects.filter(id=id)
    return render(request,'room-view.html',{'data':data})


def contact(request):
    if request.method=='POST':
        nm=request.POST.get('nm')
        em=request.POST.get('em')
        no=request.POST.get('no')
        sub=request.POST.get('sub')
        msg=request.POST.get('msg')
        insert=Contact(nm=nm,em=em,no=no,sub=sub,msg=msg)
        insert.save()
        return render(request, 'contact.html',{'thank':'Your Request Has Been Sent..!'})
    else:
        return render(request, 'contact.html')


def booking(request):
    if request.method=="POST":
        nm = request.POST['nm']
        uid=request.POST['uid']
        rnm=request.POST['rnm']
        price=request.POST['price']
        startdate=request.POST['startdate']
        enddate=request.POST['enddate']
        rid=request.POST['rid']
        unm=request.POST['unm']
        adds=request.POST['adds']
        insert=Booking(nm=nm,uid=uid,no=unm,adds=adds,rid=rid,room_name=rnm,price=price,startdate=startdate,enddate=enddate,payment='COD',status='pending')
        insert.save()
        book_id=insert.id
        c1=startdate[3:5]
        c2=enddate[3:5]
        month=enddate[0:2]
        month1=startdate[0:2]

        year=enddate[6:10]
        year1=startdate[6:10]

        dt=month + '/' + c1 + '/'+year
        if c1<c2 and month==month1:
            count= int(c2) - int(c1)
        elif month1==str(10) and int(c1)==31 and c2==str(0)+str(2):
            count=2

        elif month1==str(11) and int(c1)==30 and c2==str(0)+str(2):
             count=2

        elif month1==str(12) and int(c1)==31 and c2==str(0)+str(2):
            count=2



        else:
            count=1


        c3=0
        while (count>c3):
            dt=month1 + '/' + str(c1) + '/'+str(year1)

            order=Order(booking_id=book_id,startdate=dt,enddate=enddate,room_id=rid)
            order.save()

            if int(c1)>8:
                c1=int(c1)+ 1
            else:
                c1=int(c1)+ 1
                c1=str(0)+str(c1)
            if month1==str(10) and int(c1)>31 and c2==str(0)+str(2):
               c1=str(0)+str(1)
               month1=str(11)

            elif month1==str(11) and int(c1)>30 and c2==str(0)+str(2):
                  c1=str(0)+str(1)
                  month1=str(12)

            elif month1==str(12) and int(c1)>31 and c2==str(0)+str(2):
                     c1=str(0)+str(1)
                     month1=str(0)+str(1)
                     year1=2020

            c3=c3+1

        return render(request,'booking.html',{'thank':'thank'})

    else:
        return render(request,'booking.html')


def logout(request):
    auth.logout(request)
    return redirect('/')

def restaurant(request):
    data=Restaurant.objects.all()
    return render(request,'restaurant.html',{'data':data})

def review(request):
    return render(request,'review.html')

def select(request):
    return render(request,'select.html')
