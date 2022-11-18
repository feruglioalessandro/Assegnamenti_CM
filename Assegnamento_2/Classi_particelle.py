import math

## Class - Particle
class Particle:
    def __init__(self, name, mass, charge, momentum =  0):
        self.name = name
        self.mass = mass
        self.charge = charge
        self.momentum = momentum
        
    def print_info(self):
        print(f'Particella: {self.name} \nMassa: {self.mass} MeV/c^2 \nCarica: {self.charge} \n')
    
    def print_more_info(self):
        print(f'Impulso: {self.momentum} MeV/c^2 \nEnergia: {self.energy} MeV/c^2 \nBeta = {self.beta} MeV/c^2 \n')

# Energia
    @property
    def energy(self):
        return math.sqrt(self.mass**2 + self.momentum**2)
    
    @energy.setter
    def energy(self, valore):
        if valore < self.mass:
            print(f'Errore: l\'energia deve essere maggiore o uguale alla massa - Impulso posto a 0 \n')
            self.energy = self.mass
        else:
            self.momentum = math.sqrt(valore**2 - self.mass**2)

# Impulso
    @property
    def momentum(self):
        return self._momentum
    
    @momentum.setter
    def momentum(self, valore):
        if valore < 0:
            print('L\'impulso deve essere positivo - Impulso posto a 0 \n')
            self._momentum = 0
        else:
            self._momentum = valore

# Beta
    @property
    def beta(self):
        return self.momentum
    
    @beta.setter
    def beta(self, valore):
        if valore < 0:
            print('Beta deve essere positivo - Beta posto a 0 \n')
            self.momentum = 0
        else:
            self.momentum = valore
            
# # Gamma
#     @property
#     def gamma(self):
#         return 1/math.sqrt(1 - self.momentum**2)
#     
#     @gamma.setter
#     def gamma(self, valore):
#         if valore < 1:
#             print(f'Il valore di gamma deve essere maggiore o uguale a 1 - Gamma posto a 1 \n')
#             self.momentum = 0
#         else:
#             self.momentum = math.sqrt(1 - 1/valore**2)
            
## Class - Elettrone
class Electron(Particle):
    def __init__(self, momentum = 0):
        Particle.__init__(self, 'electron', 0.511, -1, momentum)

## Main
elettrone = Particle('elettrone', 0.511, -1, -2)
elettrone.print_info()


elettrone.energy = 10
elettrone.print_more_info()

elettrone.beta = 100
elettrone.print_more_info()

elettrone2 = Electron(-5)
elettrone2.print_info()
elettrone2.print_more_info()
