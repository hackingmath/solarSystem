'''Solar System Model 
Peter Farrell with Curtis
October 20, 2017'''

class Planet:
    def __init__(self,dist_from_sun,sz,tex):
        self.x,self.y,self.z = 0,0,0
        self.r = dist_from_sun
        self.sz = sz
        self.tex = loadImage(tex)
        self.globe = createShape(SPHERE, self.sz)
        self.globe.setTexture(self.tex)
        self.points = [] #list to save location points
        self.speed = float(width)/self.r
        
    def update(self,t):
        self.x = self.r*cos(self.speed*t)
        self.y = 0
        self.z = self.r*sin(self.speed*t)
        self.points.append([self.x,self.y,self.z])
        if len(self.points) > 800:
            self.points.pop(0)
        pushMatrix()
        translate(self.x,self.y,self.z)
        #texture(self.tex)
        rotateY(t)
        shape(self.globe)
        popMatrix()
        
    def createTrail(self):
        for i,pt in enumerate(self.points):
            pushMatrix()
            stroke(255)
            if i < len(self.points)-1:
                line(pt[0],0,pt[2],self.points[i+1][0],
                    self.points[i+1][1],
                    self.points[i+1][2],)
            popMatrix()
            
class Moon:
    def __init__(self,planet):
        self.planet = planet
        self.globe = createShape(SPHERE, 5)
        self.delay = random(TWO_PI) #spacing
        
    def update(self,t):
        pushMatrix()
        translate(self.planet.x+((self.planet.sz+20)*cos(5*(t+self.delay))),
                  0,
                  self.planet.z+((self.planet.sz+20)*sin(5*(t+self.delay))))
        shape(self.globe)
        popMatrix()
        
t = 0.0
dt = 0.01

planetList = [] #list to store planets

def setup():
    global earth,sunglobe, planetList
    size(800,800,P3D)
    noStroke()
    sunimg = loadImage('sun.jpg')#pumpkin.png')
    sunglobe = createShape(SPHERE, 100)
    sunglobe.setTexture(sunimg)
    earth = Planet(400,30.0,'earth.png')
    planetList.append(earth)
    venus = Planet(300,20,'venus.jpg')
    planetList.append(venus)
    mars = Planet(460,15,'mars.jpg')
    planetList.append(mars)
    jupiter = Planet(550,60,'jupiter.jpg')
    planetList.append(jupiter)
    planetList.append(Moon(earth))
    for i in range(3):
        planetList.append(Moon(jupiter))
    
def draw():
    global t, dt, earth,sunglobe
    background(0) #black
    translate(width/2,height/2,-width/2)
    #mouse rotations
    rot = map(mouseX,0,width,0,TWO_PI)
    rotateY(rot)
    tilt = map(mouseY,0,height,0,TWO_PI)
    rotateX(tilt)
    #stroke(255,0,0)
    #sphere(100)
    noStroke()
    shape(sunglobe)
    for planet in planetList:
        planet.update(t)
        #planet.createTrail()
    t += dt