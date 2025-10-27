
# ...existing code...
import Dimensions
import GeoDimensions
import ifcopenshell

model = ifcopenshell.open("samples/25-16-D-STR.ifc")

D_psets = Dimensions.beam_dimensions(model)
D_Geo = GeoDimensions.checkRule(model)

def first_item_from(obj):
    if isinstance(obj, dict):
        return next(iter(obj.items()))            # (key, value)
    if isinstance(obj, list):
        if not obj:
            return (None, None)
        first = obj[0]
        key = None
        if isinstance(first, dict):
            key = first.get("GlobalId") or first.get("id")   # try common id keys
        return (key, first)
    return (None, None)

first_key_psets, first_val_psets = first_item_from(D_psets)
first_key_geo, first_val_geo   = first_item_from(D_Geo)

print("PSET first:", first_key_psets, first_val_psets)
print("GEO first:", first_key_geo, first_val_geo)

