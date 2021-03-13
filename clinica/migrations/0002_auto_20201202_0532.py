# Generated by Django 3.1.3 on 2020-12-02 08:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clinica', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=60)),
                ('telefono', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('medico', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_pago', models.CharField(choices=[('T', 'Tarjeta de credito'), ('B', 'Billetera virtual'), ('E', 'Efectivo'), ('D', 'Debito')], default='E', max_length=1)),
                ('estado', models.CharField(choices=[('PT', 'Pendiente'), ('PD', 'Pedido'), ('TL', 'Taller'), ('FL', 'Finalizado')], default='PT', max_length=2)),
                ('subtotal', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('fecha', models.DateTimeField(auto_now=True)),
                ('fechaCreacion', models.DateField(auto_now=True)),
                ('paciente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='clinica_paciente', to='clinica.paciente')),
                ('vendedor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='producto',
            name='armazon',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='producto',
            name='enfoque',
            field=models.CharField(blank=True, choices=[('L', 'Lejos'), ('C', 'Cerca')], max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='producto',
            name='lado',
            field=models.CharField(blank=True, choices=[('I', 'Izqierda'), ('D', 'Derecha')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='producto',
            name='tipo',
            field=models.CharField(choices=[('L', 'Lente'), ('E', 'Estuche'), ('G', 'Gotita'), ('A', 'Accesorios')], default='L', max_length=1),
        ),
        migrations.CreateModel(
            name='Turnos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FechaTurno', models.DateField()),
                ('HoraTurno', models.TimeField()),
                ('Asistencia', models.CharField(blank=True, choices=[('P', 'Pendiente'), ('A', 'Asistió'), ('F', 'Faltó')], max_length=1, null=True)),
                ('Paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinica.paciente')),
            ],
        ),
        migrations.CreateModel(
            name='PedidoDetalle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField(default=1)),
                ('precio', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10)),
                ('pedido', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='clinica.pedido')),
                ('producto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='clinica.producto')),
            ],
        ),
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('observaciones', models.TextField()),
                ('motivo', models.CharField(max_length=150)),
                ('diagnostico', models.CharField(max_length=150)),
                ('tratamiento', models.CharField(max_length=150)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinica.paciente')),
            ],
        ),
    ]
