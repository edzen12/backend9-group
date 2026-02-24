class A:
    def a(self):
        print("A Gena")

class B:
    def a(self):
        print("B Vitya")

class C:
    def a(self):
        print("C Cargo")

class D(B, A, C): #
    def a(self):
        super().a()

D().a() 

# №№№№№№№№№
class Doctor:
    def can_cure(self):
        print("Я доктор, я умею лечить")

    def can_build(self):
        print("Я хоть и доктор, но тоже умею строить")

    def lesson(self):
        print("Ура я отучился на доктора")


class Builder:
    def can_build(self):
        print("Я строитель, я мастер стройки")

    def lesson(self):
        print("Ура я отучился на строителя")


class Person(Builder, Doctor):
    def lesson(self):
        print("Посмотрим кем я стал")
        super().lesson()
        Doctor.lesson(self) # вызываю метод lesson из Doctor'a

per = Person()
per.lesson()