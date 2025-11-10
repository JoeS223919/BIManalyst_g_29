import Dimensions
import GeoDimensions
import ifcopenshell

# Open the IFC model
model = ifcopenshell.open("samples/25-16-D-STR.ifc")

# Ask the user for the GlobalId they want to inspect
target_global_id = input("Enter the GlobalId to inspect: ").strip()

# Get all data from both modules
D_psets = Dimensions.beam_dimensions(model)
D_Geo = GeoDimensions.checkRule(model)

# Filter results by GlobalId
def filter_by_global_id(data, gid):
    if isinstance(data, dict):
        # If dict has the GlobalId as a key
        if gid in data:
            return {gid: data[gid]}
        # Or if it's nested and we need to search inside
        for key, val in data.items():
            if isinstance(val, dict) and val.get("GlobalId") == gid:
                return {key: val}
        return {}
    elif isinstance(data, list):
        for item in data:
            if isinstance(item, dict) and item.get("GlobalId") == gid:
                return item
        return None
    else:
        return None

# Filter both datasets
filtered_psets = filter_by_global_id(D_psets, target_global_id)
filtered_geo   = filter_by_global_id(D_Geo, target_global_id)

# Print results
print("PSET result for", target_global_id, ":\n", filtered_psets)
print("\nGEO result for", target_global_id, ":\n", filtered_geo)
