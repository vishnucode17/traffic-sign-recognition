from django.shortcuts import render
import numpy as np
import tensorflow as tf
from PIL import Image
from keras.models import load_model
from urllib.request import Request
import urllib.request as req
# Create your views here.
label_dict={
    0:"speed limit 20 km/h",
    1:"speed limit 30 km/h",
    2:"speed limit 50 km/h",
    3:"speed limit 60 km/h",
    4:"speed limit 70 km/h",
    5:"speed limit 80 km/h",
    6:"End of speed limit 80 km/h",
    7:"speed limit 100 km/h",
    8:"speed limit 120 km/h",
    9:"No passing",
    10:"No passing vehicles over 3.5 tons",
    11:"Right of the wat ar intersection",
    12:"priority road",
    13:"Yield",
    14:"Stop",
    15:"No vehicles",
    16:"Vehicles above 3.5 tons prohibited",
    17:"No entry",
    18:"General caution",
    19:"Dangerous curve left",
    20:'Dangerous curve right', 
            21:'Double curve', 
            22:'Bumpy road', 
            23:'Slippery road', 
            24:'Road narrows on the right', 
            25:'Road work', 
            26:'Traffic signals', 
            27:'Pedestrians', 
            28:'Children crossing', 
            29:'Bicycles crossing', 
            30:'Beware of ice/snow',
            31:'Wild animals crossing', 
            32:'End speed + passing limits', 
            33:'Turn right ahead', 
            34:'Turn left ahead', 
            35:'Ahead only', 
            36:'Go straight or right', 
            37:'Go straight or left', 
            38:'Keep right', 
            39:'Keep left', 
            40:'Roundabout mandatory', 
            41:'End of no passing', 
            42:'End no passing veh > 3.5 tons'
}

def Home(request):
    model=load_model('./traffic_sign.h5')
    result=""
    graph_div=""
    img_url=''
    a=np.array([])
    if request.method == "POST":
        try:
            img_url=request.POST['img_url']
            test_img=req.urlretrieve(img_url,"new_image.png")
            test_image=Image.open("new_image.png").convert('RGB')
            test_image=test_image.resize((30,30))
            test_image=np.array(test_image)
            test_image=test_image/255
            image_pred=model.predict_classes([np.expand_dims(test_image, 0)])[0]
            new_img_pred=model.predict(np.expand_dims(test_image,0))
            a=list(new_img_pred[0]*100)
            result=label_dict[image_pred]
            
        except:
            result="Image not loaded properly!"
    return render(request,'index.html',{'result':result,'img_url':img_url,'a':a})
