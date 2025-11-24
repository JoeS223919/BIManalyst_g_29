import ifcopenshell
import ifcopenshell.util.classification

from rules import BeamClassifications
from rules import Dimensions
from rules import GeoDimensions
from rules import max_UDL
from rules import i_beam_ULC


model = ifcopenshell.open("samples/25-16-D-STR.ifc")
model1 = ifcopenshell.open("samples/Exercise9_Group10.ifc")




#GeodimensionsResult =  GeoDimensions.checkRule(model)
# print("GeoDimensions result:", GeodimensionsResult)
# print(GeodimensionsResult['08KUHnYqn7HvCxSyjUsDVX'])

DimensionsResult = Dimensions.beam_dimensions(model)
#print("Dimensions result:", DimensionsResult)
# print(DimensionsResult['08KUHnYqn7HvCxSyjUsDQb'])

maxUDLResult = max_UDL.checkRule(DimensionsResult)
# print("Max UDL result:", maxUDLResult)
# print(maxUDLResult["0kMAKvmNr5WhMLClkIAwid"])


LineloadsReport = {"Concrete": 26.12, "Steel": 14.97, "Glulam": 17.2}

# Validate beams against LineloadsReport
material_counts_right = {"Concrete": 0, "Steel": 0, "Glulam": 0}
material_counts_wrong = {"Concrete": 0, "Steel": 0, "Glulam": 0}


for beam_id, result in maxUDLResult.items():
    if result is None:
        continue
    
    max_udl, material_type = result
    
    # Normalize material type for lookup
    material_key = material_type.capitalize()
    
    if material_key in LineloadsReport:
        allowable_load = LineloadsReport[material_key]
        
        # Check if max_udl is higher than or equal to the allowable load
        if max_udl >= allowable_load:
            material_counts_right[material_key] += 1
        else:
            material_counts_wrong[material_key] += 1
        
# Print results
print(f"{material_counts_right['Concrete']} Concrete beams are dimensioned right")
print(f"{material_counts_wrong['Concrete']} Concrete beams are NOT dimensioned right")
print(f"{material_counts_right['Steel']} Steel beams are dimensioned right")
print(f"{material_counts_wrong['Steel']} Steel beams are NOT dimensioned right")
print(f"{material_counts_right['Glulam']} Glulam beams are dimensioned right")
print(f"{material_counts_wrong['Glulam']} Glulam beams are NOT dimensioned right")


