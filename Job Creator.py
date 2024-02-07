class job:
  name = None
  salary = None
  hours = None

  def __init__(self, name, salary, hours):
    self.name = name
    self.salary = salary
    self.hours = hours

  def print(self):
    print(f"Job type: {self.name}")
    print(f"Salary: $ {self.salary}")
    print(f"Hours worked: {self.hours}")

class doctor(job):
  speciality = None
  yearsXP = None

  def __init__(self, salary, hours, speciality, yearsXP):
    self.name = "Doctor"
    self.salary = salary
    self.hours = hours
    self.speciality = speciality
    self.yearsXP = yearsXP

  def print(self):
    print(f"Job type: {self.name}")
    print(f"Salary: $ {self.salary}")
    print(f"Hours worked: {self.hours}")
    print(f"Speciality: {self.speciality}")
    print(f"Years of experience: {self.yearsXP}")

class teacher(job):
  subject = None
  position = None

  def __init__(self, salary, hours, subject, position):
    self.name = "Teacher"
    self.salary = salary
    self.hours = hours
    self.subject = subject
    self.position = position

  def print(self):
    print(f"Job type: {self.name}")
    print(f"Salary: $ {self.salary}")
    print(f"Hours worked: {self.hours}")
    print(f"Subject: {self.subject}")
    print(f"Position: {self.position}")

print("🌟Jobs Jobs Jobs!🌟\n")
lawyer = job("Lawyer", "Squillions", 60)
lawyer.print()
print()
teacher = teacher("Nowhere near enough", "All of them", "Computer Science", "Classroom Teacher")
teacher.print()
print()
doctor = doctor("Doing very nicely thank you", 50, "Pediatric Consultant", 7)
doctor.print()