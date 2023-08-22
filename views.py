from django.shortcuts import render

# Create your views here.
def index(req):
    return render(req,'index.html')
def chokolate(req,id):
    id=int(id)
    if id==0:
        name='Snickers'
        img='img/img.png'
        text='Не тормзи -- сникерсни'
    elif id==1:
        name='Mars'
        img='img/img_1.png'
        text='Марс выручай, силу мне давай'
    elif id==2:
        name='Nuts'
        img='img/img_2.png'
        text='Бeлки наше всё, белки выручат нас, а потом мы их'
    elif id==3:
        name='Twix'
        img='img/img_3.png'
        text='Такие разные и похожие, но очень вкусные)'
    elif id==4:
        name='MilkyWay'
        img='img/img_4.png'
        text='Ничего лучше нет, чем с другом съесть MilkyWay'
    data={'id':id,'k1':name,'k2':img,'k3':text}
    return render(req,'prochokolad.html',context=data)

