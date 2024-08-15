import speech_recognition as sr
import pyttsx3         
import pywhatkit as pk
import wikipedia as wiki
import datetime as dt

listener =sr.Recognizer()
speaker = pyttsx3.init()


voices = speaker.getProperty('voices')       #getting details of current voice
#speaker.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
speaker.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female


rate=speaker.getProperty('rate')  # this is for speed of the voice
speaker.setProperty('rate',150)   # this two for voice speed 


def speak(text):
    speaker.say(text)
    speaker.runAndWait()
ass_name="sivakoti"
voi="i am your voice assistant"+ass_name+",how can i help you"
print(voi)
speak(voi)


def take_command():
    command = ' '
    try:
        with sr.Microphone() as source:
            print("Listening.....")
            voice = listener.listen(source)
                         # there are so many recognizers  like 'sphinx','wit.ai','google_cloud'.......""search in google"
            command = listener.recognize_google(voice)
            #print(command)        this is print the our voice in to text
            command = command.lower()
            if ass_name in command:
                command = command.replace(ass_name+' ',' ')
                #print(command)
                #speak(command)
            
    except:
        print("check your Microphone")
    return command

while True:
    user_command = take_command()
    #print(user_command)
    #speak(user_command)
    if 'remove' in user_command or 'stop' in user_command or 'exit' in user_command or 'close' in user_command:
        x="see you again have a nice day"
        print(x)
        speak(x)
        break
    elif "what is my name" in user_command:
        x="sorry ,i dont no your name but my creater is shiva"
        print(x)
        speak(x)
    elif "how are you" in user_command:
        y="i am always good"
        print(y)
        speak(y)
    elif "who are you" in user_command:
        print("i am shiva voice assistant")
        speak("i am shiva voice assistant")
    elif 'time' in user_command:
        cur_time=dt.datetime.now().strftime("%I:%M%p")
        print(cur_time)
        speak(cur_time)
    elif 'play' in user_command:
        user_command = user_command.replace('play',' ')
        print("playing"+user_command)
        speak("playing"+user_command+"enjoy boss")
        pk.playonyt(user_command)
        break
    elif 'search for' in user_command or 'google' in user_command:
        user_command = user_command.replace('search for','')
        
        user_command = user_command.replace('google','')
        print(user_command)
        speak("search for"+user_command)
        pk.search(user_command)
        
    

    #elif wiki.summary(user_command) in user_command:
       # print(wiki.summary(user_command))
        #speak(wiki.summary(user_command))
        
    elif 'who is' in user_command or 'what is' in user_command:
        user_command = user_command.replace('who is','')
        user_command = user_command.replace('what is','')
        info=wiki.summary(user_command,3)
        print(info)
        speak(info)

   # elif pk.search(user_command) is user_command:

      #  speak("the results for you")
      #  pk.search(user_command)

        
        #break                   
    else:
        speak("please say it again")
        
        
