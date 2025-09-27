# This Script analyses a claim made in a report and verifies its validity.

import ifcopenshell

def checkRule(model):
    storeys = model.by_type("IfcBuildingStorey")
    over_ground = 0
    under_ground = 0

    details = []
    for storey in storeys:
        elevation = getattr(storey, 'Elevation', None)
        details.append(f"- {storey.Name} (Elevation: {elevation if elevation is not None else 'Unknown'})")
        if elevation is not None:
            if elevation < 0:
                under_ground += 1
            else:
                over_ground += 1

    claim = "Correct" if len(storeys) == 6 else "Incorrect"

    text = (
        f"Total storeys: {len(storeys)}\n"
        f"Above ground: {over_ground}\n"
        f"Below ground: {under_ground}\n"
        f"Claim (6 storeys): {claim}\n"
        "Details:\n" +
        "\n".join(details)
    )
    return text