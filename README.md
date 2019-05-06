# Mahasiswa RestApi

**At the end of this guide, you should have this API endpoints available:**
* GET - /api/Collage - Retrieve all Collage

* GET - /api/Collage/<id> - Retrieve by id Collage

* POST - /api/Collage - Add a new Collage

* PUT - /api/Collage - Update a Collage

* DELETE - /api/Collage - Delete a Collage

* GET - /api/Biodata - Retrieve all the stored Biodata

* POST - /api/Biodata - Add new Biodata

**Install Web Service Requirement**

    `pip install -r requirement.txt`
    
**Running migrations**

**Migrations**

    $ python migrate.py db init
    $ python migrate.py db migrate
    $ python migrate.py db upgrade

**In the Category resources, we have creating 4 endpoints:**


GET - http://127.0.0.1:5000/api/Collage

GET - http://127.0.0.1:5000/api/Collage/<id>

POST - http://127.0.0.1:5000/api/Collage

PUT - http://127.0.0.1:5000/api/Collage

DELETE - http://127.0.0.1:5000/api/Collage