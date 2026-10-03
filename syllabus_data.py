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

    # =========================================================
    # M110A - MATRICES AND CALCULUS
    # =========================================================

    {
        "semester": 1,
        "subject_code": "M110A",
        "subject_name": "Matrices and Calculus",
        "modules": [
            {
                "module": 1,
                "title": "Matrices",
                "topics": [
                    {
                        "topic": "Matrices",
                        "subtopics": [
                            "Rank of a matrix",
                            "Echelon form",
                            "Normal form",
                            "Consistency of linear systems",
                            "Gauss elimination method",
                            "Gauss-Jordan method",
                            "Eigenvalues",
                            "Eigenvectors",
                            "Cayley-Hamilton theorem",
                            "Inverse using Cayley-Hamilton theorem"
                        ]
                    }
                ]
            },
            {
                "module": 2,
                "title": "Differential Calculus",
                "topics": [
                    {
                        "topic": "Functions of Several Variables",
                        "subtopics": [
                            "Partial derivatives",
                            "Total derivatives",
                            "Chain rule",
                            "Jacobian"
                        ]
                    },
                    {
                        "topic": "Maxima and Minima",
                        "subtopics": [
                            "Maxima",
                            "Minima",
                            "Functions of two variables",
                            "Lagrange multipliers"
                        ]
                    }
                ]
            },
            {
                "module": 3,
                "title": "Integral Calculus",
                "topics": [
                    {
                        "topic": "Multiple Integrals",
                        "subtopics": [
                            "Double integrals",
                            "Change of order of integration",
                            "Change of variables",
                            "Triple integrals",
                            "Applications of multiple integrals"
                        ]
                    }
                ]
            },
            {
                "module": 4,
                "title": "Sequences and Series",
                "topics": [
                    {
                        "topic": "Sequences",
                        "subtopics": [
                            "Convergence of sequences",
                            "Monotonic sequences",
                            "Bounded sequences"
                        ]
                    },
                    {
                        "topic": "Series",
                        "subtopics": [
                            "Convergence of series",
                            "Comparison test",
                            "Ratio test",
                            "Root test",
                            "Alternating series"
                        ]
                    }
                ]
            },
            {
                "module": 5,
                "title": "Fourier Series",
                "topics": [
                    {
                        "topic": "Fourier Series",
                        "subtopics": [
                            "Fourier series",
                            "Dirichlet conditions",
                            "Fourier coefficients",
                            "Even and odd functions",
                            "Half-range Fourier series",
                            "Parseval's identity"
                        ]
                    }
                ]
            }
        ]
    },


    # =========================================================
    # M110B - ENGINEERING PHYSICS
    # =========================================================

    {
        "semester": 1,
        "subject_code": "M110B",
        "subject_name": "Engineering Physics",
        "modules": [
            {
                "module": 1,
                "title": "Wave Optics",
                "topics": [
                    {
                        "topic": "Interference",
                        "subtopics": [
                            "Principle of superposition",
                            "Coherent sources",
                            "Young's double slit experiment",
                            "Interference in thin films",
                            "Newton's rings"
                        ]
                    },
                    {
                        "topic": "Diffraction",
                        "subtopics": [
                            "Single slit diffraction",
                            "Diffraction grating",
                            "Resolving power"
                        ]
                    }
                ]
            },
            {
                "module": 2,
                "title": "Quantum Physics",
                "topics": [
                    {
                        "topic": "Quantum Mechanics",
                        "subtopics": [
                            "Black body radiation",
                            "Planck's quantum theory",
                            "Photoelectric effect",
                            "Compton effect",
                            "de Broglie hypothesis",
                            "Heisenberg uncertainty principle"
                        ]
                    }
                ]
            },
            {
                "module": 3,
                "title": "Semiconductor Physics",
                "topics": [
                    {
                        "topic": "Semiconductors",
                        "subtopics": [
                            "Intrinsic semiconductors",
                            "Extrinsic semiconductors",
                            "Fermi level",
                            "Carrier concentration",
                            "Hall effect"
                        ]
                    }
                ]
            },
            {
                "module": 4,
                "title": "Magnetic and Dielectric Materials",
                "topics": [
                    {
                        "topic": "Magnetic Materials",
                        "subtopics": [
                            "Diamagnetism",
                            "Paramagnetism",
                            "Ferromagnetism",
                            "Antiferromagnetism",
                            "Ferrimagnetism",
                            "Hysteresis"
                        ]
                    },
                    {
                        "topic": "Dielectric Materials",
                        "subtopics": [
                            "Polarization",
                            "Electronic polarization",
                            "Ionic polarization",
                            "Orientation polarization",
                            "Dielectric constant",
                            "Applications"
                        ]
                    }
                ]
            },
            {
                "module": 5,
                "title": "Nanotechnology",
                "topics": [
                    {
                        "topic": "Nanomaterials",
                        "subtopics": [
                            "Introduction",
                            "Properties of nanomaterials",
                            "Top-down approach",
                            "Bottom-up approach",
                            "Applications of nanomaterials"
                        ]
                    }
                ]
            }
        ]
    },


    # =========================================================
    # M110C - PROGRAMMING FOR PROBLEM SOLVING
    # =========================================================

    {
        "semester": 1,
        "subject_code": "M110C",
        "subject_name": "Programming for Problem Solving",
        "modules": [
            {
                "module": 1,
                "title": "Introduction to Programming",
                "topics": [
                    {
                        "topic": "Programming Fundamentals",
                        "subtopics": [
                            "Problem solving",
                            "Algorithms",
                            "Flowcharts",
                            "Program development process",
                            "Structure of a C program",
                            "Variables",
                            "Constants",
                            "Data types",
                            "Operators"
                        ]
                    }
                ]
            },
            {
                "module": 2,
                "title": "Control Structures",
                "topics": [
                    {
                        "topic": "Decision Making",
                        "subtopics": [
                            "if statement",
                            "if-else statement",
                            "Nested if",
                            "Switch statement"
                        ]
                    },
                    {
                        "topic": "Looping",
                        "subtopics": [
                            "while loop",
                            "do-while loop",
                            "for loop",
                            "Nested loops",
                            "Break",
                            "Continue"
                        ]
                    }
                ]
            },
            {
                "module": 3,
                "title": "Arrays and Strings",
                "topics": [
                    {
                        "topic": "Arrays",
                        "subtopics": [
                            "One-dimensional arrays",
                            "Two-dimensional arrays",
                            "Multidimensional arrays",
                            "Array operations"
                        ]
                    },
                    {
                        "topic": "Strings",
                        "subtopics": [
                            "String declaration",
                            "String input and output",
                            "String handling functions",
                            "String operations"
                        ]
                    }
                ]
            },
            {
                "module": 4,
                "title": "Functions and Pointers",
                "topics": [
                    {
                        "topic": "Functions",
                        "subtopics": [
                            "Function declaration",
                            "Function definition",
                            "Function calls",
                            "Parameter passing",
                            "Recursion"
                        ]
                    },
                    {
                        "topic": "Pointers",
                        "subtopics": [
                            "Pointer variables",
                            "Pointer operators",
                            "Pointers and arrays",
                            "Pointers and functions"
                        ]
                    }
                ]
            },
            {
                "module": 5,
                "title": "Structures and Files",
                "topics": [
                    {
                        "topic": "Structures and Unions",
                        "subtopics": [
                            "Structure declaration",
                            "Structure initialization",
                            "Array of structures",
                            "Nested structures",
                            "Unions"
                        ]
                    },
                    {
                        "topic": "File Handling",
                        "subtopics": [
                            "File opening",
                            "File closing",
                            "Reading files",
                            "Writing files",
                            "File handling functions"
                        ]
                    }
                ]
            }
        ]
    },


    # =========================================================
    # M113A - ENGLISH FOR SKILL DEVELOPMENT
    # =========================================================

    {
        "semester": 1,
        "subject_code": "M113A",
        "subject_name": "English for Skill Development",
        "modules": [
            {
                "module": 1,
                "title": "Language Skills",
                "topics": [
                    {
                        "topic": "Communication",
                        "subtopics": [
                            "Listening skills",
                            "Speaking skills",
                            "Reading skills",
                            "Writing skills"
                        ]
                    }
                ]
            },
            {
                "module": 2,
                "title": "Grammar",
                "topics": [
                    {
                        "topic": "Grammar Fundamentals",
                        "subtopics": [
                            "Parts of speech",
                            "Tenses",
                            "Articles",
                            "Prepositions",
                            "Subject-verb agreement"
                        ]
                    }
                ]
            },
            {
                "module": 3,
                "title": "Vocabulary",
                "topics": [
                    {
                        "topic": "Vocabulary Development",
                        "subtopics": [
                            "Synonyms",
                            "Antonyms",
                            "Word formation",
                            "Idioms and phrases"
                        ]
                    }
                ]
            },
            {
                "module": 4,
                "title": "Writing Skills",
                "topics": [
                    {
                        "topic": "Professional Writing",
                        "subtopics": [
                            "Paragraph writing",
                            "Letter writing",
                            "Email writing",
                            "Report writing"
                        ]
                    }
                ]
            },
            {
                "module": 5,
                "title": "Presentation Skills",
                "topics": [
                    {
                        "topic": "Presentation",
                        "subtopics": [
                            "Presentation techniques",
                            "Group discussions",
                            "Public speaking",
                            "Interview skills"
                        ]
                    }
                ]
            }
        ]
    },


    # =========================================================
    # M110D - ENGINEERING CHEMISTRY
    # =========================================================

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
    },


    # =========================================================
    # M112A - BASIC ELECTRICAL ENGINEERING
    # =========================================================

    {
        "semester": 1,
        "subject_code": "M112A",
        "subject_name": "Basic Electrical Engineering",
        "modules": [
            {
                "module": 1,
                "title": "DC Circuits",
                "topics": [
                    {
                        "topic": "Basic Concepts",
                        "subtopics": [
                            "Voltage",
                            "Current",
                            "Power",
                            "Energy",
                            "Ohm's law",
                            "Kirchhoff's laws"
                        ]
                    }
                ]
            },
            {
                "module": 2,
                "title": "AC Circuits",
                "topics": [
                    {
                        "topic": "Alternating Current",
                        "subtopics": [
                            "RMS value",
                            "Average value",
                            "Phase",
                            "Power factor",
                            "RLC circuits",
                            "Resonance"
                        ]
                    }
                ]
            },
            {
                "module": 3,
                "title": "Transformers",
                "topics": [
                    {
                        "topic": "Single Phase Transformer",
                        "subtopics": [
                            "Construction",
                            "Working principle",
                            "EMF equation",
                            "Losses",
                            "Efficiency",
                            "Applications"
                        ]
                    }
                ]
            },
            {
                "module": 4,
                "title": "Electrical Machines",
                "topics": [
                    {
                        "topic": "DC Machines",
                        "subtopics": [
                            "Construction",
                            "Working principle",
                            "DC generator",
                            "DC motor",
                            "Applications"
                        ]
                    },
                    {
                        "topic": "Induction Motors",
                        "subtopics": [
                            "Construction",
                            "Working principle",
                            "Three phase induction motor",
                            "Applications"
                        ]
                    }
                ]
            },
            {
                "module": 5,
                "title": "Electrical Installations",
                "topics": [
                    {
                        "topic": "Electrical Safety",
                        "subtopics": [
                            "Earthing",
                            "Fuses",
                            "MCB",
                            "MCCB",
                            "Electrical safety practices"
                        ]
                    }
                ]
            }
        ]
    },


    # =========================================================
    # M114A - ENGINEERING GRAPHICS
    # =========================================================

    {
        "semester": 1,
        "subject_code": "M114A",
        "subject_name": "Engineering Graphics",
        "modules": [
            {
                "module": 1,
                "title": "Introduction to Engineering Drawing",
                "topics": [
                    {
                        "topic": "Drawing Fundamentals",
                        "subtopics": [
                            "Engineering drawing instruments",
                            "Lettering",
                            "Dimensioning",
                            "Geometrical constructions"
                        ]
                    }
                ]
            },
            {
                "module": 2,
                "title": "Projection of Points and Lines",
                "topics": [
                    {
                        "topic": "Projection",
                        "subtopics": [
                            "Projection of points",
                            "Projection of straight lines",
                            "True length",
                            "True inclination"
                        ]
                    }
                ]
            },
            {
                "module": 3,
                "title": "Projection of Planes",
                "topics": [
                    {
                        "topic": "Planes",
                        "subtopics": [
                            "Projection of planes",
                            "Inclination to reference planes",
                            "True shape"
                        ]
                    }
                ]
            },
            {
                "module": 4,
                "title": "Projection of Solids",
                "topics": [
                    {
                        "topic": "Solids",
                        "subtopics": [
                            "Prisms",
                            "Pyramids",
                            "Cylinders",
                            "Cones",
                            "Projection of solids"
                        ]
                    }
                ]
            },
            {
                "module": 5,
                "title": "Sections and Development",
                "topics": [
                    {
                        "topic": "Sections",
                        "subtopics": [
                            "Sections of solids",
                            "Sectional views",
                            "True shape of sections"
                        ]
                    },
                    {
                        "topic": "Development",
                        "subtopics": [
                            "Development of surfaces",
                            "Prisms",
                            "Pyramids",
                            "Cylinders",
                            "Cones"
                        ]
                    }
                ]
            }
        ]
    },


    # =========================================================
    # M1101 - ENGINEERING CHEMISTRY LAB
    # =========================================================

    {
        "semester": 1,
        "subject_code": "M1101",
        "subject_name": "Engineering Chemistry Laboratory",
        "modules": [
            {
                "module": 1,
                "title": "Chemistry Laboratory Experiments",
                "topics": [
                    {
                        "topic": "Experiments",
                        "subtopics": [
                            "Estimation of hardness of water",
                            "Estimation of alkalinity of water",
                            "Determination of dissolved oxygen",
                            "Conductometric titrations",
                            "pH metric titrations",
                            "Preparation of polymers",
                            "Determination of viscosity",
                            "Determination of surface tension"
                        ]
                    }
                ]
            }
        ]
    },


    # =========================================================
    # M1102 - PROGRAMMING FOR PROBLEM SOLVING LAB
    # =========================================================

    {
        "semester": 1,
        "subject_code": "M1102",
        "subject_name": "Programming for Problem Solving Laboratory",
        "modules": [
            {
                "module": 1,
                "title": "C Programming Laboratory",
                "topics": [
                    {
                        "topic": "Programming Exercises",
                        "subtopics": [
                            "Basic C programs",
                            "Operators",
                            "Conditional statements",
                            "Looping statements",
                            "Arrays",
                            "Strings",
                            "Functions",
                            "Recursion",
                            "Pointers",
                            "Structures",
                            "File handling"
                        ]
                    }
                ]
            }
        ]
    },


    # =========================================================
    # M11AC1 - LINGUASKILL FOR PROFESSIONALS-A2
    # =========================================================

    {
        "semester": 1,
        "subject_code": "M11AC1",
        "subject_name": "Linguaskill for Professionals-A2",
        "modules": [
            {
                "module": 1,
                "title": "Communication Skills",
                "topics": [
                    {
                        "topic": "English Language Skills",
                        "subtopics": [
                            "Listening",
                            "Speaking",
                            "Reading",
                            "Writing",
                            "Grammar",
                            "Vocabulary",
                            "Pronunciation"
                        ]
                    }
                ]
            },
            {
                "module": 2,
                "title": "Everyday Communication",
                "topics": [
                    {
                        "topic": "Communication Activities",
                        "subtopics": [
                            "Introducing yourself",
                            "Giving personal information",
                            "Asking questions",
                            "Making requests",
                            "Giving directions"
                        ]
                    }
                ]
            },
            {
                "module": 3,
                "title": "Professional Communication",
                "topics": [
                    {
                        "topic": "Workplace English",
                        "subtopics": [
                            "Workplace vocabulary",
                            "Emails",
                            "Telephone conversations",
                            "Meetings",
                            "Presentations"
                        ]
                    }
                ]
            },
            {
                "module": 4,
                "title": "Reading and Listening",
                "topics": [
                    {
                        "topic": "Comprehension",
                        "subtopics": [
                            "Reading comprehension",
                            "Listening comprehension",
                            "Identifying main ideas",
                            "Identifying specific information"
                        ]
                    }
                ]
            },
            {
                "module": 5,
                "title": "Speaking and Writing",
                "topics": [
                    {
                        "topic": "Language Production",
                        "subtopics": [
                            "Short conversations",
                            "Describing experiences",
                            "Writing short messages",
                            "Writing emails",
                            "Basic professional communication"
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

semester_2 = [

    # =========================================================
    # M120A - DIFFERENTIAL EQUATIONS AND VECTOR CALCULUS
    # =========================================================

    {
        "semester": 2,
        "subject_code": "M120A",
        "subject_name": "Differential Equations and Vector Calculus",

        "modules": [

            {
                "module": 1,
                "title": "First Order, First Degree ODE and its Applications",
                "topics": [
                    {
                        "topic": "First Order Differential Equations",
                        "subtopics": [
                            "Exact differential equation",
                            "Linear differential equation",
                            "Bernoulli differential equation"
                        ]
                    },
                    {
                        "topic": "Applications",
                        "subtopics": [
                            "Newton's law of cooling",
                            "Law of natural growth and decay",
                            "Orthogonal trajectories"
                        ]
                    }
                ]
            },

            {
                "module": 2,
                "title": "Second and Higher Order ODE with Constant Coefficients",
                "topics": [
                    {
                        "topic": "Second Order Linear Differential Equations",
                        "subtopics": [
                            "Homogeneous differential equations",
                            "Non-homogeneous differential equations",
                            "Non-homogeneous terms of the type e^ax",
                            "Non-homogeneous terms of the type sin(ax)",
                            "Non-homogeneous terms of the type cos(ax)",
                            "Non-homogeneous terms of the type polynomials in x^k",
                            "Non-homogeneous terms of the type e^ax V(x)",
                            "Non-homogeneous terms of the type xV(x)"
                        ]
                    },
                    {
                        "topic": "Methods and Reducible Equations",
                        "subtopics": [
                            "Method of variation of parameters",
                            "Euler-Cauchy equation",
                            "Legendre's equation"
                        ]
                    }
                ]
            },

            {
                "module": 3,
                "title": "Laplace Transforms",
                "topics": [
                    {
                        "topic": "Laplace Transform",
                        "subtopics": [
                            "Existence condition",
                            "Laplace transform of elementary functions",
                            "Properties of Laplace transforms"
                        ]
                    },
                    {
                        "topic": "Special Functions",
                        "subtopics": [
                            "Unit step function",
                            "Dirac delta function",
                            "Periodic function"
                        ]
                    },
                    {
                        "topic": "Inverse Laplace Transform",
                        "subtopics": [
                            "Inverse Laplace transform",
                            "Properties of inverse Laplace transform",
                            "Convolution theorem",
                            "Applications of convolution theorem",
                            "Solving linear differential equations with constant coefficients using Laplace transform"
                        ]
                    }
                ]
            },

            {
                "module": 4,
                "title": "Vector Differential Calculus",
                "topics": [
                    {
                        "topic": "Vector Fields",
                        "subtopics": [
                            "Scalar fields",
                            "Vector fields",
                            "Vector differentiation",
                            "Level surfaces"
                        ]
                    },
                    {
                        "topic": "Vector Derivatives",
                        "subtopics": [
                            "Gradient of a scalar field",
                            "Directional derivative",
                            "Divergence",
                            "Curl of a vector field"
                        ]
                    },
                    {
                        "topic": "Applications",
                        "subtopics": [
                            "Scalar potential energy",
                            "Tangent plane",
                            "Normal line",
                            "Vector identities"
                        ]
                    }
                ]
            },

            {
                "module": 5,
                "title": "Vector Integral Calculus",
                "topics": [
                    {
                        "topic": "Vector Integrals",
                        "subtopics": [
                            "Line integrals",
                            "Surface integrals",
                            "Volume integrals"
                        ]
                    },
                    {
                        "topic": "Integral Theorems",
                        "subtopics": [
                            "Green's theorem in a plane",
                            "Gauss-Divergence theorem",
                            "Stokes theorem"
                        ]
                    }
                ]
            }
        ]
    },


    # =========================================================
    # M120B - APPLIED PHYSICS
    # =========================================================

    {
        "semester": 2,
        "subject_code": "M120B",
        "subject_name": "Applied Physics",

        "modules": [

            {
                "module": 1,
                "title": "LASERs and Optical Fibers",
                "topics": [
                    {
                        "topic": "LASERs",
                        "subtopics": [
                            "Introduction",
                            "Properties of laser beam",
                            "Monochromaticity",
                            "Coherence",
                            "Directionality",
                            "Brightness",
                            "Einstein coefficients",
                            "Population inversion",
                            "Ruby laser",
                            "He-Ne laser",
                            "Semiconductor laser",
                            "Applications of lasers"
                        ]
                    },
                    {
                        "topic": "Optical Fibers",
                        "subtopics": [
                            "Introduction",
                            "Principle and construction of optical fiber",
                            "Total internal reflection",
                            "Acceptance angle",
                            "Numerical aperture",
                            "Single mode optical fiber",
                            "Multimode optical fiber",
                            "Step index optical fiber",
                            "Graded index optical fiber",
                            "Losses in optical fibers",
                            "Optical fiber communication system",
                            "Applications of optical fibers"
                        ]
                    }
                ]
            },

            {
                "module": 2,
                "title": "Fundamentals of Quantum Mechanics and Band Theory of Solids",
                "topics": [
                    {
                        "topic": "Fundamentals of Quantum Mechanics",
                        "subtopics": [
                            "Introduction to quantum physics",
                            "Black body radiation",
                            "Planck's radiation law",
                            "Photoelectric effect",
                            "de-Broglie hypothesis",
                            "Davisson and Germer's experiment",
                            "Concept of wave function",
                            "Heisenberg uncertainty principle",
                            "Time independent Schrödinger wave equation",
                            "Particle in one-dimensional infinite potential well"
                        ]
                    },
                    {
                        "topic": "Band Theory of Solids",
                        "subtopics": [
                            "Free electron theory",
                            "Drude theory",
                            "Lorentz theory",
                            "Sommerfeld theory",
                            "Bloch's theorem",
                            "Kronig-Penney model",
                            "E-K diagram",
                            "Effective mass of electron",
                            "Origin of energy bands",
                            "Classification of solids"
                        ]
                    }
                ]
            },

            {
                "module": 3,
                "title": "Semiconductor Physics and Devices",
                "topics": [
                    {
                        "topic": "Semiconductor Physics",
                        "subtopics": [
                            "Density of states",
                            "Intrinsic semiconductor",
                            "Intrinsic carrier concentration",
                            "Extrinsic semiconductors",
                            "Fermi level",
                            "Temperature dependence of Fermi level",
                            "Hall effect",
                            "Hall coefficient",
                            "Applications of Hall effect"
                        ]
                    },
                    {
                        "topic": "Semiconductor Devices",
                        "subtopics": [
                            "Direct bandgap semiconductor",
                            "Indirect bandgap semiconductor",
                            "Formation of PN junction",
                            "Working of PN junction diode in forward bias",
                            "Working of PN junction diode in reverse bias",
                            "V-I characteristics",
                            "Zener diode",
                            "LED",
                            "Photodiode",
                            "Solar cell",
                            "Structure of semiconductor devices",
                            "Working principles",
                            "Characteristics"
                        ]
                    }
                ]
            },

            {
                "module": 4,
                "title": "Dielectric, Energy and Magnetic Materials",
                "topics": [
                    {
                        "topic": "Dielectric and Energy Materials",
                        "subtopics": [
                            "Introduction",
                            "Electronic polarization",
                            "Ionic polarization",
                            "Orientation polarization",
                            "Internal field",
                            "Clausius-Mossotti relation",
                            "Piezoelectricity",
                            "Pyroelectricity",
                            "Ferroelectricity",
                            "Applications of dielectric materials",
                            "Materials and electrolytes for super capacitors",
                            "Rechargeable ion batteries",
                            "Lithium ion batteries",
                            "Sodium ion batteries",
                            "Solid fuel cells"
                        ]
                    },
                    {
                        "topic": "Magnetic Materials",
                        "subtopics": [
                            "Introduction",
                            "Origin of magnetic moment",
                            "Bohr magneton",
                            "Diamagnetic materials",
                            "Paramagnetic materials",
                            "Ferromagnetic materials",
                            "Classification based on magnetic moment",
                            "Hysteresis curve",
                            "Domain theory",
                            "Soft magnetic materials",
                            "Hard magnetic materials",
                            "Antiferromagnetic materials",
                            "Ferrimagnetic materials"
                        ]
                    }
                ]
            },

            {
                "module": 5,
                "title": "Nanoscience and Characterization Techniques",
                "topics": [
                    {
                        "topic": "Nanoscience",
                        "subtopics": [
                            "Introduction to nanomaterials",
                            "Surface area to volume ratio",
                            "Quantum confinement",
                            "Top-down fabrication",
                            "Ball milling",
                            "Chemical Vapor Deposition",
                            "Bottom-up fabrication",
                            "Sol-Gel method",
                            "Combustion method"
                        ]
                    },
                    {
                        "topic": "Characterization Techniques",
                        "subtopics": [
                            "X-Ray Diffraction",
                            "Scanning Electron Microscope",
                            "Transmission Electron Microscope",
                            "Scanning Tunnelling Microscope",
                            "Applications of nanomaterials"
                        ]
                    }
                ]
            }
        ]
    },


    # =========================================================
    # M122A - BASIC ELECTRICAL ENGINEERING
    # =========================================================

    {
        "semester": 2,
        "subject_code": "M122A",
        "subject_name": "Basic Electrical Engineering",

        "modules": [

            {
                "module": 1,
                "title": "DC Circuits and Circuit Elements",
                "topics": [
                    {
                        "topic": "Basic Electrical Quantities",
                        "subtopics": [
                            "Voltage",
                            "Current",
                            "Power",
                            "Energy",
                            "Active elements",
                            "Passive elements",
                            "Voltage sources",
                            "Current sources",
                            "Source conversions",
                            "Open circuit",
                            "Short circuit"
                        ]
                    },
                    {
                        "topic": "Circuit Laws and Analysis",
                        "subtopics": [
                            "Ohm's law",
                            "Kirchhoff's laws",
                            "Loop current method",
                            "Node voltage method",
                            "Solving electrical networks"
                        ]
                    },
                    {
                        "topic": "Resistance",
                        "subtopics": [
                            "Resistance",
                            "Laws of resistance",
                            "Temperature coefficient of resistance",
                            "Resistors in series",
                            "Resistors in parallel",
                            "Uses of resistor"
                        ]
                    }
                ]
            },

            {
                "module": 2,
                "title": "AC Circuits",
                "topics": [
                    {
                        "topic": "Single Phase AC Circuits",
                        "subtopics": [
                            "Alternating quantity",
                            "Cycle",
                            "Time period",
                            "Frequency",
                            "Amplitude",
                            "RMS value",
                            "Average value",
                            "Form factor",
                            "Peak factor",
                            "Phase",
                            "Phase difference",
                            "AC through R circuit",
                            "AC through L circuit",
                            "AC through C circuit",
                            "RL series circuit",
                            "RC series circuit",
                            "RLC series circuit",
                            "Resonance in series RLC circuit"
                        ]
                    },
                    {
                        "topic": "Three Phase AC Circuits",
                        "subtopics": [
                            "Phase sequence",
                            "Three phase connections",
                            "Star connection",
                            "Delta connection",
                            "Relationship between line and phase voltage",
                            "Relationship between line and phase current",
                            "Power in three phase circuit"
                        ]
                    }
                ]
            },

            {
                "module": 3,
                "title": "Static Electric Machine",
                "topics": [
                    {
                        "topic": "Single Phase Transformer",
                        "subtopics": [
                            "Principle",
                            "Constructional details",
                            "Parts of transformer",
                            "Core type transformer",
                            "Shell type transformer",
                            "Equivalent circuit",
                            "EMF equation"
                        ]
                    },
                    {
                        "topic": "Transformer Performance and Applications",
                        "subtopics": [
                            "Losses",
                            "Efficiency",
                            "Regulation",
                            "Applications"
                        ]
                    }
                ]
            },

            {
                "module": 4,
                "title": "DC and AC Machines",
                "topics": [
                    {
                        "topic": "DC Motor",
                        "subtopics": [
                            "Principle",
                            "Constructional details",
                            "DC series motor",
                            "DC shunt motor",
                            "Torque-current characteristics",
                            "Speed-current characteristics",
                            "Applications"
                        ]
                    },
                    {
                        "topic": "Three Phase Induction Motor",
                        "subtopics": [
                            "Principle",
                            "Construction",
                            "Generation of rotating magnetic field",
                            "Torque-slip characteristics"
                        ]
                    }
                ]
            },

            {
                "module": 5,
                "title": "Electrical Installations and Measuring Instruments",
                "topics": [
                    {
                        "topic": "Electrical Installations",
                        "subtopics": [
                            "Components of LT switchgear",
                            "Switch Fuse Unit",
                            "MCB",
                            "MCCB",
                            "Earthing"
                        ]
                    },
                    {
                        "topic": "Measuring Instruments",
                        "subtopics": [
                            "Construction of PMMC instruments",
                            "Working principle of PMMC instruments",
                            "Advantages of PMMC instruments",
                            "Disadvantages of PMMC instruments",
                            "Applications of PMMC instruments",
                            "Construction of MI instruments",
                            "Working principle of MI instruments",
                            "Advantages of MI instruments",
                            "Disadvantages of MI instruments",
                            "Applications of MI instruments"
                        ]
                    }
                ]
            }
        ]
    },


    # =========================================================
    # M125A - DATA STRUCTURES
    # =========================================================

    {
        "semester": 2,
        "subject_code": "M125A",
        "subject_name": "Data Structures",

        "modules": [

            {
                "module": 1,
                "title": "Basic Concepts and Linked Lists",
                "topics": [
                    {
                        "topic": "Basic Concepts",
                        "subtopics": [
                            "Algorithm specification",
                            "Performance analysis",
                            "Time complexity",
                            "Space complexity",
                            "Asymptotic notation",
                            "Big O notation",
                            "Omega notation",
                            "Theta notation",
                            "Linear data structures",
                            "Non-linear data structures"
                        ]
                    },
                    {
                        "topic": "Linked Lists",
                        "subtopics": [
                            "Linear list",
                            "Singly linked list",
                            "Insertion",
                            "Deletion",
                            "Searching",
                            "Circular linked list",
                            "Doubly linked list",
                            "Applications of linked lists"
                        ]
                    }
                ]
            },

            {
                "module": 2,
                "title": "Stacks and Queues",
                "topics": [
                    {
                        "topic": "Stacks",
                        "subtopics": [
                            "Stack operations",
                            "Array representation",
                            "Linked representation",
                            "Infix to postfix conversion",
                            "Postfix expression evaluation",
                            "Recursion implementation"
                        ]
                    },
                    {
                        "topic": "Queues",
                        "subtopics": [
                            "Queue operations",
                            "Array representation",
                            "Linked representation",
                            "Circular queue",
                            "Circular queue operations",
                            "Deque",
                            "Applications of queue"
                        ]
                    }
                ]
            },

            {
                "module": 3,
                "title": "Trees",
                "topics": [
                    {
                        "topic": "Binary Trees",
                        "subtopics": [
                            "Tree terminology",
                            "Representation of trees",
                            "Binary tree ADT",
                            "Properties of binary trees",
                            "Array representation",
                            "Linked representation",
                            "Binary tree traversals",
                            "Threaded binary trees"
                        ]
                    },
                    {
                        "topic": "Binary Heap",
                        "subtopics": [
                            "Heap properties",
                            "Max heap",
                            "Min heap",
                            "Insertion",
                            "Deletion",
                            "Heap sort"
                        ]
                    },
                    {
                        "topic": "Search Trees",
                        "subtopics": [
                            "Binary search tree",
                            "Tree traversals",
                            "AVL tree",
                            "AVL tree operations",
                            "B-tree",
                            "B-tree operations",
                            "B+ trees",
                            "Red Black tree"
                        ]
                    }
                ]
            },

            {
                "module": 4,
                "title": "Graphs, Searching and Sorting",
                "topics": [
                    {
                        "topic": "Graphs",
                        "subtopics": [
                            "Graph terminology",
                            "Sequential representation",
                            "Linked representation",
                            "Depth First Search",
                            "Breadth First Search",
                            "Minimum spanning trees",
                            "Prim's method",
                            "Kruskal's method"
                        ]
                    },
                    {
                        "topic": "Searching",
                        "subtopics": [
                            "Linear search",
                            "Binary search"
                        ]
                    },
                    {
                        "topic": "Sorting",
                        "subtopics": [
                            "Bubble sort",
                            "Insertion sort",
                            "Quick sort",
                            "Merge sort"
                        ]
                    }
                ]
            },

            {
                "module": 5,
                "title": "Hashing and Pattern Matching",
                "topics": [
                    {
                        "topic": "Hashing",
                        "subtopics": [
                            "Hash table",
                            "Hash table representations",
                            "Hash functions",
                            "Collision resolution",
                            "Separate chaining",
                            "Open addressing",
                            "Linear probing",
                            "Quadratic probing",
                            "Double hashing",
                            "Rehashing",
                            "Extendible hashing"
                        ]
                    },
                    {
                        "topic": "Pattern Matching",
                        "subtopics": [
                            "Introduction",
                            "Brute force",
                            "Boyer-Moore algorithm",
                            "Knuth-Morris-Pratt algorithm"
                        ]
                    }
                ]
            }
        ]
    },


    # =========================================================
    # M1201 - PHYSICS LABORATORY
    # =========================================================

    {
        "semester": 2,
        "subject_code": "M1201",
        "subject_name": "Physics Laboratory",

        "modules": [
            {
                "module": 1,
                "title": "Physics Laboratory Experiments",
                "topics": [
                    {
                        "topic": "Experiments",
                        "subtopics": [
                            "Energy gap of P-N junction diode",
                            "V-I characteristics of solar cell",
                            "V-I characteristics of light emitting diode",
                            "V-I characteristics of laser diode",
                            "Determination of numerical aperture of optical fibre",
                            "Determination of Hall coefficient",
                            "Determination of work function using photoelectric effect",
                            "Determination of dielectric constant",
                            "Determination of quality factor of LCR circuit",
                            "Determination of time constant of R-C circuit",
                            "Determination of frequency using Melde's experiment",
                            "Determination of rigidity modulus using torsional pendulum",
                            "Determination of frequency of AC supply using sonometer"
                        ]
                    }
                ]
            }
        ]
    },


    # =========================================================
    # M1221 - BASIC ELECTRICAL ENGINEERING LAB
    # =========================================================

    {
        "semester": 2,
        "subject_code": "M1221",
        "subject_name": "Basic Electrical Engineering Lab",

        "modules": [
            {
                "module": 1,
                "title": "Basic Electrical Engineering Experiments",
                "topics": [
                    {
                        "topic": "Circuit Experiments",
                        "subtopics": [
                            "Verification of Ohm's Law",
                            "Determination of unknown resistance",
                            "Verification of KVL and KCL",
                            "Transient response of series RL circuit using DC excitation",
                            "Transient response of series RC circuit using DC excitation",
                            "Transient response of RLC series circuit using DC excitation",
                            "Resonance in series RLC circuit",
                            "Verification of impedance and current of RL series circuit",
                            "Verification of impedance and current of RC series circuit",
                            "Verification of impedance and current of RLC series circuit"
                        ]
                    },
                    {
                        "topic": "Transformer and Motor Experiments",
                        "subtopics": [
                            "Measurement of voltage, current and real power in primary and secondary circuits of a single phase transformer",
                            "Performance characteristics of a DC shunt motor",
                            "Load test on single phase transformer",
                            "Calculation of transformer efficiency",
                            "Calculation of transformer regulation"
                        ]
                    }
                ]
            }
        ]
    },


    # =========================================================
    # M1252 - DATA STRUCTURES LAB
    # =========================================================

    {
        "semester": 2,
        "subject_code": "M1252",
        "subject_name": "Data Structures Lab",

        "modules": [
            {
                "module": 1,
                "title": "Data Structures Laboratory Experiments",
                "topics": [
                    {
                        "topic": "Linked Lists",
                        "subtopics": [
                            "Singly linked list creation",
                            "Singly linked list insertion",
                            "Singly linked list deletion",
                            "Singly linked list traversal",
                            "Merging two singly linked lists",
                            "Doubly linked list creation",
                            "Doubly linked list insertion",
                            "Doubly linked list deletion",
                            "Doubly linked list traversal"
                        ]
                    },
                    {
                        "topic": "Stacks and Queues",
                        "subtopics": [
                            "Stack implementation using arrays",
                            "Stack implementation using linked lists",
                            "Infix to postfix conversion",
                            "Postfix expression evaluation",
                            "Infix to prefix conversion",
                            "Linear queue using arrays",
                            "Linear queue using linked lists",
                            "Circular queue insertion",
                            "Circular queue deletion",
                            "Circular queue search and count"
                        ]
                    },
                    {
                        "topic": "Trees and Graphs",
                        "subtopics": [
                            "Binary tree traversals",
                            "AVL tree operations",
                            "Graph representation using adjacency matrix"
                        ]
                    },
                    {
                        "topic": "Searching and Sorting",
                        "subtopics": [
                            "Linear search",
                            "Binary search",
                            "Bubble sort",
                            "Insertion sort",
                            "Quick sort",
                            "Merge sort"
                        ]
                    }
                ]
            }
        ]
    },


    # =========================================================
    # M1233 - ENGINEERING AND IT WORKSHOP
    # =========================================================

    {
        "semester": 2,
        "subject_code": "M1233",
        "subject_name": "Engineering and IT Workshop",

        "modules": [
            {
                "module": 1,
                "title": "Engineering Workshop",
                "topics": [
                    {
                        "topic": "Workshop Experiments",
                        "subtopics": [
                            "Half Lap joint",
                            "Dovetail joint",
                            "Rectangular scoop using sheet metal",
                            "Hooper using sheet metal",
                            "Parallel and series wiring connection",
                            "Staircase wiring connection",
                            "Square rod from a round rod",
                            "S-hook from a round rod",
                            "Sand mould for single piece pattern",
                            "Sand mould for split-piece pattern"
                        ]
                    }
                ]
            },
            {
                "module": 2,
                "title": "IT Workshop",
                "topics": [
                    {
                        "topic": "Computer Hardware",
                        "subtopics": [
                            "Identification of peripherals",
                            "Study of UPS",
                            "Study of SMPS"
                        ]
                    },
                    {
                        "topic": "Computer Assembly and Operating Systems",
                        "subtopics": [
                            "Assembling a PC",
                            "Disassembling a PC",
                            "Hardware diagnostic exercises",
                            "Installation of Windows operating system",
                            "Installation of Linux operating system",
                            "Basic Windows commands",
                            "Basic Linux commands",
                            "Operating system diagnostic exercises"
                        ]
                    }
                ]
            }
        ]
    },


    # =========================================================
    # M12AC1 - LINGUASKILL FOR PROFESSIONALS - B1
    # =========================================================

    {
        "semester": 2,
        "subject_code": "M12AC1",
        "subject_name": "Linguaskill for Professionals-B1",

        "modules": [

            {
                "module": 1,
                "title": "Grammar, Vocabulary, Pronunciation and Everyday English",
                "topics": [
                    {
                        "topic": "Unit 1",
                        "subtopics": [
                            "Subject-Object",
                            "Present Tense",
                            "Words about friendship",
                            "Words about communication",
                            "Words about work and technology",
                            "Word stress",
                            "Sentence stress"
                        ]
                    },
                    {
                        "topic": "Unit 2",
                        "subtopics": [
                            "Opinions and suggestions",
                            "Listening Activity 1",
                            "Listening Activity 2",
                            "Reading Activity 1",
                            "Reading Activity 2",
                            "Speaking Activity 1",
                            "Speaking Activity 2",
                            "Guide",
                            "Email giving news"
                        ]
                    }
                ]
            },

            {
                "module": 2,
                "title": "Modals, Relationships and Communication",
                "topics": [
                    {
                        "topic": "Unit 1",
                        "subtopics": [
                            "Modals",
                            "Phrases of ability",
                            "Articles",
                            "Used to",
                            "Usually",
                            "Words about relationship",
                            "Words about ability",
                            "Linking sounds",
                            "Intonation in question tags"
                        ]
                    },
                    {
                        "topic": "Unit 2",
                        "subtopics": [
                            "Telling a story",
                            "Offering help",
                            "Asking for help",
                            "Listening Activity 1",
                            "Listening Activity 2",
                            "Reading Activity 1",
                            "Reading Activity 2",
                            "Speaking Activity 1",
                            "Speaking Activity 2",
                            "About someone's life",
                            "Online advertisement"
                        ]
                    }
                ]
            },

            {
                "module": 3,
                "title": "Future Forms, Environment and Recommendations",
                "topics": [
                    {
                        "topic": "Unit 1",
                        "subtopics": [
                            "Future forms",
                            "Zero conditionals",
                            "First conditionals",
                            "Comparatives",
                            "Superlatives",
                            "Words about the natural world",
                            "Environmental issues",
                            "Food",
                            "Sound and spelling 'a'",
                            "/ʃ/",
                            "/tʃ/"
                        ]
                    },
                    {
                        "topic": "Unit 2",
                        "subtopics": [
                            "Giving reasons",
                            "Giving results",
                            "Giving examples",
                            "Asking for recommendations",
                            "Giving recommendations",
                            "Listening Activity 1",
                            "Listening Activity 2",
                            "Reading Activity 1",
                            "Reading Activity 2",
                            "Speaking Activity 1",
                            "Speaking Activity 2",
                            "Discussion essay",
                            "Review of a restaurant or cafe"
                        ]
                    }
                ]
            },

            {
                "module": 4,
                "title": "Quantifiers, Reported Speech and Information Sharing",
                "topics": [
                    {
                        "topic": "Unit 1",
                        "subtopics": [
                            "Quantifiers",
                            "Reported speech",
                            "Words about buildings",
                            "Sharing information",
                            "Sounds /t/",
                            "Sounds /d/",
                            "Sounds /k/",
                            "Sounds /g/",
                            "Sounds /h/",
                            "Sounds /w/"
                        ]
                    },
                    {
                        "topic": "Unit 2",
                        "subtopics": [
                            "Offers",
                            "Requests",
                            "Permission",
                            "Generalising",
                            "Being vague",
                            "Listening Activity 1",
                            "Listening Activity 2",
                            "Reading Activity 1",
                            "Reading Activity 2",
                            "Speaking Activity 1",
                            "Speaking Activity 2",
                            "A note with useful information",
                            "Email summary of a news story"
                        ]
                    }
                ]
            },

            {
                "module": 5,
                "title": "Passive Voice, Relative Clauses and Professional Communication",
                "topics": [
                    {
                        "topic": "Unit 1",
                        "subtopics": [
                            "Passive voice",
                            "Relative clause",
                            "Second conditional",
                            "Third conditional",
                            "Words about music",
                            "Words about sport",
                            "Expressions with do",
                            "Expressions with make",
                            "Expressions with take",
                            "-ed ending words",
                            "Mostly confused words"
                        ]
                    },
                    {
                        "topic": "Unit 2",
                        "subtopics": [
                            "Recommending",
                            "Discussing problems",
                            "Reassuring",
                            "Listening Activity 1",
                            "Listening Activity 2",
                            "Reading Activity 1",
                            "Reading Activity 2",
                            "Speaking Activity 1",
                            "Speaking Activity 2",
                            "Article",
                            "Email with advice"
                        ]
                    }
                ]
            }
        ]
    }
]


semester_3 = [

    # =========================================================
    # M210A - PROBABILITY AND STATISTICS
    # =========================================================

    {
        "semester": 3,
        "subject_code": "M210A",
        "subject_name": "Probability and Statistics",
        "modules": [
            {
                "module": 1,
                "title": "Single Random Variables",
                "topics": [
                    {
                        "topic": "Random Variables and Probability",
                        "subtopics": [
                            "Introduction to Probability",
                            "Random Variables",
                            "Discrete Random Variables",
                            "Continuous Random Variables",
                            "Probability distributions",
                            "Probability mass function",
                            "Probability density function",
                            "Mathematical expectation",
                            "Moments about the origin",
                            "Central moments"
                        ]
                    }
                ]
            },
            {
                "module": 2,
                "title": "Probability Distributions",
                "topics": [
                    {
                        "topic": "Probability Distributions",
                        "subtopics": [
                            "Binomial distribution",
                            "Poisson distribution",
                            "Normal distribution",
                            "Exponential distribution",
                            "Properties of probability distributions",
                            "Moment generating functions",
                            "Mean",
                            "Variance"
                        ]
                    }
                ]
            },
            {
                "module": 3,
                "title": "Sampling and Testing of Hypothesis for Large Samples",
                "topics": [
                    {
                        "topic": "Sampling",
                        "subtopics": [
                            "Population",
                            "Sampling",
                            "Statistic",
                            "Parameter",
                            "Types of sampling",
                            "Sample mean",
                            "Sample variance",
                            "Sampling distribution",
                            "Standard error",
                            "Sampling distributions of means and variance"
                        ]
                    },
                    {
                        "topic": "Testing of Hypothesis",
                        "subtopics": [
                            "Null hypothesis",
                            "Alternative hypothesis",
                            "Type I error",
                            "Type II error",
                            "Critical region",
                            "Confidence interval",
                            "Level of significance",
                            "One-tailed test",
                            "Two-tailed test"
                        ]
                    },
                    {
                        "topic": "Large Sample Tests",
                        "subtopics": [
                            "Test of hypothesis for single mean",
                            "Difference between means",
                            "Single proportion",
                            "Difference between proportions",
                            "Difference between sample S.D and population S.D"
                        ]
                    }
                ]
            },
            {
                "module": 4,
                "title": "Testing of Hypothesis for Small Samples",
                "topics": [
                    {
                        "topic": "Small Sample Tests",
                        "subtopics": [
                            "t-distribution",
                            "Paired t-test",
                            "Confidence interval for t-distribution",
                            "F-test",
                            "Chi-square test for goodness of fit",
                            "Chi-square test for independence of attributes"
                        ]
                    }
                ]
            },
            {
                "module": 5,
                "title": "Correlation and Regression",
                "topics": [
                    {
                        "topic": "Correlation",
                        "subtopics": [
                            "Types of correlation",
                            "Coefficient of correlation",
                            "Rank correlation",
                            "Covariance of two random variables"
                        ]
                    },
                    {
                        "topic": "Regression",
                        "subtopics": [
                            "Regression coefficient",
                            "Lines of regression"
                        ]
                    }
                ]
            }
        ]
    },


    # =========================================================
    # M214E - DIGITAL LOGIC DESIGN
    # =========================================================

    {
        "semester": 3,
        "subject_code": "M214E",
        "subject_name": "Digital Logic Design",
        "modules": [
            {
                "module": 1,
                "title": "Boolean Algebra and Logic Gates",
                "topics": [
                    {
                        "topic": "Digital Systems and Number Systems",
                        "subtopics": [
                            "Digital systems",
                            "Binary numbers",
                            "Number base conversions",
                            "Octal numbers",
                            "Hexadecimal numbers",
                            "Complements",
                            "Signed binary numbers",
                            "Binary codes",
                            "Binary storage and registers",
                            "Binary logic"
                        ]
                    },
                    {
                        "topic": "Boolean Algebra and Logic Gates",
                        "subtopics": [
                            "Basic definitions",
                            "Axiomatic definition of Boolean algebra",
                            "Basic theorems and properties",
                            "Boolean functions",
                            "Canonical forms",
                            "Standard forms",
                            "Logic operations",
                            "Digital logic gates"
                        ]
                    }
                ]
            },
            {
                "module": 2,
                "title": "Gate Level Minimization",
                "topics": [
                    {
                        "topic": "Karnaugh Maps and Minimization",
                        "subtopics": [
                            "Map method",
                            "Four-variable map",
                            "Five-variable map",
                            "Product of sums simplification",
                            "Don't-care conditions",
                            "NAND implementation",
                            "NOR implementation",
                            "Two-level implementations",
                            "Exclusive-OR function"
                        ]
                    }
                ]
            },
            {
                "module": 3,
                "title": "Combinational Logic",
                "topics": [
                    {
                        "topic": "Combinational Circuits",
                        "subtopics": [
                            "Combinational circuits",
                            "Analysis procedure",
                            "Design procedure",
                            "Binary adder",
                            "Subtractor",
                            "Decimal adder",
                            "Binary multiplier",
                            "Magnitude comparator",
                            "Decoders",
                            "Encoders",
                            "Multiplexers",
                            "HDL for combinational circuits"
                        ]
                    }
                ]
            },
            {
                "module": 4,
                "title": "Sequential Logic",
                "topics": [
                    {
                        "topic": "Sequential Circuits",
                        "subtopics": [
                            "Sequential circuits",
                            "Latches",
                            "Flip-flops",
                            "Analysis of clocked sequential circuits",
                            "State reduction",
                            "State assignment",
                            "Design procedure",
                            "Registers",
                            "Shift registers",
                            "Ripple counters",
                            "Synchronous counters",
                            "Other counters"
                        ]
                    }
                ]
            },
            {
                "module": 5,
                "title": "Memories and Asynchronous Sequential Logic",
                "topics": [
                    {
                        "topic": "Memories and Programmable Devices",
                        "subtopics": [
                            "Random-access memory",
                            "Memory decoding",
                            "Error detection and correction",
                            "Read-only memory",
                            "Programmable Logic Array",
                            "Programmable Array Logic",
                            "Sequential programmable devices"
                        ]
                    },
                    {
                        "topic": "Asynchronous Sequential Logic",
                        "subtopics": [
                            "Introduction",
                            "Analysis procedure",
                            "Circuits with latches",
                            "Design procedure",
                            "Reduction of state",
                            "Flow tables",
                            "Race-free state assignment",
                            "Hazards",
                            "Design example"
                        ]
                    }
                ]
            }
        ]
    },


    # =========================================================
    # M215B - PYTHON PROGRAMMING
    # =========================================================

    {
        "semester": 3,
        "subject_code": "M215B",
        "subject_name": "Python Programming",
        "modules": [
            {
                "module": 1,
                "title": "Python Fundamentals",
                "topics": [
                    {
                        "topic": "Programming Paradigms and OOP Fundamentals",
                        "subtopics": [
                            "Structured programming",
                            "Object oriented programming",
                            "Class",
                            "Object",
                            "Abstraction",
                            "Encapsulation",
                            "Polymorphism",
                            "Inheritance"
                        ]
                    },
                    {
                        "topic": "Introduction to Python",
                        "subtopics": [
                            "Interpreted high level language",
                            "Interactive mode",
                            "Script mode",
                            "Variables",
                            "Expressions",
                            "Statements",
                            "Values and types",
                            "Keywords",
                            "Evaluating expressions",
                            "Operators and operands",
                            "Order of operations",
                            "Composition"
                        ]
                    },
                    {
                        "topic": "Functions and Control Flow",
                        "subtopics": [
                            "Function calls",
                            "Type conversion",
                            "Type coercion",
                            "Pre-defined functions",
                            "User-defined functions",
                            "Flow of execution",
                            "Passing parameters",
                            "Function parameters and scope",
                            "Conditionals",
                            "Recursion",
                            "Modulus operator",
                            "Boolean expressions",
                            "Logical operators",
                            "Conditional execution",
                            "Alternative execution",
                            "Chained and nested conditionals",
                            "Return statement",
                            "Infinite recursion"
                        ]
                    }
                ]
            },
            {
                "module": 2,
                "title": "Python Data Structures",
                "topics": [
                    {
                        "topic": "Strings",
                        "subtopics": [
                            "Creating strings",
                            "Initializing strings",
                            "Accessing elements",
                            "String operators",
                            "Comparing strings using relational operators",
                            "String functions and methods"
                        ]
                    },
                    {
                        "topic": "Lists",
                        "subtopics": [
                            "Mutable lists",
                            "Creating and initializing lists",
                            "Traversing",
                            "Appending",
                            "Updating",
                            "Deleting elements",
                            "List operations",
                            "List functions and methods",
                            "List parameters",
                            "Nested lists",
                            "Matrices"
                        ]
                    },
                    {
                        "topic": "Dictionaries",
                        "subtopics": [
                            "Key-value pairs",
                            "Creating dictionaries",
                            "Initializing dictionaries",
                            "Accessing elements",
                            "Dictionary operations",
                            "Traversing",
                            "Appending",
                            "Updating",
                            "Deleting elements",
                            "Dictionary functions and methods"
                        ]
                    },
                    {
                        "topic": "Tuples and Sets",
                        "subtopics": [
                            "Mutability and tuples",
                            "Immutable concept",
                            "Creating tuples",
                            "Initializing tuples",
                            "Accessing tuple elements",
                            "Tuple functions",
                            "Set operations",
                            "Set methods",
                            "Frozenset operations",
                            "Frozenset methods"
                        ]
                    }
                ]
            },
            {
                "module": 3,
                "title": "Object Oriented Programming Using Python",
                "topics": [
                    {
                        "topic": "Classes and Objects",
                        "subtopics": [
                            "Creating Python classes",
                            "Classes and objects",
                            "User-defined compound types",
                            "Mutable objects",
                            "Copying",
                            "Access modifiers",
                            "Classes and functions",
                            "Pure functions",
                            "Modifiers",
                            "Classes and methods",
                            "Optional arguments",
                            "Initialization method",
                            "Operator overloading",
                            "Polymorphism"
                        ]
                    },
                    {
                        "topic": "Inheritance",
                        "subtopics": [
                            "Basic inheritance",
                            "Extending built-ins",
                            "Overriding",
                            "super",
                            "Multiple inheritance",
                            "Diamond problem"
                        ]
                    }
                ]
            },
            {
                "module": 4,
                "title": "Exceptions and Regular Expressions",
                "topics": [
                    {
                        "topic": "Exceptions",
                        "subtopics": [
                            "Raising exceptions",
                            "Handling exceptions",
                            "Exception hierarchy"
                        ]
                    },
                    {
                        "topic": "Regular Expressions",
                        "subtopics": [
                            "Match",
                            "Search",
                            "Replace function",
                            "Regular expression modifiers",
                            "Special character classes",
                            "Repetition cases",
                            "Non-greedy repetition",
                            "Grouping with parentheses",
                            "Back-references",
                            "Anchors"
                        ]
                    }
                ]
            },
            {
                "module": 5,
                "title": "Files, Database Programming and Machine Learning",
                "topics": [
                    {
                        "topic": "File Handling and Exceptions",
                        "subtopics": [
                            "Text files",
                            "Writing variables",
                            "Directories",
                            "Pickling"
                        ]
                    },
                    {
                        "topic": "Database Programming in Python",
                        "subtopics": [
                            "Connection module",
                            "Connecting MySQL database",
                            "DDL operations",
                            "DML operations",
                            "DQL operations"
                        ]
                    },
                    {
                        "topic": "Machine Learning with Python",
                        "subtopics": [
                            "Introduction to Machine Learning with Python",
                            "Tasks in Machine Learning using Python",
                            "Applications of Python Machine Learning"
                        ]
                    }
                ]
            }
        ]
    },


    # =========================================================
    # M215C - DESIGN AND ANALYSIS OF ALGORITHMS
    # =========================================================

    {
        "semester": 3,
        "subject_code": "M215C",
        "subject_name": "Design and Analysis of Algorithms",
        "modules": [
            {
                "module": 1,
                "title": "Introduction to Algorithms",
                "topics": [
                    {
                        "topic": "Algorithm Analysis",
                        "subtopics": [
                            "Algorithm",
                            "Pseudo Code for expressing Algorithms",
                            "Space Complexity",
                            "Time Complexity",
                            "Big-oh Notation",
                            "Omega Notation",
                            "Theta Notation",
                            "Little-oh Notation"
                        ]
                    },
                    {
                        "topic": "Disjoint Sets",
                        "subtopics": [
                            "Disjoint Set Operations",
                            "Union Algorithm",
                            "Find Algorithm",
                            "Spanning Trees",
                            "Connected Components",
                            "Biconnected Components"
                        ]
                    }
                ]
            },
            {
                "module": 2,
                "title": "Divide and Conquer and Greedy Method",
                "topics": [
                    {
                        "topic": "Divide and Conquer",
                        "subtopics": [
                            "General Method",
                            "Binary Search",
                            "Quick Sort",
                            "Merge Sort",
                            "Strassen's Matrix Multiplication"
                        ]
                    },
                    {
                        "topic": "Greedy Method",
                        "subtopics": [
                            "General Method",
                            "Job Sequencing with Deadlines",
                            "0/1 Knapsack Problem",
                            "Minimum Cost Spanning Trees",
                            "Prim's Algorithm",
                            "Kruskal's Algorithm",
                            "Single Source Shortest Path Problem",
                            "Huffman Codes"
                        ]
                    }
                ]
            },
            {
                "module": 3,
                "title": "Dynamic Programming",
                "topics": [
                    {
                        "topic": "Dynamic Programming",
                        "subtopics": [
                            "General Method",
                            "Principle of Optimality",
                            "Multistage Graphs",
                            "Matrix Chain Multiplication",
                            "Optimal Binary Search Trees",
                            "0/1 Knapsack Problem",
                            "All Pairs Shortest Path Problem",
                            "Travelling Sales Person Problem",
                            "Reliability Design"
                        ]
                    }
                ]
            },
            {
                "module": 4,
                "title": "Backtracking",
                "topics": [
                    {
                        "topic": "Backtracking",
                        "subtopics": [
                            "General Method",
                            "N-Queen Problem",
                            "Recursive Permutation Generator",
                            "Sum of Subsets Problem",
                            "Graph Coloring",
                            "Hamiltonian Cycles"
                        ]
                    }
                ]
            },
            {
                "module": 5,
                "title": "Branch and Bound",
                "topics": [
                    {
                        "topic": "Branch and Bound",
                        "subtopics": [
                            "General Method",
                            "Travelling Sales Person Problem",
                            "0/1 Knapsack Problem",
                            "LC Branch and Bound Solution",
                            "FIFO Branch and Bound Solution"
                        ]
                    },
                    {
                        "topic": "NP-Hard and NP-Complete Problems",
                        "subtopics": [
                            "Basic Concepts",
                            "Non-Deterministic Algorithms",
                            "NP-Hard Classes",
                            "NP-Complete Classes",
                            "Cook's Theorem"
                        ]
                    }
                ]
            }
        ]
    },


    # =========================================================
    # M216D - DATABASE MANAGEMENT SYSTEMS
    # =========================================================

    {
        "semester": 3,
        "subject_code": "M216D",
        "subject_name": "Database Management Systems",
        "modules": [
            {
                "module": 1,
                "title": "Introduction and Database Design",
                "topics": [
                    {
                        "topic": "Introduction",
                        "subtopics": [
                            "Purpose of DBMS",
                            "Database System Applications",
                            "Database Systems versus File Systems",
                            "View of Data",
                            "Data Abstraction",
                            "Instances and Schemas",
                            "ER Model",
                            "Relational Model",
                            "Other Data Models",
                            "Database Languages",
                            "Database System Architecture",
                            "Types of Database Users",
                            "Storage Manager",
                            "Query Processor"
                        ]
                    },
                    {
                        "topic": "Introduction to Database Design",
                        "subtopics": [
                            "Database Design",
                            "ER Diagrams",
                            "Entities",
                            "Attributes",
                            "Entity Sets",
                            "Relationships",
                            "Relationship Sets",
                            "Key Constraints",
                            "Participation Constraints",
                            "Weak Entities",
                            "Class Hierarchies",
                            "Aggregation",
                            "Conceptual Design with ER Model"
                        ]
                    }
                ]
            },
            {
                "module": 2,
                "title": "Relational Model and Relational Algebra",
                "topics": [
                    {
                        "topic": "Relational Model",
                        "subtopics": [
                            "Introduction to Relational Model",
                            "Integrity Constraints over Relations",
                            "Enforcing Integrity Constraints",
                            "Querying Relational Data",
                            "Logical Database Design",
                            "Introduction to Views",
                            "Destroying Tables and Views",
                            "Altering Tables and Views"
                        ]
                    },
                    {
                        "topic": "Relational Algebra and Calculus",
                        "subtopics": [
                            "Selection",
                            "Projection",
                            "Set Operations",
                            "Renaming",
                            "Joins",
                            "Division",
                            "Algebra Queries",
                            "Tuple Relational Calculus",
                            "Domain Relational Calculus",
                            "Expressive Power of Algebra and Calculus"
                        ]
                    }
                ]
            },
            {
                "module": 3,
                "title": "SQL Queries and Schema Refinement",
                "topics": [
                    {
                        "topic": "SQL Queries",
                        "subtopics": [
                            "Basic SQL Query",
                            "Union",
                            "Intersect",
                            "Except",
                            "Nested Queries",
                            "Correlated Nested Queries",
                            "Set-Comparison Operators",
                            "Aggregate Operators",
                            "Null Values",
                            "Comparison Using Null Values",
                            "AND",
                            "OR",
                            "NOT",
                            "Outer Joins",
                            "Disallowing Null Values",
                            "Complex Integrity Constraints",
                            "Triggers",
                            "Active Databases"
                        ]
                    },
                    {
                        "topic": "Schema Refinement",
                        "subtopics": [
                            "Problems Caused by Redundancy",
                            "Decompositions",
                            "Problems Related to Decomposition",
                            "Lossless Join Decomposition",
                            "Dependency Preserving Decomposition",
                            "Functional Dependencies",
                            "Reasoning about Functional Dependencies",
                            "First Normal Form",
                            "Second Normal Form",
                            "Third Normal Form",
                            "BCNF",
                            "Multivalued Dependencies",
                            "Fourth Normal Form"
                        ]
                    }
                ]
            },
            {
                "module": 4,
                "title": "Transaction Management and Recovery System",
                "topics": [
                    {
                        "topic": "Transaction Management",
                        "subtopics": [
                            "Transaction Concept",
                            "ACID Properties",
                            "Transaction State",
                            "Implementation of Atomicity and Durability",
                            "Implementation of Isolation",
                            "Concurrent Executions",
                            "Serializability",
                            "Testing for Serializability",
                            "Lock-Based Protocols",
                            "Timestamp-Based Protocols",
                            "Validation-Based Protocols",
                            "Multiple Granularity"
                        ]
                    },
                    {
                        "topic": "Recovery System",
                        "subtopics": [
                            "Failure Classification",
                            "Storage Structure",
                            "Recovery and Atomicity",
                            "Log-Based Recovery",
                            "Recovery with Concurrent Transactions",
                            "Buffer Management",
                            "Failure with Loss of Nonvolatile Storage",
                            "Advanced Recovery Techniques",
                            "Remote Backup Systems"
                        ]
                    }
                ]
            },
            {
                "module": 5,
                "title": "Storage and Indexing",
                "topics": [
                    {
                        "topic": "Storage and Indexing",
                        "subtopics": [
                            "Data on External Storage",
                            "File Organization",
                            "Indexing",
                            "Cluster Indexes",
                            "Primary Indexes",
                            "Secondary Indexes",
                            "Index Data Structures",
                            "Hash-Based Indexing",
                            "Tree-Based Indexing",
                            "Comparison of File Organizations",
                            "Indexes and Performance"
                        ]
                    },
                    {
                        "topic": "Tree-Structured Indexing",
                        "subtopics": [
                            "Intuitions for Tree Indexes",
                            "Indexed Sequential Access Methods (ISAM)",
                            "B+ Trees",
                            "Dynamic Index Structure"
                        ]
                    }
                ]
            }
        ]
    },


    # =========================================================
    # M2151 - PYTHON PROGRAMMING LAB
    # =========================================================

    {
        "semester": 3,
        "subject_code": "M2151",
        "subject_name": "Python Programming Lab",
        "modules": [
            {
                "module": 1,
                "title": "Python Programming Experiments",
                "topics": [
                    {
                        "topic": "Basic Input, Output and Arithmetic",
                        "subtopics": [
                            "User input using int, float and string",
                            "Display input data",
                            "Roots of a quadratic equation",
                            "Arithmetic operations",
                            "Addition",
                            "Subtraction",
                            "Multiplication",
                            "Division",
                            "Modulus"
                        ]
                    },
                    {
                        "topic": "Functions and Operators",
                        "subtopics": [
                            "Recursive functions",
                            "Non-recursive functions",
                            "Factorial",
                            "Arithmetic operators",
                            "Relational operators",
                            "Logical operators",
                            "Operator precedence",
                            "Expressions and statements",
                            "Assignment statements",
                            "Input and output",
                            "Comments"
                        ]
                    },
                    {
                        "topic": "Strings and Student Details",
                        "subtopics": [
                            "len",
                            "capitalize",
                            "find",
                            "isalnum",
                            "isalpha",
                            "isdigit",
                            "lower",
                            "islower",
                            "isupper",
                            "upper",
                            "lstrip",
                            "rstrip",
                            "isspace",
                            "istitle",
                            "partition",
                            "replace",
                            "join",
                            "split",
                            "count",
                            "decode",
                            "encode",
                            "swapcase",
                            "Student details"
                        ]
                    },
                    {
                        "topic": "Lists and Strings",
                        "subtopics": [
                            "List joining",
                            "List slices",
                            "len",
                            "insert",
                            "append",
                            "extend",
                            "sort",
                            "remove",
                            "reverse",
                            "pop",
                            "Palindrome checking"
                        ]
                    },
                    {
                        "topic": "Tuples",
                        "subtopics": [
                            "cmp",
                            "len",
                            "max",
                            "min",
                            "tuple",
                            "Searching for a word in tuple",
                            "Creating pairs using tuple"
                        ]
                    },
                    {
                        "topic": "Dictionaries",
                        "subtopics": [
                            "cmp",
                            "len",
                            "clear",
                            "get",
                            "has_key",
                            "items",
                            "keys",
                            "update",
                            "values",
                            "Animal dictionary"
                        ]
                    },
                    {
                        "topic": "Classes and Objects",
                        "subtopics": [
                            "Creating classes",
                            "Creating objects",
                            "Accessing attributes",
                            "Customer class",
                            "Balance",
                            "Withdraw",
                            "Deposit"
                        ]
                    },
                    {
                        "topic": "Exception Handling",
                        "subtopics": [
                            "Robust exception handling",
                            "Checking whether input is a float",
                            "File operation exceptions",
                            "Opening nonexistent files"
                        ]
                    },
                    {
                        "topic": "Polymorphism",
                        "subtopics": [
                            "Python polymorphism"
                        ]
                    },
                    {
                        "topic": "Directory and File Handling",
                        "subtopics": [
                            "Listing files in a directory",
                            "Open",
                            "Close",
                            "Read",
                            "Append",
                            "Move"
                        ]
                    },
                    {
                        "topic": "GUI Programming",
                        "subtopics": [
                            "GUI window",
                            "Two text fields",
                            "Submit button",
                            "Reset button"
                        ]
                    }
                ]
            }
        ]
    },


    # =========================================================
    # M2162 - DATABASE MANAGEMENT SYSTEMS LAB
    # =========================================================

    {
        "semester": 3,
        "subject_code": "M2162",
        "subject_name": "Database Management Systems Lab",
        "modules": [
            {
                "module": 1,
                "title": "Database Design and SQL Experiments",
                "topics": [
                    {
                        "topic": "ER Model and Roadway Travels",
                        "subtopics": [
                            "ER Model for Roadway Travels",
                            "Conceptual design with ER Model",
                            "Relational Model for Roadway Travels"
                        ]
                    },
                    {
                        "topic": "Normalization",
                        "subtopics": [
                            "Normalization techniques for Roadway Travels"
                        ]
                    },
                    {
                        "topic": "MySQL",
                        "subtopics": [
                            "Installation of MySQL",
                            "DDL commands",
                            "DML commands"
                        ]
                    },
                    {
                        "topic": "SQL Queries",
                        "subtopics": [
                            "Aggregate functions",
                            "GROUP BY",
                            "HAVING",
                            "Creating views",
                            "Dropping views"
                        ]
                    },
                    {
                        "topic": "Database Schema",
                        "subtopics": [
                            "Student table",
                            "Class table",
                            "Enrolled table",
                            "Faculty table"
                        ]
                    },
                    {
                        "topic": "SQL Query Practice",
                        "subtopics": [
                            "Queries without duplicates",
                            "Queries involving juniors",
                            "Queries involving classes",
                            "Queries involving students",
                            "Queries involving faculty",
                            "Queries involving enrolment"
                        ]
                    },
                    {
                        "topic": "Stored Procedures",
                        "subtopics": [
                            "Creation of stored procedures",
                            "Execution of procedures",
                            "Modification of procedures"
                        ]
                    },
                    {
                        "topic": "Hospital Management System",
                        "subtopics": [
                            "ER model",
                            "Hospital departments",
                            "Hospital rooms",
                            "Hospital doctors",
                            "Relational database schema",
                            "SQL queries",
                            "Recording query results"
                        ]
                    }
                ]
            }
        ]
    },


    # =========================================================
    # M2153 - INTERNSHIP-I
    # =========================================================

    {
        "semester": 3,
        "subject_code": "M2153",
        "subject_name": "Internship-I",
        "modules": []
    },


    # =========================================================
    # M21MC1 - ENVIRONMENTAL SCIENCE
    # =========================================================

    {
        "semester": 3,
        "subject_code": "M21MC1",
        "subject_name": "Environmental Science",
        "modules": [
            {
                "module": 1,
                "title": "Ecosystem and Natural Resources",
                "topics": [
                    {
                        "topic": "Natural Resources",
                        "subtopics": [
                            "Concept of resources",
                            "Classification of resources",
                            "Water resources",
                            "Land resources",
                            "Land degradation",
                            "Forest resources",
                            "Mineral resources",
                            "Energy resources"
                        ]
                    },
                    {
                        "topic": "Ecosystem",
                        "subtopics": [
                            "Concept of ecosystem",
                            "Classification of ecosystem",
                            "Functions of ecosystem"
                        ]
                    },
                    {
                        "topic": "Biodiversity",
                        "subtopics": [
                            "Biodiversity",
                            "Levels of biodiversity",
                            "Values of biodiversity",
                            "Biodiversity hotspots",
                            "Threats to biodiversity",
                            "Conservation of biodiversity"
                        ]
                    }
                ]
            },
            {
                "module": 2,
                "title": "Global Environmental Problems and Environmental Impact Assessment",
                "topics": [
                    {
                        "topic": "Global Environmental Problems and Global Efforts",
                        "subtopics": [
                            "Deforestation",
                            "Greenhouse effect",
                            "Global warming",
                            "Sea level rise",
                            "Ozone depletion",
                            "International conventions and protocols",
                            "Green belt development",
                            "Green building",
                            "Clean Development Mechanism (CDM)"
                        ]
                    },
                    {
                        "topic": "Environmental Impact Assessment",
                        "subtopics": [
                            "Definition of impact",
                            "Classification of impacts",
                            "Methods of baseline data acquisition",
                            "Impacts on human health",
                            "Impacts on resources",
                            "Impacts on air",
                            "Impacts on water",
                            "Impacts on flora",
                            "Impacts on fauna",
                            "Impacts on society",
                            "Impact assessment methodologies",
                            "Environmental Management Plan (EMP)"
                        ]
                    }
                ]
            },
            {
                "module": 3,
                "title": "Environmental Policy and Sustainable Future",
                "topics": [
                    {
                        "topic": "Environmental Policy, Legislation, Rules and Regulations",
                        "subtopics": [
                            "Environmental Protection Act",
                            "Air (Prevention and Control of Pollution) Act, 1981",
                            "Water (Prevention and Control of Pollution) Act, 1974",
                            "Forest Conservation Act"
                        ]
                    },
                    {
                        "topic": "Towards Sustainable Future",
                        "subtopics": [
                            "Concept of Sustainable Development",
                            "Threats to Sustainability",
                            "Strategies for achieving Sustainable Development",
                            "Environmental Ethics",
                            "Environmental Economics",
                            "Green Computing"
                        ]
                    }
                ]
            }
        ]
    }

]

semester_4 = [

    # =========================================================
    # M225B - COMPUTER ORGANIZATION AND ARCHITECTURE
    # =========================================================

    {
        "semester": 4,
        "subject_code": "M225B",
        "subject_name": "Computer Organization and Architecture",
        "modules": [
            {
                "module": 1,
                "title": "Digital Computers and Basic Computer Organization",
                "topics": [
                    {
                        "topic": "Digital Computers",
                        "subtopics": [
                            "Introduction",
                            "Block diagram of Digital Computer",
                            "Definition of Computer Organization",
                            "Computer Architecture",
                            "Central Processing Unit",
                            "General Register Organization"
                        ]
                    },
                    {
                        "topic": "Basic Computer Organization and Design",
                        "subtopics": [
                            "Instruction codes",
                            "Computer instructions",
                            "Timing and Control",
                            "Instruction cycle",
                            "Instruction formats",
                            "Memory Reference Instructions",
                            "Addressing modes",
                            "Data Transfer",
                            "Data Manipulation"
                        ]
                    }
                ]
            },
            {
                "module": 2,
                "title": "Register Transfer and Microprogrammed Control",
                "topics": [
                    {
                        "topic": "Register Transfer Language and Micro Operations",
                        "subtopics": [
                            "Register Transfer Language",
                            "Register Transfer",
                            "Bus and Memory Transfers",
                            "Arithmetic Micro Operations",
                            "Logic Micro Operations",
                            "Shift Micro Operations",
                            "Arithmetic Logic Shift Unit"
                        ]
                    },
                    {
                        "topic": "Microprogrammed Control",
                        "subtopics": [
                            "Control Memory",
                            "Address Sequencing",
                            "Microprogram Example",
                            "Design of Control Unit"
                        ]
                    }
                ]
            },
            {
                "module": 3,
                "title": "Data Representation and Computer Arithmetic",
                "topics": [
                    {
                        "topic": "Data Representation",
                        "subtopics": [
                            "Data Types",
                            "Complements",
                            "Fixed Point Representation",
                            "Floating Point Representation"
                        ]
                    },
                    {
                        "topic": "Computer Arithmetic",
                        "subtopics": [
                            "Addition and Subtraction",
                            "Multiplication Algorithms",
                            "Division Algorithms",
                            "Floating Point Arithmetic Operations",
                            "Decimal Arithmetic Unit",
                            "Decimal Arithmetic Operations"
                        ]
                    }
                ]
            },
            {
                "module": 4,
                "title": "Input-Output Organization and Memory",
                "topics": [
                    {
                        "topic": "Input-Output Organization",
                        "subtopics": [
                            "Input-Output Interface",
                            "Asynchronous Data Transfer",
                            "Modes of Transfer",
                            "Priority Interrupt",
                            "Direct Memory Access"
                        ]
                    },
                    {
                        "topic": "Memory Organization",
                        "subtopics": [
                            "Concept of Memory",
                            "RAM",
                            "ROM Memories",
                            "Memory Hierarchy",
                            "Cache Memory",
                            "Cache Mapping",
                            "Secondary Storage"
                        ]
                    }
                ]
            },
            {
                "module": 5,
                "title": "RISC, CISC and Pipelining",
                "topics": [
                    {
                        "topic": "Instruction Set Architecture",
                        "subtopics": [
                            "Reduced Instruction Set Computer",
                            "CISC Characteristics",
                            "RISC Characteristics"
                        ]
                    },
                    {
                        "topic": "Pipelining",
                        "subtopics": [
                            "Basic Concepts",
                            "Data Hazards",
                            "Instruction Hazards",
                            "Influence on Instruction Sets",
                            "Data Path Considerations",
                            "Control Considerations",
                            "Superscalar Operation"
                        ]
                    }
                ]
            }
        ]
    },


    # =========================================================
    # M225A - MATHEMATICAL FOUNDATIONS OF COMPUTER SCIENCE
    # =========================================================

    {
        "semester": 4,
        "subject_code": "M225A",
        "subject_name": "Mathematical Foundations of Computer Science",
        "modules": [
            {
                "module": 1,
                "title": "Mathematical Logic",
                "topics": [
                    {
                        "topic": "Propositional Logic",
                        "subtopics": [
                            "Statements and Notations",
                            "Connectives",
                            "Well-formed Formulas",
                            "Truth Tables",
                            "Tautology",
                            "Equivalence",
                            "Implication",
                            "Normal Forms",
                            "Quantifiers",
                            "Universal Quantifiers"
                        ]
                    },
                    {
                        "topic": "Predicates",
                        "subtopics": [
                            "Predicate Logic",
                            "Free Variables",
                            "Bound Variables",
                            "Rules of Inference",
                            "Consistency",
                            "Proof by Contradiction",
                            "Automatic Theorem Proving"
                        ]
                    }
                ]
            },
            {
                "module": 2,
                "title": "Relations, Functions and Algebraic Structures",
                "topics": [
                    {
                        "topic": "Relations",
                        "subtopics": [
                            "Properties of Binary Relations",
                            "Equivalence Relations",
                            "Transitive Closure",
                            "Compatibility",
                            "Partial Ordering Relations",
                            "Lattices",
                            "Hasse Diagram"
                        ]
                    },
                    {
                        "topic": "Functions",
                        "subtopics": [
                            "Inverse Function",
                            "Composition of Functions",
                            "Recursive Functions",
                            "Lattice and its Properties"
                        ]
                    },
                    {
                        "topic": "Algebraic Structures",
                        "subtopics": [
                            "Algebraic Systems",
                            "Examples and General Properties",
                            "Semigroups",
                            "Monoids",
                            "Groups",
                            "Subgroups",
                            "Homomorphism",
                            "Isomorphism"
                        ]
                    }
                ]
            },
            {
                "module": 3,
                "title": "Elementary Combinatorics",
                "topics": [
                    {
                        "topic": "Counting Techniques",
                        "subtopics": [
                            "Basis of Counting",
                            "Combinations",
                            "Permutations",
                            "Permutations with Repetitions",
                            "Constrained Repetitions",
                            "Binomial Coefficients",
                            "Binomial Theorem",
                            "Multinomial Theorem"
                        ]
                    },
                    {
                        "topic": "Counting Principles",
                        "subtopics": [
                            "Principle of Inclusion",
                            "Principle of Exclusion",
                            "Pigeonhole Principle",
                            "Applications of Pigeonhole Principle"
                        ]
                    }
                ]
            },
            {
                "module": 4,
                "title": "Generating Functions and Recurrence Relations",
                "topics": [
                    {
                        "topic": "Generating Functions",
                        "subtopics": [
                            "Generating Functions",
                            "Functions of Sequences",
                            "Calculating Coefficients of Generating Functions"
                        ]
                    },
                    {
                        "topic": "Recurrence Relations",
                        "subtopics": [
                            "Solving Recurrence Relations by Substitution",
                            "Solving Recurrence Relations using Generating Functions",
                            "Characteristic Roots",
                            "Solution of Inhomogeneous Recurrence Relations"
                        ]
                    }
                ]
            },
            {
                "module": 5,
                "title": "Graph Theory",
                "topics": [
                    {
                        "topic": "Graph Theory",
                        "subtopics": [
                            "Representation of Graphs",
                            "Depth First Search",
                            "Breadth First Search",
                            "Spanning Trees",
                            "Planar Graphs"
                        ]
                    },
                    {
                        "topic": "Applications of Graph Theory",
                        "subtopics": [
                            "Basic Concepts",
                            "Isomorphism",
                            "Subgraphs",
                            "Multigraphs",
                            "Euler Circuits",
                            "Hamiltonian Graphs",
                            "Chromatic Numbers"
                        ]
                    }
                ]
            }
        ]
    },


    # =========================================================
    # M226A - OBJECT ORIENTED PROGRAMMING THROUGH JAVA
    # =========================================================

    {
        "semester": 4,
        "subject_code": "M226A",
        "subject_name": "Object Oriented Programming through Java",
        "modules": [
            {
                "module": 1,
                "title": "Java Fundamentals, Classes and Objects",
                "topics": [
                    {
                        "topic": "Introduction to Java",
                        "subtopics": [
                            "OOP Concepts",
                            "History of Java",
                            "Java Buzzwords",
                            "Data Types",
                            "Variables",
                            "Scope and Lifetime of Variables",
                            "Arrays",
                            "Operators",
                            "Expressions",
                            "Control Statements",
                            "Type Conversion",
                            "Casting",
                            "Simple Java Program"
                        ]
                    },
                    {
                        "topic": "Classes and Objects",
                        "subtopics": [
                            "Classes",
                            "Objects",
                            "Constructors",
                            "Methods",
                            "this Keyword",
                            "Garbage Collection",
                            "Method Overloading",
                            "Constructor Overloading",
                            "Parameter Passing",
                            "Recursion"
                        ]
                    },
                    {
                        "topic": "String Handling",
                        "subtopics": [
                            "String",
                            "StringBuffer",
                            "StringTokenizer"
                        ]
                    }
                ]
            },
            {
                "module": 2,
                "title": "Inheritance and Interfaces",
                "topics": [
                    {
                        "topic": "Inheritance",
                        "subtopics": [
                            "Base Class Object",
                            "Subclass",
                            "Member Access Rules",
                            "super",
                            "final with Inheritance",
                            "Method Overriding",
                            "Abstract Classes"
                        ]
                    },
                    {
                        "topic": "Interfaces",
                        "subtopics": [
                            "Defining an Interface",
                            "Implementing Interfaces",
                            "Classes versus Interfaces",
                            "Extending Interfaces"
                        ]
                    }
                ]
            },
            {
                "module": 3,
                "title": "Packages and Exception Handling",
                "topics": [
                    {
                        "topic": "Packages",
                        "subtopics": [
                            "Defining Packages",
                            "Creating Packages",
                            "Accessing Packages",
                            "Importing Packages",
                            "Access Control",
                            "java.io Package"
                        ]
                    },
                    {
                        "topic": "Exception Handling",
                        "subtopics": [
                            "Exception Handling Concepts",
                            "Benefits of Exception Handling",
                            "Exception Hierarchy",
                            "Checked Exceptions",
                            "Unchecked Exceptions",
                            "try",
                            "catch",
                            "throw",
                            "throws",
                            "finally",
                            "Built-in Exceptions",
                            "User-defined Exception Subclasses"
                        ]
                    }
                ]
            },
            {
                "module": 4,
                "title": "Multithreading and Event Handling",
                "topics": [
                    {
                        "topic": "Multithreading",
                        "subtopics": [
                            "Multithreading",
                            "Multitasking",
                            "Thread Life Cycle",
                            "Creating Threads",
                            "Synchronizing Threads",
                            "Daemon Threads",
                            "Thread Groups"
                        ]
                    },
                    {
                        "topic": "Event Handling and AWT",
                        "subtopics": [
                            "Events",
                            "Event Sources",
                            "Event Classes",
                            "Event Listeners",
                            "Delegation Event Model",
                            "Mouse Events",
                            "Keyboard Events",
                            "Adapter Classes",
                            "AWT Class Hierarchy",
                            "Labels",
                            "Buttons",
                            "Canvas",
                            "Scrollbars",
                            "Text Components",
                            "Checkboxes",
                            "Checkbox Groups",
                            "Choices",
                            "Lists"
                        ]
                    }
                ]
            },
            {
                "module": 5,
                "title": "Layout Managers and Swing",
                "topics": [
                    {
                        "topic": "Layout Managers",
                        "subtopics": [
                            "Border Layout",
                            "Grid Layout",
                            "Flow Layout",
                            "Card Layout",
                            "Grid Bag Layout"
                        ]
                    },
                    {
                        "topic": "Swing",
                        "subtopics": [
                            "Introduction to Swing",
                            "Limitations of AWT",
                            "Components",
                            "Containers",
                            "JFrame",
                            "JComponent",
                            "Icons and Labels",
                            "Text Fields",
                            "JButton",
                            "Checkboxes",
                            "Radio Buttons",
                            "Combo Boxes",
                            "Tabbed Panes",
                            "Scroll Panes",
                            "Trees",
                            "Tables"
                        ]
                    }
                ]
            }
        ]
    },


    # =========================================================
    # M225F - OPERATING SYSTEMS
    # =========================================================

    {
        "semester": 4,
        "subject_code": "M225F",
        "subject_name": "Operating Systems",
        "modules": [
            {
                "module": 1,
                "title": "Basic Concepts",
                "topics": [
                    {
                        "topic": "Operating System Overview",
                        "subtopics": [
                            "OS Introduction",
                            "Computer Systems Organization",
                            "Computer System Architecture",
                            "Operating System Architecture",
                            "Resource Management",
                            "Virtualization",
                            "Distributed Systems",
                            "Open-source Operating Systems"
                        ]
                    },
                    {
                        "topic": "Operating System Structures",
                        "subtopics": [
                            "System Calls",
                            "System Services",
                            "Linkers and Loaders",
                            "Operating System Design and Implementation",
                            "Operating System Structure",
                            "Building an Operating System",
                            "Booting an Operating System"
                        ]
                    }
                ]
            },
            {
                "module": 2,
                "title": "Process Management",
                "topics": [
                    {
                        "topic": "Process Concepts",
                        "subtopics": [
                            "Process Introduction",
                            "Process Scheduling",
                            "Interprocess Communication",
                            "Communication in Client-Server Systems",
                            "Thread Concepts",
                            "Multithreading Models",
                            "Scheduling Criteria",
                            "Scheduling Algorithms",
                            "Algorithm Evaluation"
                        ]
                    },
                    {
                        "topic": "Process Synchronization and Deadlocks",
                        "subtopics": [
                            "Critical Section Problem",
                            "Peterson's Solution",
                            "Synchronization Hardware",
                            "Semaphores",
                            "Mutex Locks",
                            "Monitors",
                            "Classic Synchronization Problems",
                            "System Model",
                            "Deadlock Characterization",
                            "Deadlock Prevention",
                            "Deadlock Detection",
                            "Deadlock Avoidance",
                            "Recovery from Deadlock"
                        ]
                    }
                ]
            },
            {
                "module": 3,
                "title": "Memory Management",
                "topics": [
                    {
                        "topic": "Main Memory",
                        "subtopics": [
                            "Main Memory Background",
                            "Contiguous Memory Allocation",
                            "Paging",
                            "Page-table Structure",
                            "Swapping",
                            "Segmentation"
                        ]
                    },
                    {
                        "topic": "Virtual Memory",
                        "subtopics": [
                            "Virtual Memory Background",
                            "Demand Paging",
                            "Page Replacement Algorithms",
                            "Frame Allocation",
                            "Thrashing"
                        ]
                    }
                ]
            },
            {
                "module": 4,
                "title": "Storage Management",
                "topics": [
                    {
                        "topic": "File System Management",
                        "subtopics": [
                            "File Concepts",
                            "Access Methods",
                            "Directory Structure",
                            "File Protection",
                            "File System Structure",
                            "File System Operations",
                            "Directory Implementation",
                            "Allocation Methods",
                            "Free-space Management",
                            "Efficiency and Performance",
                            "Recovery"
                        ]
                    },
                    {
                        "topic": "Mass Storage Structure",
                        "subtopics": [
                            "Mass Storage Overview",
                            "Disk Scheduling",
                            "Storage Device Management",
                            "Swap-space Management",
                            "Storage Attachment",
                            "RAID Structure"
                        ]
                    }
                ]
            },
            {
                "module": 5,
                "title": "Security and Protection",
                "topics": [
                    {
                        "topic": "Security",
                        "subtopics": [
                            "Security Problem",
                            "Program Threats",
                            "System Threats",
                            "Network Threats",
                            "Cryptography as a Security Tool",
                            "User Authentication",
                            "Implementing Security Defenses",
                            "Case Study: Windows 10"
                        ]
                    },
                    {
                        "topic": "Protection",
                        "subtopics": [
                            "Goals of Protection",
                            "Principles of Protection",
                            "Protection Rings",
                            "Domain of Protection",
                            "Access Matrix",
                            "Implementation of Access Matrix",
                            "Revocation of Access Rights",
                            "Role-based Access Control",
                            "Capability-based Systems",
                            "Language-based Protection"
                        ]
                    }
                ]
            }
        ]
    },


    # =========================================================
    # M225E - COMPUTER NETWORKS
    # =========================================================

    {
        "semester": 4,
        "subject_code": "M225E",
        "subject_name": "Computer Networks",
        "modules": [
            {
                "module": 1,
                "title": "Internet Overview and Physical Layer",
                "topics": [
                    {
                        "topic": "Internet and Protocol Models",
                        "subtopics": [
                            "Protocol",
                            "Layering Scenario",
                            "TCP/IP Protocol Suite",
                            "OSI Model",
                            "Internet History",
                            "Standards and Administration",
                            "OSI versus TCP/IP Reference Model"
                        ]
                    },
                    {
                        "topic": "Physical Layer",
                        "subtopics": [
                            "Guided Transmission Media",
                            "Wireless Transmission Media"
                        ]
                    }
                ]
            },
            {
                "module": 2,
                "title": "Data Link Layer",
                "topics": [
                    {
                        "topic": "Data Link Layer",
                        "subtopics": [
                            "Design Issues",
                            "Framing",
                            "Error Detection",
                            "Error Correction",
                            "Block Coding",
                            "Hamming Distance",
                            "CRC",
                            "Flow Control",
                            "Error Control",
                            "Stop-and-Wait Protocols",
                            "Sliding Window Protocols"
                        ]
                    },
                    {
                        "topic": "Connecting Devices",
                        "subtopics": [
                            "Repeaters",
                            "Hubs",
                            "Switches",
                            "Gateways",
                            "Bridges",
                            "Learning Bridges",
                            "Spanning Tree Bridges"
                        ]
                    },
                    {
                        "topic": "Multiple Access Protocols",
                        "subtopics": [
                            "Random Access",
                            "ALOHA",
                            "CSMA",
                            "CSMA/CD",
                            "CSMA/CA",
                            "Ethernet",
                            "IEEE 802.11"
                        ]
                    }
                ]
            },
            {
                "module": 3,
                "title": "Network Layer",
                "topics": [
                    {
                        "topic": "Network Layer",
                        "subtopics": [
                            "Network Layer Design Issues",
                            "Store-and-forward Packet Switching",
                            "Connectionless Network Services",
                            "Connection-oriented Network Services"
                        ]
                    },
                    {
                        "topic": "Internetworking",
                        "subtopics": [
                            "IPv4",
                            "IPv6",
                            "Logical Addressing",
                            "IPv4 Addressing",
                            "IPv6 Addressing",
                            "Tunneling",
                            "Packet Fragmentation"
                        ]
                    },
                    {
                        "topic": "Address Mapping and Routing",
                        "subtopics": [
                            "ARP",
                            "RARP",
                            "DHCP",
                            "ICMP",
                            "IGMP",
                            "Shortest Path Routing",
                            "Distance Vector Routing"
                        ]
                    }
                ]
            },
            {
                "module": 4,
                "title": "Transport Layer",
                "topics": [
                    {
                        "topic": "Transport Layer",
                        "subtopics": [
                            "Process-to-Process Communication",
                            "UDP",
                            "TCP",
                            "TCP Connection Establishment",
                            "TCP Connection Release",
                            "Crash Recovery",
                            "TCP Sliding Window",
                            "TCP Congestion Control"
                        ]
                    },
                    {
                        "topic": "Quality of Service",
                        "subtopics": [
                            "Improving Quality of Service",
                            "Leaky Bucket Algorithm"
                        ]
                    }
                ]
            },
            {
                "module": 5,
                "title": "Application Layer",
                "topics": [
                    {
                        "topic": "Application Layer",
                        "subtopics": [
                            "Introduction",
                            "Application Layer Services",
                            "Application Layer Paradigms"
                        ]
                    },
                    {
                        "topic": "Internet Applications",
                        "subtopics": [
                            "DNS",
                            "WWW",
                            "HTTP",
                            "FTP",
                            "Electronic Mail",
                            "TELNET",
                            "SNMP",
                            "SSH"
                        ]
                    }
                ]
            }
        ]
    },


    # =========================================================
    # M2261 - OBJECT ORIENTED PROGRAMMING THROUGH JAVA LAB
    # =========================================================

    {
        "semester": 4,
        "subject_code": "M2261",
        "subject_name": "Object Oriented Programming through Java Lab",
        "modules": [
            {
                "module": 1,
                "title": "Java Programming Experiments",
                "topics": [
                    {
                        "topic": "Constructors and Method Overloading",
                        "subtopics": [
                            "Constructor",
                            "Parameterized Constructor",
                            "Method Overloading",
                            "Constructor Overloading"
                        ]
                    },
                    {
                        "topic": "String and Collection Processing",
                        "subtopics": [
                            "Palindrome Checking",
                            "Sorting Names",
                            "StringTokenizer",
                            "Reading Integers",
                            "Displaying Integers",
                            "Calculating Sum"
                        ]
                    },
                    {
                        "topic": "Java Keywords and Inheritance",
                        "subtopics": [
                            "this",
                            "super",
                            "static",
                            "final",
                            "Method Overriding",
                            "Dynamic Method Dispatch",
                            "Multiple Inheritance",
                            "Access Specifiers"
                        ]
                    },
                    {
                        "topic": "File Handling",
                        "subtopics": [
                            "Checking File Existence",
                            "Checking Readability",
                            "Checking Writability",
                            "File Type",
                            "File Length",
                            "Reading Files",
                            "Line Numbering",
                            "Counting Characters",
                            "Counting Lines",
                            "Counting Words"
                        ]
                    },
                    {
                        "topic": "Exception Handling",
                        "subtopics": [
                            "Checked Exceptions",
                            "Unchecked Exceptions"
                        ]
                    },
                    {
                        "topic": "Multithreading",
                        "subtopics": [
                            "Creating Multiple Threads",
                            "Thread Timing",
                            "Inter-thread Communication",
                            "Producer Consumer Problem"
                        ]
                    },
                    {
                        "topic": "GUI and Event Handling",
                        "subtopics": [
                            "Calculator using Grid Layout",
                            "Mouse Events",
                            "Keyboard Events",
                            "Integer Division GUI",
                            "Number Format Exception",
                            "Arithmetic Exception",
                            "Traffic Light Simulation",
                            "Radio Buttons",
                            "Drawing Lines",
                            "Drawing Rectangles",
                            "Drawing Ovals",
                            "JTable",
                            "Displaying CSV-style Table Data"
                        ]
                    }
                ]
            }
        ]
    },


    # =========================================================
    # M2252 - OPERATING SYSTEMS LAB
    # =========================================================

    {
        "semester": 4,
        "subject_code": "M2252",
        "subject_name": "Operating Systems Lab",
        "modules": [
            {
                "module": 1,
                "title": "Operating Systems Laboratory Experiments",
                "topics": [
                    {
                        "topic": "CPU Scheduling",
                        "subtopics": [
                            "FCFS",
                            "SJF",
                            "Priority Scheduling",
                            "Round Robin"
                        ]
                    },
                    {
                        "topic": "Deadlock",
                        "subtopics": [
                            "Banker's Algorithm for Deadlock Avoidance",
                            "Banker's Algorithm for Deadlock Prevention"
                        ]
                    },
                    {
                        "topic": "File Allocation",
                        "subtopics": [
                            "Sequential Allocation",
                            "Indexed Allocation",
                            "Linked Allocation"
                        ]
                    },
                    {
                        "topic": "Memory Management",
                        "subtopics": [
                            "MVT",
                            "MFT"
                        ]
                    },
                    {
                        "topic": "File Organization",
                        "subtopics": [
                            "Single Level Directory",
                            "Two Level Directory",
                            "Hierarchical Directory",
                            "DAG Directory"
                        ]
                    },
                    {
                        "topic": "Page Replacement",
                        "subtopics": [
                            "FIFO",
                            "LRU",
                            "Optimal"
                        ]
                    },
                    {
                        "topic": "Disk Scheduling",
                        "subtopics": [
                            "FCFS",
                            "SSTF",
                            "CSCAN",
                            "CLOOK"
                        ]
                    },
                    {
                        "topic": "Linux System Programming",
                        "subtopics": [
                            "fork",
                            "Shared Memory",
                            "Semaphores"
                        ]
                    }
                ]
            }
        ]
    },


    # =========================================================
    # M2253 - NODE JS / REACT JS / DJANGO
    # =========================================================

    {
        "semester": 4,
        "subject_code": "M2253",
        "subject_name": "Node JS/React JS/Django",
        "modules": [
            {
                "module": 1,
                "title": "Web Application Development",
                "topics": [
                    {
                        "topic": "Responsive Web Application",
                        "subtopics": [
                            "HTML",
                            "CSS3",
                            "Flex",
                            "Grid",
                            "Shopping Cart",
                            "Registration",
                            "Login",
                            "Catalog",
                            "Cart Pages",
                            "Bootstrap"
                        ]
                    },
                    {
                        "topic": "JavaScript",
                        "subtopics": [
                            "Client-side Validation",
                            "ES6",
                            "Arrow Functions",
                            "Callbacks",
                            "Promises",
                            "async/await"
                        ]
                    },
                    {
                        "topic": "Web APIs and Database",
                        "subtopics": [
                            "OpenWeatherMap API",
                            "Weather Information",
                            "Graphical Weather Display",
                            "Java Stand-alone Application",
                            "MySQL Connection",
                            "CRUD Operations",
                            "XML",
                            "DTD",
                            "XSD"
                        ]
                    },
                    {
                        "topic": "Java Web Technologies",
                        "subtopics": [
                            "Servlets",
                            "Controllers",
                            "Database Interaction",
                            "Cookies",
                            "HTTP Session",
                            "Session Tracking"
                        ]
                    },
                    {
                        "topic": "Node JS",
                        "subtopics": [
                            "Custom HTTP Server",
                            "HTTP Module",
                            "OS Module",
                            "Path Module",
                            "Event Module",
                            "Express",
                            "REST API",
                            "CRUD Operations",
                            "Postman",
                            "JWT",
                            "Authorized Endpoints"
                        ]
                    },
                    {
                        "topic": "React JS",
                        "subtopics": [
                            "React Application",
                            "Student Management System",
                            "Registration Page",
                            "Login Page",
                            "Contact Page",
                            "About Page",
                            "Routing",
                            "React Services",
                            "Weather API",
                            "Current Weather",
                            "Historical Weather",
                            "Chart.js",
                            "TODO Application",
                            "GitHub Deployment"
                        ]
                    }
                ]
            }
        ]
    },


    # =========================================================
    # M22MC2 - GENDER SENSITIZATION
    # =========================================================

    {
        "semester": 4,
        "subject_code": "M22MC2",
        "subject_name": "Gender Sensitization",
        "modules": [
            {
                "module": 1,
                "title": "Understanding Gender",
                "topics": [
                    {
                        "topic": "Understanding Gender",
                        "subtopics": [
                            "Why Should We Study Gender?",
                            "Towards a World of Equals",
                            "Socialization",
                            "Making Women",
                            "Making Men",
                            "Preparing for Womanhood",
                            "Growing up Male",
                            "First Lessons in Caste",
                            "Different Masculinities"
                        ]
                    }
                ]
            },
            {
                "module": 2,
                "title": "Gender and Biology",
                "topics": [
                    {
                        "topic": "Gender and Biology",
                        "subtopics": [
                            "Missing Women",
                            "Sex Selection and Its Consequences",
                            "Declining Sex Ratio",
                            "Demographic Consequences",
                            "Gender Spectrum",
                            "Beyond the Binary",
                            "Two or Many?",
                            "Struggles with Discrimination"
                        ]
                    }
                ]
            },
            {
                "module": 3,
                "title": "Gender and Labour",
                "topics": [
                    {
                        "topic": "Gender and Labour",
                        "subtopics": [
                            "Housework",
                            "The Invisible Labour",
                            "My Mother Doesn't Work",
                            "Share the Load",
                            "Women's Work",
                            "Politics and Economics",
                            "Fact and Fiction",
                            "Unrecognized and Unaccounted Work",
                            "Wages and Conditions of Work"
                        ]
                    }
                ]
            },
            {
                "module": 4,
                "title": "Issues of Violence-I",
                "topics": [
                    {
                        "topic": "Sexual Harassment",
                        "subtopics": [
                            "Say No!",
                            "Sexual Harassment",
                            "Everyday Harassment",
                            "Coping with Everyday Harassment",
                            "Chupulu"
                        ]
                    },
                    {
                        "topic": "Domestic Violence",
                        "subtopics": [
                            "Speaking Out",
                            "Is Home a Safe Place?",
                            "When Women Unite",
                            "Rebuilding Lives",
                            "New Forums for Justice"
                        ]
                    }
                ]
            },
            {
                "module": 5,
                "title": "Issues of Violence-II",
                "topics": [
                    {
                        "topic": "Sexual Violence",
                        "subtopics": [
                            "Thinking about Sexual Violence",
                            "Blaming the Victim",
                            "I Fought for my Life",
                            "The Caste Face of Violence"
                        ]
                    }
                ]
            }
        ]
    },


    # =========================================================
    # M22AC1 - LINGUASKILL FOR PROFESSIONALS-B2
    # =========================================================

    {
        "semester": 4,
        "subject_code": "M22AC1",
        "subject_name": "Linguaskill for Professionals - B2",
        "modules": [
            {
                "module": 1,
                "title": "A1 Level Communication",
                "topics": [
                    {
                        "topic": "Unit 1",
                        "subtopics": [
                            "Tenses",
                            "Clauses and Conditionals",
                            "Questions",
                            "Character Adjectives",
                            "Words Connected with Get",
                            "Trying and Succeeding",
                            "Letter e and g",
                            "Rapid Speech",
                            "Intonation in Question Tags"
                        ]
                    },
                    {
                        "topic": "Unit 2",
                        "subtopics": [
                            "Breaking off a Conversation",
                            "Explaining and Checking Understanding",
                            "Agreeing",
                            "Giving Compliments and Responding",
                            "Listening Activity 1",
                            "Listening Activity 2",
                            "Reading Activity 1",
                            "Reading Activity 2",
                            "Speaking Activity 1",
                            "Speaking Activity 2",
                            "Articles",
                            "Guidelines"
                        ]
                    }
                ]
            },
            {
                "module": 2,
                "title": "A2 Level Communication",
                "topics": [
                    {
                        "topic": "Unit 1",
                        "subtopics": [
                            "Multi-word Verbs",
                            "Used to and Would",
                            "Words Related to Ability",
                            "Achievements and Sports",
                            "Cause and Result",
                            "Consonant Sounds",
                            "Sound u",
                            "Word Stress"
                        ]
                    },
                    {
                        "topic": "Unit 2",
                        "subtopics": [
                            "Making Suggestions",
                            "Describing Photos",
                            "Expressing Disagreement",
                            "Listening Activity 1",
                            "Listening Activity 2",
                            "Reading Activity 1",
                            "Reading Activity 2",
                            "Speaking Activity 1",
                            "Speaking Activity 2",
                            "Job Application",
                            "For and Against Essay"
                        ]
                    }
                ]
            },
            {
                "module": 3,
                "title": "B1 Level Communication",
                "topics": [
                    {
                        "topic": "Unit 1",
                        "subtopics": [
                            "Infinitives and -ing Forms",
                            "Passives",
                            "Attitude Adjectives",
                            "Words Related to Natural World and Travel",
                            "Sound th",
                            "Consonant Clusters",
                            "Intonation"
                        ]
                    },
                    {
                        "topic": "Unit 2",
                        "subtopics": [
                            "Responding to an Idea",
                            "Discussing Advantages and Disadvantages",
                            "Listening Activity 1",
                            "Listening Activity 2",
                            "Reading Activity 1",
                            "Reading Activity 2",
                            "Speaking Activity 1",
                            "Speaking Activity 2",
                            "Travel Blog",
                            "Complaint Email"
                        ]
                    }
                ]
            },
            {
                "module": 4,
                "title": "B1+ Level Communication",
                "topics": [
                    {
                        "topic": "Unit 1",
                        "subtopics": [
                            "Too",
                            "Enough",
                            "So and Such",
                            "Words Related to Life in Cities",
                            "Money and Finance",
                            "Crime and Film",
                            "Sound o",
                            "Sound l"
                        ]
                    },
                    {
                        "topic": "Unit 2",
                        "subtopics": [
                            "Imagining",
                            "Vague Language",
                            "Encouraging",
                            "Listening Activity 1",
                            "Listening Activity 2",
                            "Reading Activity 1",
                            "Reading Activity 2",
                            "Speaking Activity 1",
                            "Speaking Activity 2",
                            "Review",
                            "Opinion Essay"
                        ]
                    }
                ]
            },
            {
                "module": 5,
                "title": "B2 Level Communication",
                "topics": [
                    {
                        "topic": "Unit 1",
                        "subtopics": [
                            "Relative Clauses",
                            "Reported Speech",
                            "Words Related to Health",
                            "Thought and Knowledge",
                            "Sound ui",
                            "Linking"
                        ]
                    },
                    {
                        "topic": "Unit 2",
                        "subtopics": [
                            "Expressing Uncertainty",
                            "Clarifying a Misunderstanding",
                            "Interrupting",
                            "Announcing News",
                            "Listening Activity 1",
                            "Listening Activity 2",
                            "Reading Activity 1",
                            "Reading Activity 2",
                            "Speaking Activity 1",
                            "Speaking Activity 2",
                            "Story Writing"
                        ]
                    }
                ]
            }
        ]
    }

]

# Insert / replace Semester I,II,III and Semester IV syllabus

all_syllabus = semester_1 + semester_2 + semester_3 + semester_4

for syllabus in all_syllabus:
    collection.replace_one(
        {
            "semester": syllabus["semester"],
            "subject_code": syllabus["subject_code"]
        },
        syllabus,
        upsert=True
    )

print("Semester I, II, III and IV syllabus inserted successfully!")
print("Total syllabus records:", len(all_syllabus))