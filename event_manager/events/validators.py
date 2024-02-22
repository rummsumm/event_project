from django.core.exceptions import ValidationError
from django.utils import timezone
from functools import partial


def datetime_in_future(value) -> None:
    """Wenn das Datum in der Vergangenheit liegt, erhebe einen Validation Error."""
    if value < timezone.now():
        raise ValidationError("Das Datum des Termins darf nicht in der Vergangenheit liegen!")
    

def bad_word_filter(word_list: list[str], value):
    for word in value.split():
        if word in word_list:
            raise ValidationError(f"Dieses Wort ist nicht erlaubt: {word}")



# def fn(a, b):
#     print("das ist der Aufruf:", a, b)


# word_list_error = partial(fn, "a1")
# print(word_list_error)

# word_list_error("b2")