import subprocess
import time

def temp_freq():
	freq = subprocess.run(['cat', '/sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq'], stdout=subprocess.PIPE)
	freq = str(freq.stdout.decode('utf-8'))
	temp = subprocess.run(['vcgencmd', 'measure_temp'], stdout=subprocess.PIPE)
	temp = str(temp.stdout.decode('utf-8')) 
	return freq, temp


def volts():
	voltage = subprocess.run(['/opt/vc/bin/vcgencmd', 'get_throttled'], stdout=subprocess.PIPE)
	voltage = str(voltage.stdout.decode('utf-8'))
	return voltage

def run_interupt():
	print('\n\nSpooling...')
	time.sleep(5)
	test()
	



def dashboard():
	freq, temp  = temp_freq()
	state = volts()
	while True:
		if state == 'throttled=0x0\n':
			print ("\n\nVoltage is nominal...")
			print (temp, 'Freq: ', freq)
			return
		elif state == 'throttled=0x50000\n':
			print ("\n\nPower is unstable. CPU is throttled...")
			print (temp, 'Freq: ', freq)
			return
		elif state == 'throttled=0x50005\n':
			print ('\n\nUnder-voltage, process delayed while volage spools up...')
			run_interupt()  
		else: 
			print (state)
			break
	

