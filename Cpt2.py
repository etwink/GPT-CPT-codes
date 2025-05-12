import json

# Full CPT Category I code groupings based on AMA structure
full_cpt_category_I = {
    "Evaluation and Management (E/M)": {
        "code_range": ["99202", "99499"],
        "subcategories": {
            "Office or outpatient visits": ["99202", "99215"],
            "Hospital inpatient services": ["99221", "99239"],
            "Emergency department services": ["99281", "99288"],
            "Consultations": ["99241", "99255"],
            "Home and domiciliary visits": ["99341", "99350"],
            "Preventive medicine": ["99381", "99429"],
            "Care management & coordination": ["99487", "99490"],
            "Telehealth & digital services": ["99421", "99443"]
        }
    },
    "Anesthesia": {
        "code_range": ["00100", "01999"],
        "subcategories": {
            "Head, neck, spine, thorax": ["00100", "01933"],
            "Obstetric procedures": ["01958", "01969"],
            "Radiologic procedures": ["01916", "01933"],
            "Burn excision/debridement": ["01951", "01953"]
        },
        "add_on_codes": {
            "Qualifying circumstances": ["99100", "99140"]
        }
    },
    "Surgery": {
        "code_range": ["10021", "69990"],
        "subcategories": {
            "Integumentary System": ["10021", "11983"],
            "Musculoskeletal System": ["20005", "29999"],
            "Respiratory System": ["30000", "32999"],
            "Cardiovascular System": ["33010", "37799"],
            "Digestive System": ["40490", "49999"],
            "Urinary System": ["50010", "53899"],
            "Male Genital System": ["54000", "55899"],
            "Female Genital System": ["56405", "58999"],
            "Nervous System": ["61000", "64999"],
            "Eye and Ocular Adnexa": ["65091", "68899"],
            "Auditory System": ["69000", "69990"]
        }
    },
    "Radiology": {
        "code_range": ["70010", "79999"],
        "subcategories": {
            "Diagnostic Radiology (X-ray, Fluoroscopy)": ["70010", "76499"],
            "Diagnostic Ultrasound": ["76506", "76999"],
            "Radiologic Guidance": ["77001", "77022"],
            "Breast, Bone Density, and Other": ["77046", "77089"],
            "CT and CTA": ["70450", "70498"],
            "MRI and MRA": ["70540", "70559"],
            "Nuclear Medicine": ["78012", "78999"],
            "Radiation Oncology": ["77261", "77799"]
        }
    },
    "Pathology and Laboratory": {
        "code_range": ["80047", "89398"],
        "subcategories": {
            "Organ/Disease-Oriented Panels": ["80047", "80081"],
            "Drug Assay": ["80150", "80299"],
            "Chemistry": ["82000", "84999"],
            "Hematology and Coagulation": ["85002", "85999"],
            "Immunology": ["86000", "86849"],
            "Transfusion Medicine": ["86850", "86999"],
            "Microbiology": ["87003", "87999"],
            "Anatomic Pathology": ["88000", "88099"],
            "Cytopathology": ["88104", "88199"],
            "Surgical Pathology": ["88300", "88399"],
            "Genetic/Molecular Pathology": ["81200", "81479"],
            "Other Pathology Services": ["89049", "89398"]
        }
    },
    "Medicine": {
        "code_range": ["90281", "99607"],
        "subcategories": {
            "Immunization Administration": ["90460", "90759"],
            "Vaccines, Toxoids": ["90281", "90399"],
            "Psychiatric Services": ["90785", "90899"],
            "Biofeedback": ["90901", "90911"],
            "Dialysis": ["90935", "90999"],
            "Gastroenterology": ["91010", "91299"],
            "Cardiovascular": ["93000", "93799"],
            "Pulmonary": ["94002", "94799"],
            "Neurology and Neuromuscular": ["95800", "96020"],
            "Health and Behavior Assessment": ["96105", "96171"],
            "Ophthalmology": ["92002", "92499"],
            "Special Services, Procedures and Reports": ["99000", "99091"],
            "Home Health Procedures/Services": ["99500", "99607"],
            "Physical Medicine and Rehabilitation": ["97010", "97799"],
            "Chiropractic Manipulative Treatment": ["98940", "98943"],
            "Acupuncture": ["97810", "97814"]
        }
    }
}

# Save to JSON file
full_schema_path = "/mnt/data/full_cpt_category_I_schema.json"
with open(full_schema_path, "w") as file:
    json.dump(full_cpt_category_I, file, indent=4)

full_schema_path
