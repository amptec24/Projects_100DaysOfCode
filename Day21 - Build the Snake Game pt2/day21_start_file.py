# Example of Class Inheritance

class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("doing this underwater.")

    def swim(self):
        print("moving in water.")


nemo = Fish()
nemo.breathe()


# Slicing code
piano_keys = ["a", "b", "c", "d", "e", "f", "g"]
piano_tuple = ("do", "re", "mi", "fa", "so", "la", "ti")
print(f"The main list {piano_keys}")
print(piano_keys[2:5])
print(piano_keys[2:])
print(piano_keys[:5])
# Set the increment by adding third number with :
print(piano_keys[2:5:2])
print(piano_keys[::2])
# Reversing the order of the list by using -1 :
print(piano_keys[::-1])
piano_keys = ["a", "b", "c", "d", "e", "f", "g"]
print(f"\nTuple list {piano_tuple}")
print(piano_tuple[2:5])
