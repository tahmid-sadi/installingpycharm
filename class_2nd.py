class aeroplane:

    feature = ''

    def __init__(self, string):
        self.feature = string

    def check(self):
        if self.feature == 'Carry passengers':
            return 'Passenger aircraft'
        elif self.feature == 'Carry weapons':
            return 'Combat aircraft'
        elif self.feature == 'Does not carry weapons or passengers':
            return 'Trainer aircraft'
        else:
            return 'Biplane'


Boeing = aeroplane('Carry passengers')
F_18 = aeroplane('Carry weapons')
Cessna = aeroplane('Does not carry weapons or passengers')
Glider = aeroplane('Entertainment')

aircraft_type = Boeing.check()
print(aircraft_type)
print(F_18.check())
print(Glider.check())
aircraft_type2 = Cessna.check()
print(aircraft_type2)