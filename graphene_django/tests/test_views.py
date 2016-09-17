import json


def format_response(response):
    return json.loads(response.content.decode())


def test_client_get_good_query(settings, client):
    settings.ROOT_URLCONF = 'graphene_django.tests.urls'
    response = client.get('/graphql', {'query': '{ human { headline } }'})
    json_response = format_response(response)
    expected_json = {
        'data': {
            'human': {
                'headline': None
            }
        }
    }
    assert json_response == expected_json


def test_client_get_good_query_with_raise(settings, client):
    settings.ROOT_URLCONF = 'graphene_django.tests.urls'
    response = client.get('/graphql', {'query': '{ human { raises } }'})
    json_response = format_response(response)
    assert json_response['errors'][0]['message'] == 'This field should raise exception'
    assert json_response['data']['human']['raises'] is None


def test_client_post_good_query_json(settings, client):
    settings.ROOT_URLCONF = 'graphene_django.tests.urls'
    response = client.post(
        '/graphql', json.dumps({'query': '{ human { headline } }'}), 'application/json')
    json_response = format_response(response)
    expected_json = {
        'data': {
            'human': {
                'headline': None
            }
        }
    }
    assert json_response == expected_json


def test_client_post_good_query_graphql(settings, client):
    settings.ROOT_URLCONF = 'graphene_django.tests.urls'
    response = client.post(
        '/graphql', '{ human { headline } }', 'application/graphql')
    json_response = format_response(response)
    expected_json = {
        'data': {
            'human': {
                'headline': None
            }
        }
    }
    assert json_response == expected_json
