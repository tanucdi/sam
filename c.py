class Train:
    global l
    l={1,2,3,4,5}
    @staticmethod
    def freet():
        print("Welcome to the Indian Railways")

    def __init__(self,name,fare):
        self.name=name
        self.fare=fare
        self.seats=len(l)
    
    def getInfo(self):
        print(f"In train {self.name} fare is {self.fare} and seats available from 0 to {self.seats}")
    
    def bookTicket(self,num):
        if num in l:
            print(f'BOOKED - your ticket number is {num}')
            l.remove(l[num])
            self.seats=self.seats-1
        else:
            print('choose a correct seat number')

    def canelTicket(self,n):
        if l[n] not in l:
            print("Ticket Cancelled.")
            l.append(n)
            self.seats=self.seats+1

tanishq = Train('Intercity 203',90)
tanishq.freet()
tanishq.getInfo()
tanishq.bookTicket(4)
tanishq.getInfo()
tanishq.bookTicket(2)
tanishq.canelTicket(2)
