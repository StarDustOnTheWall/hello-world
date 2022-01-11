from sklearn.datasets import fetch_openml
import dill

with open(f"test-data.pkl", 'rb') as pickle_file:
    df = dill.load(pickle_file)