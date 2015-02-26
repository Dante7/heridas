#encoding:utf-8

from django.forms import ModelForm
from django.forms.widgets import HiddenInput, RadioSelect, DateInput
from django.contrib.admin.widgets import AdminDateWidget
from django import forms
from captura.models import *

sino = (
			('Si','Si'),
			('No','No'),
)

tipo = (
			('Saber si la clasificación ¿es de él o si sigue alguna guía y cuál o cuáles son?','Saber si la clasificación ¿es de él o si sigue alguna guía y cuál o cuáles son?'),
			('¿Cómo es la clasificación?','¿Cómo es la clasificación?'),
			('Aproximadamente, de los pacientes que tienen heridas ¿cuántos tiene en cada grupo?','Aproximadamente, de los pacientes que tienen heridas ¿cuántos tiene en cada grupo?'),
			('¿Cómo cambia el tratamiento de acuerdo a esa clasificación?','¿Cómo cambia el tratamiento de acuerdo a esa clasificación?'),
)

class FrmTbl1(ModelForm):
	"""Formulario"""
	folio = forms.CharField()
	folio.widget.attrs['class']='form-control'

	nombre = forms.CharField()
	nombre.widget.attrs['class']='form-control'

	especialidad = forms.CharField()
	especialidad.widget.attrs['class']='form-control'

	calle = forms.CharField()
	calle.widget.attrs['class']='form-control'

	numero = forms.CharField()
	numero.widget.attrs['class']='form-control'

	colonia = forms.CharField()
	colonia.widget.attrs['class']='form-control'

	ciudad_estado = forms.CharField()
	ciudad_estado.widget.attrs['class']='form-control'

	telefono = forms.CharField()
	telefono.widget.attrs['class']='form-control'

	fecha = forms.DateField()
	fecha.widget.attrs['class']='form-control'

	hora_ini = forms.CharField()
	hora_ini.widget.attrs['class']='form-control'

	hora_fin = forms.CharField()
	hora_fin.widget.attrs['class']='form-control'

	entrevistador = forms.CharField()
	entrevistador.widget.attrs['class']='form-control'

	supervisor = forms.CharField()
	supervisor.widget.attrs['class']='form-control'

	fecha_supervision = forms.DateField()
	fecha_supervision.widget.attrs['class']='form-control'


	class Meta:
		model = Tbl1Generales

class FrmTbl2(ModelForm):
	"""docstring for ClassName"""
	id_tbl1 = forms.CharField(widget=forms.HiddenInput())
	disponibilidad = forms.CharField(label='¿podemos contar con su apoyo?')
	disponibilidad.widget.attrs['class']='form-control'

	publica_privada = forms.CharField(label='F1. Dr. ¿Actualmente cuenta con práctica pública y privada?')
	publica_privada.widget.attrs['class']='form-control'

	pacientes_pub = forms.CharField(label='F2.	Dr., aproximadamente ¿cuántos pacientes atiende en un mes? (pública)')
	pacientes_pub.widget.attrs['class']='form-control'

	pacientes_priv = forms.CharField(label='F2.	Dr., aproximadamente ¿cuántos pacientes atiende en un mes? (privada)')
	pacientes_priv.widget.attrs['class']='form-control'

	trata_heridas = forms.CharField(label='F3. Dr. ¿usted trata heridas hospitalarias?')
	trata_heridas.widget.attrs['class']='form-control'

	tratados_pub = forms.CharField(label='F4.  Considerando los pacientes que ve en un mes en su práctica pública ¿qué porcentaje de estos requirió tratamiento de heridas?')
	tratados_pub.widget.attrs['class']='form-control'

	tratados_priv = forms.CharField(label='F5. Considerando los pacientes que ve en un mes en su práctica privada ¿qué porcentaje de estos requirió tratamiento de heridas? ')
	tratados_priv.widget.attrs['class']='form-control'

	class Meta:
		model = Tbl2Filtros

class FrmTbl3(ModelForm):
	"""Formulario"""
	id = forms.CharField(widget=forms.HiddenInput())
	id_tbl1 = forms.CharField(widget=forms.HiddenInput())
	pac_mes = forms.CharField(label='TOTAL DE PACIENTES EN CONSULTA (en un mes promedio)')
	pac_mes.widget.attrs['class']='form-control'

	pac_h = forms.CharField(label='TOTAL PACIENTES CON HERIDAS')
	pac_h.widget.attrs['class']='form-control'

	pac_h_f = forms.CharField(label='GENERO: Femenino')
	pac_h_f.widget.attrs['class']='form-control'

	pac_h_m = forms.CharField(label='GENERO: Masculino')
	pac_h_m.widget.attrs['class']='form-control'

	pac_h_tot_genero = forms.CharField(label='GENERO: Total')
	pac_h_tot_genero.widget.attrs['class']='form-control'

	pac_h_ped = forms.CharField(label='EDAD: Pediátricos')
	pac_h_ped.widget.attrs['class']='form-control'

	pac_h_adol = forms.CharField(label='EDAD: Adolecente')
	pac_h_adol.widget.attrs['class']='form-control'

	pac_h_jov = forms.CharField(label='EDAD: Adulto joven')
	pac_h_jov.widget.attrs['class']='form-control'

	pac_h_may = forms.CharField(label='EDAD: Adultos mayores')
	pac_h_may.widget.attrs['class']='form-control'

	pac_h_tot_edad = forms.CharField(label='EDAD: Total')
	pac_h_tot_edad.widget.attrs['class']='form-control'

	pac_h_antisep = forms.CharField(label='TIPO DE CURACIÓN EMPLEADO: Antiséptico')
	pac_h_antisep.widget.attrs['class']='form-control'

	pac_h_antimic = forms.CharField(label='TIPO DE CURACIÓN EMPLEADO: Antimicrobiano')
	pac_h_antimic.widget.attrs['class']='form-control'

	pac_h_parche = forms.CharField(label='TIPO DE CURACIÓN EMPLEADO: Parche')
	pac_h_parche.widget.attrs['class']='form-control'

	pac_h_cica = forms.CharField(label='TIPO DE CURACIÓN EMPLEADO: Cicatrizante')
	pac_h_cica.widget.attrs['class']='form-control'

	pac_h_tot_curacion = forms.CharField(label='TIPO DE CURACIÓN EMPLEADO: Total')
	pac_h_tot_curacion.widget.attrs['class']='form-control'

	pac_h_consult = forms.CharField(label='LUGAR DE USO: Consultorio')
	pac_h_consult.widget.attrs['class']='form-control'

	pac_h_hosp = forms.CharField(label='LUGAR DE USO: Hospitalario')
	pac_h_hosp.widget.attrs['class']='form-control'

	pac_h_tot_lugar = forms.CharField(label='LUGAR DE USO: Total')
	pac_h_tot_lugar.widget.attrs['class']='form-control'

	class Meta:
		model = Tbl3Dimensionamiento

class FrmTbl4(ModelForm):
	id = forms.CharField(widget=forms.HiddenInput())
	id_tbl1 = forms.CharField(widget=forms.HiddenInput())
	pac_h_pub_tx = forms.CharField(label='2. Dr. De los pacientes que ve en un mes, ¿cuántos requieren tratamiento de heridas? (público)')
	pac_h_pub_tx.widget.attrs['class']='form-control'

	pac_h_priv_tx = forms.CharField(label='2. Dr. De los pacientes que ve en un mes, ¿cuántos requieren tratamiento de heridas? (privado)')
	pac_h_priv_tx.widget.attrs['class']='form-control'

	pac_h_priv_tx_nuevos = forms.CharField(label='3. Pensando en sus pacientes privados que requieren tratamiento de heridas, ¿cuántos son nuevos?')
	pac_h_priv_tx_nuevos.widget.attrs['class']='form-control'

	pac_h_priv_tx_referidos = forms.CharField(label='3.	Pensando en sus pacientes privados que requieren tratamiento de heridas, ¿cuántos son referidos?')
	pac_h_priv_tx_referidos.widget.attrs['class']='form-control'

	pac_h_pub_tx_nuevos = forms.CharField(label='4. Pensando en sus pacientes públicos que requieren tratamiento de heridas, ¿cuántos son nuevos?')
	pac_h_pub_tx_nuevos.widget.attrs['class']='form-control'

	pac_h_pub_tx_referidos = forms.CharField(label='4. Pensando en sus pacientes públicos que requieren tratamiento de heridas, ¿cuántos son referidos?')
	pac_h_pub_tx_referidos.widget.attrs['class']='form-control'

	clas_det_tx = forms.ChoiceField(choices=sino, label='5. Dr. hablando específicamente de heridas, ¿usted hace alguna clasificación para determinar el tratamiento a seguir?')
	clas_det_tx.widget.attrs['class']='form-control'

	clas_det_tx_tipo = forms.ChoiceField(choices=tipo, label='En caso de que SI haga alguna clasificación, indagar en la clasificación:')
	clas_det_tx_tipo.widget.attrs['class']='form-control'


	class Meta:
		model = Tbl4TxP5

class FrmTbl5(ModelForm):
	id = forms.CharField(widget=forms.HiddenInput())
	id_tbl1 = forms.CharField(widget=forms.HiddenInput())
	herida = forms.CharField(label='Tipo de Herida tratada')
	herida.widget.attrs['class']='form-control'

	porc = forms.CharField(label='%')
	porc.widget.attrs['class']='form-control'

	tx = forms.CharField(label='TRATAMIENTO')
	tx.widget.attrs['class']='form-control'

	tx_protec = forms.CharField(label='TRATAMIENTO DE CUBRIMIENTO/PROTECCIÓN')
	tx_protec.widget.attrs['class']='form-control'


	class Meta:
		model = Tbl5TxP6