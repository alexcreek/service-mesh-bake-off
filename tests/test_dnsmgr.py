from io import StringIO
import pytest
import dnsmgr

class MockClient:
    @staticmethod
    def create_domain_entry(**kwargs):
        domain_created_resp = {}
        return  domain_created_resp

    @staticmethod
    def delete_domain_entry(**kwargs):
        domain_deleted_resp = {}
        return  domain_deleted_resp

def test_creating_a_record(monkeypatch):
    def mock_client(*args):
        return MockClient()

    monkeypatch.setattr(dnsmgr.boto3, 'client', mock_client)

    assert dnsmgr.create_records('json_input')

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
