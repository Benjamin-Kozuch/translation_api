# Translation API
Provide an API to translate any phrase from any language into english and store the translation

# Setup

#### STEP 1
```
git clone git@github.com:Benjamin-Kozuch/translation_api.git
cd translation_api
python tests.py 
```
(this will work with python 3.5-3.7 although you will see some SQLAlchemy deprecation warnings when running above tests using python3.7)

#### STEP 2
After cloning this repo and running it's tests, set up MySQL database container using the mysql-server:5.7 image
(leave the following out to use the default sqlite db instead)
```
docker run --name mysql -d -e MYSQL_RANDOM_ROOT_PASSWORD=yes -e MYSQL_DATABASE=translation_api_db -e MYSQL_USER=translation_api -e MYSQL_PASSWORD=changethis mysql/mysql-server:5.7
```

#### STEP 3
Create an image of this repo
```
docker build -t translation_api:latest .
```

#### STEP 4
Run a containter using that image
```
docker run --name translation_api -d -p 8080:5000 --rm --link mysql:dbserver -e DATABASE_URL=mysql+pymysql://translation_api:changethis@dbserver/translation_api_db translation_api:latest
```

If STEP 1 was left out then leave out the following from STEP 3: 
`--link mysql:dbserver -e DATABASE_URL=mysql+pymysql://translation_api:<password>@dbserver/translation_api_db` 
an image of this repo

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

# Live Demo
http://ec2-18-237-78-24.us-west-2.compute.amazonaws.com/translate/שלום
http://ec2-18-237-78-24.us-west-2.compute.amazonaws.com/translate/hola
http://ec2-18-237-78-24.us-west-2.compute.amazonaws.com/translations


# Endpoints

`/translate/<phrase>`

`/translations/<int:page>/<int:num_items>`

`/translations` (with defaults page:1 and num_items:20)


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
