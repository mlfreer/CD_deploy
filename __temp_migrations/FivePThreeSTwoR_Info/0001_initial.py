# Generated by Django 2.2.12 on 2022-01-31 23:35

from django.db import migrations, models
import django.db.models.deletion
import otree.db.idmap
import otree.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('otree', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_subsession', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('state_of_world', otree.db.models.IntegerField(null=True)),
                ('public_evidence', otree.db.models.IntegerField(null=True)),
                ('str_public_evidence', otree.db.models.StringField(max_length=10000, null=True)),
                ('correct_guess', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False, null=True)),
                ('group_guess', otree.db.models.IntegerField(null=True)),
                ('str_group_guess', otree.db.models.StringField(max_length=10000, null=True)),
                ('opinions_result1', otree.db.models.StringField(max_length=10000, null=True)),
                ('opinions_result2', otree.db.models.StringField(max_length=10000, null=True)),
                ('opinions_result3', otree.db.models.StringField(max_length=10000, null=True)),
                ('opinions_result4', otree.db.models.StringField(max_length=10000, null=True)),
                ('opinions_result5', otree.db.models.StringField(max_length=10000, null=True)),
                ('disclosure_decision1', otree.db.models.StringField(max_length=10000, null=True)),
                ('disclosure_decision2', otree.db.models.StringField(max_length=10000, null=True)),
                ('disclosure_decision3', otree.db.models.StringField(max_length=10000, null=True)),
                ('disclosure_decision4', otree.db.models.StringField(max_length=10000, null=True)),
                ('disclosure_decision5', otree.db.models.StringField(max_length=10000, null=True)),
                ('disclosure_information1', otree.db.models.StringField(default='None', max_length=10000, null=True)),
                ('disclosure_information2', otree.db.models.StringField(default='None', max_length=10000, null=True)),
                ('disclosure_information3', otree.db.models.StringField(default='None', max_length=10000, null=True)),
                ('disclosure_information4', otree.db.models.StringField(default='None', max_length=10000, null=True)),
                ('disclosure_information5', otree.db.models.StringField(default='None', max_length=10000, null=True)),
                ('gray_votes', otree.db.models.IntegerField(null=True)),
                ('group_votes', otree.db.models.IntegerField(default=0, null=True)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fivepthreestwor_info_group', to='otree.Session')),
            ],
            options={
                'db_table': 'FivePThreeSTwoR_Info_group',
            },
            bases=(models.Model, otree.db.idmap.GroupIDMapMixin),
        ),
        migrations.CreateModel(
            name='Subsession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fivepthreestwor_info_subsession', to='otree.Session')),
            ],
            options={
                'db_table': 'FivePThreeSTwoR_Info_subsession',
            },
            bases=(models.Model, otree.db.idmap.SubsessionIDMapMixin),
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_group', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_payoff', otree.db.models.CurrencyField(default=0, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_role', otree.db.models.StringField(max_length=10000, null=True)),
                ('opinion', otree.db.models.IntegerField(choices=[[1, 'Orange'], [-1, 'Gray'], [0, 'Indifferent']], null=True, verbose_name='Which project do you prefer?')),
                ('disclose', otree.db.models.IntegerField(blank=True, choices=[[1, 'Yes'], [0, 'No']], default=0, null=True, verbose_name='Would you like to disclose your private evidence?')),
                ('vote', otree.db.models.IntegerField(choices=[[1, 'Orange'], [-1, 'Gray']], null=True, verbose_name='Which project would you like to get implemented?')),
                ('iteration', otree.db.models.IntegerField(default=0, null=True)),
                ('opinion_iteration1', otree.db.models.IntegerField(default=-2, null=True)),
                ('opinion_iteration2', otree.db.models.IntegerField(default=-2, null=True)),
                ('private_evidence', otree.db.models.IntegerField(null=True)),
                ('str_private_evidence', otree.db.models.StringField(default='None', max_length=10000, null=True)),
                ('publicized_evidence', otree.db.models.IntegerField(default=0, null=True)),
                ('earnings', otree.db.models.CurrencyField(default=0, null=True)),
                ('final_earnings', otree.db.models.CurrencyField(default=0, null=True)),
                ('final_profit', otree.db.models.CurrencyField(default=0, null=True)),
                ('paying_round', otree.db.models.IntegerField(default=0, null=True)),
                ('MyNumber', otree.db.models.IntegerField(default=0, null=True)),
                ('type', otree.db.models.IntegerField(default=0, null=True)),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='FivePThreeSTwoR_Info.Group')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fivepthreestwor_info_player', to='otree.Participant')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fivepthreestwor_info_player', to='otree.Session')),
                ('subsession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FivePThreeSTwoR_Info.Subsession')),
            ],
            options={
                'db_table': 'FivePThreeSTwoR_Info_player',
            },
            bases=(models.Model, otree.db.idmap.PlayerIDMapMixin),
        ),
        migrations.AddField(
            model_name='group',
            name='subsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FivePThreeSTwoR_Info.Subsession'),
        ),
    ]
