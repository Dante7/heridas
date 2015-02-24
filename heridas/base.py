# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class Tbl10MercadoProd(models.Model):
    id = models.IntegerField(primary_key=True)
    id_tbl1 = models.IntegerField()
    parche_elec = models.CharField(max_length=300, blank=True)
    class Meta:
        db_table = u'tbl10_mercado_prod'

class Tbl11MercadoProdPro(models.Model):
    id = models.IntegerField(primary_key=True)
    id_tbl1 = models.IntegerField()
    ventajas = models.CharField(max_length=300, blank=True)
    class Meta:
        db_table = u'tbl11_mercado_prod_pro'

class Tbl12MercadoProdContra(models.Model):
    id = models.IntegerField(primary_key=True)
    id_tbl1 = models.IntegerField()
    desventajas = models.CharField(max_length=300, blank=True)
    class Meta:
        db_table = u'tbl12_mercado_prod_contra'

class Tbl13MercadoProdIdeal(models.Model):
    id = models.IntegerField(primary_key=True)
    id_tbl1 = models.IntegerField()
    atributos = models.CharField(max_length=300, blank=True)
    class Meta:
        db_table = u'tbl13_mercado_prod_ideal'

class Tbl14MercadoProdRestric(models.Model):
    id = models.IntegerField(primary_key=True)
    id_tbl1 = models.IntegerField()
    razones = models.CharField(max_length=300, blank=True)
    class Meta:
        db_table = u'tbl14_mercado_prod_restric'

class Tbl15AtributoRank(models.Model):
    id = models.IntegerField(primary_key=True)
    id_tbl1 = models.IntegerField()
    ambiente_humedo = models.IntegerField(null=True, blank=True)
    precio = models.IntegerField(null=True, blank=True)
    presentaciones = models.IntegerField(null=True, blank=True)
    aplicacion = models.IntegerField(null=True, blank=True)
    cicatrizante = models.IntegerField(null=True, blank=True)
    tipo_lesion = models.IntegerField(null=True, blank=True)
    eficacia = models.IntegerField(null=True, blank=True)
    adhesion = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'tbl15_atributo_rank'

class Tbl16AtributoRankProd(models.Model):
    id = models.IntegerField(primary_key=True)
    id_tbl1 = models.IntegerField()
    ambiente_humedo_actcoat = models.IntegerField(null=True, blank=True)
    precio_actcoat = models.IntegerField(null=True, blank=True)
    presentaciones_actcoat = models.IntegerField(null=True, blank=True)
    aplicacion_actcoat = models.IntegerField(null=True, blank=True)
    cicatrizante_actcoat = models.IntegerField(null=True, blank=True)
    tipo_lesion_actcoat = models.IntegerField(null=True, blank=True)
    eficacia_actcoat = models.IntegerField(null=True, blank=True)
    adhesion_actcoat = models.IntegerField(null=True, blank=True)
    ambiente_humedo_allevyn = models.IntegerField(null=True, blank=True)
    precio_allevyn = models.IntegerField(null=True, blank=True)
    presentaciones_allevyn = models.IntegerField(null=True, blank=True)
    aplicacion_allevyn = models.IntegerField(null=True, blank=True)
    cicatrizante_allevyn = models.IntegerField(null=True, blank=True)
    tipo_lesion_allevyn = models.IntegerField(null=True, blank=True)
    eficacia_allevyn = models.IntegerField(null=True, blank=True)
    adhesion_allevyn = models.IntegerField(null=True, blank=True)
    ambiente_humedo_aquacel = models.IntegerField(null=True, blank=True)
    precio_aquacel = models.IntegerField(null=True, blank=True)
    presentaciones_aquacel = models.IntegerField(null=True, blank=True)
    aplicacion_aquacel = models.IntegerField(null=True, blank=True)
    cicatrizante_aquacel = models.IntegerField(null=True, blank=True)
    tipo_lesion_aquacel = models.IntegerField(null=True, blank=True)
    eficacia_aquacel = models.IntegerField(null=True, blank=True)
    adhesion_aquacel = models.IntegerField(null=True, blank=True)
    ambiente_humedo_comfeel_h = models.IntegerField(null=True, blank=True)
    precio_comfeel_h = models.IntegerField(null=True, blank=True)
    presentaciones_comfeel_h = models.IntegerField(null=True, blank=True)
    aplicacion_comfeel_h = models.IntegerField(null=True, blank=True)
    cicatrizante_comfeel_h = models.IntegerField(null=True, blank=True)
    tipo_lesion_comfeel_h = models.IntegerField(null=True, blank=True)
    eficacia_comfeel_h = models.IntegerField(null=True, blank=True)
    adhesion_comfeel_h = models.IntegerField(null=True, blank=True)
    ambiente_humedo_comfeel_plus = models.IntegerField(null=True, blank=True)
    precio_comfeel_plus = models.IntegerField(null=True, blank=True)
    presentaciones_comfeel_plus = models.IntegerField(null=True, blank=True)
    aplicacion_comfeel_plus = models.IntegerField(null=True, blank=True)
    cicatrizante_comfeel_plus = models.IntegerField(null=True, blank=True)
    tipo_lesion_comfeel_plus = models.IntegerField(null=True, blank=True)
    eficacia_comfeel_plus = models.IntegerField(null=True, blank=True)
    adhesion_comfeel_plus = models.IntegerField(null=True, blank=True)
    ambiente_humedo_duoderm = models.IntegerField(null=True, blank=True)
    precio_duoderm = models.IntegerField(null=True, blank=True)
    presentaciones_duoderm = models.IntegerField(null=True, blank=True)
    aplicacion_duoderm = models.IntegerField(null=True, blank=True)
    cicatrizante_duoderm = models.IntegerField(null=True, blank=True)
    tipo_lesion_duoderm = models.IntegerField(null=True, blank=True)
    eficacia_duoderm = models.IntegerField(null=True, blank=True)
    adhesion_duoderm = models.IntegerField(null=True, blank=True)
    ambiente_humedo_kaltostat = models.IntegerField(null=True, blank=True)
    precio_kaltostat = models.IntegerField(null=True, blank=True)
    presentaciones_kaltostat = models.IntegerField(null=True, blank=True)
    aplicacion_kaltostat = models.IntegerField(null=True, blank=True)
    cicatrizante_kaltostat = models.IntegerField(null=True, blank=True)
    tipo_lesion_kaltostat = models.IntegerField(null=True, blank=True)
    eficacia_kaltostat = models.IntegerField(null=True, blank=True)
    adhesion_kaltostat = models.IntegerField(null=True, blank=True)
    ambiente_humedo_tegaderm = models.IntegerField(null=True, blank=True)
    precio_tegaderm = models.IntegerField(null=True, blank=True)
    presentaciones_tegaderm = models.IntegerField(null=True, blank=True)
    aplicacion_tegaderm = models.IntegerField(null=True, blank=True)
    cicatrizante_tegaderm = models.IntegerField(null=True, blank=True)
    tipo_lesion_tegaderm = models.IntegerField(null=True, blank=True)
    eficacia_tegaderm = models.IntegerField(null=True, blank=True)
    adhesion_tegaderm = models.IntegerField(null=True, blank=True)
    ambiente_humedo_varihesive = models.IntegerField(null=True, blank=True)
    precio_varihesive = models.IntegerField(null=True, blank=True)
    presentaciones_varihesive = models.IntegerField(null=True, blank=True)
    aplicacion_varihesive = models.IntegerField(null=True, blank=True)
    cicatrizante_varihesive = models.IntegerField(null=True, blank=True)
    tipo_lesion_varihesive = models.IntegerField(null=True, blank=True)
    eficacia_varihesive = models.IntegerField(null=True, blank=True)
    adhesion_varihesive = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'tbl16_atributo_rank_prod'

class Tbl17NivelSatisfac(models.Model):
    id = models.IntegerField(primary_key=True)
    id_tbl1 = models.IntegerField()
    nivel_satisfaccion = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'tbl17_nivel_satisfac'

class Tbl1Generales(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=300, blank=True)
    especialidad = models.CharField(max_length=300, blank=True)
    calle = models.CharField(max_length=300, blank=True)
    numero = models.CharField(max_length=150, blank=True)
    colonia = models.CharField(max_length=300, blank=True)
    ciudad_estado = models.CharField(max_length=300, blank=True)
    telefono = models.CharField(max_length=300, blank=True)
    fecha = models.DateField(null=True, blank=True)
    hora_ini = models.TextField(blank=True) # This field type is a guess.
    hora_fin = models.TextField(blank=True) # This field type is a guess.
    entrevistador = models.CharField(max_length=300, blank=True)
    supervisor = models.CharField(max_length=300, blank=True)
    fecha_supervision = models.DateField(null=True, blank=True)
    class Meta:
        db_table = u'tbl1_generales'

class Tbl2Filtros(models.Model):
    id = models.IntegerField(primary_key=True)
    id_tbl1 = models.IntegerField()
    disponibilidad = models.CharField(max_length=30, blank=True)
    publica_privada = models.CharField(max_length=30, blank=True)
    pacientes_pub = models.IntegerField(null=True, blank=True)
    pacientes_priv = models.IntegerField(null=True, blank=True)
    trata_heridas = models.CharField(max_length=30, blank=True)
    tratados_pub = models.IntegerField(null=True, blank=True)
    tratados_priv = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'tbl2_filtros'

class Tbl3Dimensionamiento(models.Model):
    id = models.IntegerField(primary_key=True)
    id_tbl1 = models.IntegerField()
    pac_mes = models.IntegerField(null=True, blank=True)
    pac_h = models.IntegerField(null=True, blank=True)
    pac_h_f = models.IntegerField(null=True, blank=True)
    pac_h_m = models.IntegerField(null=True, blank=True)
    pac_h_tot_genero = models.IntegerField(null=True, blank=True)
    pac_h_ped = models.IntegerField(null=True, blank=True)
    pac_h_adol = models.IntegerField(null=True, blank=True)
    pac_h_jov = models.IntegerField(null=True, blank=True)
    pac_h_may = models.IntegerField(null=True, blank=True)
    pac_h_tot_edad = models.IntegerField(null=True, blank=True)
    pac_h_antisep = models.IntegerField(null=True, blank=True)
    pac_h_antimic = models.IntegerField(null=True, blank=True)
    pac_h_parche = models.IntegerField(null=True, blank=True)
    pac_h_cica = models.IntegerField(null=True, blank=True)
    pac_h_tot_curacion = models.IntegerField(null=True, blank=True)
    pac_h_consult = models.IntegerField(null=True, blank=True)
    pac_h_hosp = models.IntegerField(null=True, blank=True)
    pac_h_tot_lugar = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'tbl3_dimensionamiento'

class Tbl4TxP5(models.Model):
    id = models.IntegerField(primary_key=True)
    id_tbl1 = models.IntegerField()
    pac_h_pub_tx = models.IntegerField(null=True, blank=True)
    pac_h_priv_tx = models.IntegerField(null=True, blank=True)
    pac_h_priv_tx_nuevos = models.IntegerField(null=True, blank=True)
    pac_h_priv_tx_referidos = models.IntegerField(null=True, blank=True)
    pac_h_pub_tx_nuevos = models.IntegerField(null=True, blank=True)
    pac_h_pub_tx_referidos = models.IntegerField(null=True, blank=True)
    clas_det_tx = models.CharField(max_length=30, blank=True)
    clas_det_tx_tipo = models.CharField(max_length=300, blank=True)
    class Meta:
        db_table = u'tbl4_tx_p5'

class Tbl5TxP6(models.Model):
    id = models.IntegerField(primary_key=True)
    id_tbl1 = models.IntegerField()
    herida = models.CharField(max_length=300, blank=True)
    porc = models.IntegerField(null=True, blank=True)
    tx = models.CharField(max_length=300, blank=True)
    tx_protec = models.CharField(max_length=300, blank=True)
    class Meta:
        db_table = u'tbl5_tx_p6'

class Tbl6TxP7(models.Model):
    id = models.IntegerField(primary_key=True)
    id_tbl1 = models.IntegerField()
    herida = models.CharField(max_length=300, blank=True)
    porc = models.IntegerField(null=True, blank=True)
    tx = models.CharField(max_length=300, blank=True)
    tx_protec = models.CharField(max_length=300, blank=True)
    class Meta:
        db_table = u'tbl6_tx_p7'

class Tbl7TxP8(models.Model):
    id = models.IntegerField(primary_key=True)
    id_tbl1 = models.IntegerField()
    heridas_no_tratadas = models.CharField(max_length=30, blank=True)
    class Meta:
        db_table = u'tbl7_tx_p8'

class Tbl8TxP8(models.Model):
    id = models.IntegerField(primary_key=True)
    id_tbl1 = models.IntegerField()
    tipo_herida = models.CharField(max_length=300, blank=True)
    espe_refiere = models.CharField(max_length=300, blank=True)
    class Meta:
        db_table = u'tbl8_tx_p8'

class Tbl9MercadoTabla(models.Model):
    id = models.IntegerField(primary_key=True)
    id_tbl1 = models.IntegerField()
    actcoat = models.CharField(max_length=300, blank=True)
    actcoat_pres = models.CharField(max_length=150, blank=True)
    allevyn = models.CharField(max_length=300, blank=True)
    allevyn_pres = models.CharField(max_length=150, blank=True)
    aquacel = models.CharField(max_length=300, blank=True)
    aquacel_pres = models.CharField(max_length=150, blank=True)
    comfeel_h = models.CharField(max_length=300, blank=True)
    comfeel_h_pres = models.CharField(max_length=150, blank=True)
    comfeel_plus = models.CharField(max_length=300, blank=True)
    comfeel_plus_pres = models.CharField(max_length=150, blank=True)
    duoderm = models.CharField(max_length=300, blank=True)
    duoderm_pres = models.CharField(max_length=150, blank=True)
    kaltostat = models.CharField(max_length=300, blank=True)
    kaltostat_pres = models.CharField(max_length=150, blank=True)
    tegaderm = models.CharField(max_length=300, blank=True)
    tegaderm_pres = models.CharField(max_length=150, blank=True)
    varihesive = models.CharField(max_length=300, blank=True)
    varihesive_pres = models.CharField(max_length=150, blank=True)
    otro1_cual = models.CharField(max_length=300, blank=True)
    otro1 = models.CharField(max_length=300, blank=True)
    otro1_pres = models.CharField(max_length=150, blank=True)
    otro2_cual = models.CharField(max_length=300, blank=True)
    otro2 = models.CharField(max_length=300, blank=True)
    otro2_pres = models.CharField(max_length=150, blank=True)
    class Meta:
        db_table = u'tbl9_mercado_tabla'

