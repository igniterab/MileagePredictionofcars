from django.shortcuts import render
from django.http import HttpResponse
import joblib
import pandas as pd
import numpy as np

ReloadModel = joblib.load('./mlmodel/RFModelforMPG.pkl')


def index(request):
    return render(request, 'index.html')


def PredictMPG(request):
    try:
        temp = {}
        if request.method == 'POST':
            temp['cylinders'] = request.POST.get('cylinders')
            temp['displacement'] = request.POST.get('displacement')
            temp['horsepower'] = request.POST.get('horsepower')
            temp['weight'] = request.POST.get('weight')
            temp['acceleration'] = request.POST.get('acceleration')
            temp['model year'] = request.POST.get('model')
            temp['origin'] = request.POST.get('origin')

        testdata = pd.DataFrame({'X': temp}).transpose()
        score_predicted = ReloadModel.predict(testdata)[0]
        score_predicted = np.ceil(score_predicted)
        return render(request, 'res.html', {'score': score_predicted})
    except:
        return HttpResponse("<h2>All fields are mandatory kindly fill them all</h2>")
