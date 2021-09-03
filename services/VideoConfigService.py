class VideoConfigService:
    video_width:int
    video_height: int
    video_fps: int

    def set_video_width(self,width:str):
        self.video_width = width

    def set_video_height(self,height:str):
        self.video_height = height

    def set_video_fps(self,fps:str):
        self.video_fps = fps

    
    def get_video_width(self):
        if self.video_width is None:
            raise Exception("video width was not set up correctly")
        return self.video_width


    def get_video_height(self):
        if self.video_height is None:
            raise Exception("video height was not set up correctly")
        return self.video_height 

    def get_video_fps(self):
        if self.video_fps is None:
            raise Exception("video fps was not set up correctly")
        return self.video_fps 
