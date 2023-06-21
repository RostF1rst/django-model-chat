#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import warnings


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_model_chat.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    try:
        model_path_listdir = os.listdir('./model_chat/models')
    except FileNotFoundError:
        warnings.warn('Path "./model_chat/models" doesn\'t exist!')
    else:
        if model_path_listdir:
            if not any(i.endswith('.bin') for i in model_path_listdir):
                warnings.warn("Model should be a .bin file")
        else:
            warnings.warn("Put model in '/model_chat/models' directory")

    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
