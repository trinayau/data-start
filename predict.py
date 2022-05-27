import pandas as pd
import pickle
# do not use the filterwarnings in dev environment, but for production!
from warnings import filterwarnings

filterwarnings("ignore")

with open("./output/penguin_model", "rb") as f_obj:
    model = pickle.load(f_obj)

def predict_penguin(penguin):
    X = pd.DataFrame(columns=['culmen_length_mm', 'culmen_depth_mm', 'flipper_length_mm',
       'body_mass_g', 'is_female'])
    X = X.append(penguin, ignore_index=True)
    
    return model.predict(X)[0]


if __name__ == "__main__":
    penguin = {
        "culmen_length_mm": 30,
        "culmen_depth_mm":20,
        "flipper_length_mm": 200,
        "body_mass_g": 4000,
        "is_female": 1
    }
    prediction = predict_penguin(penguin)

    print(prediction)


