# Generated by Django 2.2.12 on 2021-08-23 20:25

from django.db import migrations, models
import django.db.models.deletion
import otree.common
import otree.db.idmap
import otree.db.models
import otree.db.vars
import time


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BrowserBotsLauncherSessionCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('pre_create_id', models.CharField(max_length=10)),
                ('is_only_record', models.BooleanField(default=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='PageTimeBatch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ParticipantRoomVisit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_name', models.CharField(max_length=50)),
                ('participant_label', models.CharField(max_length=200)),
                ('tab_unique_id', models.CharField(max_length=20, unique=True)),
                ('last_updated', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vars', otree.db.vars._PickleField(default=dict)),
                ('config', otree.db.vars._PickleField(default=dict, null=True)),
                ('label', otree.db.models.StringField(blank=True, help_text='For internal record-keeping', max_length=300, null=True)),
                ('code', otree.db.models.StringField(default=otree.common.random_chars_8, max_length=16, null=True, unique=True)),
                ('mturk_HITId', otree.db.models.StringField(blank=True, help_text='Hit id for this session on MTurk', max_length=300, null=True)),
                ('mturk_HITGroupId', otree.db.models.StringField(blank=True, help_text='Hit id for this session on MTurk', max_length=300, null=True)),
                ('is_mturk', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False, null=True)),
                ('mturk_use_sandbox', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=True, help_text='Should this session be created in mturk sandbox?', null=True)),
                ('mturk_expiration', otree.db.models.FloatField(null=True)),
                ('mturk_qual_id', otree.db.models.StringField(default='', max_length=50, null=True)),
                ('archived', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], db_index=True, default=False, null=True)),
                ('comment', otree.db.models.LongStringField(blank=True, null=True)),
                ('_anonymous_code', otree.db.models.StringField(db_index=True, default=otree.common.random_chars_10, max_length=10, null=True)),
                ('is_demo', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False, null=True)),
                ('_admin_report_app_names', otree.db.models.LongStringField(default='', null=True)),
                ('_admin_report_num_rounds', otree.db.models.StringField(default='', max_length=255, null=True)),
                ('num_participants', otree.db.models.PositiveIntegerField(null=True)),
            ],
            options={
                'ordering': ['pk'],
            },
            bases=(models.Model, otree.db.vars.VarsMixin, otree.db.idmap.SessionIDMapMixin),
        ),
        migrations.CreateModel(
            name='TaskQueueMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('method', models.CharField(max_length=50)),
                ('kwargs_json', models.TextField()),
                ('epoch_time', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UndefinedFormModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='RoomToSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_name', models.CharField(max_length=255, unique=True)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='otree.Session')),
            ],
        ),
        migrations.CreateModel(
            name='ParticipantVarsFromREST',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('participant_label', models.CharField(max_length=255)),
                ('room_name', models.CharField(max_length=255)),
                ('_json_data', models.TextField(default='')),
            ],
            options={
                'unique_together': {('participant_label', 'room_name')},
                'index_together': {('participant_label', 'room_name')},
            },
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vars', otree.db.vars._PickleField(default=dict)),
                ('label', otree.db.models.StringField(max_length=50, null=True)),
                ('id_in_session', otree.db.models.PositiveIntegerField(null=True)),
                ('payoff', otree.db.models.CurrencyField(default=0, null=True)),
                ('time_started', models.DateTimeField(null=True)),
                ('mturk_assignment_id', otree.db.models.StringField(max_length=50, null=True)),
                ('mturk_worker_id', otree.db.models.StringField(max_length=50, null=True)),
                ('_index_in_pages', otree.db.models.PositiveIntegerField(db_index=True, default=0, null=True)),
                ('_monitor_note', otree.db.models.StringField(max_length=300, null=True)),
                ('code', otree.db.models.StringField(default=otree.common.random_chars_8, max_length=16, null=True, unique=True)),
                ('_session_code', models.CharField(max_length=16)),
                ('visited', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], db_index=True, default=False, null=True)),
                ('_last_page_timestamp', otree.db.models.PositiveIntegerField(null=True)),
                ('_last_request_timestamp', otree.db.models.PositiveIntegerField(null=True)),
                ('is_on_wait_page', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False, null=True)),
                ('_current_page_name', otree.db.models.StringField(max_length=200, null=True, verbose_name='page')),
                ('_current_app_name', otree.db.models.StringField(max_length=200, null=True, verbose_name='app')),
                ('_round_number', otree.db.models.PositiveIntegerField(null=True)),
                ('_current_form_page_url', models.URLField()),
                ('_max_page_index', otree.db.models.PositiveIntegerField(null=True)),
                ('_is_bot', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False, null=True)),
                ('is_browser_bot', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False, null=True)),
                ('_timeout_expiration_time', otree.db.models.FloatField(null=True)),
                ('_timeout_page_index', otree.db.models.PositiveIntegerField(null=True)),
                ('_gbat_is_waiting', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False, null=True)),
                ('_gbat_page_index', otree.db.models.PositiveIntegerField(null=True)),
                ('_gbat_grouped', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], null=True)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='otree.Session')),
            ],
            options={
                'ordering': ['pk'],
                'index_together': {('session', 'mturk_worker_id', 'mturk_assignment_id')},
            },
            bases=(models.Model, otree.db.vars.VarsMixin, otree.db.idmap.ParticipantIDMapMixin),
        ),
        migrations.CreateModel(
            name='CompletedSubsessionWaitPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_index', models.PositiveIntegerField()),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='otree.Session')),
            ],
            options={
                'index_together': {('page_index', 'session')},
            },
        ),
        migrations.CreateModel(
            name='CompletedGroupWaitPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_index', models.PositiveIntegerField()),
                ('group_id', models.PositiveIntegerField()),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='otree.Session')),
            ],
            options={
                'index_together': {('page_index', 'session', 'group_id')},
            },
        ),
        migrations.CreateModel(
            name='CompletedGBATWaitPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_index', models.PositiveIntegerField()),
                ('id_in_subsession', models.PositiveIntegerField(default=0)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='otree.Session')),
            ],
            options={
                'index_together': {('page_index', 'session', 'id_in_subsession')},
            },
        ),
        migrations.CreateModel(
            name='ChatMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel', models.CharField(max_length=255)),
                ('nickname', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('timestamp', models.FloatField(default=time.time)),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chat_messages_core', to='otree.Participant')),
            ],
            options={
                'index_together': {('channel', 'timestamp')},
            },
        ),
    ]
