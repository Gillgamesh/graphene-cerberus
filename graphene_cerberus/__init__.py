from functools import wraps

from cerberus import Validator
from graphql import GraphQLError


def validate_input(validator: Validator,
                   enforce_allow_unknown: bool = True,
                   auto_camelcase: bool = True,
                   extensions_param_name: str = 'invalidArgs',
                   error_message: str =
                   'Invalid Arguments Provided by Client!'
                   ):
    """Wraps mutate calls and validates input before running."""
    def decorator(f):
        @wraps(f)
        def check_and_call(*args, **kwargs):
            if (not validator.allow_unknown and
                    enforce_allow_unknown):
                validator.allow_unknown = True
            if (not validator.validate(kwargs)):
                errors = validator.errors
                if (auto_camelcase):
                    errors = {
                        to_camel_case(key): value
                        for key, value in errors.items()
                    }

                raise GraphQLError(
                    error_message,
                    extensions={extensions_param_name: errors}
                )
            return f(*args, **kwargs)

        return check_and_call
    return decorator


def to_camel_case(snake: str) -> str:
    words = snake.split('_')
    if len(words) <= 1:
        return snake
    return (words[0]).join(
        word.title() for word in words[1:])
