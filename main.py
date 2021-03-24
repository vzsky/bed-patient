import RPi.GPIO as GPIO
from hx711 import HX711 as LoadCell
from motor import Motor

MOTOR_DIR = 29
MOTOR_PULSE = 31
LOADCELL_A_DT = 11
LOADCELL_A_SCK = 13
LOADCELL_A_DT = 16
LOADCELL_A_SCK = 18
MEASURE_TIMES = 50

GPIO.setmode(GPIO.BOARD)
loadcell_a = LoadCell(dout_pin=LOADCELL_A_DT, pd_sck_pin=LOADCELL_A_SCK)
loadcell_b = LoadCell(dout_pin=LOADCELL_A_DT, pd_sck_pin=LOADCELL_A_SCK)
motor = Motor(pin_dir=MOTOR_DIR, pin_pulse=MOTOR_PULSE)

# weight_a = loadcell_a.get_raw_data_mean(MEASURE_TIMES)
# weight_b = loadcell_b.get_raw_data_mean(MEASURE_TIMES)

motor.spin(0, 2, 10)

GPIO.cleanup()
