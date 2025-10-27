
import ifcopenshell
import ifcopenshell.util.classification

from rules import HowManyBeams
from rules import BeamClassifications
from rules import checkIfBeamHasClassification
from rules import Dimensions
from rules import max_UDL
from rules import GeoDimensions

model = ifcopenshell.open("samples/25-16-D-STR.ifc")
model1 = ifcopenshell.open("samples/Exercise9_Group10.ifc")


D_psets = Dimensions.beam_dimensions(model)
D_Geo = GeoDimensions.checkRule(model)

print(D_psets)
print(D_Geo)