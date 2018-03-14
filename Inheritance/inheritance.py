class Parent():
    def __init__(self, name,eyecolor):
        #print("Parent Called")
        self.name = name
        self.eyecolor = eyecolor

    def showinfo(self):
        print("Name - "+self.name)
        print("Kolor oczu - "+self.eyecolor)

class Child(Parent):
    def __init__(self, name,eyecolor,numberoftoys):
        #print ("Child Called")
        Parent.__init__(self, name,eyecolor)
        self.numberoftoys = numberoftoys

    def showinfo(self):
        Parent.showinfo(self)
        print("Ilosc zabawek - "+str(self.numberoftoys))

Tata = Parent("Marian","brown")
Dziecko = Child("Marcin","brown",10)
