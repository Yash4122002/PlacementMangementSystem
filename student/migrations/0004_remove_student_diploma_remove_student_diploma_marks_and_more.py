# Generated by Django 4.0.2 on 2022-03-22 10:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_delete_event_delete_pm'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='diploma',
        ),
        migrations.RemoveField(
            model_name='student',
            name='diploma_marks',
        ),
        migrations.RemoveField(
            model_name='student',
            name='diploma_passout',
        ),
        migrations.RemoveField(
            model_name='student',
            name='diploma_stream',
        ),
        migrations.RemoveField(
            model_name='student',
            name='hsc',
        ),
        migrations.RemoveField(
            model_name='student',
            name='hsc_marks',
        ),
        migrations.RemoveField(
            model_name='student',
            name='roll',
        ),
        migrations.RemoveField(
            model_name='student',
            name='school',
        ),
        migrations.RemoveField(
            model_name='student',
            name='school_marks',
        ),
        migrations.RemoveField(
            model_name='student',
            name='school_passout',
        ),
        migrations.RemoveField(
            model_name='student',
            name='ug',
        ),
        migrations.RemoveField(
            model_name='student',
            name='ug_backlogs',
        ),
        migrations.RemoveField(
            model_name='student',
            name='ug_marks',
        ),
        migrations.RemoveField(
            model_name='student',
            name='ug_passout',
        ),
        migrations.RemoveField(
            model_name='student',
            name='ug_stream',
        ),
        migrations.CreateModel(
            name='StudentEducation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ug_stream', models.CharField(max_length=100)),
                ('ug_admmision', models.IntegerField()),
                ('ug_passout', models.IntegerField()),
                ('ug_fy_sem1', models.IntegerField(null=True)),
                ('ug_sy_sem1', models.IntegerField(null=True)),
                ('ug_ty_sem1', models.IntegerField(null=True)),
                ('ug_be_sem1', models.IntegerField(null=True)),
                ('ug_fy_sem2', models.IntegerField(null=True)),
                ('ug_sy_sem2', models.IntegerField(null=True)),
                ('ug_ty_sem2', models.IntegerField(null=True)),
                ('ug_be_sem2', models.IntegerField(null=True)),
                ('ug_fy_atkt', models.IntegerField(null=True)),
                ('ug_sy_atkt', models.IntegerField(null=True)),
                ('ug_ty_atkt', models.IntegerField(null=True)),
                ('ug_be_atkt', models.IntegerField(null=True)),
                ('ug_fy_gap', models.IntegerField(null=True)),
                ('ug_sy_gap', models.IntegerField(null=True)),
                ('ug_ty_gap', models.IntegerField(null=True)),
                ('ug_be_gap', models.IntegerField(null=True)),
                ('diploma_college_name', models.CharField(max_length=100)),
                ('diploma_stream', models.CharField(max_length=50)),
                ('diploma_passout', models.IntegerField()),
                ('diploma_fy', models.IntegerField(null=True)),
                ('diploma_sy', models.IntegerField(null=True)),
                ('diploma_ty', models.IntegerField(null=True)),
                ('diploma_total', models.IntegerField()),
                ('hsc_college_name', models.CharField(max_length=100)),
                ('hsc_marks', models.IntegerField()),
                ('hsc_passout', models.IntegerField()),
                ('school_name', models.CharField(max_length=100)),
                ('school_marks', models.IntegerField()),
                ('school_passout', models.IntegerField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student')),
            ],
        ),
    ]