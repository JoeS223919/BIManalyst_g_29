import ifcopenshell
import ifcopenshell.util.classification

from rules import HowManyBeams
from rules import BeamClassifications
from rules import checkIfBeamHasClassification
from rules import Dimensions
<<<<<<< Updated upstream
from rules import GeoDimensions
=======
from rules import max_UDL
>>>>>>> Stashed changes


model = ifcopenshell.open("samples/25-16-D-STR.ifc")
model1 = ifcopenshell.open("samples/Exercise9_Group10.ifc")


<<<<<<< Updated upstream
=======
# windowResult = windowRule.checkRule(model)
# doorResult = doorRule.checkRule(model)
# beamResult = beamRule.checkRule(model)
# checkBeamClassificationResult = checkBeamClassification.checkRule(model1)
# beamClassificationsResult = BeamClassifications.checkRule(model1, 1)

>>>>>>> Stashed changes

DimensionsResult = Dimensions.beam_dimensions(model)
print("Dimensions result:", DimensionsResult)

<<<<<<< Updated upstream
GeoDimensionsResult = GeoDimensions.checkRule(model)

print(DimensionsResult)
print(GeoDimensionsResult)

=======
maxUDLResult = max_UDL.checkRule(DimensionsResult)
print("Max UDL result:", maxUDLResult)
>>>>>>> Stashed changes


<<<<<<< Updated upstream

# for beam_info in DimensionsResult:
#     print(f"GlobalId: {beam_info['GlobalId']}, Name: {beam_info['Name']}")
#     print(f"  Dimensions: {beam_info['Dimensions']}")
#     print(f"  Cut Length: {beam_info['CutLength']}")
#     print()
=======
#for beam_info in DimensionsResult:
#    print(f"GlobalId: {beam_info['GlobalId']}, Name: {beam_info['Name']}")
#    print(f"  Dimensions: {beam_info['Dimensions']}")
#    print(f"  Cut Length: {beam_info['CutLength']}")
 #   print()
>>>>>>> Stashed changes
