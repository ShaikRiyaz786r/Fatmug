from django.db import models

class Vendor(models.Model):
    name = models.CharField(max_length=255)
    contact = models.TextField()
    details = models.TextField(null=True)
    address = models.TextField()
    vendor_code = models.CharField(max_length=255,primary_key=True)
    on_time_delivery_rate: models.FloatField(null=True, blank=True)
    quality_rating_avg: models.FloatField(null=True, blank=True)
    average_response_time: models.FloatField(null=True, blank=True)
    fulfillment_rate: models.FloatField(null=True, blank=True)
    

class PurchaseOrder(models.Model):
    po_number: models.CharField()
    vendor: models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date: models.DateTimeField()
    delivery_date: models.DateTimeField()
    items: models.JSONField()
    quantity: models.IntegerField()
    status: models.CharField(max_length=255)
    quality_rating: models.FloatField(null=True, blank=True)
    issue_date: models.DateTimeField(auto_now=True)
    acknowledgment_date: models.DateTimeField(auto_now=True)


class VendorPerformance(models.Model):
    vendor: models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date: models.DateTimeField()
    on_time_delivery_rate: models.FloatField(null=True, blank=True)
    quality_rating_avg: models.FloatField(null=True, blank=True)
    average_response_time: models.FloatField(null=True, blank=True)
    fulfillment_rate: models.FloatField(null=True, blank=True)