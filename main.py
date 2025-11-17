import ifcopenshell
import ifcopenshell.util.classification

from rules import BeamClassifications
from rules import Dimensions
from rules import GeoDimensions
from rules import max_UDL
from rules import i_beam_ULC


model = ifcopenshell.open("samples/25-16-D-STR.ifc")
model1 = ifcopenshell.open("samples/Exercise9_Group10.ifc")


# windowResult = windowRule.checkRule(model)
# doorResult = doorRule.checkRule(model)
# beamResult = beamRule.checkRule(model)
# checkBeamClassificationResult = checkBeamClassification.checkRule(model1)
# beamClassificationsResult = BeamClassifications.checkRule(model1, 1)




GeodimensionsResult =  GeoDimensions.checkRule(model)
print("GeoDimensions result:", GeodimensionsResult)
# print(GeodimensionsResult['08KUHnYqn7HvCxSyjUsDVX'])

#DimensionsResult = Dimensions.beam_dimensions(model)
#print("Dimensions result:", DimensionsResult)
#print(DimensionsResult['08KUHnYqn7HvCxSyjUsDQb'])

# maxUDLResult = max_UDL.checkRule(DimensionsResult)
#print("Max UDL result:", maxUDLResult)
# print(maxUDLResult['08KUHnYqn7HvCxSyjUsDVX'])


# Example usage:









# print("Beam classifications:", beamClassificationsResult)
# print('--------------------------------------------------')
# print('Number of beams with classification: ', len(checkBeamClassificationResult[0]), 
#       'Number of beams without classification: ', len(checkBeamClassificationResult[1]),
#       'Total number of beams: ', len(model1.by_type("IfcBeam")))

#for beam_info in DimensionsResult:
#    print(f"GlobalId: {beam_info['GlobalId']}, Name: {beam_info['Name']}")
#    print(f"  Dimensions: {beam_info['Dimensions']}")
#    print(f"  Cut Length: {beam_info['CutLength']}")
 #   print()