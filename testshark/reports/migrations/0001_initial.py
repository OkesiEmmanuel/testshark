# Generated by Django 4.2.9 on 2024-07-02 21:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('scripts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('PASSED', 'Passed'), ('FAILED', 'Failed'), ('SKIPPED', 'Skipped')], default='SKIPPED', max_length=10)),
                ('error_message', models.TextField(blank=True)),
                ('screenshot', models.ImageField(blank=True, null=True, upload_to='screenshots')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('test_script', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scripts.testscript')),
            ],
        ),
    ]
