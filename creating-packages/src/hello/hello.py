def hello(lang):
    f = {
        "en": hello_en,
        "it": hello_it
    }

    return f.get(lang, hello_en)()


def hello_en():
    return "hello!"


def hello_it():
    return "ciao!"

