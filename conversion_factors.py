# Conversion factors for volume units
volume_conversion_factors = {
    'm3': 1,                     # 1 m³ = 1 m³
    'L': 1e-3,                   # convert value to m³
    'mL': 1e-6,                  # convert value to m³
    'gal': 0.00378541,           # convert value to m³
    'qt': 0.000946353,           # convert value to m³
    'pt': 0.000473176,           # convert value to m³
    'fl_oz': 2.95735e-5,         # convert value to m³
    'cu_in': 1.63871e-5,         # convert value to m³
    'cu_ft': 0.0283168           # convert value to m³
}

# Conversion factors for mass/weight units
mass_conversion_factors = {
    'kg': 1,                      # assuming value is in kg
    'g': 1e-3,                   # convert value to kg
    'mg': 1e-6,                  # convert value to kg
    'lb': 0.45359237,            # convert value to kg
    'oz': 0.0283495,             # convert value to kg
    'troy_oz': 0.0311035,        # convert value to kg
    'kt': 0.0002,                # convert value to kg
    'ton': 907.185,              # convert value to kg
    'long_ton': 1016.05,         # convert value to kg
    't': 1000                    # convert value to kg
}