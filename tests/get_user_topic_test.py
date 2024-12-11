import pytest
from unittest.mock import patch
from app.news import get_user_topic

def test_get_user_topic():
    with patch('builtins.input', side_effect=['1', '3', 'technology', '5']):
        topic, keyword, num_headlines, sources = get_user_topic()
        assert topic == 'sports' 
        assert keyword == 'technology'
        assert num_headlines == 5
        assert sources is None
