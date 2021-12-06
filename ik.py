import math
import serial
import lewansoul_lx16a
import time


SERIAL_PORT_1 = '/dev/ttyUSB0'

controller_1 = lewansoul_lx16a.ServoController(
    serial.Serial(SERIAL_PORT_1, 115200, timeout=1),
)


# Constante
_coxa = 6.5
_femour = 7.5
_tibia = 12.5

#_posX = 13
#_posY = 3
#_zOffset = 6

def _ik (_posX, _posY, _zOffset) :
    L1 =  math.sqrt( (_posX**2) + (_posY**2))
    print ("L1 : " , L1)

    _teta = math.atan(_posY/_posX)
    print ("Teta : " , _teta , " Rads | Degrees ", math.degrees(_teta))

    L = math.sqrt ( (_zOffset**2) + (L1-_coxa)**2  )
    print ("L : " , L)

    _alpha1 = math.acos(_zOffset/L)
    print ("Aplha -1  : " , _alpha1 , " Rads | Degrees ", math.degrees(_alpha1))

    _alpha2 = math.acos ( ((_tibia**2) - (_femour**2) - (L**2)) / (2*(_femour)*(L) ) )
    print ("Aplha -2  : " , _alpha2 , " Rads | Degrees ", math.degrees(_alpha2))

    _alpha = _alpha2  + _alpha1
    print ("Aplha (1+2)  : " , _alpha , " Rads | Degrees ", math.degrees(_alpha))

    _beta = math.acos( ((L**2) - (_tibia**2) - (_femour**2))/(-2*(_tibia)*(_femour)  )   )
    print ("Beta  : " , _beta , " Rads | Degrees ", math.degrees(_beta))


    _teta = math.degrees(_teta)
    _alpha = math.degrees(_alpha)
    _beta = math.degrees(_beta)

    return _teta, _alpha, _beta


def moveLeg(perna, _teta, _alpha, _beta ) :

    if perna == 2 :
        coxa_servo = controller_1.servo(4)
        femour_servo = controller_1.servo(5)
        tibia_servo = controller_1.servo(6)
        _teta = (180 - _teta)/0.24
        print ('Perna ', perna, ' Coxa_Servo ', _teta)
        coxa_servo.move_prepare(_teta)
        controller_1.move_start()

        _alpha = (180 - _teta)/0.24
        print ('Perna ', perna, ' Femour_Servo ', _alpha)
        femour_servo.move_prepare(_alpha)
        controller_1.move_start()

        _beta = (180 - _teta)/0.24
        print ('Perna ', perna, ' Tibia_Servo ', _beta)
        tibia_servo.move_prepare(_beta)
        controller_1.move_start()


_teta , _alpha, _beta = _ik(1,14,10)

moveLeg(2,_teta,_alpha,_beta)

