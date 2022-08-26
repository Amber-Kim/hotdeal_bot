from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deal',
            fields=[
                ('image_url', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('link', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('reply_count', models.IntegerField()),
                ('up_count', models.IntegerField()),
            ],
        ),
    ]