from graphics import *
from time import *
import graphlib
def main():
    w =GraphWin("Rate Me Please",800,580)
    w.setBackground("white")

    x,y=650,280
    
    t0 = Text(Point(400,30),'Please grade me from 1 to 5 (worest to best) or you can say you have no idea.')
    t0.setSize(16)
    t0.draw(w)
    t0 = Text(Point(400,70),'Thank you!')
    t0.setSize(16)
    t0.draw(w)
    t0 = Text(Point(400,110),'Your rating will be completely anonymous, don\'t worry.')
    t0.setSize(16)
    t0.draw(w)
    t0 = Text(Point(150,y+100),'(Optional) Anything you want to say:')
    t0.setSize(13)
    t0.draw(w)
    t0 = Text(Point(650,y+240),'(that\'s for me, just ignore it.)')
    t0.setSize(11)
    t0.draw(w)

    t2 = Text(Point(400,230),'Select one of six(and add comment if you want), then click "Enter" to submit.')
    t2.setSize(16)
    t2.setTextColor("blue")
    t2.draw(w)

    n=1

    t3 = Text(Point(110,190),'You are No.'+str(n)+':')
    t3.setSize(16)
    t3.setTextColor("blue")
    t3.draw(w)

##(Enter):(650,280) to (750,330)
    b0 = Rectangle(Point(x,y),Point(x+100,y+50))
    b0.setOutline("green")
    t0 = Text(Point(x+50,y+25),'Enter')
    t0.setSize(16)
    b0.draw(w)
    t0.draw(w)


    bb = []

    for i in range(1,6):
        x0 = 50+(i-1)*90
        b = Rectangle(Point(x0,y),Point(x0+50,y+50))
        t = Text(Point(x0+25,y+25),str(i))
        t.setSize(16)
        b.draw(w)
        t.draw(w)
        bb.append(b)


##(No Idea):(500,280) to (600,330)
    x2 = x0 + 90
    b = Rectangle(Point(x2,y),Point(x2+100,y+50))
    t = Text(Point(x2+50,y+25),"No Idea")
    t.setSize(16)
    b.draw(w)
    t.draw(w)
    bb.append(b)

##(Result):(610,460) to (710,510)
    x2 = x0 + 200
    y2 = y + 180
    b = Rectangle(Point(x2,y2),Point(x2+100,y2+50))
    t = Text(Point(x2+50,y2+25),"Result")
    t.setSize(16)
    t.draw(w)
    b.draw(w)
    

    I = Entry(Point(400,y+133),80)
    I.setSize(12)
    I.setText("")
    I.draw(w)
    
    outfile = open("comments.txt",'w')  

    h=50
    t=0
    r=0
    g=0

    while(True):
        p = w.getMouse()
        a = p.getX()
        b = p.getY()

        if (a>610 and a<710 and b>460 and b<510):
            m=I.getText()
            if m=='137528':
                w.close()
                break

        if (a>x and a<x+100 and b>y and b<y+50):
            if g==0:
                t2.setText("Please make a selection before click 'Enter'.")
            else:
                m = I.getText()
                if m!="":
                    print(m+'\n\n',file=outfile)
                n = n+1
                if g==6:
                    r = r + 1
                else:
                    t = t + g
                t2.setText("Submitted already! Please pass it to others.")
                for k in range (6):
                    bb[k].setFill("white")
                ##sleep change
                sleep(2)
                I.setText("")
                t2.setText('Select one of six(and add comment if you want), then click "Enter" to submit.')
                t3.setText('You are No.'+str(n)+':')
            g=0


        for i in range (6):
            if i==5:
                h=100
            a0=50+90*i
            if (a>a0 and a<a0+h and b>y and b<y+50):
                bb[i].setFill("light blue")
                for k in range (i):
                    bb[k].setFill("white")
                for k in range (i+1,6):
                    bb[k].setFill("white")
                g = i+1
            

    ave = t/(n-r-1)
    print("My grade is:",ave)
    print("Totally",n-1, "students take votes.")
    print(r,"student have no idea.")
    outfile.close()



main()
    
