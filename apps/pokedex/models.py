from django.db import models

class TblPokemon(models.Model):
    id_pokemon = models.AutoField(primary_key=True)
    num_pokedex_pokemon = models.IntegerField()
    name_pokemon = models.CharField(max_length=40)
    img_pokemon = models.CharField(max_length=255, blank=True, null=True)
    type_1_pokemon = models.ForeignKey('TblTypes', models.DO_NOTHING, db_column='type_1_pokemon')
    type_2_pokemon = models.ForeignKey('TblTypes', models.DO_NOTHING, db_column='type_2_pokemon', related_name='tblpokemon_type_2_pokemon_set', blank=True, null=True)
    total_pokemon = models.IntegerField()
    hp_pokemon = models.IntegerField()
    atk_pokemon = models.IntegerField()
    def_pokemon = models.IntegerField()
    sp_atk_pokemon = models.IntegerField()
    sp_def_pokemon = models.IntegerField()
    speed_pokemon = models.IntegerField()
    generation_pokemon = models.IntegerField()
    legendary_pokemon = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_pokemon'


class TblTypes(models.Model):
    type = models.CharField(primary_key=True, max_length=20)
    weaknesses_1 = models.CharField(max_length=20, blank=True, null=True)
    weaknesses_2 = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_types'