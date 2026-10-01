
def on_sound_loud():
    led.enable(True)
    i = 10
    while(i > 0):
        print(input.sound_level())
        led.plot_bar_graph(input.sound_level(), 255)
        control.wait_micros(250000)
        i = i-1
    led.plot_bar_graph(input.sound_level(), 255)
    led.enable(False)
    
input.on_sound(DetectedSound.LOUD, on_sound_loud)
