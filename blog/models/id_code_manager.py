from .id_code import IdCode
from better_profanity import profanity
import random, string



class IdCodeManager:

    @classmethod
    def get_new_id(cls):
        code = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        id_code = IdCode.objects.filter(code=code)
        if id_code:
            return code
        while profanity.contains_profanity(code):
            code = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        IdCode.objects.create(code=code)
        return code

