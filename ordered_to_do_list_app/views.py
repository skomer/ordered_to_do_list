from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
# from django.core.urlresolvers import reverse
from django.template.context_processors import csrf
import datetime

# do I need this one?
# from django.conf import settings

from models import ListItem


# Create your views here.

# Add an item to the to do list
def add_item(request):
	name_for_item = request.POST.get('name_for_item')
	item_datetime = datetime.datetime.utcnow()
	item_status = "incomplete"
	new_item_entry = ListItem()
	new_item_entry.item = name_for_item
	new_item_entry.datetime = item_datetime
	new_item_entry.status = item_status
	new_item_entry.save()
	current_list = ListItem.objects.order_by('item')
	return render(request, 'ordered_to_do_list_app/index.html', { 'current_list' : current_list })



def index(request):
    return render(request, 'ordered_to_do_list_app/index.html', {})



# look up how to view my migrated database in sqlite3
# .schema etc but how I get the db to show in the terminal. I've forgotten everything
# make a cheatsheet with this ^^ info
# 


# how does it work with each user showing a different list at any one time?
# and how will the database forget each user?


# some other features:
# 	- user can click somewhere and then enter text to add an item to the list (adds a new row to the database)
# 	- user can see the status of each item
# 	- user can check and uncheck a box to change the status of the item
# 	- user can click a wee X symbol to delete the item
# 	- user can amend the text of any item
# to be honest, it sounds like javascript can do most of that
# but I don't know any javascript
# it's the interactivity of it that reeks of javascript
# I wonder if html can do it in a fancy way
# 


# questions:
# 	- can javascript talk to a database in the same way as python talks to sqlite?
# 	- if so, what/how?
# 	- onclick - is that javascript or html?
# 	- look up those commands for sqlite3, and make notes, then figure out how to order my list by datetime
#	- 




