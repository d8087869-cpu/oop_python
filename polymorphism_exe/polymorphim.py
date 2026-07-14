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
'''
'''
#4
class Device:
    def __init__(self,name):
        self.name=name
    def activaet(self):
        print(f'{self.name} is on.')
class SmartTv(Device):
    def activaet(self):
        print(f'TV {self.name} is playing the home screen')
class SmartLamp(Device):
    def activaet(self):
        print(f'{self.name} is glowing warmly.')
class SmartSpeaker(Device):
    def activaet(self):
        print(f'Speaker {self.name} is ready to play music')

tv = SmartTv('LG')
lamp=SmartLamp('Desk Lamp')
speaker=SmartSpeaker('Echo')
devices= [SmartTv('LG'),SmartLamp('Desk Lamp'),SmartSpeaker('Echo')]
for device in devices:
    device.activaet()
'''
#5 
class Device:
    def __init__(self,name):
        self.name=name
    def set_volume(self,level):
        self.level =level
        print(f'Device {self.name} volume set to {self.level}')
class SmartSpeaker(Device):
    def set_volume(self,level):
        self.level = level
        print(f'Speaker {self.name} is now at volume {self.level}/10')
        if self.level > 7:
            print('loud')
        else:
            print("Up the volume")
class SmartTV(Device):
    def set_volume(self,level):
        self.level =level
        print(f'TV {self.name} volume: {self.level}.')
        if self.level == 0:
            print('muted!')
        else:
            print('')
speaker = SmartSpeaker("BOSE")
speaker.set_volume(9)
speaker.set_volume(3)

tv =SmartTV('LG')
tv.set_volume(0)
tv.set_volume(5)