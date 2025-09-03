
import win32com.client as wincl
import datetime
import os
import webbrowser
import psutil
import requests
import colorama 
from colorama import Fore, Style, init

#Initialize Coloroma
init(autoreset=True)

#Create Speaker
speaker=wincl.Dispatch("SAPI.SpVoice")


def speak(text, rate=2):
    speaker.Rate = rate   # Speed (-10 slow to +10 fast)
    speaker.Speak("")  # flush buffer
    speaker.speak(text)

def get_ip():
    try:
        return requests.get("https://api.ipify.org").text
    except:
        return "Unable to fetch IP address"
    
if __name__ == '__main__':
    print(Fore.CYAN + "Robo Speaker is ready!")
    speak("Hello! I am your Robo Speaker")
    print(Fore.YELLOW + "Type 'q' or 'quit' to exit")

    while True:
        x = input(Fore.GREEN + "Say something: ")

        #Exit conditions
        if x.lower() in ["q", "quit"]:
            print(Fore.RED + "Exiting program...")
            speak("Bye, thank you for your time")
            break
        
        #Custom Commands
        #Time
        elif x.lower()=="time":
            now=datetime.datetime.now().strftime("%H:%M %p")
            print(Fore.MAGENTA + f"Time: {now}")
            speak(f"The current time is {now}")
        
        #Date
        elif x.lower()=="date":
            today=datetime.date.today().strftime("%d/%m%Y")
            print(Fore.MAGENTA + f"Date: {today}")
            speak(f"Today's' Date is {today}")
        
        #Notepad 
        elif x == "open notepad":
            print(Fore.YELLOW + "Opening Notepad...")
            speak("Opening Notepad")
            os.system("notepad")
        
        #Search Something: primary search engine= Google
        elif x.startswith("search- "):
            query = x.replace("search ", "")
            print(Fore.CYAN + f"Searching: {query}")
            speak(f"Searching for {query}")
            webbrowser.open(f"https://www.google.com/search?q={query}")

        #Battery Status
        elif x == "battery":
            battery = psutil.sensors_battery()
            if battery:
                print(Fore.BLUE + f"Battery: {battery.percent}%")
                speak(f"Battery is at {battery.percent} percent")
            else:
                print(Fore.RED + "Unable to read battery status")
                speak("Unable to read battery status")

        #Get IP Address
        elif x == "ip":
            ip = get_ip()
            print(Fore.BLUE + f"IP Address: {ip}")
            speak(f"Your IP address is {ip}")

        #Write Notes
        elif x.startswith("note "):
            note = x.replace("note ", "")
            with open("notes.txt", "a", encoding="utf-8") as f:
                f.write(note + "\n")
            print(Fore.YELLOW + f"Note saved: {note}")
            speak("Note saved")

        #Show Notes
        elif x == "show notes":
            if os.path.exists("notes.txt"):
                with open("notes.txt", "r", encoding="utf-8") as f:
                    notes = f.readlines()
                if notes:
                    print(Fore.CYAN + "Your notes:")
                    speak("Here are your notes:")
                    for n in notes:
                        speak(n.strip())
                else:
                    print(Fore.RED + "No notes found")
                    speak("No notes found")
            else:
                print(Fore.RED + "No notes file exists yet")
                speak("No notes file exists yet")
                
        #Show History
        elif x == "show history":
            if os.path.exists("history.txt"):
                with open("history.txt", "r", encoding="utf-8") as f:
                    history = f.readlines()
                if history:
                    print(Fore.CYAN + "Command History:")
                    for h in history:
                        print("   - " + h.strip())
                    speak("Here is your command history.")
                else:
                    print(Fore.RED + "History is empty.")
                    speak("History is empty.")
            else:
                print(Fore.RED + "No history file exists yet.")
                speak("No history file exists yet.")

        
        #Clear History
        elif x == "clear history":
            open("history.txt", "w").close()
            print(Fore.YELLOW + "History cleared")
            speak("History cleared")

        elif x == "help":
            speak("I can do the following: tell time, today's date, battery status, IP Address, open notepad, search on Google, take notes, show notes, show history, clear history, tell me about myself and repeat your input.")

        elif x == "who are you?":
            print(Fore.CYAN + "I am Robo Speaker, your voice assistant built in Python.")
            speak("I am Robo Speaker, your voice assistant built in Python.")
        else:
            print(Fore.WHITE + f"You said: {x}")
            speak(x)

        #Save History
        with open("history.txt", "a", encoding="utf-8") as f:
            f.write(f"{x}\n")



      
    
