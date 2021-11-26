from django.db import models

class s_user(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 50, unique = True)
    description = models.TextField()
    email = models.EmailField(unique = True)
    password = models.CharField(max_length = 30)
    
    def __str__(self):
        return self.name


class s_test(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 50, default = "Test")
    question = models.JSONField()
    answer = models.JSONField()
    author = models.ManyToManyField(s_user)
    
    def __str__(self):
        return self.name

class s_group(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 50, unique = True)
    description = models.TextField()
    user = models.ManyToManyField(s_user)

    def __str__(self):
        return self.name

class s_module(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 150)
    description = models.TextField()
    s_test = models.ManyToManyField(s_test, null = True)

    def __str__(self):
        return self.name

class s_course(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 150, unique = True)
    description = models.TextField()
    is_open = models.BooleanField(default = False)
    teacher = models.ManyToManyField(s_user, related_name = 'teacher')
    group = models.ManyToManyField(s_group, null = True)
    user = models.ManyToManyField(s_user, related_name = 'student', null = True)
    s_test = models.ManyToManyField(s_test, null = True)
    s_module = models.ForeignKey(s_module, on_delete = models.DO_NOTHING, null = True)

    def __str__(self):
        return self.name