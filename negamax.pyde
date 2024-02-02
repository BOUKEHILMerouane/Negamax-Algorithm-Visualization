import math

class square :
      def __init__(self, lvl, pth, value, turn, wr):
          self.lvl = lvl
          self.pth = pth
          self.value = value
          self.turn = turn
          self.wr = 0

values = [15,6,3,12,42,45,42,39,-9,66,27,36,33,30,61,60]
squares = []
temp = []
ways = []

#initialize
lvl = 5
init = square(0,'','','Max',0)
squares.append(init)
temp.append(init)
while temp :
    tmp = temp.pop(0)
    if (int(tmp.lvl)+1 != lvl) :
        if tmp.turn == 'Max' :
           if (int(tmp.lvl)+1 == lvl-1) :
               l = square(int(tmp.lvl)+1,tmp.pth+'L',values.pop(0),'Min',0)
               r = square(int(tmp.lvl)+1,tmp.pth+'R',values.pop(0),'Min',0)
           else : 
               l = square(int(tmp.lvl)+1,tmp.pth+'L','','Min',0)
               r = square(int(tmp.lvl)+1,tmp.pth+'R','','Min',0)
           squares.extend([l,r])
           temp.extend([l,r])
        else : 
           if (int(tmp.lvl)+1 == lvl-1) :
               l = square(int(tmp.lvl)+1,tmp.pth+'L',values.pop(0),'Max',0)
               r = square(int(tmp.lvl)+1,tmp.pth+'R',values.pop(0),'Max',0)
           else : 
               l = square(int(tmp.lvl)+1,tmp.pth+'L','','Max',0)
               r = square(int(tmp.lvl)+1,tmp.pth+'R','','Max',0)
           squares.extend([l,r])
           temp.extend([l,r])

def findSquare(sq,pth) :
    for i in squares :
        if sq.pth + pth == i.pth :
            return i

    
def negamax(sq) :
    nextpath = ['L','R']
    if (sq.lvl == lvl-1) :
        return sq.value
    Max = -float('inf')
    for np in nextpath :
        nsq = findSquare(sq,np)
        value = -negamax(nsq)
        if (value != '') :
            Max = max(Max, value)
    sq.value = Max
    return Max
    
def findPos (path):
    i=2
    dist = 0
    for pth in path :  
        if (pth == 'L') :
            dist -= 640/i
        else :
            dist += 640/i
        i*=2
    return dist
        
negamax(squares[0])
for i in range(3,-1,-1) :
    for sq in squares :
       if sq.lvl == i :
           ways.append(sq)

def setup() :
    background(255,255,255)
    size(1360,600)

def draw () :
    stroke(0,0,0)
    line(680, 115, 360, 185)
    line(680, 115, 1000, 185)
    line(360, 215, 200, 285)
    line(360, 215, 520, 285)
    line(1000, 215, 840, 285)
    line(1000, 215, 1160, 285)
    line(200, 315, 120, 385)
    line(200, 315, 280, 385)
    line(520, 315, 440, 385)
    line(520, 315, 600, 385)
    line(840, 315, 760, 385)
    line(840, 315, 920, 385)
    line(1160, 315, 1080, 385)
    line(1160, 315, 1240, 385)
    line(120, 415, 80, 485)
    line(120, 415, 160, 485)
    line(280, 415, 240, 485)
    line(280, 415, 320, 485)
    line(440, 415, 400, 485)
    line(440, 415, 480, 485)
    line(600, 415, 560, 485)
    line(600, 415, 640, 485)
    line(760, 415, 720, 485)
    line(760, 415, 800, 485)
    line(920, 415, 880, 485)
    line(920, 415, 960, 485)
    line(1080, 415, 1040, 485)
    line(1080, 415, 1120, 485)
    line(1240, 415, 1200, 485)
    line(1240, 415, 1280, 485)
    
    noFill()
    stroke(0,0,0)
    circle(80, 500, 30);
    fill(0,0,0)
    textSize(15);
    text(15, 80-6, 500+6)
    
    noFill()
    stroke(0,0,0)
    circle(160, 500, 30);
    fill(0,0,0)
    textSize(15);
    text(6, 160-6, 500+6)
    
    noFill()
    stroke(0,0,0)
    circle(240, 500, 30);
    fill(0,0,0)
    textSize(15);
    text(3, 240-6, 500+6)
    
    noFill()
    stroke(0,0,0)
    circle(320, 500, 30);
    fill(0,0,0)
    textSize(15);
    text(12, 320-6, 500+6)
    
    noFill()
    stroke(0,0,0)
    circle(400, 500, 30);
    fill(0,0,0)
    textSize(15);
    text(42, 400-6, 500+6)
    
    noFill()
    stroke(0,0,0)
    circle(480, 500, 30);
    fill(0,0,0)
    textSize(15);
    text(45, 480-6, 500+6)
    
    noFill()
    stroke(0,0,0)
    circle(560, 500, 30);
    fill(0,0,0)
    textSize(15);
    text(42, 560-6, 500+6) 
    
    noFill()
    stroke(0,0,0)
    circle(640, 500, 30);
    fill(0,0,0)
    textSize(15);
    text(39, 640-6, 500+6) 
    
    noFill()
    stroke(0,0,0)
    circle(720, 500, 30);
    fill(0,0,0)
    textSize(15);
    text(-9, 720-6, 500+6) 
    
    noFill()
    stroke(0,0,0)
    circle(800, 500, 30);
    fill(0,0,0)
    textSize(15);
    text(66, 800-6, 500+6) 
    
    noFill()
    stroke(0,0,0)
    circle(880, 500, 30);
    fill(0,0,0)
    textSize(15);
    text(27, 880-6, 500+6) 
    
    noFill()
    stroke(0,0,0)
    circle(960, 500, 30);
    fill(0,0,0)
    textSize(15);
    text(36, 960-6, 500+6) 
    
    noFill()
    stroke(0,0,0)
    circle(1040, 500, 30);
    fill(0,0,0)
    textSize(15);
    text(33, 1040-6, 500+6) 
    
    noFill()
    stroke(0,0,0)
    circle(1120, 500, 30);
    fill(0,0,0)
    textSize(15);
    text(30, 1120-6, 500+6) 
    
    noFill()
    stroke(0,0,0)
    circle(1200, 500, 30);
    fill(0,0,0)
    textSize(15);
    text(61, 1200-6, 500+6) 
    
    noFill()
    stroke(0,0,0)
    circle(1280, 500, 30);
    fill(0,0,0)
    textSize(15);
    text(60, 1280-6, 500+6) 
    
    noFill()
    stroke(0,0,0)
    
    circle(120, 400, 30);
    circle(280, 400, 30);
    circle(440, 400, 30);
    circle(600, 400, 30);
    circle(760, 400, 30);
    circle(920, 400, 30);
    circle(1080, 400, 30);
    circle(1240, 400, 30);
    
    circle(200, 300, 30);
    circle(520, 300, 30);
    circle(840, 300, 30);
    circle(1160, 300, 30);
    
    circle(360, 200, 30);
    circle(1000, 200, 30);
    
    circle(680, 100, 30);
    
    if ways :
       tp = ways.pop(0)
       stroke(255,0,0)
       noFill()
       circle(680+findPos(tp.pth), 100*(len(tp.pth)+1), 33);
       fill(0,0,0)
       textSize(15);
       text(tp.value, 680+findPos(tp.pth)-13, 100*(len(tp.pth)+1)+6)
    delay(200)

    

    
