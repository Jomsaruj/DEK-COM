from better_profanity import profanity
import random, string


class Tag:
    __all_tag = []

    @classmethod
    def get_new_tag(cls):
        tag = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        while tag in cls.__all_tag or profanity.contains_profanity(tag):
            tag = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        cls.__all_tag.append(tag)
        return tag


if __name__ == '__main__':
    Tag.get_new_tag('Post')
    print(Tag.all_tag)