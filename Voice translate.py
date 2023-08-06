import gtts as gt
import playsound as sound

tts = gt.gTTS(
    'rabi shrestha ' * 5
)
tts.save('love.mp3')
sound.playsound('love.mp3')
