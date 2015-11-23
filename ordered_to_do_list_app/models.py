from django.db import models

# Create your models here.

class ListItem(models.Model):
	# should 'item' in fact be TextField? for a longer string? investigate
	item = models.CharField(max_length=255)
	datetime = models.CharField(max_length=128)
	status = models.CharField(max_length=128)



# want to enter datetime stamp whenever a new row is added to the db (ie when the user adds a new item)
# I'm assuming there's a way of doing this more simply
# but I haven't found it so I could write a script to say:
# 	- datetime = a text field (charfield?) and whenever 