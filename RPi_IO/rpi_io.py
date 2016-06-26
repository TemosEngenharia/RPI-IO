import RPi.GPIO as GPIO

# Set up GPIO using BCM numbering
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

def modo0():
    input_pins = [0, 1, 5, 6, 7, 8, 9, 10, 11, 12, 13, 16, 17, 18, 19, 20,
                21, 22, 23, 24, 25, 26, 27]

    output_pins = [26, 27]

    for pin in input_pins:
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    for pin in output_pins:
        GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)

if __name__ == "__main__":
    print "Entrando em modo 0"
    modo0()
