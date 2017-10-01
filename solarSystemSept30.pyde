
G = 30.0 #graviational constant
sunSize = 100

class Planet:
    def __init__(self,sz,distanceFromSun,col):
        self.sz = sz #diameter
        self.distanceFromSun = distanceFromSun 
        self.col = col #color
        self.acc = PVector(0,0,0) #acceleration vector
        self.vel = PVector(0,0,20.0) #velocity vector
        self.loc = PVector(distanceFromSun,0,0) #location vector
        self.points = [] #list of locations
    
    def update(self):
        self.distanceFromSun = dist(self.loc.x,self.loc.y,self.loc.z,
                                    0,0,0)
        
        #radial vector
        forceVector = PVector(self.loc.x,0,self.loc.z)
        #unit radial vector
        forceVector.normalize()
        
        #use Newton's formula to calculate the force of gravity
        force = -G*self.sz*sunSize/self.distanceFromSun**2
        
        #multiply force by unit radial vector
        self.acc = PVector.mult(forceVector,force)
        #add acceleration vector to velocity vector
        self.vel.add(self.acc)
        
        #add velocity vector to location vector
        self.loc.add(self.vel)
        
        #add location points to points list
        self.points.append(PVector(self.loc.x,
                                   self.loc.y,
                                   self.loc.z))
        
        
        #go to location, draw planet
        pushMatrix()
        translate(self.points[-1].x,0,self.points[-1].z)
        fill(self.col)
        noStroke()
        sphere(self.sz)
        popMatrix()
        #if len(self.points) > 100:
            #self.points.pop(0)
        
    def drawTrail(self):
        if len(self.points) > 2:
            for i,pt in enumerate(self.points):
                if i < len(self.points) -2:
                    stroke(255)
                    #line(300*cos(i),0,300*sin(i),
                     #    300*cos(i+1),0,300*sin(i+1))
                    line(self.points[i].x,
                         self.points[i].y,
                         self.points[i].z,
                         self.points[i+1].x,
                         self.points[i+1].y,
                         self.points[i+1].z)
        
def sun():
    noStroke()
    fill(255,255,0) #yellow
    sphere(sunSize)
        
def setup():
    global earth
    size(800,800,P3D)
    sphereDetail(24)
    noStroke()
    background(0)
    earth = Planet(30,300.0,color(0,0,255))
    
def draw():
    global earth
    background(0)
    translate(width/2,height/2,-width/2)
    rotateX(radians(-90))
    rotateX(-mouseY/10.0)
    rotateY(mouseX/10.0)
    sun() #draw the sun
    earth.update()
    earth.drawTrail()