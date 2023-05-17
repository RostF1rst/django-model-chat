import os.path

from pyllamacpp.model import Model

from django_model_chat.settings import BASE_DIR


class LlamaModel:
    __path = os.path.join(BASE_DIR, 'model_chat', 'models', 'ggjt-model.bin')
    __prefix = 'Prompt: '
    __suffix = '\nResponse that is fully reasoned and justified and fully satisfies the prompt:'

    def __init__(self):
        self.model = Model(self.__path, prompt_prefix=self.__prefix, prompt_suffix=self.__suffix)

    def get_answer(self, prompt=''):
        if not prompt:
            return 'No prompt!'
        result = ""
        for i in self.model.generate(prompt):
            result += i
            print(i, end='')
        return result
