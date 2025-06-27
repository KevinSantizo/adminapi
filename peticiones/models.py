from django.db import models

# Create your models here.



class Department(models.Model):
    department_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.department_name}"


class User(models.Model):
    user_name = models.CharField(max_length=100, null=True, blank=True)
    user_email = models.EmailField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.user_name} - {self.user_email}"

class Gestor(models.Model):
    gestor_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.gestor_name}"

class Task(models.Model):
    gestor = models.ForeignKey('Gestor', on_delete=models.CASCADE, null=True, blank=True)
    department = models.ForeignKey('Department', on_delete=models.CASCADE, null=True, blank=True)
    task_name = models.CharField(max_length=100, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f"{self.gestor} - {self.department} - {self.task_name} - {self.created}"

class Status(models.Model):
    status_name = models.CharField(max_length=100, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f"{self.status_name} - {self.created}"

class SubTask(models.Model):
    TYPE = (
        (1, '1.	Solicitud de tarea'),
        (2, '2.	Tarea completada'),
        (3, '3.	Información incompleta'),
        (4, '4.	Solicitud de modificación'),
        (5, '5. Tarea Finalizada'),
        (6, '6.	Trabajo Enviado al Cliente'),
        (7, '7.	Modificacion Solicitada por el Cliente'),
        (8, '8.	Trabajo Aceptado por Cliente'),
    )

    status = models.ForeignKey('Status', on_delete=models.CASCADE, null=True, blank=True)
    task = models.ForeignKey('Task', on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE, null=True, blank=True)
    subtask_name = models.CharField(max_length=100, null=True, blank=True)
    subtask_type = models.IntegerField(choices=TYPE, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f"{self.subtask_name} - {self.subtask_type} - {self.created} - {self.created}"