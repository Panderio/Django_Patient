# Generated by Django 3.2.5 on 2021-07-28 21:19

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('add', models.CharField(max_length=150)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_expertise', models.DateField(blank=True, null=True)),
                ('Bureau_CNAM', models.TextField(blank=True, null=True)),
                ('médecin_conseil', models.CharField(blank=True, max_length=100, null=True)),
                ('date_demande', models.DateField(blank=True, null=True)),
                ('civil', models.CharField(choices=[('Madame', 'Madame'), ('Monsieur', 'Monsieur'), ('Divorcée', 'Divorcée'), ('Mademoiselle', 'Mademoiselle')], max_length=12)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('matricule', models.CharField(max_length=100)),
                ('secteur_professionnel', models.TextField(blank=True, null=True)),
                ('grade', models.CharField(blank=True, max_length=100, null=True)),
                ('adresse_délégation', models.TextField(blank=True, null=True)),
                ('gouvernorat', models.CharField(blank=True, max_length=250, null=True)),
                ('date_naissance', models.DateField(blank=True, null=True)),
                ('lieu_naissance', models.CharField(blank=True, max_length=250, null=True)),
                ('cin', models.SmallIntegerField()),
                ('carte_handicapé', models.IntegerField(blank=True, null=True)),
                ('handicap', models.CharField(blank=True, max_length=250, null=True)),
                ('date_arret_de_travail', models.DateField(blank=True, null=True)),
                ('Type_ACT_MLD', models.CharField(choices=[('ACT', 'ACT'), ('MLD', 'MLD')], max_length=3)),
                ('mode_début', models.CharField(choices=[('ACT', 'ACT'), ('MLD', 'MLD')], max_length=11)),
                ('date_début', models.DateField(blank=True, null=True)),
                ('date_1ère_Consolidation', models.DateField(blank=True, null=True)),
                ('date_rechute', models.DateField(blank=True, null=True)),
                ('date_dernière_rechute', models.DateField(blank=True, null=True)),
                ('date_dernière_consolidation', models.DateField(blank=True, null=True)),
                ('mécanisme', models.TextField(blank=True, null=True)),
                ('lombalgies', models.CharField(default='oui', max_length=3)),
                ('sciatalgie', models.CharField(default='non', max_length=3)),
                ('diabète', models.CharField(default=0, max_length=3)),
                ('HTA', models.CharField(blank=True, default=0, max_length=3, null=True)),
                ('respiratoire', models.CharField(blank=True, default=0, max_length=3, null=True)),
                ('Autre', models.CharField(blank=True, default=0, max_length=250, null=True)),
                ('Autre_1', models.CharField(blank=True, default=0, max_length=250, null=True)),
                ('mariage', models.CharField(choices=[('oui', 'oui'), ('non', 'non'), ('divorcé', 'divorcé(é)'), ('veuve', 'veuve')], max_length=7)),
                ('nombre_enfants', models.PositiveSmallIntegerField()),
                ('durée_cotisation_an', models.PositiveSmallIntegerField()),
                ('dernier_emploi', models.TextField(blank=True, null=True)),
                ('scolarisation', models.TextField(blank=True, null=True)),
                ('plainte', models.TextField(blank=True, null=True)),
                ('Pb_sphinctérien', models.TextField(blank=True, null=True)),
                ('rééducation', models.TextField(blank=True, null=True)),
                ('état_général', models.TextField(blank=True, null=True)),
                ('coopérant', models.TextField(blank=True, null=True)),
                ('poids', models.TextField(blank=True, null=True)),
                ('taille', models.TextField(blank=True, null=True)),
                ('IMC', models.TextField(blank=True, null=True)),
                ('corpulence', models.TextField(blank=True, null=True)),
                ('ceinture_de_soutien', models.TextField(blank=True, null=True)),
                ('boiterie', models.TextField(blank=True, null=True)),
                ('déroulement_du_pas', models.TextField(blank=True, null=True)),
                ('droit', models.TextField(blank=True, null=True)),
                ('gauche', models.TextField(blank=True, null=True)),
                ('sur_les_talons', models.TextField(blank=True, null=True)),
                ('sur_les_pointes_des_pieds', models.TextField(blank=True, null=True)),
                ('mode', models.TextField(blank=True, null=True)),
                ('stabilité', models.TextField(blank=True, null=True)),
                ('indice_de_schober', models.TextField(blank=True, null=True)),
                ('distance_doigts_sol', models.TextField(blank=True, null=True)),
                ('lordose_lombaire', models.TextField(blank=True, null=True)),
                ('droit_1', models.TextField(blank=True, null=True)),
                ('gauche_1', models.TextField(blank=True, null=True)),
                ('cicatrice', models.TextField(blank=True, null=True)),
                ('date_opération', models.TextField(blank=True, null=True)),
                ('type_opération', models.TextField(blank=True, null=True)),
                ('ROT', models.TextField(blank=True, null=True)),
                ('canal_étroit', models.CharField(blank=True, choices=[('oui', 'oui'), ('non', 'non')], max_length=3, null=True)),
                ('état_discal', models.TextField(blank=True, null=True)),
                ('L3_L4', models.TextField(blank=True, null=True)),
                ('L4_L5', models.TextField(blank=True, null=True)),
                ('L5_S1', models.TextField(blank=True, null=True)),
                ('malformation', models.TextField(blank=True, null=True)),
                ('repos', models.CharField(blank=True, max_length=25, null=True)),
                ('reprise', models.CharField(blank=True, choices=[('oui', 'oui'), ('non', 'non')], max_length=3, null=True)),
                ('mise_en_Invalidité', models.CharField(blank=True, choices=[('oui', 'oui'), ('non', 'non')], max_length=3, null=True)),
                ('Comments1', models.TextField(blank=True, null=True)),
                ('Comments2', models.TextField(blank=True, null=True)),
                ('age', models.PositiveSmallIntegerField()),
                ('ImagePic', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Expert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
