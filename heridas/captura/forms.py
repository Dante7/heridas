#encoding:utf-8

from django.forms import ModelForm
from django.forms.widgets import HiddenInput, RadioSelect, DateInput
from django.contrib.admin.widgets import AdminDateWidget
from django import forms
from captura.models import *

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
	disponibilidad = forms.CharField(label='')
	disponibilidad.widget.attrs['class']='form-control'

	publica_privada = forms.CharField(label='')
	publica_privada.widget.attrs['class']='form-control'

	pacientes_pub = forms.CharField(label='')
	pacientes_pub.widget.attrs['class']='form-control'

	pacientes_priv = forms.CharField(label='')
	pacientes_priv.widget.attrs['class']='form-control'

	trata_heridas = forms.CharField(label='')
	trata_heridas.widget.attrs['class']='form-control'

	tratados_pub = forms.CharField(label='')
	tratados_pub.widget.attrs['class']='form-control'

	tratados_priv = forms.CharField(label='')
	tratados_priv.widget.attrs['class']='form-control'

	class Meta:
		model = Tbl2Filtros

class FrmTbl3(ModelForm):
	"""Formulario"""
	id_tbl1 = forms.CharField(widget=forms.HiddenInput())
	pac_mes = forms.CharField(label='')
	pac_mes.widget.attrs['class']='form-control'

	pac_h = forms.CharField(label='')
	pac_h.widget.attrs['class']='form-control'

	pac_h_f = forms.CharField(label='')
	pac_h_f.widget.attrs['class']='form-control'

	pac_h_m = forms.CharField(label='')
	pac_h_m.widget.attrs['class']='form-control'

	pac_h_tot_genero = forms.CharField(label='')
	pac_h_tot_genero.widget.attrs['class']='form-control'

	pac_h_ped = forms.CharField(label='')
	pac_h_ped.widget.attrs['class']='form-control'

	pac_h_adol = forms.CharField(label='')
	pac_h_adol.widget.attrs['class']='form-control'

	pac_h_jov = forms.CharField(label='')
	pac_h_jov.widget.attrs['class']='form-control'

	pac_h_may = forms.CharField(label='')
	pac_h_may.widget.attrs['class']='form-control'

	pac_h_tot_edad = forms.CharField(label='')
	pac_h_tot_edad.widget.attrs['class']='form-control'

	pac_h_antisep = forms.CharField(label='')
	pac_h_antisep.widget.attrs['class']='form-control'

	pac_h_antimic = forms.CharField(label='')
	pac_h_antimic.widget.attrs['class']='form-control'

	pac_h_parche = forms.CharField(label='')
	pac_h_parche.widget.attrs['class']='form-control'

	pac_h_cica = forms.CharField(label='')
	pac_h_cica.widget.attrs['class']='form-control'

	pac_h_tot_curacion = forms.CharField(label='')
	pac_h_tot_curacion.widget.attrs['class']='form-control'

	pac_h_consult = forms.CharField(label='')
	pac_h_consult.widget.attrs['class']='form-control'

	pac_h_hosp = forms.CharField(label='')
	pac_h_hosp.widget.attrs['class']='form-control'

	pac_h_tot_lugar = forms.CharField(label='')
	pac_h_tot_lugar.widget.attrs['class']='form-control'

	class Meta:
		model = Tbl3Dimensionamiento