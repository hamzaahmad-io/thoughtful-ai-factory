"""Package sorting module for robotic automation factory."""


def sort(width: float, height: float, length: float, mass: float) -> str:
    """Dispatch packages to correct stack based on volume and mass."""
    volume: float = width * height * length
    max_dimension: float = max(width, height, length)

    is_bulky: bool = volume >= 1_000_000 or max_dimension >= 150
    is_heavy: bool = mass >= 20

    if is_bulky and is_heavy:
        return "REJECTED"
    if is_bulky or is_heavy:
        return "SPECIAL"
    return "STANDARD"
