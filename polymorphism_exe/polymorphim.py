'''
#1 
class Device:
    def __init__(self,name):
        self.name =name
    def activate(self):
        print(f'Divice {self.name} is now on.')
class SmartTV(Device):
    def activate(self):
        print(f'TV {self.name} is playing the home screen.')
class SmartSpeaker(Device):
    def activate(self):
        print(f'Speaker {self.name} is ready to play music.')
tv = SmartTV('Samsung')
tv.activate()
speaker =SmartSpeaker('Echo')
speaker.activate()
#2
class Device:
    def __init__(self,name):
        self.name= name
    def deactivate(self):
        print(f'Device {self.name} is now off.')
class SmartLamp(Device):
    def deactivate(self):
        print(f'Lamp {self.name} is dimming and turning off.')
class SmartAC(Device):
    def deactivate(self):
        print(f'AC {self.name} is cooling down and switching off.')
lamp = SmartLamp('Bedroom Lamp')
lamp.deactivate()
ac = SmartAC('Living Room AC')
ac.deactivate()        
'''
#3
class Device:
    def __init__(self,name,is_on):
        self.name = name
        self.is_on = is_on
    def status(self):
        if self.is_on:
            print(f'{self.name}: on')
        else:
            print(f'{self.name}: off')
class SamrtTV(Device):
    def __init__(self, name, is_on,channel):
        super().__init__(name, is_on)
        self.channel = channel
    def status(self):
        if self.is_on:
            print(f'{self.name} : on, watcing channel {self.channel}.')
        else:
            print(f'{self.name}: off')
class SamrtSpeaker(Device):
    def __init__(self, name, is_on,song):
        super().__init__(name, is_on)
        self.song = song
    def status(self):
        if self.is_on:
            print(f'{self.name} : on, playing {self.song}.')
        else:
            print(f'{self.name}: off')
tv = SamrtTV('LG',True,8)
tv.status()
speaker = SamrtSpeaker(f'Alexa',True,"Bohemian Rhapsody")
speaker.status()