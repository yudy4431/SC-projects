"""
File: Peace and Love.
Name:Yudy
----------------------
When I was a child, I loved to draw. The highest frequency I drew was dinosaur.
Also, The first toy my uncle gave me was Ultra-man. The emotion I had that time was impressed.
According to the memories, I decide to combine them.
But I don't want ultra-man or dinosaur to hurt each other, I try to let them hug each other to
bring more warm to the world.
"""

from campy.graphics.gobjects import GOval, GRect, GPolygon, GLabel, GArc
from campy.graphics.gwindow import GWindow

window = GWindow(800, 600)


def main():
    background()
    ultra_man()
    monster()
    heart()
    love_label()
    my_sign()


# make a ultra man.
def ultra_man():
    ear()
    head()
    top()
    eye()
    mouth()
    down_mouth()
    leg()
    arm()
    body()
    hand()
    chest_logo()


def head():
    head = GOval(150, 200, x=100, y=100)
    head.filled = True
    head.fill_color = 'silver'
    window.add(head)


def eye():
    eye0 = GOval(50, 70, x=120, y=130)
    window.add(eye0)
    eye0.filled = True
    eye0.fill_color = 'yellow'
    eye1 = GOval(50, 70, x=180, y=130)
    eye1.filled = True
    eye1.fill_color = 'yellow'
    window.add(eye1)


def top():
    top = GOval(20, 100, x=165, y=50)
    top.filled = True
    top.fill_color = 'red'
    window.add(top)


def mouth():
    mouth = GRect(90, 20, x=130, y=250)
    mouth.filled = True
    mouth.fill_color = 'white'
    window.add(mouth)


def down_mouth():
    down_mouth = GRect(10, 30, x=172, y=270)
    down_mouth.filled = True
    down_mouth.fill_color = 'white'
    window.add(down_mouth)


def ear():
    ear0 = GRect(20, 40, x=85, y=170)
    window.add(ear0)
    ear0.filled = True
    ear0.fill_color = 'grey'
    ear1 = GRect(20, 40, x=245, y=170)
    ear1.filled = True
    ear1.fill_color = 'grey'
    window.add(ear1)


def body():
    body0 = GOval(150, 200, x=105, y=300)
    body0.filled = True
    body0.fill_color = 'silver'
    window.add(body0)
    body1 = GArc(130, 200, 0, -180, x=115, y=400)
    body1.filled = True
    body1.fill_color = 'red'
    window.add(body1)


def leg():
    left_leg0 = GOval(40, 80, x=130, y=480)
    left_leg0.filled = True
    left_leg0.fill_color = 'silver'
    window.add(left_leg0)
    left_leg1 = GArc(40, 80, 0, -180, x=130, y=520)
    left_leg1.filled = True
    left_leg1.fill_color = 'red'
    window.add(left_leg1)
    right_leg = GOval(40, 80, x=190, y=480)
    right_leg.filled = True
    right_leg.fill_color = 'silver'
    window.add(right_leg)
    right_leg1 = GArc(40, 80, 0, -180, x=190, y=520)
    right_leg1.filled = True
    right_leg1.fill_color = 'red'
    window.add(right_leg1)


def arm():
    arm0 = GOval(70, 20, x=230, y=350)
    arm0.filled = True
    arm0.fill_color = 'silver'
    window.add(arm0)
    arm1 = GOval(70, 20, x=60, y=350)
    arm1.filled = True
    arm1.fill_color = 'silver'
    window.add(arm1)


def hand():
    hand0 = GOval(20, 90, x=290, y=280)
    hand0.filled = True
    hand0.fill_color = 'silver'
    window.add(hand0)
    hand00 = GArc(20, 100, 0, 180, x=290, y=280)
    hand00.filled = True
    hand00.fill_color = 'red'
    window.add(hand00)

    hand1 = GOval(20, 90, x=50, y=280)
    hand1.filled = True
    hand1.fill_color = 'silver'
    window.add(hand1)
    hand11 = GArc(20, 100, 0, 180, x=50, y=280)
    hand11.filled = True
    hand11.fill_color = 'red'
    window.add(hand11)


def chest_logo():
    logo = GOval(15, 30, x=170, y=320)
    logo.filled = True
    logo.fill_color = 'yellow'
    window.add(logo)


# make a monster.
def monster():
    monster_head()
    eyebrow()
    monster_eye()
    monster_mouth()
    teeth()
    monster_leg()
    monster_body()
    monster_inbody()
    body_line()
    monster_feet()
    down_feet()
    toes()
    monster_hand()
    hand_finger()
    tail()
    back()
    face_red()


def monster_head():
    m_h = GRect(200, 150, x=450, y=80)
    m_h.filled = True
    m_h.fill_color = 'green'
    window.add(m_h)


def eyebrow():
    brow = GPolygon()
    brow.add_vertex((540, 50))
    brow.add_vertex((600, 45))
    brow.add_vertex((600, 30))
    brow.filled = True
    brow.fill_color = 'black'
    window.add(brow)


def monster_eye():
    m_e = GOval(30, 60, x=560, y=50)
    m_e.filled = True
    m_e.fill_color = 'black'
    window.add(m_e)


def monster_mouth():
    m_m = GRect(90, 60, x=450, y=170)
    m_m.filled = True
    m_m.fill_color = 'red'
    window.add(m_m)


def teeth():
    tooth1 = GPolygon()
    tooth1.add_vertex((450, 170))
    tooth1.add_vertex((480, 170))
    tooth1.add_vertex((465, 190))
    tooth1.filled = True
    tooth1.fill_color = 'white'
    window.add(tooth1)
    tooth2 = GPolygon()
    tooth2.add_vertex((480, 170))
    tooth2.add_vertex((510, 170))
    tooth2.add_vertex((495, 190))
    tooth2.filled = True
    tooth2.fill_color = 'white'
    window.add(tooth2)
    tooth3 = GPolygon()
    tooth3.add_vertex((510, 170))
    tooth3.add_vertex((540, 170))
    tooth3.add_vertex((525, 190))
    tooth3.filled = True
    tooth3.fill_color = 'white'
    window.add(tooth3)
    tooth4 = GPolygon()
    tooth4.add_vertex((450, 230))
    tooth4.add_vertex((480, 230))
    tooth4.add_vertex((465, 210))
    tooth4.filled = True
    tooth4.fill_color = 'white'
    window.add(tooth4)
    tooth5 = GPolygon()
    tooth5.add_vertex((480, 230))
    tooth5.add_vertex((510, 230))
    tooth5.add_vertex((495, 210))
    tooth5.filled = True
    tooth5.fill_color = 'white'
    window.add(tooth5)
    tooth6 = GPolygon()
    tooth6.add_vertex((510, 230))
    tooth6.add_vertex((540, 230))
    tooth6.add_vertex((525, 210))
    tooth6.filled = True
    tooth6.fill_color = 'white'
    window.add(tooth6)


def monster_body():
    m_body = GRect(130, 270, x=520, y=230)
    m_body.filled = True
    m_body.fill_color = 'green'
    window.add(m_body)


def monster_inbody():
    inbody = GRect(70, 180, x=520, y=320)
    inbody.filled = True
    inbody.fill_color = 'yellow'
    window.add(inbody)


def monster_leg():
    leg0 = GOval(100, 60, x=520, y=480)
    leg0.filled = True
    leg0.fill_color = 'dark green'
    window.add(leg0)
    leg1 = GOval(100, 60, x=560, y=480)
    leg1.filled = True
    leg1.fill_color = 'dark green'
    window.add(leg1)


def monster_feet():
    foot0 = GOval(100, 40, x=460, y=520)
    foot0.filled = True
    foot0.fill_color = 'green'
    window.add(foot0)
    foot1 = GOval(100, 40, x=560, y=520)
    foot1.filled = True
    foot1.fill_color = 'green'
    window.add(foot1)


def down_feet():
    down0 = GOval(70, 20, x=475, y=540)
    down0.filled = True
    down0.fill_color = 'pink'
    window.add(down0)
    down1 = GOval(70, 20, x=580, y=540)
    down1.filled = True
    down1.fill_color = 'pink'
    window.add(down1)


def toes():
    toe0 = GPolygon()
    toe0.add_vertex((420, 555))
    toe0.add_vertex((475, 555))
    toe0.add_vertex((475, 525))
    toe0.filled = True
    toe0.fill_color = 'ivory'
    window.add(toe0)
    toe1 = GPolygon()
    toe1.add_vertex((525, 555))
    toe1.add_vertex((580, 555))
    toe1.add_vertex((580, 525))
    toe1.filled = True
    toe1.fill_color = 'ivory'
    window.add(toe1)


def monster_hand():
    m_hand0 = GOval(80, 50, x=440, y=300)
    m_hand0.filled = True
    m_hand0.fill_color = 'dark green'
    window.add(m_hand0)
    m_hand1 = GOval(80, 50, x=440, y=330)
    m_hand1.filled = True
    m_hand1.fill_color = 'dark green'
    window.add(m_hand1)


def hand_finger():
    fin0 = GPolygon()
    fin0.add_vertex((420, 300))
    fin0.add_vertex((450, 300))
    fin0.add_vertex((450, 325))
    fin0.filled = True
    fin0.fill_color = 'ivory'
    window.add(fin0)
    fin1 = GPolygon()
    fin1.add_vertex((420, 325))
    fin1.add_vertex((450, 325))
    fin1.add_vertex((450, 350))
    fin1.filled = True
    fin1.fill_color = 'ivory'
    window.add(fin1)
    fin2 = GPolygon()
    fin2.add_vertex((420, 350))
    fin2.add_vertex((450, 350))
    fin2.add_vertex((450, 375))
    fin2.filled = True
    fin2.fill_color = 'ivory'
    window.add(fin2)


def tail():
    tail = GPolygon()
    tail.add_vertex((650, 450))
    tail.add_vertex((650, 500))
    tail.add_vertex((780, 430))
    tail.filled = True
    tail.fill_color = 'green'
    window.add(tail)


def back():
    back0 = GPolygon()
    back0.add_vertex((650, 230))
    back0.add_vertex((650, 280))
    back0.add_vertex((700, 255))
    back0.filled = True
    back0.fill_color = 'white'
    window.add(back0)
    back1 = GPolygon()
    back1.add_vertex((650, 280))
    back1.add_vertex((650, 330))
    back1.add_vertex((700, 305))
    back1.filled = True
    back1.fill_color = 'white'
    window.add(back1)
    back2 = GPolygon()
    back2.add_vertex((650, 330))
    back2.add_vertex((650, 380))
    back2.add_vertex((700, 355))
    back2.filled = True
    back2.fill_color = 'white'
    window.add(back2)


def face_red():
    face = GOval(60, 20, x=550, y=150)
    face.filled = True
    face.fill_color = 'red'
    window.add(face)


def body_line():
    line0 = GRect(50, 3, x=520, y=370)
    line0.filled = True
    line0.fill_color = 'black'
    window.add(line0)
    line1 = GRect(50, 3, x=520, y=400)
    line1.filled = True
    line1.fill_color = 'black'
    window.add(line1)
    line2 = GRect(50, 3, x=520, y=430)
    line2.filled = True
    line2.fill_color = 'black'
    window.add(line2)


# background
def background():
    bg = GRect(800, 600)
    bg.filled = True
    bg.fill_color = 'pale turquoise'
    window.add(bg)


# label
def love_label():
    label = GLabel('Hug!', x=265, y=100)
    label.font = 'Times New Roman-60-bold'
    window.add(label)


# label heart
def heart():
    my_heart = GPolygon()
    my_heart.add_vertex((280, 10))
    my_heart.add_vertex((230, 60))
    my_heart.add_vertex((330, 180))
    my_heart.add_vertex((430, 60))
    my_heart.add_vertex((380, 10))
    my_heart.add_vertex((330, 50))
    my_heart.filled = True
    my_heart.fill_color = 'light pink'
    window.add(my_heart)


# my sign
def my_sign():
    sign = GLabel('by Yudy', x=700, y=580)
    sign.font = 'courier-20-italic'
    window.add(sign)




if __name__ == '__main__':
    main()
