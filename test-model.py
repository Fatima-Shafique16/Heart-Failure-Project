import pickle

model = pickle.load(open("model.pkl", "rb"))
print("MODEL FEATURES:", model.n_features_in_)
