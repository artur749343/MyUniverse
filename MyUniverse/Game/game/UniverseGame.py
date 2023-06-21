import pygame, json, os
from math import acos, degrees, cos, sin, pi


def scalar(v1, v2):
    return v1[0]*v2[0]+v1[1]*v2[1]
 
def module(v1):
    return (v1[0]**2+v1[1]**2)**0.5

def v_to_ang(v1, v2):
    return degrees(acos(scalar(v1, v2)/(module(v1)*module(v2))))

def ang_to_v(angle): return [cos(angle*pi/180), sin(angle*pi/180)]

# ang=v_to_ang((1,1), (object.all["x"], object.all["y"]))


class Object():
    def __init__(self,all:dict={}) -> None:
        self.all=all
    def update(self):
        for i, v in self.all.items():
            if type(v)==list and i!="space" and v[2]=="time":
                if type(self.all[v[1]])==list:
                    for x in range(len(v[0])):
                        if type(self.all[v[1]][0])==list: self.all[v[1]][0][x]+=v[0][x]
                        else: self.all[v[1]][x]+=v[0][x]
                else:
                    self.all[v[1]]+=v[0]
        if self.all["power"]<0:
            self.all["power"]=0
        elif self.all["power"]>255:
            self.all["power"]=255

# def add(t, x, num):
#         x=[num]+x
#         for t1 in range(t):
#             for x1 in range(len(x)-1):
#                 x[x1+1]+=x[x1]
#         return x[1:]



if __name__=="__main__":
    pygame.init()
    path="\\".join(str(os.path.abspath(__file__)).split("\\")[:-1])+"\\"
    gameDisplay = pygame.display.set_mode((800,600))
    gameDisplay.fill((0,0,0))
    all, other=json.load(open(path+"game.json", 'r', encoding="utf-8")), json.load(open(path+"other.json", 'r', encoding="utf-8"))
    size, objects, t, clock=all["size"], [Object(a) for a in all["objects"]], 0, pygame.time.Clock()
    for v in other["formules"]:
        for i, obj in enumerate(all["objects"]):
            if type(obj[v[2]][0])==list: all["objects"][i][v[0]]+=v[1]*obj[v[2]][0][0]
            else: all["objects"][i][v[0]]+=v[1]*obj[v[2]][0]
    while True:
        clock.tick(all["fps"])
        t+=1
        [object.update() for object in objects]
        gameDisplay.fill((0,0,0))
        [pygame.draw.rect(gameDisplay, (object.all["power"],object.all["power"],object.all["power"]), (object.all["space"][0]*size,object.all["space"][1]*size,size,size)) for object in objects]
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                for e in other["events"]:
                    if event.key==e[0]:
                        exec(e[1])
        for k, v in other["rules"]:
            if eval(k):exec(v)
        pygame.display.update()