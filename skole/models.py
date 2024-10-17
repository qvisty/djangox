from django.db import models

# Create your models here.

 
class SfoGruppe(models.Model):
    gruppe_nummer = models.CharField(max_length=1)

    def __str__(self):
        return self.gruppe_nummer

class Afdeling(models.Model):
    navn = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = "afdeling"
        verbose_name_plural = "afdelinger"
        ordering = ['navn']



    def __str__(self):
        return self.navn

class Team(models.Model):
    navn = models.CharField(max_length=50)
    afdeling = models.ForeignKey(Afdeling, on_delete= models.SET_NULL, blank=True, null=True)
    
    def __str__(self):
        return self.navn

class Klasse(models.Model):
    navn = models.CharField(max_length=50)
    team = models.ForeignKey(Team, on_delete= models.SET_NULL, blank=True, null=True)

    class Meta:
        verbose_name = "klasse"
        verbose_name_plural = "klasser"
        
    def __str__(self):
        return self.navn
    
class SfoModul(models.Model):
    navn = models.CharField(max_length=50)
    pasning_morgen = models.BooleanField()
    pasning_eftermiddag = models.BooleanField()
    pasning_ferier = models.BooleanField()

    def __str__(self):
        return self.navn

class Elev(models.Model):
    fornavn = models.CharField(max_length=100)
    efternavn = models.CharField(max_length=100)
    sfo_gruppe = models.ForeignKey(SfoGruppe, blank=True, null=True, on_delete = models.SET_NULL)
    klasse = models.ForeignKey(Klasse, blank=True, null=True, on_delete = models.SET_NULL)
    sfomodul = models.ForeignKey(SfoModul, blank=True, null=True, on_delete=models.SET_NULL)
    
    class Meta:
        verbose_name = "elev"
        verbose_name_plural = "elever"
        ordering = ['fornavn', 'efternavn']

    def is_in_sfo_gruppe(self):
        return bool(self.sfo_gruppe)

    def __str__(self):
        return f"{self.fornavn} {self.efternavn}"

class Medarbejder(models.Model):
    fornavn = models.CharField('fornavn', max_length=100)
    efternavn = models.CharField('efternavn', max_length=100)
    sfo_gruppe = models.ForeignKey(SfoGruppe, blank=True, null=True, on_delete = models.SET_NULL)
    klasser = models.ManyToManyField(Klasse)
    
    class Meta:
        verbose_name = "medarbejder"
        verbose_name_plural = "medarbejdere"
        ordering = ['fornavn', 'efternavn']


    def __str__(self):
        return f"{self.fornavn} {self.efternavn}"

# vi får brug for en modul-klasse eller lignende, men hvordan skal det struktureres med modulers start og slutdato mv.`?` 
