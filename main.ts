input.onSound(DetectedSound.Loud, function on_sound_loud() {
    led.enable(true)
    let i = 10
    while (i > 0) {
        console.log(input.soundLevel())
        led.plotBarGraph(input.soundLevel(), 255)
        control.waitMicros(250000)
        i = i - 1
    }
    led.plotBarGraph(input.soundLevel(), 255)
    led.enable(false)
})
