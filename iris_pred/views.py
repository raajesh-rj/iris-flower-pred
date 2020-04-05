from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View 
from .forms import *
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from tensorflow.keras.models import load_model
import joblib
import json
import numpy as np


# flower_model = load_model(settings.FLOWER_MODEL_PATH + '/final_iris_model_RJ.h5')
# flower_scaler = joblib.load(settings.FLOWER_MODEL_PATH + '/iris_scaler.pkl')




# Create your views here.
@csrf_exempt
def model_prediction(request):
    # return HttpResponse('<h3>Welcome to iris predictions</h3>')
    flower_form = FlowerForm(request.POST)
    context = {'flower_form':flower_form}
    if request.method == 'POST':
        print('Inside post')
        flower_form = FlowerForm(request.POST)
        if flower_form.is_valid():
            sepal_length = flower_form.cleaned_data['sepal_length']
            sepal_width = flower_form.cleaned_data['sepal_width']
            petal_length = flower_form.cleaned_data['petal_length']
            petal_width = flower_form.cleaned_data['petal_width']
            
            flower_model = load_model(settings.FLOWER_MODEL_PATH + '/final_iris_model_RJ.h5')
            flower_scaler = joblib.load(settings.FLOWER_MODEL_PATH + '/iris_scaler.pkl')
            
            flower = np.array([sepal_length, sepal_width, petal_length, petal_width]).reshape(-1,4)
            flower = flower_scaler.transform(flower)
            classes = np.array(['setosa', 'versicolor', 'virginica'])
            class_ind = flower_model.predict_classes(flower)[0]
            output = classes[class_ind]
            context.update({'flower_prediction': classes[class_ind]})
    
    return render(request,'iris-pred.html', context)




class Iris(View):
    template_name = 'iris-pred.html'
    flower_form = FlowerForm()
    context = {'flower_form':flower_form}
    flower_model = load_model(settings.FLOWER_MODEL_PATH + '/final_iris_model_RJ.h5')
    flower_scaler = joblib.load(settings.FLOWER_MODEL_PATH + '/iris_scaler.pkl')

    def get(self,request):
        return render(request, self.template_name, self.context)

    def post(self,request):
        flower_form = FlowerForm(request.POST)
        if flower_form.is_valid():
            sepal_length = flower_form.cleaned_data['sepal_length']
            sepal_width = flower_form.cleaned_data['sepal_width']
            petal_length = flower_form.cleaned_data['petal_length']
            petal_width = flower_form.cleaned_data['petal_width']

            flower = np.array([sepal_length, sepal_width, petal_length, petal_width]).reshape(-1,4)
            flower = self.flower_scaler.transform(flower)
            classes = np.array(['setosa', 'versicolor', 'virginica'])
            class_ind = self.flower_model.predict_classes(flower)[0]
            self.context.update({'flower_prediction': classes[class_ind]})

            return render(request, self.template_name, self.context)
