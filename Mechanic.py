

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
            print(f"Client list: {client.ClientID} - {client.name}")


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
        
        
def run_demo(db):
    name = input("Client name: ")
    
    while True:
        license = input("License number (numbers only): ")
        if license.isdigit():
            break
        print("❌ Retry (only use numbers)")

    nationality = input("Car nationality: ")
    brand = input("Car brand: ")
    model_name = input("Car model (e.g CX-5, RAV4): ")
    
    model_id = f"{brand}_{model_name}".lower()
    
    if model_id in db.models:
        car_model = db.models[model_id]
        print("✅ Model loaded from database.")
   
    else:
        print("⚠️ Model not found. Creating new entry.")
        car_model = CarModel(nationality, brand, model_name)

    colour = input("Car colour: ")
    body_type = input("Body type: ")
    no_plate = input("Plate number: ")
    build_date = input("Build year: ")

    client = Client(name, license)
    car_model = CarModel(nationality, brand, model_name)
    car = Car(colour, body_type, no_plate, build_date, car_model)

    client.addCar(car)
    ClientDataBase().registerClient(client)
    CarRegistry().registerCar(car)

    service = Service(car)
    print("-----------------------------------------------------")
    print(f"Service cost: ${service.baseServicePrice}")
    print(f"Client Assigned and Client ID: {client.ClientID}")
    print(f"Employee ID: {Employee('Alice', '234567').EmployeeID}")
    
    
def main():
   db = CarModelDataBase()
   run_demo(db)

if __name__ == "__main__":
    main()
    
    
