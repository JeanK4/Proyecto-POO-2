class Usuario:
    def __init__(self, nickname, password):
        self.nickname = nickname
        self.password = password

    def setNickname(self, name):
        self.nickname = name

    def setPassword(self, passw):
        self.password = passw

    def getNickname(self):
        return self.nickname

    def getPassword(self):
        return self.password
