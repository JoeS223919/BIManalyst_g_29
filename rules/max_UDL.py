import ifcopenshell

def checkRule(beam_info_dict):
    results = {}

    for beam_id, dimensions in beam_info_dict.items():
        # Extract dimensions
        width_mm = dimensions.get('b')
        height_mm = dimensions.get('h')
        length_mm = dimensions.get('l')
        radius_mm = dimensions.get('r')
        thickness_body_mm = dimensions.get('tw') 
        thickness_flange_mm = dimensions.get('tf')

        if not all([width_mm, height_mm, length_mm]):
            results[beam_id] = None  # Incomplete data
            continue

        if length_mm < 500:
            continue

        # Convert mm to meters
        width_m = width_mm / 1000
        height_m = height_mm / 1000
        length_m = length_mm / 1000
        radius_m = radius_mm / 1000
        thickness_body_m = thickness_body_mm / 1000
        thickness_flange_m = thickness_flange_mm / 1000

        if "HEM".lower() in dimensions.get('Name').lower():
            material_strength_mpa = 250  # Example: 250 MPa for structural steel

            results[beam_id] = max_uniform_load_kn_per_m
        
        elif "concrete".lower() in dimensions.get('Name').lower():
            material_strength_mpa = 30  # Example: 30 MPa for normal concrete
            
            # Convert MPa to N/m²
            f_c = material_strength_mpa * 10**6

            # Allowable bending stress (approximate factor for concrete)
            allowable_stress = 0.45 * f_c

            # Section modulus (S) for rectangular section
            section_modulus = (width_m * height_m**2) / 6  # in m³

            # Maximum uniform load formula: w = (8 * f * S) / L²
            max_uniform_load_n_per_m = (8 * allowable_stress * section_modulus) / (length_m**2)

            # Convert N/m to kN/m
            max_uniform_load_kn_per_m = max_uniform_load_n_per_m / 1000

            # Store result
            results[beam_id] = max_uniform_load_kn_per_m
        
        elif "glulam".lower() in dimensions.get('Name').lower():

            results[beam_id] = max_uniform_load_kn_per_m
    

    return results