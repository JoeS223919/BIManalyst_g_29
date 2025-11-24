import ifcopenshell
from rules import i_beam_ULC
from rules import Glulam_ULC
from rules import Concrete_ULC

def checkRule(beam_info_dict):
    results = {}

    for beam_id, dimensions in beam_info_dict.items():
        # Extract dimensions
        width_mm = dimensions.get('b')
        height_mm = dimensions.get('h')
        length_mm = dimensions.get('l')
        thickness_body_mm = dimensions.get('tw') 
        thickness_flange_mm = dimensions.get('tf')

        if not all([width_mm, height_mm, length_mm]):
            results[beam_id] = None  # Incomplete data
            continue

        if length_mm < 500:
            results[beam_id] = None  # Length too short for calculation
            continue
        
        
        # Convert length to meters  
        length_m = length_mm / 1000

        if "HEM".lower() in dimensions.get('Name').lower():
            # Example: 250 MPa for structural steel
            material_strength_mpa = 250

            # Calculate maximum uniform load using i_beam_ULC module
            results[beam_id] = i_beam_ULC.uniform_load_capacity(height_mm, width_mm, thickness_body_mm, thickness_flange_mm, length_m, material_strength_mpa), 'Steel'
        
        elif "concrete".lower() in dimensions.get('Name').lower():
            # Example: 30 MPa for normal concrete
            fck = 30
            fyk = 500
            d = 0.9 * height_mm
            As = (0.85 * fck * width_mm * d) / (0.87 * fyk) # Simplified area of steel calculation

            # Calculate maximum uniform load using concrete beam ULC function
            results[beam_id] = Concrete_ULC. uniform_load_capacity(height_mm, width_mm, length_m, d, As, fck, fyk), 'Concrete'
        
        elif "glulam".lower() in dimensions.get('Name').lower():
            if height_mm < 130:
                results[beam_id] = None  # Width too small for glulam calculation
                continue

            # Example: 24 MPa for glulam
            material_strength_mpa = 24 

            # Calculate maximum uniform load using Glulam_ULC module
            results[beam_id] = Glulam_ULC.uniform_load_capacity(height_mm, width_mm, length_m, material_strength_mpa), 'Glulam'
    
    # Remove entries with None values
    results = {k: v for k, v in results.items() if v is not None}

    return results