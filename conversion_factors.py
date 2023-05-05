# Conversion factors for volume units

volume_conversion_factors = {
    'm3': 1,                    # 1 m³ = 1 m³
    'L': 1e-3,                  # convert litres to m³
    'mL': 1e-6,                 # convert millilitres to m³
    'gal': 0.00378541,          # convert gallons to m³
    'qt': 0.000946353,          # convert quarts to m³
    'pt': 0.000473176,          # convert pints to m³
    'fl_oz': 2.95735e-5,        # convert fluid ounces to m³
    'cu_in': 1.63871e-5,        # convert cubic inches to m³
    'cu_ft': 0.0283168,         # convert cubic feet to m³
    'cu_yard': 0.764555,        # convert cubic yard to m³
    'BBL': 0.158987294928,      # convert barrel to m³
    'BF_1000': 2.35974          # convert 1000 board feet to m³
}

# Conversion factors for mass/weight units
mass_conversion_factors = {
    'kg': 1,                    # 1 kg = 1 kg
    'g': 1e-3,                  # convert grams to kg
    'mg': 1e-6,                 # convert milligrams to kg
    'lb': 0.45359237,           # convert pounds to kg
    'oz': 0.0283495,            # convert ounces to kg
    'troy_oz': 0.0311035,       # convert troy ounces to kg
    'kt': 0.0002,               # convert karats value to kg
    'ton': 907.185,             # convert ton to kg
    'long_ton': 1016.05,        # convert long ton (UK) to kg
    't': 1000,                  # convert metric ton to kg
    'BU_60': 27.2155            # convert 60 lbs to kg
}
