from django.shortcuts import render, redirect
import random

# Create your views here.
def root(request):
    if 'computer_guess' not in request.session:
        request.session['computer_guess'] = random.randint(1, 100)
    # context = {
    #     'too_low': request.session['too_low'],
    #     'too_high': request.session['too_high'],
    #     'just_right': request.session['just_right']
    # }
    return render(request,'index.html')

def guess(request):
    request.session['too_low'] = False,
    request.session['too_high'] = False,
    request.session['just_right'] = False

    if (int(request.POST['guess']) < request.session['computer_guess']):
        request.session['too_low'] = True
    elif (int(request.POST['guess']) > request.session['computer_guess']):
        request.session['too_high'] = True
    else:
        request.session['just_right'] = True
    return redirect('/')

def reset(request):
    request.session.flush()
    return redirect('/')