from better_profanity import profanity
import random, string


class IdCode:
    __all_code = []

    @classmethod
    def get_new_tag(cls):
        id_code = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        while id_code in cls.__all_code or profanity.contains_profanity(id_code):
            id_code = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        cls.__all_code.append(id_code)
        return id_code

    @classmethod
    def delete_tag(cls, tag):
        if tag in cls.__all_code:
            cls.__all_code.remove(tag)
