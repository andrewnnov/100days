def greet():
    print("Hello")
    print("How do you do?")
    print("Isn't the weather nice today?")

greet()
#Function that allows for input

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")

greet_with_name("Andrew")

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")
    
greet_with("Jack", "London")    

def greet_with_dir(name="Mark", location="Kirov"):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")
