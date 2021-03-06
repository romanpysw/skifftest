# Generated by Django 3.2.9 on 2021-11-06 03:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('skiff', '0009_alter_s_module_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='s_course',
            name='s_module',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='skiff.s_module'),
        ),
        migrations.AlterField(
            model_name='s_course',
            name='group',
            field=models.ManyToManyField(null=True, to='skiff.s_group'),
        ),
        migrations.AlterField(
            model_name='s_course',
            name='s_test',
            field=models.ManyToManyField(null=True, to='skiff.s_test'),
        ),
        migrations.AlterField(
            model_name='s_course',
            name='user',
            field=models.ManyToManyField(null=True, related_name='student', to='skiff.s_user'),
        ),
        migrations.AlterField(
            model_name='s_module',
            name='s_test',
            field=models.ManyToManyField(null=True, to='skiff.s_test'),
        ),
    ]
