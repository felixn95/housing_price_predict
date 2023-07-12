import gradio as gr
import requests

# Define the prediction function
def predict_housing_price(
    living_space, rooms, abstellraum, bad_wc_getrennt, barriefrei, dusche, elektro, erdwaerme, fenster,
    ferne, fliesen, frei, fussbodenheizung, gaestewc, garage, kable_sat_tv, kontrollierte_be_entlueftungsanlage,
    kunststofffenster, luftwp, parkett, personenaufzug, reinigung, rollstuhlgerecht, speisekammer, terrasse,
    wanne, zentralheizung, construction_year, estate_type_apartment, distribution_type_rent, zip_code
):
    # Prepare the data dictionary
    data = {
        "LivingSpace": living_space,
        "Rooms": rooms,
        "abstellraum": abstellraum,
        "bad/wc_getrennt": bad_wc_getrennt,
        "barriefrei": barriefrei,
        "dusche": dusche,
        "elektro": elektro,
        "erdwaerme": erdwaerme,
        "fenster": fenster,
        "ferne": ferne,
        "fliesen": fliesen,
        "frei": frei,
        "fussbodenheizung": fussbodenheizung,
        "gaestewc": gaestewc,
        "garage": garage,
        "kable_sat_tv": kable_sat_tv,
        "kontrollierte_be-/entlueftungsanlage": kontrollierte_be_entlueftungsanlage,
        "kunststofffenster": kunststofffenster,
        "luftwp": luftwp,
        "parkett": parkett,
        "personenaufzug": personenaufzug,
        "reinigung": reinigung,
        "rollstuhlgerecht": rollstuhlgerecht,
        "speisekammer": speisekammer,
        "terrasse": terrasse,
        "wanne": wanne,
        "zentralheizung": zentralheizung
        "ConstructionYear": construction_year,
        "EstateType_APARTMENT": estate_type_apartment,
        "DistributionType_RENT": distribution_type_rent,
        "ZipCode": zip_code,
    }

    print(data)

    # Send a POST request to the /predict endpoint
    response = requests.post("http://localhost:8000/predict", json=data)

    # Parse the response
    result = response.json()["result"]

    return result

# Define the Gradio interface
iface = gr.Interface(
    fn=predict_housing_price,
    inputs=[
        gr.inputs.Group(
            "Property Details",
            [
                gr.inputs.Slider(minimum=0, maximum=1000, step=1, label="Living Space (sqm)"),
                gr.inputs.Slider(minimum=0, maximum=15, step=1, label="Number of Rooms"),
                gr.inputs.Checkbox(label="Abstellraum"),
                gr.inputs.Checkbox(label="Bad/WC Getrennt"),
                gr.inputs.Checkbox(label="Barriefrei"),
                gr.inputs.Checkbox(label="Dusche"),
                gr.inputs.Checkbox(label="Elektro"),
                gr.inputs.Checkbox(label="Erdwaerme"),
                gr.inputs.Checkbox(label="Fenster"),
                gr.inputs.Checkbox(label="Ferne"),
                gr.inputs.Checkbox(label="Fliesen"),
                gr.inputs.Checkbox(label="Frei"),
                gr.inputs.Checkbox(label="Fussbodenheizung"),
                gr.inputs.Checkbox(label="Gaestewc"),
                gr.inputs.Checkbox(label="Garage"),
                gr.inputs.Checkbox(label="Kabel/Sat TV"),
                gr.inputs.Checkbox(label="Kontrollierte Be-/Entlueftungsanlage"),
                gr.inputs.Checkbox(label="Kunststofffenster"),
                gr.inputs.Checkbox(label="Luftwp"),
                gr.inputs.Checkbox(label="Parkett"),
                gr.inputs.Checkbox(label="Personenaufzug"),
                gr.inputs.Checkbox(label="Reinigung"),
                gr.inputs.Checkbox(label="Rollstuhlgerecht"),
                gr.inputs.Checkbox(label="Speisekammer"),
                gr.inputs.Checkbox(label="Terrasse"),
                gr.inputs.Checkbox(label="Wanne"),
                gr.inputs.Checkbox(label="Zentralheizung"),
            ],
        ),
        gr.inputs.Group(
            "Additional Information",
            [
                gr.inputs.Slider(minimum=1900, maximum=2023, step=1, label="Construction Year"),
                gr.inputs.Checkbox(label="Estate Type: Apartment"),
                gr.inputs.Checkbox(label="Distribution Type: Rent"),
                gr.inputs.Textbox(label="Zip Code"),
            ],
        ),
    ],
    outputs=gr.outputs.Textbox(label="Prediction Result"),
    title="Housing Price Prediction",
    description="Enter the required data to predict the housing price.",
)

# Run the Gradio interface
iface.launch(share=True)
