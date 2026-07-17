import pandas as pd

def test_no_missing_values():
    df = pd.read_csv("WA_Fn-UseC_-HR-Employee-Attrition.csv")
    assert df.isnull().sum().sum() == 0
