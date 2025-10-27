import ifcopenshell
import ifcopenshell.util.classification

from rules import HowManyBeams
from rules import BeamClassifications
from rules import checkIfBeamHasClassification
from rules import Dimensions
from rules import max_UDL


model = ifcopenshell.open("samples/25-16-D-STR.ifc")
model1 = ifcopenshell.open("samples/Exercise9_Group10.ifc")


# windowResult = windowRule.checkRule(model)
# doorResult = doorRule.checkRule(model)
# beamClassificationsResult = BeamClassifications.checkRule(model1, 1)


DimensionsResult = Dimensions.beam_dimensions(model)
print("Dimensions result:", DimensionsResult)
maxUDLResult = max_UDL.checkRule(DimensionsResult)
print("Max UDL result:", maxUDLResult)


#for beam_info in DimensionsResult:
#    print(f"GlobalId: {beam_info['GlobalId']}, Name: {beam_info['Name']}")
#    print(f"  Dimensions: {beam_info['Dimensions']}")
#    print(f"  Cut Length: {beam_info['CutLength']}")
 #   print()
