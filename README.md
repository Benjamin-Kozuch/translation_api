# Translation API
Provide an API to translate any phrase from any language into english and store the translation


# Endpoints

`/translate/<phrase>`

`/translations/<int:page>/<int:num_items>`

`/translations` (with defaults page:1 and num_items:20)


# Setup

# Usage

```
http://localhost:5000/translate/Hola
{
  "data": "Hello"
}
```
```
http://localhost:5000/translate/שלום
{
  "data": "Hello"
}
```
```
http://localhost:5000/translations
{
  "data": [
    {
      "english_translation": "Hello",
      "original_language": "Hebrew",
      "original_message": "שלום"
    },
    {
      "english_translation": "Hello",
      "original_language": "Spanish",
      "original_message": "Hola"
    }
  ]
}
```

# Translation API

We are using Yandex to detect which language the phrase is in and then another Yandex api to translate the phrase to english

```
Detect language
https://translate.yandex.net/api/v1.5/tr.json/detect
 ? key=<API key>
 & text=<text>
```

```
Translate to another language
https://translate.yandex.net/api/v1.5/tr.json/translate
 ? key=<API key>
 & text=<text to translate>
 & lang=<translation direction>
```


# iso639

This was a useful library to get the Full English Name of a language based off the language code
```
from iso639 import languages
languages.get(alpha2='en').name

---> English
```
