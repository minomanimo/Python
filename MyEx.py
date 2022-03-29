a = 0
class my_car:
    
    def __init__ (self):
        print("Benz amg GT")
        print("Porsche 911")
        print("Corvette")
        
    def accelB(self):
        global a
        a = a + 35
        print("Accelerating... %d km/h"% (a))
        
    def accelP(self):
        global a
        a = a+ 37
        print("Accelerating... %d km/h"% (a))
        
    def accelC(self):
        global a
        a = a + 34
        print("Accelerating... %d km/h"% (a))
    
    def shift(self):
        global a
        if a > 60 & a < 80:
            print ("shift succeed")
        elif a < 60:
            print ("shift timing is too early")
        elif a > 80:
            print ("shift timing is too late")
            
    def brakeB(self):
        global a
        a = a - 35
        print("Braking... %d km/h"%(a))
        
    def brakeP(self):
        global a
        a = a - 37
        print("Braking... %d km/h"%(a))
        
    def brakeC(self):
        global a
        a = a - 34
        print("Braking... %d km/h"%(a))
        
    def turn_left (self):
        global a
        if a < 100 :
            print("Turn left...")
        else:
            print("Speed is too fast. Slipped.")
            print("WASTED")
            a = 0
            
            
    def turn_right (self):
        global a
        if a < 100:
            print("Turn right")
        else:
            print("Speed is too fast. Slipped.")
            print("WASTED")
            a = 0
            
    
    def reverse (self):
        global a
        if a == 0:
            a = a - 10
            print("Going backward... %d km/h"%(-a))
        elif a > 0:
            print("Can't go backward during the driving.")
    
if __name__ == '__main__':
    drive = my_car()
    print("Pick the car")
    b = input()
    if b == "Benz amg GT":
        while True:
            print("Accelerate : ac Brake : br Shift : sh Turn left : tl Turn right : tr Go backward : R Stop : st")
            c = input()
            if c == "ac":
                drive.accelB()
            elif c == "br":
                drive.brakeB()
            elif c == "sh": 
                drive.shift()
            elif c == "tl":
                drive.turn_left()
                if a == 0:
                    break
            elif c == "tr":
                drive.turn_right()
                if a == 0:
                    break
            elif c == "R":
                drive.reverse()
            elif c == "st":
                break
    if b == "Porsche 911":
        while True:
            print("Accelerate : ac Brake : br Shift : sh Turn left : tl Turn right : tr Go backward : R Stop : st")
            c = input()
            if c == "ac":
                drive.accelP()
            elif c == "br":
                drive.brakeP()
            elif c == "sh": 
                drive.shift()
            elif c == "tl":
                drive.turn_left()
                if a == 0:
                    break
            elif c == "tr":
                drive.turn_right()
                if a == 0:
                    break
            elif c == "R":
                drive.reverse()
            elif c == "st":
                break
    if b == "Corvette":
        while True:
            print("Accelerate : ac Brake : br Shift : sh Turn left : tl Turn right : tr Go backward : R Stop : st")
            c = input()
            if c == "ac":
                drive.accelC()
            elif c == "br":
                drive.brakeC()
            elif c == "sh": 
                drive.shift()
            elif c == "tl":
                drive.turn_left()
                if a == 0:
                    break
            elif c == "tr":
                drive.turn_right()
                if a == 0:
                    break
            elif c == "R":
                drive.reverse()
            elif c == "st":
                break