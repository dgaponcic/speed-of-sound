import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons

plt.style.use('dark_background')

fig, ax = plt.subplots()
plt.subplots_adjust(left=0.25, bottom=0.25)
t = np.arange(0.0111, 33.0, 0.001)
temp0 = 0
speed0 = 331
delta_speed = 0.0001
s = (331 + 0.6 * temp0)/t
lines = plt.plot(t, s, lw=2, color='red')
l = lines[0]
plt.xlabel('wave length, m')
plt.ylabel('frequency, Hz')
plt.axis([0.0, 35.0, 8.1, 32768])

axcolor = 'lightgoldenrodyellow'
axspeed = plt.axes([0.25, 0.05, 0.65, 0.03], facecolor=axcolor)
axtemp = plt.axes([0.25, 0.1, 0.55, 0.03], facecolor=axcolor)
sspeed = Slider(axspeed, 'Speed', 274.6, 365.2, valinit=speed0, valstep=delta_speed)
stemp = Slider(axtemp, 'Temp', -94, 57, valinit=temp0, valstep=0.001)
temperature = temp0
absSpeed = speed0

def updateTemp(val):
    temp = stemp.val
    speed = 331 + 0.6 * temp
    if speed != sspeed.val:
        sspeed.set_val(speed)
    l.set_ydata(speed/t)
    fig.canvas.draw_idle()

def updateSpeed(val):
    speed = sspeed.val
    temp = (speed - 331) / 0.6
    if(temp != stemp.val):
        stemp.set_val(temp)
    l.set_ydata((331 + 0.6 * temp)/t)
    fig.canvas.draw_idle()


sspeed.on_changed(updateSpeed)
stemp.on_changed(updateTemp)

resetax = plt.axes([0.0, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')

def reset(event):
    sspeed.reset()
    stemp.reset()
button.on_clicked(reset)

rax = plt.axes([0.01, 0.7, 0.15, 0.15], facecolor=axcolor)
radio = RadioButtons(rax, ('yellow', 'pink', 'green'), active=0)

def colorfunc(label):
    l.set_color(label)
    fig.canvas.draw_idle()
radio.on_clicked(colorfunc)

plt.show()