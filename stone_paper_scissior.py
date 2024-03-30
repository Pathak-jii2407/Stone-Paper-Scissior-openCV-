import pyttsx3
import cv2
import mediapipe as mp
import time
import random as rd




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def points(get,bot):
    speak(f"I choose for {bot}")
    speak(f"You choose for {get}")
def game():
    # speak("Jarvis Here")
    speak("Lets play Stone Paper Scissior")

    def count_fingers(lst):
        cnt = 0

        thresh = (lst.landmark[0].y * 100 - lst.landmark[9].y * 100) / 2

        if (lst.landmark[5].y * 100 - lst.landmark[8].y * 100) > thresh:
            cnt += 1

        if (lst.landmark[9].y * 100 - lst.landmark[12].y * 100) > thresh:
            cnt += 1

        if (lst.landmark[13].y * 100 - lst.landmark[16].y * 100) > thresh:
            cnt += 1

        if (lst.landmark[17].y * 100 - lst.landmark[20].y * 100) > thresh:
            cnt += 1

        if (lst.landmark[5].x * 100 - lst.landmark[4].x * 100) > 6:
            cnt += 1

        return cnt


    cap = cv2.VideoCapture(0)

    drawing = mp.solutions.drawing_utils
    hands = mp.solutions.hands
    hand_obj = hands.Hands(max_num_hands=2)

    start_init = False

    prev = -1


    bot_points=0
    user_points=0
    draw=0
    over=1
    speak("I am ready")
    while True:
        
        end_time = time.time()
        _, frm = cap.read()
        frm = cv2.flip(frm, 1)

        res = hand_obj.process(cv2.cvtColor(frm, cv2.COLOR_BGR2RGB))

        if res.multi_hand_landmarks:
            hand_keyPoints = res.multi_hand_landmarks[0]
            cnt = count_fingers(hand_keyPoints)
            time.sleep(0.10)
            if not (prev == cnt):
                if not (start_init):
                    start_time = time.time()
                    start_init = True

                elif (end_time - start_time) > 0.2:
                    get_user_value=''
                    
                    if (cnt == 0):
                        get_user_value='rock'
                        over+=1                   
                        
                    if (cnt == 2):
                        get_user_value='scissor'
                        over+=1
                        
                    if (cnt == 5):
                        get_user_value='paper'
                        over+=1


    
                    prev = cnt
                    tart_init = False
                    
                    game=rd.choices(['rock','paper','scissor'])
                    bot=game[0]

                    
                
                    if bot==get_user_value:
                        points(get_user_value,bot)
                        speak("\nDraw Match")
                        draw+=1 
                    else:
                        if get_user_value=='':
                            speak('Sorry, I do not get your hand')
                            continue
                        
                        elif bot=="rock" and get_user_value=='paper':
                            points(get_user_value,bot)
                            speak("\nYou won!\n")
                            user_points+=1
                        
                        elif bot=="paper" and get_user_value=='scissor':
                            points(get_user_value,bot)
                            speak("\nYou won!\n")
                            user_points+=1

                        elif bot=="scissor" and get_user_value=='rock':
                            points(get_user_value,bot)
                            speak("\nYou won!\n")
                            user_points+=1
                        
                        else:
                            points(get_user_value,bot)
                            speak("\n I won!\n you looser ")
                            bot_points+=1                      
            if over>=6:
                break
            drawing.draw_landmarks(frm, hand_keyPoints, hands.HAND_CONNECTIONS)

        # cv2.imshow("window", frm)
        if cv2.waitKey(1) == ord('q'):
            cv2.destroyAllWindows()
            cap.release()
            break
    print("*"*5,"RESULT","*"*5)
    print(f"Your points : {user_points}")
    print(f"Bot points : {bot_points}")
    print(f"Draw matches :{draw}")
    speak(f"Your points : {user_points}")
    speak(f"My points : {bot_points}")
    speak(f"Draw matches :{draw}")

    print("*"*5,"RESULT","*"*5)
    if user_points>bot_points:
        speak('Finally, You Win')
    elif user_points<bot_points:
        speak('Finally, I Win, You Looser, Go and Do Homework\nDuffer')
    else:
        speak('Draw')

game()