from io import StringIO
import pytest
import dnsmgr

def test_creating_a_record():
    assert False

def test_updating_a_record():
    assert False

def test_deleting_a_record():
    assert False

def test_reading_json_from_a_pipe(monkeypatch):
    monkeypatch.setattr('sys.argv', [])
    monkeypatch.setattr('sys.stdin', StringIO('{"asdf": 123}\n'))
    assert dnsmgr.collect_input() == {'asdf': 123}

def test_zone_not_found():
    assert False

def test_invalid_creds():
    assert False
