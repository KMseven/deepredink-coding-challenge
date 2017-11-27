# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 05:30:50 2017

@author: krishna
"""

import speech_recognition as sr
import requests
import json
import webbrowser
import requests_cache
from fake_useragent import UserAgent


def listen():
    """ Takes the voice input and returns text"""    
    
    data="none"
      
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print "Wait for 5 seconds calibrating microphone...."
        #Code may take more time to detect speech due to ambient noise the microphone
        #may be picking up.Setting the proper energy threshold will counter the ambient
        #noise.The easiest is to use this below function.It adjusts the proper threshold
        r.adjust_for_ambient_noise(source,duration=5)
        print "Speak:"
        audio=r.listen(source)
    
    
    try:
        data=r.recognize_google(audio)
        print "You said "+data
    except Exception as e:
        print e
        
    return data
    
def response(pokemon):
    '''Sends request and reads the response'''  
    ua = UserAgent()
    headers={
        'User-Agent':ua.chrome#Fakes browser visit
        }
    base_url='http://pokeapi.co/api/v2/pokemon/'
    url=base_url+pokemon+"/"
    requests_cache.install_cache('pokemon_cache')#All the responses with status code 200 will be cached into pokemon_cache.sqlite. 
    response=requests.get(url,headers=headers)
    status_code=response.status_code
    print status_code
    if status_code==200:#Success
        data=json.loads(response.text)
        poke_images=[]
        poke_images.append(data['sprites']['back_default'])
        poke_images.append(data['sprites']['back_shiny'])
        poke_images.append(data['sprites']['front_default'])
        poke_images.append(data['sprites']['front_shiny'])
        for i in poke_images:
            webbrowser.open_new_tab(i)
    elif status_code==404:#Page not found
        print "There's no pokemon with name "+pokemon
    elif status_code==403:#Forbidden error
        print "Your Ip adress may be blocked. Try VPN"
    else:
        print "Error in quering API"
        
        
def main():
    pokemon=listen()    
    if(pokemon!="none"):
        response(pokemon.lower())
    return True
main()

   