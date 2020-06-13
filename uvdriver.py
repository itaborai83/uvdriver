import pigpio
import time

PWM         = 4
DECDUTY     = 5
INCDUTY     = 6
DC_LVL      = 4
DC_MAX_LVL  = 8
CBK_DECDUTY = None
CBK_INCDUTY = None

def setup():
    global CBK_DECDUTY, CBK_INCDUTY
    pi = pigpio.pi()
    pi.set_mode(PWM, pigpio.OUTPUT)
    pi.set_mode(DECDUTY, pigpio.INPUT)
    pi.set_mode(INCDUTY, pigpio.INPUT)
    pi.set_pull_up_down(DECDUTY, pigpio.PUD_UP)
    pi.set_pull_up_down(INCDUTY, pigpio.PUD_UP)
    pi.set_glitch_filter(DECDUTY, 100)
    pi.set_glitch_filter(INCDUTY, 100)
    CBK_DECDUTY = pi.callback(DECDUTY, pigpio.RISING_EDGE, decrease_dc_cbk)
    CBK_INCDUTY = pi.callback(INCDUTY, pigpio.RISING_EDGE, increase_dc_cbk)
    return pi

def teardown(pi):
    CBK_DECDUTY.cancel()
    CBK_INCDUTY.cancel()
    stop_pwm(pi)
    pi.set_glitch_filter(DECDUTY, 0)
    pi.set_glitch_filter(INCDUTY, 0)
    pi.set_pull_up_down(DECDUTY, pigpio.PUD_OFF)
    pi.set_pull_up_down(INCDUTY, pigpio.PUD_OFF)
    pi.stop()

def start_pwm(pi):
    set_dutycycle(DC_LVL)

def stop_pwm(pi):
    set_dutycycle(0)

def set_dutycycle(lvl):
    assert 0 <= lvl <= 8
    dc = (1 << lvl) - 1
    print('setting duty cycle to ', dc)
    pi.set_PWM_dutycycle(PWM, dc)

def increase_dc_cbk(gpio, logic_level, tick):
    assert gpio == INCDUTY
    assert logic_level == True # rising edge
    global DC_LVL
    DC_LVL += 1
    if DC_LVL > DC_MAX_LVL:
        DC_LVL = DC_MAX_LVL
    set_dutycycle(DC_LVL)

def decrease_dc_cbk(gpio, logic_level, tick):
    assert gpio == DECDUTY
    assert logic_level == True # rising edge
    global DC_LVL
    DC_LVL -= 1
    if DC_LVL < 0:
        DC_LVL = 0
    set_dutycycle(DC_LVL)

try:
    pi = setup()
    start_pwm(pi)
    while 1: 
        time.sleep(0.1)
finally:    
    teardown(pi)


