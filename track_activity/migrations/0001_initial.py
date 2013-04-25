# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Activity'
        db.create_table('track_activity_activity', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('has_end_time', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('track_activity', ['Activity'])


    def backwards(self, orm):
        # Deleting model 'Activity'
        db.delete_table('track_activity_activity')


    models = {
        'track_activity.activity': {
            'Meta': {'object_name': 'Activity'},
            'has_end_time': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['track_activity']