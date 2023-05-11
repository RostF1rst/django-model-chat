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
        form_prompt = 'Prompt: {}\nResponse that is fully reasoned and justified and fully satisfies the prompt:'.\
            format(prompt)
        result = self.model.generate(form_prompt, n_predict=256)
        if not full_answer:
            result = result.split('Response that is fully reasoned and justified and fully satisfies the prompt:')[-1]
            while result.startswith('\n'):
                result = result.replace('\n', '', 1)
        print(result)
        return result
