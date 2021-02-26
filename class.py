class Car:
    def __init__(self,model,type,plate):
        self.model = model
        self.type = type
        self.plate= plate
    def getModel(self):
        return self.model
    def getType(self):
        return self.type
    def getPlate(self):
        return self.plate   
Car1 = Car ("BMW", "Sedan", "KDC 001")
print(Car1.getModel())
print(Car1.getType())
print(Car1.getPlate())
