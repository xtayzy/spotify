# Generated by Django 4.2.13 on 2024-07-03 15:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('address', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('exp', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('salary', models.IntegerField()),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('type_of_job', models.CharField(choices=[('FULL_TIME', 'Полная занятость'), ('PART_TIME', 'Частичная зфнятость'), ('REMOTE', 'Удаленная работа')], max_length=100)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vacancies', to='user.company')),
                ('skills', models.ManyToManyField(related_name='vacancy_skills', to='user.skills')),
            ],
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dream_job', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=16)),
                ('exp', models.CharField(max_length=100)),
                ('education', models.CharField(choices=[('SCHOOL', 'Школьное'), ('BAKALAVR', 'Бакалавр'), ('PROFESSOR', 'Профессор'), ('MAGISTR_DJEDAY', 'Магистр джедаев')], max_length=100)),
                ('gender', models.CharField(choices=[('MALE', 'муж.'), ('FEMALE', 'жен.'), ('ЕГОРФАН', 'шухназар'), ('DOB', 'доб'), ('SCHOOL', 'школьник'), ('LAMINAT', 'ламинат'), ('MAYONEZ', 'майонез'), ('KETCHUB', 'кетчук'), ('KETCHUNEZ', 'кетчнез'), ('OTHER', 'другие'), ('GAU', 'gau написано значит гей')], max_length=100)),
                ('skills', models.ManyToManyField(related_name='resume_skills', to='user.skills')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('NEW', 'новый'), ('ACCEPT', 'принят'), ('RE_CALL', 'перезвонят')], max_length=100)),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='request', to='user.resume')),
                ('vacancy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='request', to='user.vacancy')),
            ],
        ),
    ]
