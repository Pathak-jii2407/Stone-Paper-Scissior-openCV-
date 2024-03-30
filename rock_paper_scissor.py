
import random as rd


def take_input(bot):
    print("Enter Rock/paper/scissor :\n")
    user_input=input("You Choose: ").lower()
    print(f'Bot Choose: {bot}')
    return user_input
bot_points=0
user_points=0
draw=0

for times in range(5):
    game=rd.choices(['Rock','Paper','scissor'])
    bot=game[0].lower()
    

    for i in game:
        get_user_value=take_input(bot=bot)
        if bot==get_user_value:
            print("\nDraw")
            draw+=1
        else:
            if bot=="rock" and get_user_value=='paper':
                print("\nUser won!\n")
                user_points+=1
               
            elif bot=="paper" and get_user_value=='scissor':
                print("\nUser won!\n")
                user_points+=1

            elif bot=="scissor" and get_user_value=='rock':
                print("\nUser won!\n")
                user_points+=1
            else:
                print("\nBot won!\n")
                bot_points+=1


print("*"*5,"RESULT","*"*5)
print(f"Your points : {user_points}")
print(f"Bot points : {bot_points}")
print(f"Draw matches :{draw}")
print("*"*5,"RESULT","*"*5)

if bot_points>user_points:
    print("\n You Loss \n")
if bot_points<user_points:
    print("\n You Win \n")
else: 
    print("Draw")






