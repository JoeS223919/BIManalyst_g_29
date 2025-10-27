import ifcopenshell

def checkRule(beam_info_dict, concrete_strength_mpa=25):
    results = {}

    for beam_id, dimensions in beam_info_dict.items():
        # Extract dimensions
        width_mm = dimensions.get('b')
        height_mm = dimensions.get('h')
        length_mm = dimensions.get('l')

        if not all([width_mm, height_mm, length_mm]):
            results[beam_id] = None  # Incomplete data
            continue

        if length_mm < 500:
            continue

        # Convert mm to meters
        width_m = width_mm / 1000
        height_m = height_mm / 1000
        length_m = length_mm / 1000

        # Convert MPa to N/m²
        f_c = concrete_strength_mpa * 10**6

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

    return results