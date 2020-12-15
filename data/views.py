from django.shortcuts import render

from .models import Apod

import requests

# from PIL import Image

import time,schedule

from django.shortcuts import render,get_object_or_404

from django.shortcuts import redirect #нужно для перехода на какую-либо html страницу

from .forms import DataForm,DataInTimeForm #форма для получения даты

def main_page(request):

    return render(request,'main_page.html')

def received_data(request):

    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():

            year = form.cleaned_data.get('year')
            month = form.cleaned_data.get('month')
            day = form.cleaned_data.get('day')

            URL = 'https://api.nasa.gov/planetary/apod'

            PARAMS = {'api_key':'YhdS3u89MYhYPTqhfRbsaSZGAffATbIEumF0Xt1H','date':str(year) + '-' + str(month) + '-' + str(day),'hd':True}

            r = requests.get(url = URL,params = PARAMS)

            a = r.json()

            new_apod = Apod()
            new_apod.pub_date = a.get('date')
            new_apod.explanation = a.get('explanation')
            new_apod.title = a.get('title')

            new_apod.image_url = a.get('url')
            if a.get('hdurl') != None:
                new_apod.image_hd_url = a.get('hdurl')
            else:
                new_apod.image_hd_url = a.get('url')

            new_apod.media_type = a.get('media_type')
            new_apod.service_version = a.get('service_version')

            new_apod.save()

            return redirect('received_data')
    else:
        form = DataForm()



    data = Apod.objects.order_by('-received_date')


    return render(request,'received_data.html',{'data':data,'form':form})

def extended_info(request,pk):
    apod = get_object_or_404(Apod,pk = pk)

    return render(request,'extended_info.html',{'apod':apod})
