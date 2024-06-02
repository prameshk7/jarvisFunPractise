
# import speech_recognition as sr
# import pyttsx3



# r=sr.Recognizer()




# def record_text():
#     #error handling in case of not detecting #loop
#     while(1):
#         try:
#             with sr.Microphone() as source2:
#                 r.adjust_for_ambient_noise(source2, duration=0.2)
                
                
#                 audio2= r.listen(source2)
                
#                 MyText = r.recognize_google(audio2)
                
#         except sr.RequestError as e:
#             print("Could not request results; {0}".format(e))
            
#         except sr.ResponseError as e:
#             print("Unknown error occured")        
#     return

# def output_text(text):
    
#     f= open("output.txt", "a")
#     f.write(text)
#     f.write("\n")
#     f.close()
    
#     return

# while(1):
#     text=record_text()
#     output_text(text)
    
#     print("Text Written Successfully.")
    
    
import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()

def record_text():
    # error handling in case of not detecting # loop
    while True:
        try:
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2, duration=0.2)
                audio2 = r.listen(source2)
                MyText = r.recognize_google(audio2)
                return MyText  # return the recognized text
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand what you said.")

def output_text(text):
    with open("output.txt", "a") as f:
        f.write(text)
        f.write("\n")

while True:
    text = record_text()
    output_text(text)
    print("Text Written Successfully.")
    
    