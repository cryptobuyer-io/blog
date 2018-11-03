from django.utils import translation
LANGUAGE = ''


class SetLanguageFromRequestMiddleware(object):
    def process_request(self, request):
        global LANGUAGE

        language_from_path = translation.get_language_from_path(
            request.path_info
        )

        language_from_request = translation.get_language_from_request(request)

        if language_from_path:
            LANGUAGE = language_from_path
        else:
            LANGUAGE = language_from_request

        return None


class TranslatedField(object):
    def __init__(self, es_field, en_field, pt_field):
        self.es_field = es_field
        self.en_field = en_field
        self.pt_field = pt_field

    def get(self, instance, language):
        es = getattr(instance, self.es_field)
        en = getattr(instance, self.en_field)
        pt = getattr(instance, self.pt_field)

        if language == 'es' or '':
            translated_string = es

        elif language == 'en':
            translated_string = en

        elif language == 'pt':
            translated_string = pt
        else:
            translated_string = es

        return translated_string
