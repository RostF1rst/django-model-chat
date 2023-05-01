# Django model chat
Chat with llama.cpp language model created using pyllamacpp and django framework
### Setup
* Download your model (I use [this model](https://huggingface.co/LLukas22/gpt4all-lora-quantized-ggjt/resolve/main/ggjt-model.bin)) and put it in `model_chat/models` (don't forget to change `__path` variable in `model_chat/llama.py` if you use different model than I use)
* Install required modules in terminal: `pip install -r requirements.txt`
* Apply migrations to database: `python manage.py migrate`
* (Optionally) Create superuser: `python manage.py createsuperuser`
* Run test server: `python manage.py runserver`
