import os.path

from pyllamacpp.model import Model

from django_model_chat.settings import BASE_DIR


class LlamaModel:
    __path = os.path.join(BASE_DIR, 'model_chat', 'models', 'ggjt-model.bin')

    def __init__(self):
        self.model = Model(self.__path, seed=0)

    def get_answer(self, prompt='', full_answer=True):
        if not prompt:
            return 'No prompt!'
        form_prompt = 'Prompt: {}\nResponce:'.format(prompt)
        result = self.model.generate(form_prompt)
        if not full_answer:
            result = result.split('Responce:')[-1]
        return result
