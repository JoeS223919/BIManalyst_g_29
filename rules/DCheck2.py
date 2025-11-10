import Dimensions
import GeoDimensions
import ifcopenshell

# Open the IFC model
model = ifcopenshell.open("samples/25-16-D-STR.ifc")

# Ask for GlobalId
target_global_id = input("Enter the GlobalId to inspect: ").strip()

# Get full datasets
D_psets = Dimensions.beam_dimensions(model)
D_Geo = GeoDimensions.checkRule(model)

# Helper: filter dataset by GlobalId
def filter_by_global_id(data, gid):
    if isinstance(data, dict):
        if gid in data:
            return data[gid]
        for val in data.values():
            if isinstance(val, dict) and val.get("GlobalId") == gid:
                return val
    elif isinstance(data, list):
        for item in data:
            if isinstance(item, dict) and item.get("GlobalId") == gid:
                return item
    return None

# Extract entries
pset_entry = filter_by_global_id(D_psets, target_global_id)
geo_entry = filter_by_global_id(D_Geo, target_global_id)

# Check and compare dimensions
def approx_equal(a, b, tol=1.0):
    try:
        return abs(float(a) - float(b)) <= tol
    except (TypeError, ValueError):
        return False

if pset_entry and geo_entry:
    b_match = approx_equal(pset_entry.get("b"), geo_entry.get("b"))
    h_match = approx_equal(pset_entry.get("h"), geo_entry.get("h"))
    l_match = approx_equal(pset_entry.get("l"), geo_entry.get("l"))

    if b_match and h_match and l_match:
        print("TRUE")
    else:
        print("FALSE")
        print("\nD_psets:", pset_entry)
        print("\nD_Geo:", geo_entry)
else:
    print("GlobalId not found in one or both datasets.")
