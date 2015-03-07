# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'NewsImage'
        db.create_table('main_newsimage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('news', self.gf('django.db.models.fields.related.ForeignKey')(related_name='images', to=orm['main.News'])),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal('main', ['NewsImage'])

        # Deleting field 'News.image'
        db.delete_column('main_news', 'image')

        # Adding field 'News.main_image'
        db.add_column('main_news', 'main_image',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'NewsImage'
        db.delete_table('main_newsimage')


        # User chose to not deal with backwards NULL issues for 'News.image'
        raise RuntimeError("Cannot reverse this migration. 'News.image' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'News.image'
        db.add_column('main_news', 'image',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True),
                      keep_default=False)

        # Deleting field 'News.main_image'
        db.delete_column('main_news', 'main_image')


    models = {
        'main.constant': {
            'Meta': {'unique_together': "(('name', 'site'),)", 'object_name': 'Constant'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': "orm['sites.Site']"}),
            'value': ('django.db.models.fields.TextField', [], {})
        },
        'main.news': {
            'Meta': {'ordering': "['created_date']", 'object_name': 'News'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'headline': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'main_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['main.News']"}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'updated_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'})
        },
        'main.newsimage': {
            'Meta': {'object_name': 'NewsImage'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'news': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'images'", 'to': "orm['main.News']"})
        },
        'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['main']