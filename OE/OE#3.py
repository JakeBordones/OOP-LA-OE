class SocMedia:
    def __init__(self, username, psswrd):
        self.username = username
        self.psswrd = psswrd
     
class InstagramAccount(SocMedia):
    def __init__(self, username, psswrd, number_of_followers):
        super().__init__(self, username, psswrd, number_of_followers)
    def share_story(self):
        pass

class TwitterAccount(SocMedia):        
    def __init__(self, username, psswrd, number_of_followers):
        super().__init__(self, username, psswrd, number_of_followers)
    def tweet(self):
        pass