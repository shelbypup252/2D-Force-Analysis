import math
from scipy import constants as scp


def welcome():
    print('Welcome to Force Analysis!')
    print('-------------------------------')
    print('[1]: Magnitude/Direction to Composite Parts Force Analysis')
    print('[2]: Magnitude/Direction and Gravity (Earth) Force Analysis')
    print('[3]: Magnitude/Direction and Gravity (specific body mass) Force Analysis')
    print('[4]: Magnitude/Direction and Gravity (Earth) and Friction Force Analysis')
    print('[5]: Magnitude/Direction and Gravity (specific body mass) and Friction Force Analysis')
    print('-------------------------------')


def magnitudeToXComponentForm(magnitude, degDirection):
    radAngle = float((degDirection / (180 / scp.pi))) #converts from degrees to radians
    radcos = math.cos(radAngle) #finds the cosine of radian-converted degree input

    xcompositepart = magnitude * radcos
    return xcompositepart #returns composite part


def magnitudeToYComponentForm(magnitude, degDirection):
    radAngle = float((degDirection / (180 / scp.pi))) #converts from degrees to radians
    radsin = math.sin(radAngle) #finds the cosine of radian-converted degree input

    ycompositepart = magnitude * radsin
    return ycompositepart #returns composite part


def forceGravityEarth(mass):
    forceGravEarth = mass * scp.g
    return forceGravEarth


def forceGravitySpecified(mass, massBody, distanceBetween):
    forceGravitySpecified = float( ( (scp.G) * mass * massBody ) / (distanceBetween ** 2) )
    return forceGravitySpecified


def forceFriction(fricMu, forceNormal):
    forceFriction = float(fricMu * forceNormal)
    return forceFriction




welcome()
userMenuInput = int(input('Please pick an option from the menu above: '))



if userMenuInput == 1:
    
    forceApplied = float(input('Please input the magnitude of the force applied (in Newtons) [float]: '))
    degDirection = float(input('Please input the direction (in degrees) of the force applied [float]: '))

    forceAppliedX = magnitudeToXComponentForm(forceApplied, degDirection)
    forceAppliedY = magnitudeToYComponentForm(forceApplied, degDirection)
    print('')
    print('Analysis:')
    print('')
    print('Force applied on X axis:', forceAppliedX, 'newtons')
    print('Force applied on Y axis:', forceAppliedY, 'newtons')

if userMenuInput == 2:
    
    mass = float(input('Please input the mass of the object that the force is being applied to (in kg) [float]: '))
    forceApplied = float(input('Please input the magnitude of the force applied (in Newtons) [float]: '))
    degDirection = float(input('Please input the direction (in degrees) of the force applied [float]: '))

    forceAppliedX = magnitudeToXComponentForm(forceApplied, degDirection)
    forceAppliedY = magnitudeToYComponentForm(forceApplied, degDirection)
    forceGravEarth = forceGravityEarth(mass)
    forceNormal = forceGravEarth - forceAppliedY
    
    print('')
    print('Analysis:')
    print('')
    print('Force applied on X axis:', forceAppliedX, 'newtons')
    print('Force applied on Y axis:', forceAppliedY, 'newtons')
    print('Gravitational force applied (on -Y axis):', forceGravEarth, 'newtons')
    print('Normal force applied (on +Y axis):', forceNormal, 'newtons')

if userMenuInput == 3:
    
    mass = float(input('Please input the mass of the object that the force is being applied to (in kg) [float]: '))
    massBody = float(input('Please input the mass of the body applying gravity on the object (in kg) [float]: '))
    distanceBetween = float(input('Please input the distance between the centers of both the object and the body (in meters) [float]: '))
    forceApplied = float(input('Please input the magnitude of the force applied (in Newtons) [float]: '))
    degDirection = float(input('Please input the direction (in degrees) of the force applied [float]: '))

    forceAppliedX = magnitudeToXComponentForm(forceApplied, degDirection)
    forceAppliedY = magnitudeToYComponentForm(forceApplied, degDirection)
    forceGravSpecified = forceGravitySpecified(mass, massBody, distanceBetween)
    forceNormal = forceGravSpecified - forceAppliedY
    
    print('')
    print('Analysis:')
    print('')
    print('Force applied on X axis:', forceAppliedX, 'newtons')
    print('Force applied on Y axis:', forceAppliedY, 'newtons')
    print('Gravitational force applied (on -Y axis):', forceGravSpecified, 'newtons')
    print('Normal force applied (on +Y axis):', forceNormal, 'newtons')

if userMenuInput == 4:
    
    mass = float(input('Please input the mass of the object that the force is being applied to (in kg) [float]: '))
    fricMu = float(input('Please input the friction coefficient (mu value) [float]: '))
    forceApplied = float(input('Please input the magnitude of the force applied (in Newtons) [float]: '))
    degDirection = float(input('Please input the direction (in degrees) of the force applied [float]: '))

    forceAppliedX = magnitudeToXComponentForm(forceApplied, degDirection)
    forceAppliedY = magnitudeToYComponentForm(forceApplied, degDirection)
    forceGravEarth = forceGravityEarth(mass)
    forceNormal = forceGravEarth - forceAppliedY
    forceFriction = forceFriction(fricMu, forceNormal)
    
    print('')
    print('Analysis:')
    print('')
    print('Force applied on X axis:', forceAppliedX, 'newtons')
    print('Force applied on Y axis:', forceAppliedY, 'newtons')
    print('Gravitational force applied (on -Y axis):', forceGravEarth, 'newtons')
    print('Normal force applied (on +Y axis):', forceNormal, 'newtons')
    print('Friction force applied (on -X axis):', forceFriction, 'newtons')
    
if userMenuInput == 5:
    
    mass = float(input('Please input the mass of the object that the force is being applied to (in kg) [float]: '))
    massBody = float(input('Please input the mass of the body applying gravity on the object (in kg) [float]: '))
    distanceBetween = float(input('Please input the distance between the centers of both the object and the body (in meters) [float]: '))
    fricMu = float(input('Please input the friction coefficient (mu value) [float]: '))
    forceApplied = float(input('Please input the magnitude of the force applied (in Newtons) [float]: '))
    degDirection = float(input('Please input the direction (in degrees) of the force applied [float]: '))

    forceAppliedX = magnitudeToXComponentForm(forceApplied, degDirection)
    forceAppliedY = magnitudeToYComponentForm(forceApplied, degDirection)
    forceGravSpecified = forceGravitySpecified(mass, massBody, distanceBetween)
    forceNormal = forceGravSpecified - forceAppliedY
    forceFriction = forceFriction(fricMu, forceNormal)
    
    print('')
    print('Analysis:')
    print('')
    print('Force applied on X axis:', forceAppliedX, 'newtons')
    print('Force applied on Y axis:', forceAppliedY, 'newtons')
    print('Gravitational force applied (on -Y axis):', forceGravSpecified, 'newtons')
    print('Normal force applied (on +Y axis):', forceNormal, 'newtons')
    print('Friction force applied (on -X axis):', forceFriction, 'newtons')


if not(userMenuInput >= 1 and userMenuInput <= 5):
    print('Please select a valid input')
    print('-------------------------------')
    print('[1]: Magnitude/Direction to Composite Parts Force Analysis')
    print('[2]: Magnitude/Direction and Gravity (Earth) Force Analysis')
    print('[3]: Magnitude/Direction and Gravity (specific body mass) Force Analysis')
    print('[4]: Magnitude/Direction and Gravity (Earth) and Friction Force Analysis')
    print('[5]: Magnitude/Direction and Gravity (specific body mass) and Friction Force Analysis')
    print('-------------------------------')
    userMenuInput = int(input('Please pick an option from the menu above: '))