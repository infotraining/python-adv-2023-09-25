import urllib.request
import pytest
from urllib.error import HTTPError
from unittest.mock import patch, MagicMock
from io import BytesIO

class UrlOpenContext:
    pass #TODO: Implement me


def test_UrlOpenContext_happy_path():
    # Test successful request
    with patch('urllib.request.urlopen') as mock_urlopen:
        mock_response = MagicMock()
        mock_response.read.return_value = b'This is a test response'
        mock_urlopen.return_value = mock_response

        with UrlOpenContext('https://www.google.com') as response:
            assert response.read() == b'This is a test response'
            mock_urlopen.assert_called_once_with('https://www.google.com')


def test_UrlOpenContext_sad_path():
    with patch('urllib.request.urlopen') as mock_urlopen:
        mock_urlopen.side_effect = HTTPError(
            url='', code=404, msg='', hdrs='', fp=BytesIO(b''))
        
        with pytest.raises(HTTPError):
            with UrlOpenContext('https://www.google.com') as response:
                pass
