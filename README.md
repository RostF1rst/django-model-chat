# Django model chat
Chat with gpt4all language model created using pyllamacpp and django framework
### Features
There are some features of this project:
* User system: you can log in or register on the site.
* Post system: you can post the response you got.
* Model chat itself: you can chat with language model. (Sometimes it can give meaningless response because of current settings. Waiting for your suggestions)
> :warning: **Prompts to the model are processed locally. Check if your device is suitable for these tasks**
### Setup
* Download your model (I use [this model](https://huggingface.co/LLukas22/gpt4all-lora-quantized-ggjt/resolve/main/ggjt-model.bin)) and put it in `model_chat/models` (don't forget to change `__path` variable in `model_chat/llama.py` if you use different model than I use)
* Install required modules in terminal: `pip install -r requirements.txt`
* Apply migrations to database: `python manage.py migrate`
* Create superuser: `python manage.py createsuperuser` (optional as you can register directly on the site)
* Run test server: `python manage.py runserver`
