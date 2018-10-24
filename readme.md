#Requirements
- Virtual Box
- Vagrant
- Python
- Modern Web Browser

#Installation Steps
1. Download or clone the files from this repository to your local machine
2. Change directories to the catalog directory
3. Bring up the virtual machine and connect to it
```vagrant up```
```vagrant ssh```
4. Change directories inside the virtual machine to the vagrant directory:
```cd /vagrant```
5. Set up the local database:
```python database_setup.py```
6. Populate the database tables with initial data:
```python database_seed.py```
7. Start the Python webserver and run the program:
```python catalog.py```
8. Open your web browser and go to localhost on port 5000:
```http://localhost:5000```

#Using the System
- Choose a category to explore items within that category
- Choose an item from the New items portlet on the home page
- Click the Log in menu item to log in securely with your Google account
- Once logged in you can create, edit, and delete categories and items within your categories

#Using API JSON Endpoints
The application has three JSON endpoints that can be accessed at the following URLs:
-  http://localhost:5000/category/JSON to retrieve all category IDs and names
-  http://localhost:5000/category/```[category_id]```/JSON to retrieve all item data within a given category ID
-  http://localhost:5000/item/```[item_id]```/JSON to retrieve item details with a given item ID
where ```[category_id]``` is the category ID and ```[item_id]``` is the item ID

#Attributions
- Acme Catalog logo: created by Flickr user James Vaughan and modified under a Creative Commons Attribution-NonCommercial-ShareAlike 2.0 Generic (CC BY-NC-SA 2.0) license
- Background image: created by Deviant Art user masonmouse under a Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported (CC BY-NC-SA 3.0) license
- New image graphic: from Pixabay under a Creative Commons CC0 1.0 Universal (CC0 1.0) Public Domain Dedication license
- Wile E. Coyote and Road Runner are Copyright by Warner Brothers, Inc.