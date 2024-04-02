import pyttsx3
import speech_recognition as sr
import pywhatkit as kit
import requests
import math

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
def intro():
    speak("Hello I am OGY your voice assistant. How may I help you ?")
    speak("Please say 1 for opening a video in youtube or 2 for searching something in web or 3 for knowing current temperature of a place or 4 for doing simple mathematical calculations")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("OGY is listening...")
        audio = r.record(source, duration = 5)
    try:
        print("OGY is recognising...")
        query = r.recognize_google(audio)
        print("You said "+query)
    except Exception as e:
        print(e)
        speak("OGY did not understand what you have said. Can you please repeat again?")
        return "None"
    return query

def operation(n1,op,n2):
    n1,n2 = int(n1),int(n2)
    if(op=="+"):
        speak("The sum of "+str(n1)+"and "+str(n2)+"is "+str(n1+n2))
    elif(op=="-"):
        speak("The difference of "+str(n1)+"and "+str(n2)+"is "+str(n1-n2))
    elif(op=="*"):
        speak("The product of "+str(n1)+"and "+str(n2)+"is "+str(n1*n2))
    elif(op=="/"):
        speak("The quotient of "+str(n1)+"and "+str(n2)+"is "+str(round((n1/n2),2)))
    else:
        speak("OGY can solve only simple math problem. We will upgrade soon for more problems.")
    
#call = takeCommand()
#print(call)

if __name__=="__main__":
    intro()
    while True:
        option = takeCommand()
        #option = "4"
        if("1" in option or "one" in option):
            speak("What video do you want me to open in youtube?")
            answer = takeCommand()
            kit.playonyt(answer)
            break
        elif("2" in option or "two" in option):
            speak("What do you want me to search on the web?")
            answer = takeCommand()
            kit.search(answer)
            break
        elif("3" in option or "three" in option):
            speak("For which place do you want to find the current temperature?")
            answer = takeCommand()
            #answer = "Pune"
            api = "http://api.openweathermap.org/data/2.5/weather?q="+answer+"&appid=cf68af6b1720ee2d0fb9db397e7632d2"
            response = requests.get(api)
            x = response.json()
            y = x["main"]
            temp = round((y["temp"]-273.15),2)
            speak("The current temperature of "+answer+"is "+str(temp))
            break
        elif("4" in option or "four" in option):
            speak("Please tell the math problem to be solved")
            try:
                answer = takeCommand()
                #answer = "5+3+2"
                print(answer.split())
                operation(*answer.split())
            except:
                speak("Invalid Input format! Please try again")
            break
        else:
            speak("Please try again")

