def beam_dimensions(model):
    beam_like_entities = [
        entity for entity in model
        if "beam" in entity.is_a().lower() or "member" in entity.is_a().lower()
    ]

    results = {}

    for beam in beam_like_entities:
        dimensions = {}
        cut_length = None

        # --- Type Property Set: Dimensions (height/width) ---
        for rel in getattr(beam, "IsTypedBy", []):
            type_obj = rel.RelatingType
            for type_rel in getattr(type_obj, "HasPropertySets", []):
                if type_rel.is_a("IfcPropertySet") and type_rel.Name == "Dimensions":
                    for prop in type_rel.HasProperties:
                        nv = getattr(prop, "NominalValue", None)
                        if hasattr(nv, "wrappedValue"):
                            value = nv.wrappedValue
                        elif hasattr(nv, "value"):
                            value = nv.value
                        else:
                            value = nv
                        dimensions[prop.Name.lower()] = value

        # --- Instance Property Set: Structural (cut length) ---
        for rel in getattr(beam, "IsDefinedBy", []):
            if rel.is_a("IfcRelDefinesByProperties"):
                pset = rel.RelatingPropertyDefinition
                if pset.is_a("IfcPropertySet") and pset.Name == "Structural":
                    for prop in pset.HasProperties:
                        if prop.Name.lower() == "cut length":
                            nv = getattr(prop, "NominalValue", None)
                            if hasattr(nv, "wrappedValue"):
                                cut_length = nv.wrappedValue
                            elif hasattr(nv, "value"):
                                cut_length = nv.value
                            else:
                                cut_length = nv

        # --- Build the final dictionary entry ---
        global_id = getattr(beam, "GlobalId", None)
        if global_id:
            results[global_id] = {
                "Name": getattr(beam, "Name", None),
                "b": dimensions.get("b"),
                "h": dimensions.get("h"),
                "l": cut_length
            }

    return results
