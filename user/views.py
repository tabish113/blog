from django.shortcuts import render,redirect
from punjabi.models import Room, Booking, Order, Gallery,Restaurant,Contact
from django.contrib.auth.models import User, auth

# Create your views here.
def adminlogin(request):
    if request.method=='POST':
        unm=request.POST['unm']
        ps=request.POST['ps']
        if unm=='punjabi113' and ps=='0526ec96':
            user = auth.authenticate(username=unm,password=ps)
            if user is not None:
                auth.login(request, user)
                return redirect('home')
            else:

                return render(request,'adminlogin.html',{'msg':'User Name and Password Not Exits..!'})

        else:
            return render(request,'adminlogin.html',{'msg':'User Name and Password Not Exits..!'})

    else:
        return render(request,'adminlogin.html')


def home(request):
    data=Booking.objects.all().filter(status='pending')
    data1=Booking.objects.all().filter(status='done')

    return render(request, 'home.html',{'data':data,'data1':data1})

def  addroom(request):
    if request.method=='POST':
        id = request.POST.get('id')
        nm = request.POST.get('nm','null')
        number = request.POST.get('no','null')
        space = request.POST.get('space','null')
        guest = request.POST.get('guest','null')
        price = request.POST.get('price','null')
        # i1 = request.POST.get('i1','null')
        # i2 = request.POST.get('i2','null')
        # i3 = request.POST.get('i3','null')
        # i4 = request.POST.get('i4','null')
        # i5 = request.POST.get('i5','null')
        # i6 = request.POST.get('i6','null')
        #
        # img1 = request.FILES.get('img1',i1)
        # img2 = request.FILES.get('img2',i2)
        # img3 = request.FILES.get('img3',i3)
        # img4 = request.FILES.get('img4',i4)
        # img5 = request.FILES.get('img5',i5)
        # img6 = request.FILES.get('img6',i6)
        update=Room.objects.filter(id=id).update(nm=nm,number=number,space=space,guest=guest,price=price)
        data=Room.objects.all()
        return render(request, 'add-room.html', {'data':data,'msg':'Update Successfully..!'})
    else:
        data=Room.objects.all()
        return render(request, 'add-room.html', {'data':data})


def newroom(request):
    if request.method=="POST":
        nm = request.POST.get('nm','null')
        number = request.POST.get('number','null')
        space = request.POST.get('space','null')
        guest = request.POST.get('max','null')
        price = request.POST.get('price','null')
        img1 = request.FILES.get('img1','img1')
        img2 = request.FILES.get('img2','img2')
        img3 = request.FILES.get('img3','img3')
        img4 = request.FILES.get('img4','img4')
        img5 = request.FILES.get('img5','img1')
        img6 = request.FILES.get('img6','img1')
        insert =Room(nm=nm,number=number,space=space,guest=guest,price=price,img1=img1,img2=img2,img3=img3,img4=img4,img5=img5,img6=img6)
        insert.save()
        return render(request, 'new-room.html',{'thank':'thank'})
    else:
        return render(request, 'new-room.html')

def deletebooking(request, rid):
        Order.objects.filter(booking_id=rid).delete()
        Booking.objects.get(id=rid).delete()
        return render(request, 'home.html',{'msg':'Delete Successfully..!'})

def confirm(request, cid):
    Booking.objects.filter(id=cid).update(status='done')
    return render(request, 'home.html',{'msg':'Booking Confirm Successfully..!'})

def allbooking(request):
    data1=Booking.objects.all().filter(status='done')
    return render(request,'all-booking.html',{'data1':data1})

def gallery(request):
    if request.method=='POST':
        id=request.POST.get('id')
        delete=Gallery.objects.get(id=id).delete()
        data=Gallery.objects.all()
        return render(request,'gallery.html',{'data':data,'msg':'msg'})
    else:
        data=Gallery.objects.all()
        return render(request,'gallery.html',{'data':data})

def new_gallery(request):
    if request.method=='POST':
        nm=request.POST.get('nm','null')
        img=request.FILES.get('img','img not found')
        insert=Gallery(nm=nm,img=img)
        insert.save()
        return render(request,'add_gallery.html',{'thank':'thank'})
    else:
        return render(request,'add_gallery.html')

def show_restaurant(request):
    if request.method=='POST':
        nm=request.POST.get('nm')
        title=request.POST.get('title')
        price=request.POST.get('price')
        cat=request.POST.get('cat')
        id=request.POST.get('id')

        update=Restaurant.objects.filter(id=id).update(nm=nm,title=title,price=price,cat=cat)
        data=Restaurant.objects.all()
        return render(request,'show_restaurant.html',{'data':data,'msg':'Update Successfully..!'})
    else:
        data=Restaurant.objects.all()
        return render(request,'show_restaurant.html',{'data':data})


def add_restaurant(request):
    if request.method=='POST':
        nm=request.POST.get('nm')
        title=request.POST.get('title')
        price=request.POST.get('price')
        cat=request.POST.get('cat')
        insert=Restaurant(nm=nm,title=title,price=price,cat=cat)
        insert.save()
        return render(request,'add_restaurant.html',{'msg':'Insert Successfully..!'})
    else:
        return render(request,'add_restaurant.html')

def delete_restaurant(request):
    if request.method=='POST':
        id=request.POST.get('id')
        Restaurant.objects.get(id=id).delete()
        data=Restaurant.objects.all()
        return render(request,'show_restaurant.html',{'data':data,'msg':'Delete Successfully..!'})

def show_contact(request):
    if request.method=='POST':
        id=request.POST.get('id')
        Contact.objects.get(id=id).delete()
        data=Contact.objects.all()
        return render(request,'show_contact.html',{'data':data,'msg':'Contact Delete Successfully..!'})

    else:
        data=Contact.objects.all()
        return render(request,'show_contact.html',{'data':data})
def delete_room(request,rmid):
    delete = Room.objects.filter(id=rmid).delete()
    return render(request,'add-room.html',{'msg':'Delete Successfully..!'})
