def get_temperature():
	with open("/sys/bus/w1/devices/28-000005fc565e/w1_slave") as f:
		s = f.read()
		s = s.split('\n')[1].split(' ')[9]
		temperature = float(s[2:]) / 1000.0

	return temperature

if __name__ == "__main__":
	print temperature
