from django.urls import path
from .views import * 

urlpatterns = [
    path('members/', members, name='members'),
    path('register/', Register, name='registerpage'),
    path('login/', Login, name='loginpage'),
    path('questionnaire/', questionnarire_processing, name='questionnairepage'),
    path('logout/' , Logout, name='logout'),


    path('', home, name='homepage'),
    path('programs/', programs_page, name='programspage'),
    path('hypertrophy/', hypertrophy_page, name='hypertrophypage'),
    path('fullbody/', fullbody_page, name='fullbodypage'),
    path('ppl/', ppl_page, name='pplpage'),
    path('upperlower/', upperlower_page, name='upperlowerpage'),
    path('cardio/', cardio_page, name='cardiopage'),
    path('yoga/', yoga_page, name='yogapage'),
    path('strength/', strength_page, name='strengthpage'),
    path('bmicalculator/', bmi_calculator, name='bmipage'),
    path('caloriecalculator/', calorie_calculator, name='caloriepage'),


    path('fullbody1player/', fullbody1_player, name='fullbody1page'),
    path('fullbody2player/', fullbody2_player, name='fullbody2page'),
    path('fullbody3player/', fullbody3_player, name='fullbody3page'),

    path('pushplayer/', push_player, name='pushpage'),
    path('pullplayer/', pull_player, name='pullpage'),
    path('legsplayer/', legs_player, name='legspage'),

    path('upperplayer/', upper_player, name='upperpage'),
    path('lowerplayer/', lower_player, name='lowerpage'),
    
    path('hiitplayer/', hiit_player, name='hiitpage'),
    path('lissplayer/', liss_player, name='lisspage'),
    path('circuittrainingplayer/', circuit_player, name='circuitpage'),

    path('yogaplayer/', yoga_player, name='yogapage'),

    path('benchplayer/', bench_player, name='benchpage'),
    path('squatsplayer/', squats_player, name='squatspage'),
    path('deadliftsplayer/', deadlifts_player, name='deadliftspage'),

]