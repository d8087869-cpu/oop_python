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
#6
class Device:
    def __init__(self, name):
        self.name = name
    def run_command(self, cmd):
        print(f"Device {self.name} received command: {cmd}.")
class SmartTV(Device):
    def run_command(self, cmd):
        print(f"TV {self.name} is executing '{cmd}' on the screen.")
class SmartLamp(Device):
    def run_command(self, cmd):
        print(f"Lamp {self.name} is adjusting brightness for '{cmd}'.")
class SmartSpeaker(Device):
    def run_command(self, cmd):
        print(f"Speaker {self.name} is playing a sound for '{cmd}'.")
class SmartAC(Device):
    def run_command(self, cmd):
        print(f"AC {self.name} is changing temperature for '{cmd}'.")
def send_command(device, cmd):
    device.run_command(cmd)
devices = [
    SmartTV("Samsung"),
    SmartLamp("Desk Lamp"),
    SmartSpeaker("Echo"),
    SmartAC("Living Room AC")]
for device in devices:
    send_command(device, "start")

#7
class Device:
    def __init__(self,name):
        self.name = name
    def run_schedule(self,hour):
        print(f'{self.name} is idle')
class SmartLamp(Device):
    def run_schedule(self, hour):
        if 18<= hour<= 23:
            print(f'{self.name}: turning on.')
        else:
            print(f'{self.name}: turning off.')
class SmartAC(Device):
    def run_schedule(self, hour):
        if 12<= hour<=20:
            print(f'{self.name}: turning on.')
        else:
            print(f'{self.name} turning: off.')
class SmartTV(Device):
    def run_schedule(self, hour):
        if 20 <= hour<=23:
            print(f'{self.name} turning: on')
        else:
            print(f'{self.name} turning: off.')

lamp = SmartLamp("Bedroom Lamp")
ac = SmartAC("Living Room AC")
tv = SmartTV("Samsung TV")
lamp.run_schedule(21)
ac.run_schedule(21)
tv.run_schedule(21)

#8
class Device: 
    def __init__(self,name):
        self.name =name
    def energy_usage(self):
        print( " 10 watts")
class SmartTV(Device):
    def energy_usage(self):
        return 150
class SmartAC(Device):
    def energy_usage(self):
        return 900
class SmartLamp(Device):
    def energy_usage(self):
        return 8
class SmartSpeaker(Device):
    def energy_usage(self):
        return 30

devices = [
    SmartTV("Samsung"),
    SmartAC("Living Room AC"),
    SmartLamp("Desk Lamp"),
    SmartSpeaker("Echo")]
total_energy = 0
for device in devices:
    watts = device.energy_usage()
    print(f"{watts}W")
    total_energy = total_energy + watts

print(f'Total: {total_energy}W')
'''
#9
class Device:
    def __init__(self,name):
        self.name= name
    def activate(self):
        print(f"Device {self.name} is now on.")
    def deactivate(self):
        print(f"Device {self.name} is now off.")
    def status(self):
        print(f"Device {self.name} status unknon.")

class SmartTV(Device):
    def activate(self):
        print(f"TV {self.name} is playing the home screen.")
    def deactivate(self):
        print(f"TV {self.name} is turning off.")
    def status(self):
        print(f"{self.name}: TV is ready.")

class SmartLamp(Device):
    def activate(self):
        print(f"Lamp {self.name} is glowing.")
    def deactivate(self):
        print(f"Lamp {self.name} is dimming and turning off.")
    def status(self):
        print(f"{self.name}: Lamp is set.")

class SmartSpeaker(Device):
    def activate(self):
        print(f"Speaker {self.name} is ready to play music.")
    def deactivate(self):
        print(f"Speaker {self.name} is powering down.")
    def status(self):
        print(f"{self.name}: Speaker is standing by.")

class SmartAC(Device):
    def activate(self):
        print(f"AC {self.name} is cooling the room.")
    def deactivate(self):
        print(f"AC {self.name} is cooling down and switching off.")
    def status(self):
        print(f"{self.name}: AC is regulating temperature.")

class SmartLock(Device):
    def activate(self):
        print(f"Lock {self.name} is unlocking.")
    def deactivate(self):
        print(f"Lock {self.name} is locking.")
    def status(self):
        print(f"{self.name}: Lock is secured.")

class HomeSystem:
    def __init__(self, devices):
        self.devices = devices
    def activate_all(self):
        for device in self.devices:
            device.activate()
    def deactivate_all(self):
        for device in self.devices:
            device.deactivate()
    def system_report(self):
        for device in self.devices:
            device.status()

devices = [
    SmartTV("Samsung"),
    SmartLamp("Desk Lamp"),
    SmartSpeaker("Echo"),
    SmartAC("Living Room AC"),
    SmartLock("Front Door")]
home = HomeSystem(devices)
print("--- Activating all devices ---")
home.activate_all()
print("--- Deactivating all devices ---")
home.deactivate_all()
print("--- System report ---")
home.system_report()

#10
class Device:
    def __init__(self,name):
        self.name = name 
    def trigger_alarm(self,alert_type):
        print(f"{self.name} received alert: {alert_type}.")
class SmartLamp(Device):
        def trigger_alarm(self, alert_type):
            print(f"Lamp {self.name} is flashing on and off : {alert_type}.")
class SmartSpeaker(Device):
        def trigger_alarm(self, alert_type):
            print(f"Speaker {self.name} is playing a loud for alert: {alert_type}.")
class SmartTV(Device):
    def trigger_alarm(self, alert_type):
        print(f"TV {self.name} is showing an emergency broadcast for alert: {alert_type}.")
class SmartDoorLock(Device):
    def trigger_alarm(self, alert_type):
        print(f"Lock {self.name} is locking the door. Confirmed locked due to alert: {alert_type}.")
class AlarmSystem:
    def __init__(self, devices):
        self.devices = devices
    def send_alert(self, alert_type):
        for device in self.devices:
            device.trigger_alarm(alert_type)
devices = [
    SmartLamp("Bedroom Lamp"),
    SmartSpeaker("Echo"),
    SmartTV("Samsung TV"),
    SmartDoorLock("Front Door")]

alarm_system = AlarmSystem(devices)
print("--- Fire alert ---")
alarm_system.send_alert("fire")

print("--- Break-in alert ---")
alarm_system.send_alert("break-in")