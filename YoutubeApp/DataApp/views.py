from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from googleapiclient.discovery import build
from .models import *



# Create your views here.
# API key: AIzaSyC7R7jYq97okNNfWGfbhWWmK8fXZ1D-eig
# Testing id: UCqZQlzSHbVJrwrn5XvzrzcA

def home(request):
    return render(request, 'DataApp/home.html')


def product(request):

    Image_url = "https://i.pinimg.com/originals/7d/c9/93/7dc993c70d4adba215b87cafdc59d82d.png"
    Description = "------"

    context = {
        "Image": Image_url,
        "Description": Description,
    }

    return render(request, 'DataApp/product.html', context)



def apiData(request):

    api_key = 'AIzaSyC7R7jYq97okNNfWGfbhWWmK8fXZ1D-eig'
    youtube = build('youtube','v3', developerKey=api_key)
    
    # Api Requests
    request1 = youtube.channels().list(
        part='statistics',
        id= "{}".format(request.POST['stats'])
    )

    request2 = youtube.channels().list(
        part='snippet',
        id= "{}".format(request.POST['stats'])
    )


    request3 = youtube.playlists().list(
        part='snippet',
        channelId= "{}".format(request.POST['stats'])
    )

    request4 = youtube.channels().list(
        part='contentOwnerDetails',
        id="{}".format(request.POST['stats'])
        
        
    )

    

    try:
        response = request1.execute()
        response2 = request2.execute()
        
        Data = f"Total Subscribers: {response['items'][0].get('statistics').get('subscriberCount')}"
        Data2 = f"Total Views: {response['items'][0].get('statistics').get('viewCount')}"
        Data3 = f"Total Videos:  {response['items'][0].get('statistics').get('videoCount')}"
        Description = f"{response2['items'][0].get('snippet').get('description')}"
        Location =f"{response2['items'][0].get('snippet').get('country')}"
        Image_url = f"{response2['items'][0].get('snippet').get('thumbnails').get('default').get('url')}"
        Channel = f"{response2['items'][0].get('snippet').get('title')}"
        Url = "https://www.youtube.com/channel/{}".format(request.POST['stats'])

        print(Description)
        
    except Exception:
        Url =""
        Data = "The Channel ID that you submitted is not valid."
        Data2 = ""
        Data3 = ""
        Description = "----"
        Location = "----"
        Image_url = "https://i.pinimg.com/originals/7d/c9/93/7dc993c70d4adba215b87cafdc59d82d.png"
        Channel = ""
        
    
    
    # Saves Channel data
    new_data = User_data(stats = request.POST.get('stats'))
    new_data.save()

    if Description == "":
        Description = "Not Applicable"

    

    context = {
        "Data": Data,
        "Data2": Data2,
        "Data3": Data3,
        "Channel": Channel,
        "Image": Image_url,
        "Url": Url,
        "Description": Description,
        "Location": Location,
    }

    return render(request, 'DataApp/product.html', context)