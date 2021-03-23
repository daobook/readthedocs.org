# Generated by Django 2.2.17 on 2020-12-21 18:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('socialaccount', '0003_extra_data_default_dict'),
        ('projects', '0067_change_max_length_feature_id'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('oauth', '0012_create_new_table_for_remote_organization_normalization'),
    ]

    operations = [
        migrations.CreateModel(
            name='RemoteRepository',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('full_name', models.CharField(db_index=True, max_length=255, verbose_name='Full Name')),
                ('description', models.TextField(blank=True, help_text='Description of the project', null=True, verbose_name='Description')),
                ('avatar_url', models.URLField(blank=True, null=True, verbose_name='Owner avatar image URL')),
                ('ssh_url', models.URLField(blank=True, max_length=512, validators=[django.core.validators.URLValidator(schemes=['ssh'])], verbose_name='SSH URL')),
                ('clone_url', models.URLField(blank=True, max_length=512, validators=[django.core.validators.URLValidator(schemes=['http', 'https', 'ssh', 'git', 'svn'])], verbose_name='Repository clone URL')),
                ('html_url', models.URLField(blank=True, null=True, verbose_name='HTML URL')),
                ('private', models.BooleanField(default=False, verbose_name='Private repository')),
                ('vcs', models.CharField(blank=True, choices=[('git', 'Git'), ('svn', 'Subversion'), ('hg', 'Mercurial'), ('bzr', 'Bazaar')], max_length=200, verbose_name='vcs')),
                ('default_branch', models.CharField(blank=True, max_length=150, null=True, verbose_name='Default branch of the repository')),
                ('remote_id', models.CharField(db_index=True, max_length=128)),
                ('vcs_provider', models.CharField(choices=[('github', 'GitHub'), ('gitlab', 'GitLab'), ('bitbucket', 'Bitbucket')], max_length=32, verbose_name='VCS provider')),
                ('organization', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='repositories', to='oauth.RemoteOrganization', verbose_name='Organization')),
                ('project', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='remote_repository', to='projects.Project')),
            ],
            options={
                'verbose_name_plural': 'remote repositories',
                'db_table': 'oauth_remoterepository_2020',
                'ordering': ['full_name'],
            },
        ),
        migrations.CreateModel(
            name='RemoteRepositoryRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('admin', models.BooleanField(default=False, verbose_name='Has admin privilege')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='remote_repository_relations', to='socialaccount.SocialAccount', verbose_name='Connected account')),
                ('remote_repository', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='remote_repository_relations', to='oauth.RemoteRepository')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='remote_repository_relations', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('remote_repository', 'account')},
            },
        ),
        migrations.AddField(
            model_name='remoterepository',
            name='users',
            field=models.ManyToManyField(related_name='oauth_repositories', through='oauth.RemoteRepositoryRelation', to=settings.AUTH_USER_MODEL, verbose_name='Users'),
        ),
        migrations.AlterUniqueTogether(
            name='remoterepository',
            unique_together={('remote_id', 'vcs_provider')},
        ),
    ]