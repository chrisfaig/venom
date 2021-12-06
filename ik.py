import math

# Constante
_coxa = 6
_femour = 7
_tibia = 12.5


_posX = 13
_posY = 3
_zOffset = 6


L1 =  math.sqrt( (_posX**2) + (_posY**2))
print ("L1 : " , L1)

_teta = math.atan(_posY/_posX)
print ("Teta (Servo - 1) : " , _teta , " Rads | Degrees ", math.degrees(_teta))

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


