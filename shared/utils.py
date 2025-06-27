from functools import wraps
import json
import allure


ALLURE_SUIT_TITLE = "Bitnami Opencart Eshop Tests"


def allure_annotation_fabric(feature: str, suite: str = ALLURE_SUIT_TITLE):
    """Decorators fabric for allure annotations"""

    def wrapper(title: str, description: str = None, story: str = None):
        return allure_annotation(suite, feature, title, description, story)

    return wrapper


def allure_annotation(
    suite: str, feature: str, title: str, description: str = None, story: str = None
):
    """Decorator for allure annotations"""

    def decorator(test_func):
        decorated = allure.suite(suite)(test_func)
        decorated = allure.feature(feature)(decorated)
        decorated = allure.title(title)(decorated)
        if description:
            decorated = allure.description(description)(decorated)
        if story:
            decorated = allure.story(story)(decorated)

        @wraps(decorated)
        def wrapper(*args, **kwargs):
            return decorated(*args, **kwargs)

        return wrapper

    return decorator
