# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'News.parent'
        db.add_column('main_news', 'parent',
                      self.gf('mptt.fields.TreeForeignKey')(blank=True, related_name='children', null=True, to=orm['main.News']),
                      keep_default=False)

        # Adding field 'News.lft'
        db.add_column('main_news', 'lft',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=1, db_index=True),
                      keep_default=False)

        # Adding field 'News.rght'
        db.add_column('main_news', 'rght',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=1, db_index=True),
                      keep_default=False)

        # Adding field 'News.tree_id'
        db.add_column('main_news', 'tree_id',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=1, db_index=True),
                      keep_default=False)

        # Adding field 'News.level'
        db.add_column('main_news', 'level',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=1, db_index=True),
                      keep_default=False)


        # Changing field 'News.image'
        db.alter_column('main_news', 'image', self.gf('django.db.models.fields.files.ImageField')(max_length=100))

        # Changing field 'News.slug'
        db.alter_column('main_news', 'slug', self.gf('django.db.models.fields.SlugField')(max_length=50))

    def backwards(self, orm):
        # Deleting field 'News.parent'
        db.delete_column('main_news', 'parent_id')

        # Deleting field 'News.lft'
        db.delete_column('main_news', 'lft')

        # Deleting field 'News.rght'
        db.delete_column('main_news', 'rght')

        # Deleting field 'News.tree_id'
        db.delete_column('main_news', 'tree_id')

        # Deleting field 'News.level'
        db.delete_column('main_news', 'level')


        # Changing field 'News.image'
        db.alter_column('main_news', 'image', self.gf('django.db.models.fields.URLField')(max_length=200))

        # Changing field 'News.slug'
        db.alter_column('main_news', 'slug', self.gf('django_extensions.db.fields.AutoSlugField')(populate_from='name', allow_duplicates=False, max_length=50, separator=u'-', overwrite=False))

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
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['main.News']"}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'updated_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'})
        },
        'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['main']