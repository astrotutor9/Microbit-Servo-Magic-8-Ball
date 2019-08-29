from microbit import *
import random

pin0.set_analog_period(20)

outcomes = {"yes":23, "never":58, "likely":93, "no":140}

print(outcomes.values())

print(list(outcomes.values()))

while True:
    if button_a.is_pressed():
        answer = random.choice(list(outcomes.values()))
        pin0.write_analog(answer)
        sleep(200)