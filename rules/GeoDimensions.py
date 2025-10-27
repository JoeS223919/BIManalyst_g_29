import ifcopenshell
import ifcopenshell.geom
import ifcopenshell.util.shape
import numpy as np

def checkRule(ifc_file):
    GeoDimensions = {}

    # Geometry settings
    settings = ifcopenshell.geom.settings()
    settings.set(settings.USE_WORLD_COORDS, True)

    # Get all IfcBeam elements
    beams = ifc_file.by_type("IfcBeam")

    for beam in beams:
        try:
            shape = ifcopenshell.geom.create_shape(settings, beam)
            verts = ifcopenshell.util.shape.get_vertices(shape.geometry)

            # Convert to numpy array
            verts_np = np.array(verts)

            # Apply transformation matrix to get world coordinates
            matrix = ifcopenshell.util.shape.get_shape_matrix(shape)
            verts_hom = np.hstack((verts_np, np.ones((verts_np.shape[0], 1))))
            verts_world = (matrix @ verts_hom.T).T[:, :3]

            # Compute bounding box dimensions
            min_vals = verts_world.min(axis=0)
            max_vals = verts_world.max(axis=0)
            dimensions = max_vals - min_vals

            # Identify length as the largest dimension
            length_idx = np.argmax(dimensions)
            length_mm = dimensions[length_idx] * 1000

            # Skip beams with length < 600 mm
            if length_mm < 600:
                continue

            # Get the two remaining dimensions
            other_indices = [i for i in range(3) if i != length_idx]
            dim1, dim2 = dimensions[other_indices[0]], dimensions[other_indices[1]]

            # Determine which is horizontal (width) and which is vertical (height)
            # Assume Z-axis is vertical in world coordinates
            if other_indices[0] == 2:
                height_mm = dim1 * 1000
                width_mm = dim2 * 1000
            elif other_indices[1] == 2:
                height_mm = dim2 * 1000
                width_mm = dim1 * 1000
            else:
                # Neither dimension is vertical, assign arbitrarily
                width_mm = max(dim1, dim2) * 1000
                height_mm = min(dim1, dim2) * 1000

            GeoDimensions[beam.GlobalId] = {
                "GlobalId": beam.GlobalId,
                "l": round(length_mm, 2),
                "b": round(width_mm, 2),
                "h": round(height_mm, 2)
            }

        except Exception as e:
            print(f"Failed to process beam {beam.GlobalId}: {e}")

    return GeoDimensions