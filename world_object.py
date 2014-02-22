import pygame, json, os


class WorldObject:
    
    name = 'mage'
    path = '/images/classes/'
    spritesheet = None
    spritesheet_data = {'right' : {}}
    animation_right = 'right'
    frames = 0
    current = 1
    frame = 0 
    x = 0
    y = 0
    moving_right = False
    animation_cycle = [1,2,3,4,3,2]
    
    def animate(self):
        if self.frame == 0:
            self.frame = self.frames
            self.current += 1
            if self.current >= len(self.animation_cycle):
                self.current = 0
        self.frame -= 1
        if not self.moving_right:
            self.current = 0
            self.frame = self.frames
        return self.__image_at(self.spritesheet_data[self.animation_right][self.animation_cycle[self.current]])
    
    def move_right(self):
        self.moving_right = True
        print('moving')
    
    def stop_moving(self):
        self.moving_right = False
        print('not_moving')
        
    def rect(self):
        if self.moving_right:
            self.x += 1
        return (self.x, self.y)
    
    def __init__(self, fps):
        self.frames = int(fps / 7)
        self.frame = self.frames
        self.spritesheet = pygame.image.load(self.__getFullPath() + 'model.png').convert()
        self.__loadSpriteSheetData()
        print (self.spritesheet_data)
    
    def __getFullPath(self):
        return os.path.dirname(os.path.realpath(__file__)) + self.path + self.name + '/'
    
    def __loadSpriteSheetData(self):
        datafile = open(self.__getFullPath() + 'model.json')
        json_data = json.loads(datafile.read())
        for frame, frame_data in json_data['frames'].items():
            if frame.startswith(self.animation_right):
                self.spritesheet_data[self.animation_right][int(frame[-5])] = frame_data['frame']
        datafile.close()
        
    def __image_at(self, frame_data):
        rect = pygame.Rect((frame_data['x'], frame_data['y'], frame_data['w'], frame_data['h']))
        surface = pygame.Surface(rect.size)
        surface.set_colorkey((255,255,255))
        image = surface.convert()
        image.blit(self.spritesheet, (0, 0), rect)
        return image