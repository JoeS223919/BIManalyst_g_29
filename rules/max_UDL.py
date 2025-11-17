import ifcopenshell
from rules import i_beam_ULC
from rules import Glulam_ULC'
from rules import ConcreteBeam_ULC

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

        # Convert length to meters  
        length_m = length_mm / 1000
        width_m = width_mm / 1000
        height_m = height_mm / 1000

        if "HEM".lower() in dimensions.get('Name').lower():
            # Example: 250 MPa for structural steel
            material_strength_mpa = 250

            # Calculate maximum uniform load using i_beam_ULC module
            results[beam_id] = i_beam_ULC.uniform_load_capacity(height_mm, width_mm, thickness_body_mm, thickness_flange_mm, length_m, material_strength_mpa)
        
        elif "concrete".lower() in dimensions.get('Name').lower():
            # Example: 30 MPa for normal concrete
            material_strength_mpa = 30 
            
            # Calculate maximum uniform load using concrete beam ULC function
            results[beam_id] = 
        
        elif "glulam".lower() in dimensions.get('Name').lower():
            # Example: 24 MPa for glulam
            material_strength_mpa = 24 

            # Calculate maximum uniform load using Glulam_ULC module
            results[beam_id] = Glulam_ULC.uniform_load_capacity(height_mm, width_mm, length_m, material_strength_mpa)
    

    return results