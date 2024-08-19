from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib.sessions import *
from .models import Members
from .forms import CustomUserForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from .utils import send_email_to_client

# Create your views here.

flag = False

def members(request):
    return render(request,"first.html")


# Register Endpoint
def Register(request):
    data = request.session.get('data')
    print(data)
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            customer = form.save(commit=False)
            password = form.cleaned_data['password']
            customer.password = make_password(password)
            usermail = [customer.Useremail]
            send_email_to_client(usermail)
            
            customer.save()
            data = request.session.get('data')
            storage = {
                'Fitness_goal': data[0],
                'Fitness_level': data[1],
                'week_time': data[2],
            }
            print(storage)
            for key, value in storage.items():
                setattr(customer,key,value)
            customer.save()    

            print("You are Successfully registered")
            return render(request,"Jsxlogin.html")


    # print(flag)        
    
    return render(request,"Register.html")


# login endpoint
def Login(request):

    if request.method == "POST":
        entered_email = request.POST.get("Useremail")
        entered_password = request.POST.get("password")
        user = Members.objects.get(Useremail = entered_email)
        if check_password(entered_password,user.password):
            request.session['user_id'] = user.id
            request.session['email'] = user.Useremail
            print('Customer Exists')
            global flag 
            flag = True
            print(flag)
            # global user_timer

            # usermail= [entered_email]
            # send_email_to_client(usermail)
            return render(request,"index.html",{'flag': flag})
        else :
            print("Invalid Credentials")

    return render(request,"Jsxlogin.html")


def questionnarire_processing(request):
    if request.method == 'POST':
       question_1 = request.POST.get('dropdown1') 
       question_2 = request.POST.get('dropdown2') 
       question_3 = request.POST.get('dropdown3') 
    #    print(question_1, question_2, question_3)
       request.session['data'] = [question_1, question_2, question_3]
       return render(request,"register.html",{'flag': flag})
    
    
    return render(request, "questionnaire.html")

def Logout(request):

    global flag
    flag = False
    request.session.clear()
    return render(request,"index.html",{'flag': flag})





# pages views   -------------------------------------------------------


def home(request):
    print(flag)
    return render(request, "index.html",{'flag':flag})

def programs_page(request):
    if flag != True:
        print(flag)
        return redirect('loginpage')
    else:
        return render(request,"programs.html",{'flag':flag})
    
# ------------------------------------------------
def hypertrophy_page(request):
    print(flag)
    return render(request,"hypertrophy.html",{'flag':flag})

def fullbody_page(request):
    print(flag)
    return render(request,"fullbody.html",{'flag':flag})

def ppl_page(request):
    print(flag)
    return render(request,"ppl.html",{'flag':flag})

def upperlower_page(request):
    print(flag)
    return render(request,"upperlower.html",{'flag':flag})

# ------------------------------------------------

def cardio_page(request):
    return render(request,"cardio.html",{'flag':flag})



def yoga_page(request):
    return render(request,"yogaplayer.html",{'flag':flag})



def strength_page(request):
    print(flag)
    return render(request,"strength.html",{'flag':flag})




def bmi_calculator(request):
    if flag != True:
        print(flag)
        return redirect('loginpage')
    else:
        return render(request,"calc.html",{'flag':flag})


def calorie_calculator(request):
    return render(request,"caloriecalc.html",{'flag':flag})


def videoplayer(request):
    return render(request,"player.html",{'flag':flag})


# -----------------------------------------------------------

def fullbody1_player(request):
    return render(request,"fb1player.html",{'flag':flag})

def fullbody2_player(request):
    return render(request,"fb2player.html",{'flag':flag})

def fullbody3_player(request):
    return render(request,"fb3player.html",{'flag':flag})

def push_player(request):
    return render(request,"pushplayer.html",{'flag':flag})
def pull_player(request):
    return render(request,"pullplayer.html",{'flag':flag})
def legs_player(request):
    return render(request,"legsplayer.html",{'flag':flag})

def upper_player(request):
    return render(request,"upperplayer.html",{'flag':flag})

def lower_player(request):
    return render(request,"lowerplayer.html",{'flag':flag})

def hiit_player(request):
    return render(request,"hiitplayer.html",{'flag':flag})

def liss_player(request):
    return render(request,"lissplayer.html",{'flag':flag})

def circuit_player(request):
    return render(request,"circuitplayer.html",{'flag':flag})

def yoga_player(request):
    return render(request,"yogaplayer.html",{'flag':flag})

def bench_player(request):
    return render(request,"benchplayer.html",{'flag':flag})

def squats_player(request):
    return render(request,"squatsplayer.html",{'flag':flag})

def deadlifts_player(request):
    return render(request,"deadliftsplayer.html",{'flag':flag})



        
    