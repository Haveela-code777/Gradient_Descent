from django.http import HttpResponse
import numpy
from django.shortcuts import render
from GDapp.models import Data
# Create your views here.

def regressor(x,y):
    m_curr = 0
    b_curr = 0
    iterations =10000
    n = len(x)
    learning_rate = 0.0001

    for i in range(iterations):
        y_pred = m_curr * x + b_curr  
        md = -(2/n)*sum(x*(y-y_pred))
        bd = -(2/n)*sum(y-y_pred)
        m_curr = m_curr - learning_rate*md
        b_curr = b_curr - learning_rate*bd
    return [m_curr,b_curr]
    
def home(request):
    return render(request,'gd.html')    

def gd(request):
    # x = numpy.array([70,80,90,100])
    # y = numpy.array([170,180,190,200])
    # print(x,y)
    if request.method == 'POST':
        x = list()
        y = list()
        data_objs = Data.objects.all()
        # --> Database Querysets "select * from Data d where d.feature > 70"
        for object in data_objs:
            x.append(object.feature)
            y.append(object.value)
        [m,b] = regressor(numpy.array(x),numpy.array(y))
        context = {"slope" : m, "Intercept" :b,"y":m*(int(request.POST["xdata"])) + b}
        return render(request,'result.html',context)
    return HttpResponse("Internal server error")
# Models Views Templates architecture

# URLS --->Request---> server ---> views.py -->models.py
                                    #   |
                                    #   |
                                    #   v
                                    #   templates