class Log(models.class (models.Model):
    seq=models.IntegerField()
    event=models.CharField(max_length=50, null=True)
    create_date=models.DateTimeField(auto_now=True)
    hash=models.CharField(max_length=200, null=True)
    message=models.CharField(max_length=1000, null=True)


    

    class Meta:
        managed=False
        db_table="log"

    
)