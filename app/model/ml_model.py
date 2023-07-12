import pickle
import pandas as pd
from pathlib import Path

__version__ = "0.1.0"

BASE_DIR = Path(__file__).resolve(strict=True).parent


def load_model():
    with open(f"{BASE_DIR}/ml_model-{__version__}.pkl", "rb") as f:
        model = pickle.load(f)
    return model

def preprocess_data(data):
    expected_columns = [
        'LivingSpace', 'Rooms', 'abstellraum', 'bad/wc_getrennt', 'barriefrei', 'dusche', 'elektro', 'erdwaerme',
        'fenster', 'ferne', 'fliesen', 'frei', 'fussbodenheizung', 'gaestewc', 'garage', 'kable_sat_tv',
        'kontrollierte_be-_und_entlueftungsanlage', 'kunststofffenster', 'luftwp', 'parkett', 'personenaufzug',
        'reinigung', 'rollstuhlgerecht', 'speisekammer', 'terrasse', 'wanne', 'zentralheizung', 'ConstructionYear',
        'EstateType_APARTMENT', 'DistributionType_RENT',
        'ZipCode_97070', 'ZipCode_97072', 'ZipCode_97074', 'ZipCode_97076', 'ZipCode_97078', 'ZipCode_97080',
        'ZipCode_97082', 'ZipCode_97084', 'ZipCode_97204', 'ZipCode_97209', 'ZipCode_97218', 'ZipCode_97222',
        'ZipCode_97228', 'ZipCode_97234', 'ZipCode_97236', 'ZipCode_97246', 'ZipCode_97249', 'ZipCode_97250',
        'ZipCode_97261', 'ZipCode_97270', 'ZipCode_97288', 'ZipCode_97297', 'ZipCode_97299'
    ]

    encoded_data = {
        'LivingSpace': data['LivingSpace'],
        'Rooms': data['Rooms'],
        'abstellraum': int(data['abstellraum']),  # Convert 'true'/'false' to 1/0
        'bad/wc_getrennt': int(data['bad/wc_getrennt']),  # Convert 'true'/'false' to 1/0
        'barriefrei': int(data['barriefrei']),  # Convert 'true'/'false' to 1/0
        'dusche': int(data['dusche']),  # Convert 'true'/'false' to 1/0
        'elektro': int(data['elektro']),  # Convert 'true'/'false' to 1/0
        'erdwaerme': int(data['erdwaerme']),  # Convert 'true'/'false' to 1/0
        'fenster': int(data['fenster']),  # Convert 'true'/'false' to 1/0
        'ferne': int(data['ferne']),  # Convert 'true'/'false' to 1/0
        'fliesen': int(data['fliesen']),  # Convert 'true'/'false' to 1/0
        'frei': int(data['frei']),  # Convert 'true'/'false' to 1/0
        'fussbodenheizung': int(data['fussbodenheizung']),  # Convert 'true'/'false' to 1/0
        'gaestewc': int(data['gaestewc']),  # Convert 'true'/'false' to 1/0
        'garage': int(data['garage']),  # Convert 'true'/'false' to 1/0
        'kable_sat_tv': int(data['kable_sat_tv']),  # Convert 'true'/'false' to 1/0
        'kontrollierte_be-_und_entlueftungsanlage': int(data['kontrollierte_be-_und_entlueftungsanlage']),  # Convert 'true'/'false' to 1/0
        'kunststofffenster': int(data['kunststofffenster']),  # Convert 'true'/'false' to 1/0
        'luftwp': int(data['luftwp']),  # Convert 'true'/'false' to 1/0
        'parkett': int(data['parkett']),  # Convert 'true'/'false' to 1/0
        'personenaufzug': int(data['personenaufzug']),  # Convert 'true'/'false' to 1/0
        'reinigung': int(data['reinigung']),  # Convert 'true'/'false' to 1/0
        'rollstuhlgerecht': int(data['rollstuhlgerecht']),  # Convert 'true'/'false' to 1/0
        'speisekammer': int(data['speisekammer']),  # Convert 'true'/'false' to 1/0
        'terrasse': int(data['terrasse']),  # Convert 'true'/'false' to 1/0
        'wanne': int(data['wanne']),  # Convert 'true'/'false' to 1/0
        'zentralheizung': int(data['zentralheizung']),  # Convert 'true'/'false' to 1/0
        'ConstructionYear': data['ConstructionYear'],
        'EstateType_APARTMENT': int(data['EstateType_APARTMENT']),  # Convert 'true'/'false' to 1/0
        'DistributionType_RENT': int(data['DistributionType_RENT']),  # Convert 'true'/'false' to 1/0
    }

    zip_code_key = 'ZipCode_' + data['ZipCode']
    for column in expected_columns:
        if column == zip_code_key:
            encoded_data[column] = 1
        else:
            encoded_data[column] = 0

    return encoded_data

def predict(data):
    with open("model/model.pkl", "rb") as f:
        model = pickle.load(f)
    data = preprocess_data(data)
    df = pd.DataFrame(data, index=[0])
    result = model.predict(df)[0]
    return round(result, 2)