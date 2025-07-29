

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
    def __init__(self, filename="car_models.txt"):
        self.models = {}
        try:
            with open(filename, "r") as file:
                for line in file:
                    parts = line.strip().split("|")
                    if len(parts) == 3:
                        nationality, brand, model = parts
                        car_model = CarModel(nationality, brand, model)
                        self.models[car_model.getID()] = car_model 
        except FileNotFoundError:
            print(f"Error: Could not find file {filename}")


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


def main():
    model_db = CarModelDataBase("car_models.txt")
    client_db = ClientDataBase()
    car_registry = CarRegistry()

    name = input("Enter client name: ")
    license = input("Enter driver’s license number: ")
    client = Client(name, license)

    print("Available car models:")
    for key in model_db.models:
        model = model_db.models[key]
        print(f" - {model.carBrand} {model.carModel} ({key})")

    model_id = input("Enter car model ID (e.g. audi_tt): ")
    car_model = model_db.models.get(model_id.lower())

    if not car_model:
        print("Invalid car model ID. Try respelling")
        return

    colour = input("Enter car colour: ")
    body_type = input("Enter car body type: ")
    no_plate = input("Enter car number plate: ")
    build_date = input("Enter build year: ")

    car = Car(colour, body_type, no_plate, build_date, car_model)

    client.addCar(car)
    client_db.registerClient(client)
    car_registry.registerCar(car)

    service = Service(car)
    print(f"Service cost for {car.noPlate}: ${service.baseServicePrice}")

    client_db.showClients()
    car_registry.showRegister()

    employee = Employee("Alice", "NSW123456")  
    print(f"Employee ID: {employee.EmployeeID}")
    print(f"Client ID: {client.ClientID}")
if __name__ == "__main__":
    main()
