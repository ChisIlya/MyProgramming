
import numpy
import numpy.linalg
import matplotlib.pyplot as plt

G = 50.0  
collision_distance = 3.0  
model_delta_t = 0.001
time_to_model = 10

class MaterialPoint:
    """Материальная точка, движущаяся по двумерной плоскости"""
    
    def __init__(self, mass: 'float', position: 'numpy.array', velocity: 'numpy.array'):
        self.mass = mass
        self.position = position
        self.velocity = velocity
    
    @staticmethod
    def gravity_dencity(dist: 'float')-> 'float':
        if dist > collision_distance:
            return G / dist 
    
        else:
            return -G / dist ** 3 
    
    def force_induced_by_other(self, other: 'MaterialPoint')-> 'numpy.array':
        delta_p = other.position - self.position
        distance = numpy.linalg.norm(delta_p)  
        force_direction = delta_p / distance
        force = force_direction * self.mass * other.mass * MaterialPoint.gravity_dencity(distance)
        return force
    
    def advance(self):
        self.position += self.velocity * model_delta_t

    def apply_force(self, force: 'numpy.array'):
        self.velocity += force * model_delta_t / self.mass

centrum = MaterialPoint(500.0, numpy.array([0.0, 0.0]), numpy.array([0.0, 0.0]))
point_1 = MaterialPoint(10.0, numpy.array([50.0, 0.0]), numpy.array([0.0, 15.0]))
point_2 = MaterialPoint(10.0, numpy.array([50.0, 40.0]), numpy.array([-7.0, 7.0]))

System = [centrum, point_1, point_2]
Number_of_Points = 3

def model_step():
    for number in range(1, Number_of_Points):
        System[number].apply_force(System[number].force_induced_by_other(System[0]))
        System[number].advance()

xs = []
ys = []
for number in range(Number_of_Points):
    xs.append([])
    ys.append([])

for stepn in range(int(time_to_model / model_delta_t)):
    for number in range(Number_of_Points):
        xs[number].append(System[number].position[0])
        ys[number].append(System[number].position[1])
    model_step()

c = plt.Circle((0, 0), 2, color='b')
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.add_patch(c)

for number in range(Number_of_Points):
    plt.plot(xs[number],ys[number])

plt.show()
