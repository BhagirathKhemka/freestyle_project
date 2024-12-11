from app.tools import convert_to_est 

def test_convert_to_est():
    utc_timestamp = '2024-12-11T15:00:00+0000'
    expected_est = 'December 11, 2024 10:00 AM EST'
    est_timestamp = convert_to_est(utc_timestamp)
    assert est_timestamp == expected_est
