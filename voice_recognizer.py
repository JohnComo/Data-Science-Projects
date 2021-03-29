import speech_recognition 

# Build recognizer object 
recognizer = speech_recognition.Recognizer()

while True: 

    try: 
        # Set up input and declare mic 
        with speech_recognition.Microphone() as mic: 
            recognizer.adjust_for_ambient_noise(mic, duration = .2)

            #define audio and input 
            audio = recognizer.listen(mic)

            #convert audio to text 
            text = recognizer.recognize_google(audio)
            text = text.lower()
            print(f"Recognized {text}")
    
    except speech_recognition.UnknownValueError():
        # If audio cant be picked up, try again 
         recognizer = speech_recognition.Recognizer()
         continue 
