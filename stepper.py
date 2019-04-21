import machine
import time

pins = [
	machine.Pin(5, machine.Pin.OUT),  # 1
	machine.Pin(18, machine.Pin.OUT), # 2
	machine.Pin(19, machine.Pin.OUT), # 4
	machine.Pin(21, machine.Pin.OUT), # 8
]

rychlost = 0.001
uhel = 360

def rotateCW(steps):
	totalSteps = 0	
	while totalSteps < steps:
		rotateCWStep()
		totalSteps += 8

def rotateCCW(steps):
	totalSteps = 0
	while totalSteps < steps:
		rotateCCWStep()
		totalSteps += 8

def rotateCWAngle(angle):
	for i in range(angle * 64 / 45):
		rotateCWStep()

def rotateCCWAngle(angle):
	for i in range(angle * 64 / 45):
		rotateCCWStep()

def loop():
	for i in range(uhel * 64 / 45):
		rotateCWStep()
	# pauza po dobu 1 vteřiny
	time.sleep(1)

	for i in range(uhel * 64 / 45):
		rotateCCWStep()

	# pauza po dobu 1 vteřiny
	time.sleep(1)


def rotateCWStep():
	step1()
	step2()
	step3()
	step4()
	step5()
	step6()
	step7()
	step8()


def rotateCCWStep():
	step8()
	step7()
	step6()
	step5()
	step4()
	step3()
	step2()
	step1()


def step1() :
	pins[0].value(1)
	pins[1].value(0)
	pins[2].value(0)
	pins[3].value(0)
	time.sleep(rychlost)

def step2():
	pins[0].value(1)
	pins[1].value(1)
	pins[2].value(0)
	pins[3].value(0)
	time.sleep(rychlost)

def step3():
	pins[0].value(0)
	pins[1].value(1)
	pins[2].value(0)
	pins[3].value(0)
	time.sleep(rychlost)

def step4():
	pins[0].value(0)
	pins[1].value(1)
	pins[2].value(1)
	pins[3].value(0)
	time.sleep(rychlost)

def step5():
	pins[0].value(0)
	pins[1].value(0)
	pins[2].value(1)
	pins[3].value(0)
	time.sleep(rychlost)

def step6():
	pins[0].value(0)
	pins[1].value(0)
	pins[2].value(1)
	pins[3].value(1)
	time.sleep(rychlost)

def step7():
	pins[0].value(0)
	pins[1].value(0)
	pins[2].value(0)
	pins[3].value(1)
	time.sleep(rychlost)

def step8():
	pins[0].value(1)
	pins[1].value(0)
	pins[2].value(0)
	pins[3].value(1)
	time.sleep(rychlost)