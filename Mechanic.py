
class Person:   
    def __init__(self, name, driversLicense):
        self.name = name
        self.driversLicense = driversLicense
    def getID(self):
        raise NotImplementedError()
    
class Employee(Person):
    def __init__(self, name, driversLicense):
        super().__init__(name, driversLicense)
        self.EmployeeID = self.getID()
        
    def getID(self):
        return "E-" + self.name[:2].upper() + self.driversLicense
           
        
class Client(Person):
    def __init__(self, name, driversLicense):
        super().__init__(name, driversLicense)
        self.ClientID = self.getID()
        self.ownCars = {}
    def getID(self):    
        return "C-" + self.name[:2].upper() + self.driversLicense
    def addCar(self, car):
        self.ownCars[car.noPlate] = car
       
class CarModel:
    def __init__(self, carNationality, carBrand, carModel ):
        self.carNationality = carNationality
        self.carBrand = carBrand
        self.carModel = carModel
    def getID(self):
        return F"{self.carBrand}_{self.carModel}".lower()


class Car: 
    def __init__(self, carColour, carBodyType, noPlate, buildDate, model: CarModel):
        self.carColour = carColour
        self.carBodyType = carBodyType
        self.noPlate = noPlate
        self.buildDate = buildDate
        self.model = model
    def __str__(self):
        return f"{self.model.carBrand} {self.model.carModel} - {self.carColour} {self.carBodyType} ({self.noPlate})"
    

class CarRegistry:
    def __init__(self):
        self.carRegistery = []
    def registerCar(self, car: Car):
        self.carRegistery.append(car)   
    def showRegister(self):
        for car in self.carRegistery:
            print(f"Car Registry: {car}")


class CarModelDataBase:
    def __init__(self):
        models = [
            CarModel("Gernany", "Audi", "TT"),
        ]
       
        self.models = {model.getID(): model for model in models   } 


class ClientDataBase:
    def __init__(self):
        self.clients = []
    def registerClient(self, client: Client):
        self.clients.append(client)
        
    def showClients(self):
        for client in self.clients:
            print(f"{client.ClientID} - {client.name}")


class LogbookEntry():
    def __init__(self, notes, service_date):
        self.notes = notes
        self.service_date = service_date

 
class Service:
    def __init__(self, car: Car):
        self.car = car
        self.baseServicePrice = self.setBaseServicePrice()
        
    def setBaseServicePrice(self):
        if self.car.model.carBrand == "Audi":
            return 500
        else:
            return 300
        


car1 = Car("Grey", "Sedan", "DGA99Y", "2008")


employee1 = Employee("Alice", "NSW123456")
client1 = Client("Elizabeth", "NSW1234")

 

print(employee1.EmployeeID) 
print(client1.ClientID)  
