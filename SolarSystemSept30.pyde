
G = 0.1 #graviational constant
sunSize = 100

class Planet:
    def __init__(self,sz,distanceFromSun,col):
        self.sz = sz #diameter
        self.distanceFromSun = distanceFromSun 
        self.col = col #color
        self.acc = PVector(0,0,0) #acceleration vector
        self.vel = PVector(0,0,10) #velocity vector
        self.loc = PVector(distanceFromSun,0,0) #location vector
        self.points = [] #list of locations
    
    def update(self):
        self.distanceFromSun = dist(self.loc.x,self.loc.y,self.loc.z,
                                    0,0,0)
        
        #radial vector
        forceVector = PVector(-self.loc.x,0,-self.loc.z)
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
        self.points.append(self.loc)
        
        if len(self.points) > 1:
            for i in range(len(self.points) - 1):
                point(self.points[i].x,0,self.points[i].z)
        
        #go to location, draw planet
        pushMatrix()
        translate(self.points[-1].x,0,self.points[-1].z)
        fill(self.col)
        sphere(self.sz)
        popMatrix()
        
def sun():
    fill(255,255,0) #yellow
    sphere(sunSize)
        
def setup():
    global earth
    size(800,800,P3D)
    background(0)
    earth = Planet(30,100,color(0,0,255))
    
def draw():
    global earth
    background(0)
    translate(width/2,height/2,-width/2)
    sun() #draw the sun
    earth.update()
    