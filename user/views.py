from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from user.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from user.serializers import UserSerializer

@csrf_exempt
def user(request):
    if request.method == 'GET':
        user = User.objects.all()
        return render(request, 'user/user_list.html', {'user_list':user})

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def login(request):
    if request.method == 'POST':
        try:
            name = request.POST['name']
            User.objects.all().get(name=name)
            return render(request, 'user/success.html')
        except:
            return render(request, 'user/fail.html')
        
    elif request.method =='GET':
        return render(request, 'user/login.html') 
