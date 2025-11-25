def uniform_load_capacity(h, b, L, fm):
    """
    Parameters:
        h  : beam depth (m)
        b  : beam width (m)
        L  : span (m)
        fm : bending strength (MPa = N/mm^2), 
             e.g., fm,k (characteristic) or fm,d (design)
             
    Returns:
        w  : uniform load capacity (kN/m) based on bending
    """
    from math import isfinite

    if h <= 0 or b <= 0:
        raise ValueError("Dimensions h and b must be positive.")
    if L <= 0 or not isfinite(L):
        raise ValueError("Span L must be a positive number.")

    # Convert meters → mm for section modulus calculation
    h_mm = h
    b_mm = b

    # Section modulus S = b*h^2 / 6   (rectangular section, bending about strong axis)
    S = b_mm * (h_mm**2) / 6.0  # mm^3

    # Moment capacity M = fm * S  (N*mm)
    M_Nmm = fm * S

    # Convert N*mm → kN*m
    M_kNm = M_Nmm * 1e-6

    # Uniform load for simply supported beam:  M = w * L^2 / 8
    w_kNm = (8.0 * M_kNm) / (L**2)

    return w_kNm
