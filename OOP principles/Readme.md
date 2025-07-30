Describe and explain how you used a range of OOP principles in your project. For each principle, include a very small code snippet that highlights the principle.


- Classes
<img width="493" height="128" alt="image" src="https://github.com/user-attachments/assets/85718aa6-65a0-4ef2-b8c6-83ce6d1827b3" />

I used many classes throughout my code, I have one main generalised class (Person) at the top which allows for consistency and shared behaviour throughout the whole code.



- Constructors
<img width="505" height="53" alt="image" src="https://github.com/user-attachments/assets/bcacd6bf-1eeb-4c82-80d9-51d0f23a1615" />

Using __init__ I have initialised object attributes in a class when they are instantiated.
  
- Methods
<img width="490" height="131" alt="image" src="https://github.com/user-attachments/assets/aab4019d-3dae-4193-80f6-cfd2e00d1cc0" />

In the CarRegistry class 2 methods run when the class is Instantiated. def registerCar passes the car object into a list. showRegister allows for car register to be displayed. This is only a small example of the logic and methods in my code. But simple classes that are easy to update later are on are consistent throught the program.

- Objects
<img width="814" height="76" alt="image" src="https://github.com/user-attachments/assets/362fa4d9-d0a6-4eb1-afa6-4c1aa9e1422c" />

In run_demo, mulitple objects are made to hold data and behave accordng to methods. For example a client has its own car, in a method called addCar the object is linked to client storing data cleanly and efficiently.

- Inheritance
<img width="318" height="25" alt="image" src="https://github.com/user-attachments/assets/311d8dd8-83e1-48e5-8dc2-ce38fae0fc94" />

Class Employee, inherites attirutbes from the generalised person class.

<img width="537" height="20" alt="image" src="https://github.com/user-attachments/assets/b028043c-f244-40b5-b4e4-e3fe773416cb" />

These are reused via a super() to avoid repitition.



- Polymorphism
<img width="759" height="90" alt="image" src="https://github.com/user-attachments/assets/c3fd7df8-05fa-478a-a77d-5a0807687f5b" />

The getID() method, behaves differently depending on what class its used in, it is generalised in the Person class to maintain structure. It is then overwritten by child classes like Employee and Client. In this example inside of the Employee class, getID returns a unique identifier to each employee beginging with E-then the first 2 characters of their name followed by their drivers license. This is different logic to the client class but still the same method.



- Generalisation
<img width="613" height="164" alt="image" src="https://github.com/user-attachments/assets/d5c2e029-5ae9-4c67-ab5f-1a87dc4219cd" />

The Person class is one big generalised superclass. It stores common reusable attributes of people like name and drivers license. This encourages logical behaviour and shared properties.

