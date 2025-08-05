import pyxel

class DIRECTION:
    NONE = 0
    NORTH = 1
    EAST = 2
    WEST = 3
    SOUTH = 4

WALK_STEP = 8 #4
WALK_HOLD = 3
WALK_REPEAT = 4

class Sandbox:
    def __init__(self):
        pyxel.init(256,256,title="map")
        pyxel.load('../my_resource.pyxres')
        pyxel.playm(0)
        
        self.direction = None
        self.pos_x = 0
        self.pos_y = 0
        self.hit = False
        self.tile = None

        pyxel.run(self.update, self.draw)

    #ゲーム更新
    def update(self):
        if pyxel.btnp(pyxel.KEY_LEFT,WALK_HOLD,WALK_REPEAT):
            self.direction = DIRECTION.WEST
            self.pos_x -= WALK_STEP
        elif pyxel.btnp(pyxel.KEY_RIGHT,WALK_HOLD,WALK_REPEAT):
            self.direction = DIRECTION.EAST
            self.pos_x += WALK_STEP
        elif pyxel.btnp(pyxel.KEY_UP,WALK_HOLD,WALK_REPEAT):
            self.direction = DIRECTION.NORTH
            self.pos_y -= WALK_STEP
        elif pyxel.btnp(pyxel.KEY_DOWN,WALK_HOLD,WALK_REPEAT):
            self.direction = DIRECTION.SOUTH
            self.pos_y += WALK_STEP
        self.hit = self.atari()
        self.tile = pyxel.tilemaps[0].pget(self.pos_x/8,self.pos_y/8)

        if self.pos_x > 120:
            pyxel.camera(120,0)
    
        if self.pos_y > 120:
            pyxel.camera(0, 120)

    def atari(self):
        if self.pos_x < 72 and 100 < self.pos_y + 16:
            return True
        if self.pos_x < 72 and self.pos_y < 132:
            return True
        if 40 < self.pos_x + 16 and 100 < self.pos_y + 16:
            return True
        if 40 < self.pos_x + 16 and self.pos_y < 132:
            return True

        return False
    
    #ゲーム描画
    def draw(self):
        pyxel.cls(7)
        pyxel.bltm(0,0,0,0,0,256,256)

        pyxel.rectb(5,5,50,80,0)
        pyxel.text(7,7,"walk()",0)
        pyxel.text(7,15,"talk(t)",0)
        pyxel.text(7,23, "dukusi", 0)
        pyxel.text(7,31, str(self.tile),0)
        pyxel.text(7,39, str(self.pos_x), 0)
        pyxel.text(17,39, str(self.pos_y), 0)
        pyxel.text(7,47, str(pyxel.tilemaps[0].imgsrc),0)
        
        match self.direction:
            case DIRECTION.NORTH:
                pyxel.blt(self.pos_x,self.pos_y,0,48,0,16,16,None)
            case DIRECTION.WEST:
                pyxel.blt(self.pos_x,self.pos_y,0,32,0,16,16,None)
            case DIRECTION.EAST:
                pyxel.blt(self.pos_x,self.pos_y,0,16,0,16,16,None)
            case DIRECTION.SOUTH:
                pyxel.blt(self.pos_x,self.pos_y,0,0,0,16,16,None)

        # pyxel.rect(40,100, 32,32,4)

        # pyxel.text(100,100, str(self.hit),0)

        if self.hit:
            pyxel.text(200,200,"hit",0)

Sandbox()