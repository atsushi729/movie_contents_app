1. Video
    - hosts? -> YouTube - private video -> udacity
             ->Vimeo, wistia
             -> self hosted - nginx
    - Analytics
        - lot of data
        - 1 user watcher for 10 seconds on 100 videos  * 10,000
        - lots of writes
        - frame by frame analysis -> 30 FPS -> 120 second
        - 

2. Members
    - sign up
    - login
    - remember thigs
    - email validation / confirmation

- AsrtaDB - Managed NoSQL Cassandra
- Database name
  - Keyspace name
    - table
    
- Database for Testing
  - keyspace -> projest 1
    - tables (correspond to prod)
    - py_compile.compile('./app/main.py') 
  
```python
from app import db
from app.users.models import User

db.get_session()
User.objects.create(email='hello@teamcfe.com', password='abc123')
User.objects.create(email='hello@teamcfe.com', password='abc123d')
```

```python

q = User.objects.all()

for user in q:
    print(user.email, user.user_id, user.password)
```