import pandas as pd

def test_no_missing_values():
    df = pd.read_csv("Employee-Attrition-Performance.csv")
    assert df.isnull().sum().sum() == 0
