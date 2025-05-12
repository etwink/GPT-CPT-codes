import json

# Detailed CPT code groupings
cpt_groupings = {
    "Evaluation and Management": {
        "code_range": "99202–99499",
        "subcategories": {
            "Office or outpatient visits": "99202–99215",
            "Hospital inpatient services": "99221–99239",
            "Emergency department services": "99281–99288",
            "Consultations": "99241–99255",
            "Home and domiciliary visits": "99341–99350",
            "Preventive medicine": "99381–99429",
            "Care management & coordination": "99487–99490",
            "Telehealth & digital services": "99421–99443"
        }
    },
    "Anesthesia": {
        "code_range": "00100–01999, 99100–99140",
        "subcategories": {
            "Head, neck, spine, thorax": "00100–01933",
            "Obstetric procedures": "01958–01969",
            "Radiologic procedures": "01916–01933",
            "Burn excision/debridement": "01951–01953",
            "Anesthesia add-ons & modifiers": "99100–99140"
        }
    },
    "Surgery": {
        "Integumentary System": "10021–11983",
        "Musculoskeletal System": "20005–29999",
        "Respiratory System": "30000–32999",
        "Cardiovascular System": "33010–37799",
        "Digestive System": "40490–49999",
        "Urinary System": "50010–53899",
        "Male Genital System": "54000–55899",
        "Female Genital System": "56405–58999",
        "Nervous System": "61000–64999"
    },
    "Radiology": {
        "code_range": "70010–79999",
        "subcategories": {
            "X-rays and fluoroscopy": "70010–76499",
            "CT scans": "70450–70498, 71250–71275",
            "MRI": "70540–70559, 72141–72158",
            "Ultrasound": "76506–76999",
            "Nuclear medicine": "78012–78999",
            "Radiation oncology": "77261–77799"
        }
    },
    "Pathology and Laboratory": {
        "code_range": "80047–89398",
        "subcategories": {
            "Organ/disease panels": "80047–80081",
            "Drug testing/toxicology": "80305–80377",
            "Hematology": "85002–85999",
            "Microbiology": "87003–87999",
            "Surgical pathology": "88300–88399",
            "Genetic & molecular pathology": "81200–81479"
        }
    },
    "Medicine": {
        "code_range": "90281–99607",
        "subcategories": {
            "Immunizations": "90460–90759",
            "Psychiatric services": "90785–90899",
            "Dialysis": "90935–90999",
            "Cardiovascular testing": "93000–93799",
            "Pulmonary testing": "94002–94799",
            "Gastrointestinal procedures": "91010–91299",
            "Physical and occupational therapy": "97010–97799",
            "Chiropractic": "98940–98943",
            "Ophthalmologic procedures": "92002–92499"
        }
    }
}

# Save to JSON file
output_path = "/mnt/data/detailed_cpt_groupings.json"
with open(output_path, "w") as file:
    json.dump(cpt_groupings, file, indent=4)

output_path
