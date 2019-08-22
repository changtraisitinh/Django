# Generated by Django 2.2.4 on 2019-08-17 06:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('dept_no', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('dept_name', models.CharField(max_length=40, unique=True)),
            ],
            options={
                'db_table': 'departments',
            },
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('emp_no', models.IntegerField(primary_key=True, serialize=False)),
                ('birth_date', models.DateField()),
                ('first_name', models.CharField(max_length=14)),
                ('last_name', models.CharField(max_length=16)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('hire_date', models.DateField()),
            ],
            options={
                'db_table': 'employees',
            },
        ),
        migrations.CreateModel(
            name='Titles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('from_date', models.DateField()),
                ('to_date', models.DateField(blank=True, null=True)),
                ('emp_no', models.ForeignKey(db_column='emp_no', on_delete=django.db.models.deletion.CASCADE, related_name='employeeTitles', to='myems.Employees')),
            ],
            options={
                'db_table': 'titles',
            },
        ),
        migrations.CreateModel(
            name='Salaries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salary', models.IntegerField()),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('emp_no', models.ForeignKey(db_column='emp_no', on_delete=django.db.models.deletion.CASCADE, related_name='employeeSalaries', to='myems.Employees')),
            ],
            options={
                'db_table': 'salaries',
                'unique_together': {('emp_no', 'from_date')},
            },
        ),
        migrations.CreateModel(
            name='DeptManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('dept_no', models.ForeignKey(db_column='dept_no', on_delete=django.db.models.deletion.CASCADE, to='myems.Departments')),
                ('emp_no', models.ForeignKey(db_column='emp_no', on_delete=django.db.models.deletion.CASCADE, to='myems.Employees')),
            ],
            options={
                'db_table': 'dept_manager',
                'unique_together': {('emp_no', 'dept_no')},
            },
        ),
        migrations.CreateModel(
            name='DeptEmp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('dept_no', models.ForeignKey(db_column='dept_no', on_delete=django.db.models.deletion.CASCADE, to='myems.Departments')),
                ('emp_no', models.ForeignKey(db_column='emp_no', on_delete=django.db.models.deletion.CASCADE, to='myems.Employees')),
            ],
            options={
                'db_table': 'dept_emp',
                'unique_together': {('emp_no', 'dept_no')},
            },
        ),
    ]