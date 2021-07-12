from profiles.models import Student
user=Student.objects.get(id=1)
print(user.__dict__)