

from ..utils import get_model_fields, get_reverse_fields
from .models import Film, Reporter


def test_get_reverse_fields_correct():
    reporter_reverse_fields = get_reverse_fields(Reporter)
    reporter_field_names = [field[0] for field in reporter_reverse_fields]
    assert sorted(reporter_field_names) == [
        'articles', 'films'
    ]

    film_reverse_fields = get_reverse_fields(Film)
    film_field_names = [field[0] for field in film_reverse_fields]
    assert film_field_names == ['details']


def test_get_model_fields_no_duplication():
    reporter_fields = get_model_fields(Reporter)
    reporter_name_set = set([field[0] for field in reporter_fields])
    assert len(reporter_fields) == len(reporter_name_set)

    film_fields = get_model_fields(Film)
    film_name_set = set([field[0] for field in film_fields])
    assert len(film_fields) == len(film_name_set)
