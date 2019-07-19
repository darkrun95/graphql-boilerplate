# graphql-boilerplate

Boiler Plate Setup for GraphQL with Django and Graphene
1. Database used: SQLite

#### Files Needed to be modified
1. Under <custom-app> add __schema.py__: For creating schema structure for GraphQL
2. Under __settings.py__
	- Add 'graphene_django' to INSTALLED_APPS
	- Add the following piece of code
```
GRAPHENE = {
    'SCHEMA': 'schema.schema'
}
```
3. Modify root __urls.py__ 
4. Add __schema.py__ under the root directory.