# Postgraduates backend service

Welcome to the postgraduates backend service. This is a `django` project. To install `django` for a unix filesystem just run `pip3 install django`. If youre on a windows machine and dont have [wsl](https://docs.microsoft.com/en-us/windows/wsl/install-win10) then refer to [django documentation](https://docs.djangoproject.com/en/2.2/howto/windows/).

## Running the server

In order to run the server just run `python3 manage.py runserver` in the root directory of the repo. This will start the server on `localhost:8000`. Your console will probably be filled with a lot of output. Most of it is just the `scrapy_service` running, which has a few preconditions for it to work properly. The following are:

 - The file `careers.json` under the folder `postgraduates_backend/scrapy_service/spiders/` **must only contain** the following json. (Consider this when shutting down/restarting the server)
 ```
 {
     "careers": []
 }
 ```

 - Also, the spiders must be run on the following order (only take notice of this if you feel like changing the `__init__.py` file)
    1. Um
    2. Ort

Please refer all your concerns about the `scrapy_service` to [the original repo](https://github.com/pazcuturi/webir).

## Endpoints

So far the project only counts with 2 endpoints.

1. `GET /postgraduates/show` returns a json with all the info gathered by the spiders
2. `GETH /postgraduates/` returns a friendly reminder (html) where to get the desired json.

