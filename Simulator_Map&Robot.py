import sys, pygame,math,random
'''
class robot():
    def __init__(self,coordinate):
        self.velocity=100
        self.coordinate=coordinate
        self.health=100
        self.attack=10  # -10 per hit
        self.accuracy=8 # 80% will hit
        self.angle=0    # In radian
        self.angularVelocity=1 # Rad/s
        self.range=30
    def move(self,dtime,key): #key=-1 -> keyDown, Key=1 -> keyUp
        self.coordinate[0]+=key*math.sin(self.angle)*self.velocity*dtime #X
        self.coordinate[1]+=key*math.cos(self.angle)*self.velocity*dtime #Y
    def rotate(self,dtime,key): #Key=1 -> keyRight, Key=-1 -> keyLeft
        self.angle+=key*self.angularVelocity*dtime
    def attack(self,enemy): #
        if self.
        if ((enemy.coordinate[0]-self.coordinate[0])+(enemy.coordinate[1]-self.coordinate[1]))<math.pow(self.range,2): #enemy in our range?
            i = random.randint(1,self.accuracy)
            if i<9:
                enemy.health-=self.attack
'''
pygame.init()
size=width,height = 320,240
keys=[False,False,False,False,False,False,False,False] #UpDownLeftRight W S A D
player1pos=[100,100] # Initial pos of our robot
player2pos=[200,200] # Initial pos of enemy's robot
screen = pygame.display.set_mode(size,0,32)
pygame.display.set_caption("DFB Map simulator")
time=pygame.time.get_ticks()
while True:
    dtime=pygame.time.get_ticks()-time
    for event in pygame.event.get():
        if event.type== pygame.QUIT :
            pygame.quit()
            exit()
    screen.fill(0)


    pygame.display.flip()
    time=pygame.time.get_ticks()
