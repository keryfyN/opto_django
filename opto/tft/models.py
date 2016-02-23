from django.db import models


# Create your models here.
class Tft(models.Model):
    """
    TFT object


    """
    article_number_opto = models.CharField(max_length=11)
    article_number_supplier = models.CharField(max_length=200)
    tft_brightness = models.IntegerField()
    tft_contrast = models.CharField(max_length=200)
    tft_color_amount = models.CharField(max_length=200)
    tft_viewing_angle_u = models.IntegerField()
    tft_viewing_angle_d = models.IntegerField()
    tft_viewing_angle_l = models.IntegerField()
    tft_viewing_angle_r = models.IntegerField()

    tft_operating_temperature_min = models.FloatField()
    tft_operating_temperature_max = models.FloatField()
    tft_storage_temperature_min = models.FloatField()
    tft_storage_temperature_max = models.FloatField()

    tft_outline_h_mm = models.FloatField()
    tft_outline_v_mm = models.FloatField()
    tft_outline_d_mm = models.FloatField()

    tft_active_area_h_mm = models.FloatField()
    tft_active_area_v_mm = models.FloatField()

    tft_touch_panel = models.BooleanField()
    tft_in_production = models.BooleanField()

    created_time = models.DateTimeField(auto_now_add=True)
    modificated_time = models.DateTimeField(auto_now=True)

    # ================================================================
    # Some parameters, ....

    # ================================================================
    # External links
    """tft_size_id = db.Column(db.Integer, db.ForeignKey("tft_size.id"))
    tft_size = db.relationship(TftSize, backref=db.backref('tfts', uselist=True, cascade='delete,all'))

    tft_brand_id = db.Column(db.Integer, db.ForeignKey("tft_brand.id"))
    tft_brand = db.relationship(TftBrand, backref=db.backref('tfts', uselist=True, cascade='delete,all'))

    tft_resolution_id = db.Column(db.Integer, db.ForeignKey("tft_resolution.id"))
    tft_resolution = db.relationship(TftResolution, backref=db.backref('tfts', uselist=True, cascade='delete,all'))

    ports = db.relationship('TftPort', secondary=port_tft_rel)"""

    # ================================================================
    # Class methods

    def __repr__(self):
        return '<Tft %s (%s) >' % (self.article_number_supplier, self.article_number_opto)
