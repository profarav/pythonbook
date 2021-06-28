from turtle import *
import time
bgcolor("yellow")
color('red', 'purple')
penup()

write("Thank you for everything you've done for me.", move=False,align="center", font=("Verdana", 20, "normal"))

goto(0,-50)

time.sleep(2)
write("You've inspired me with your perserverance and confidence.", move=False,align="center", font=("Verdana",
                                    20, "normal"))
goto(0,-100)
time.sleep(3)
write( "You've taught me so much and I am forever indebted for that.,", move=False,align="center", font=("Verdana",
                                    20, "normal"))
goto(0,-150)

write( "I truly am grateful on how you've mentored me growing up.", move=False,align="center", font=("Verdana",
                                    20, "normal"))                                    
goto(0,-200)
time.sleep(5)
write( "You are my hero and role model.", move=False,align="center", font=("Verdana",
                                    20, "normal"))
time.sleep(2)
goto(0,-250)
write("Happy Fathers Day!", move=False,align="center", font=("Playfair Display", 25, "normal"))


pen = Turtle()
pen.setpos(0, 50)

def curve():
    for i in range(200):
  
   
        pen.right(1)
        pen.forward(1)
  

def heart():

    pen.fillcolor('red')
  

    pen.begin_fill()
  

    pen.left(140)
    pen.forward(113)
  

    curve()
    pen.left(120)
  

    curve()

    pen.forward(112)
  

    pen.end_fill()

heart()

   
