You are in the `next` unreleased version of Graphene-Django (`1.0.dev`).
Please read [UPGRADE-v1.0.md](https://github.com/graphql-python/graphene/blob/master/UPGRADE-v1.0.md) to learn how to upgrade.

---

# ![Graphene Logo](http://graphene-python.org/favicon.png) Graphene-Django [![Build Status](https://travis-ci.org/graphql-python/graphene-django.svg?branch=master)](https://travis-ci.org/graphql-python/graphene-django) [![PyPI version](https://badge.fury.io/py/graphene-django.svg)](https://badge.fury.io/py/graphene-django) [![Coverage Status](https://coveralls.io/repos/graphql-python/graphene-django/badge.svg?branch=master&service=github)](https://coveralls.io/github/graphql-python/graphene-django?branch=master)


A [Django](https://www.djangoproject.com/) integration for [Graphene](http://graphene-python.org/).

## Installation

For instaling graphene, just run this command in your shell

```bash
pip install "graphene-django>=1.0.dev"
```

## Examples

Here is a simple Django model:

```python
from django.db import models

class UserModel(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
```

To create a GraphQL schema for it you simply have to write the following:

```python
from graphene_django import DjangoObjectType

class User(DjangoObjectType):
    class Meta:
        model = UserModel

class Query(graphene.ObjectType):
    users = graphene.List(User)

    @graphene.resolve_only_args
    def resolve_users(self):
        return UserModel.objects.all()

schema = graphene.Schema(query=QueryRoot)
```

Then you can simply query the schema:

```python
query = '''
    query {
      users {
        name,
        lastName
      }
    }
'''
result = schema.execute(query)
```

To learn more check out the following [examples](examples/):

* **Schema with Filtering**: [Cookbook example](examples/cookbook)
* **Relay Schema**: [Starwars Relay example](examples/starwars)


## Contributing

After cloning this repo, ensure dependencies are installed by running:

```sh
python setup.py install
```

After developing, the full test suite can be evaluated by running:

```sh
python setup.py test # Use --pytest-args="-v -s" for verbose mode
```
