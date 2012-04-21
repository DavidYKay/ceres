# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Crop'
        db.create_table('pricing_crop', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('pricing', ['Crop'])

        # Adding model 'Department'
        db.create_table('pricing_department', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('pricing', ['Department'])

        # Adding model 'PriceReport'
        db.create_table('pricing_pricereport', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('crop', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pricing.Crop'])),
            ('department', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pricing.Department'])),
            ('time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('pricing', ['PriceReport'])

    def backwards(self, orm):
        # Deleting model 'Crop'
        db.delete_table('pricing_crop')

        # Deleting model 'Department'
        db.delete_table('pricing_department')

        # Deleting model 'PriceReport'
        db.delete_table('pricing_pricereport')

    models = {
        'pricing.crop': {
            'Meta': {'object_name': 'Crop'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'pricing.department': {
            'Meta': {'object_name': 'Department'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'pricing.pricereport': {
            'Meta': {'object_name': 'PriceReport'},
            'crop': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pricing.Crop']"}),
            'department': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pricing.Department']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['pricing']