import pyttsx
print('enter the string you want to say')
Text=raw_input();
engine = pyttsx.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-120)
engine.say(Text)
