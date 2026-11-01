# الاستيراد 
from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from scores import Score
import time

# انشاء الشاشة
screen=Screen()
screen.setup(700,800)
screen.getcanvas().winfo_toplevel().geometry("700x800+0+0")
screen.bgcolor('black')
screen.textinput('y','g')
# ايقاف التحديث التلقائي للشاشة 
screen.tracer(0)

# إنشاء المضارب 
r_paddle=Paddle((300,0))
l_paddle=Paddle((-300,0))

# انشاء الكرة 
ball=Ball()

# إنشاء السكور
r_score=Score(200)
l_score=Score(-200)

# تحديث الشاشة
screen.update()

# جعل بايثون تستمع لإدخال الكيبورد 
screen.listen()

# تحديد الازرار
screen.onkey(r_paddle.up,'Up')
screen.onkey(r_paddle.down,'Down')
screen.onkey(l_paddle.up,'Left')
screen.onkey(l_paddle.down,'Right')

# إنشاء قيمة منطقية
game_on=True
wait=0.1
# بداية اللوب 
while game_on:
    # تحديث الشاشة 
    screen.update()
    time.sleep(wait)
    # تحريك الكرة 
    ball.goto(ball.xcor()+ball.x_move,ball.ycor()+ball.y_move)
    
    # التحقق من ما إذا كانت الكرة قد اصطدمت بالسقف أو الارص
    if ball.ycor()>=380 or ball.ycor()<=-380:
        ball.y_move *= -1
#         
    if (ball.xcor()>=280 and ball.distance(r_paddle)<=50) or (ball.xcor()<=-280 and ball.distance(l_paddle)<=50):
        ball.x_move*=-1
        wait*=0.9
        
    if ball.xcor()>300:
        ball.goto(0,0)
        ball.x_move*=-1
        l_score.update_score()
        screen.update()
        wait=0.1
        
        
        
    if ball.xcor()<-300:
        ball.goto(0,0)
        ball.x_move*=-1
        r_score.update_score()
        screen.update()
        wait=0.1
        


screen.exitonclick()