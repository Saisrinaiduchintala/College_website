from pymongo import MongoClient
from pymongo.server_api import ServerApi

import os
from dotenv import load_dotenv

load_dotenv()

# MongoDB connection
uri = os.getenv("MONGODB_URI")

client = MongoClient(uri, server_api=ServerApi("1"))

db = client["College"]
collection = db["syllabus"]


semester_1 = [

    {
        "semester": 1,
        "subject_code": "M110D",
        "subject_name": "Engineering Chemistry",

        "modules": [

            {
                "module": 1,
                "title": "Water and Its Treatment",
                "topics": [
                    {
                        "topic": "Hardness of Water",
                        "subtopics": [
                            "Introduction",
                            "Causes of hardness",
                            "Types of hardness",
                            "Temporary hardness",
                            "Permanent hardness",
                            "Units of hardness of water",
                            "Numerical problems",
                            "Estimation of hardness by complexometric method"
                        ]
                    },
                    {
                        "topic": "Boiler Troubles",
                        "subtopics": [
                            "Scale",
                            "Sludge",
                            "Causes and effects"
                        ]
                    },
                    {
                        "topic": "Water Treatment",
                        "subtopics": [
                            "Potable water",
                            "Industrial water specifications",
                            "Calgon conditioning",
                            "Phosphate conditioning",
                            "Colloidal conditioning",
                            "Ion exchange process",
                            "Reverse osmosis"
                        ]
                    },
                    {
                        "topic": "Potable Water Treatment",
                        "subtopics": [
                            "Steps involved in potable water treatment",
                            "Chlorination",
                            "Breakpoint chlorination",
                            "Ozonization"
                        ]
                    }
                ]
            },

            {
                "module": 2,
                "title": "Battery and Corrosion",
                "topics": [
                    {
                        "topic": "Batteries",
                        "subtopics": [
                            "Introduction",
                            "Classification of batteries",
                            "Primary batteries",
                            "Li-MnO2 cell",
                            "Secondary batteries",
                            "Lithium ion battery",
                            "Applications"
                        ]
                    },
                    {
                        "topic": "Fuel Cells",
                        "subtopics": [
                            "Methanol-oxygen fuel cell",
                            "Engineering applications"
                        ]
                    },
                    {
                        "topic": "Solar Cells",
                        "subtopics": [
                            "Principle",
                            "Applications"
                        ]
                    },
                    {
                        "topic": "Corrosion",
                        "subtopics": [
                            "Causes and effects",
                            "Chemical corrosion",
                            "Electrochemical corrosion",
                            "Hydrogen evolution mechanism",
                            "Galvanic corrosion",
                            "Waterline corrosion",
                            "Factors influencing rate of corrosion",
                            "Cathodic protection",
                            "Sacrificial anodic method",
                            "Impressed current cathodic method",
                            "Hot dipping",
                            "Galvanizing",
                            "Tinning"
                        ]
                    }
                ]
            },

            {
                "module": 3,
                "title": "Chemical Fuels",
                "topics": [
                    {
                        "topic": "Fuels",
                        "subtopics": [
                            "Definition",
                            "Classification",
                            "Characteristics of a good fuel",
                            "Calorific value",
                            "Calculation using Dulong's formula",
                            "Numerical problems"
                        ]
                    },
                    {
                        "topic": "Coal",
                        "subtopics": [
                            "Composition",
                            "Proximate analysis",
                            "Ultimate analysis",
                            "Significance"
                        ]
                    },
                    {
                        "topic": "Liquid Fuels",
                        "subtopics": [
                            "Gasoline and its composition",
                            "Cracking",
                            "Fixed bed catalytic cracking",
                            "Knocking",
                            "Anti-knocking agents",
                            "Octane number",
                            "Cetane number"
                        ]
                    },
                    {
                        "topic": "Gaseous Fuels",
                        "subtopics": [
                            "Natural gas",
                            "LPG",
                            "CNG",
                            "Composition",
                            "Characteristics",
                            "Applications"
                        ]
                    }
                ]
            },

            {
                "module": 4,
                "title": "Polymers",
                "topics": [
                    {
                        "topic": "Polymers",
                        "subtopics": [
                            "Definition",
                            "Monomer",
                            "Polymer",
                            "Polymerization",
                            "Addition polymerization",
                            "Condensation polymerization"
                        ]
                    },
                    {
                        "topic": "Plastics",
                        "subtopics": [
                            "Thermoplastics",
                            "Thermosetting plastics",
                            "Compounding",
                            "Compression moulding",
                            "Injection moulding",
                            "PVC",
                            "Urea-formaldehyde"
                        ]
                    },
                    {
                        "topic": "Fibers",
                        "subtopics": [
                            "Nylon-6,6",
                            "Preparation",
                            "Properties",
                            "Engineering applications"
                        ]
                    },
                    {
                        "topic": "Conducting Polymers",
                        "subtopics": [
                            "Definition",
                            "Classification",
                            "Applications"
                        ]
                    }
                ]
            },

            {
                "module": 5,
                "title": "Engineering Materials and Drugs",
                "topics": [
                    {
                        "topic": "Nanomaterials",
                        "subtopics": [
                            "Introduction",
                            "Sol-gel method",
                            "General applications",
                            "Carbon nanotubes",
                            "Properties of carbon nanotubes",
                            "Applications of carbon nanotubes"
                        ]
                    },
                    {
                        "topic": "Portland Cement",
                        "subtopics": [
                            "Chemical constituents",
                            "Manufacturing",
                            "Setting",
                            "Hardening",
                            "Applications"
                        ]
                    },
                    {
                        "topic": "Drugs",
                        "subtopics": [
                            "Antipyretics",
                            "Paracetamol",
                            "Medicinal applications"
                        ]
                    }
                ]
            }
        ]
    }
]


# Insert / replace Semester I syllabus
for subject in semester_1:

    collection.replace_one(
        {
            "semester": subject["semester"],
            "subject_code": subject["subject_code"]
        },
        subject,
        upsert=True
    )

print("Semester I syllabus inserted successfully!")