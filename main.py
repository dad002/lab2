import play
from random import randint
e = play.new_text(words = "BRAT NE PO MUSHSKI ETO :(",x=0, y = -200,font = None,font_size = 50 )
d = play.new_text(words = "MOLODEC PROSTO RAZORVAL'!!!!",x=0, y = -200,font = None,font_size = 50 )
a = play.new_box(color='green', x=0, y=0, width=100, height=200)
b = play.new_box(color='green', x=150, y=0, width=100, height=200)
c = play.new_box(color='green', x=-150, y=0, width=100, height=200)
s = play.new_circle(color='red', x=0, y=250, radius=50, border_color='light')
text1= play.new_text(words = '' , x=-150, y=0, font = None, font_size=50, color = 'black')
text2 = play.new_text(words ='' , x=0, y=0, font = None, font_size=50, color = 'black')
text3= play.new_text(words = '', x=150, y=0, font = None, font_size=50, color = 'black')
#button_text = play.new_text(words= 'Вперед!', x = 0, y = 0, font = None, font_size = 50)
@play.when_program_starts
def start():
    text1.hide()
    text2.hide()
    text3.hide()
    e.hide()
    d.hide()
@play.repeat_forever
def do():
    if s.is_clicked:
        t1 = randint(0,9)
        t2 = randint(0,9)
        t3 = randint(0,9)
        text1.words = str(t1) 
        text2.words= str(t2)
        text3.words = str(t3)
        text1.show()
        text2.show()
        text3.show()
        e.hide()
        d.hide()
        print(t1 == t2)
        print(t2 == t3)
        print(t1)
        print(t2)
        print(t3)
        if t1 == t2 and t2 == t3:
            print(1)
            d.show()
        else:
            print(2)
            e.show()

play.start_program()
