import gender_guesser.detector as gender

def get_tittle(name: str) -> str:
    d = gender.Detector()
    result = d.get_gender(name)

    if result in ("male", "mostly_male"):
        return 'Pan'
    elif result in ("female", "mostly_female"):
        return 'Paní'
    raise ValueError(f"Could not determine gender for name: {name} (detected: {result})")