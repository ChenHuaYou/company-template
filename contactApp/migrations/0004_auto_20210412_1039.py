# Generated by Django 3.1.7 on 2021-04-12 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactApp', '0003_auto_20210409_1632'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='resume',
            options={'ordering': ('-status', '-publish_data'), 'verbose_name': '简历信息', 'verbose_name_plural': '简历信息'},
        ),
        migrations.AlterField(
            model_name='resume',
            name='birth',
            field=models.DateField(default='2021-04-12', verbose_name='出生日期'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='name',
            field=models.CharField(max_length=50, verbose_name='姓名'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='status',
            field=models.IntegerField(choices=[(1, '未审'), (2, '通过'), (3, '未通过')], default=1, verbose_name='面试成绩'),
        ),
    ]
