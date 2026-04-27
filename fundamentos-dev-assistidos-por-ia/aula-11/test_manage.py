import sys
import os
import pytest
from unittest import mock

import manage

def test_main_sets_django_settings_module(monkeypatch):
    monkeypatch.delenv('DJANGO_SETTINGS_MODULE', raising=False)
    called = {}

    def fake_execute_from_command_line(args):
        called['args'] = args

    monkeypatch.setattr('django.core.management.execute_from_command_line', fake_execute_from_command_line)
    test_argv = ['manage.py', 'runserver']
    monkeypatch.setattr(sys, 'argv', test_argv)
    manage.main()
    assert os.environ['DJANGO_SETTINGS_MODULE'] == 'api.settings'
    assert called['args'] == test_argv

def test_main_importerror(monkeypatch):
    monkeypatch.delenv('DJANGO_SETTINGS_MODULE', raising=False)

    # Simula ImportError ao importar execute_from_command_line
    with mock.patch('django.core.management.execute_from_command_line', side_effect=ImportError("Couldn't import Django")):
        with pytest.raises(ImportError) as excinfo:
            manage.main()
        assert "Couldn't import Django" in str(excinfo.value)
