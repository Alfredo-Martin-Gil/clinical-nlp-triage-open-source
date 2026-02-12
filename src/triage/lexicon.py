import pandas as pd


def normalize_terms(lexicon: pd.DataFrame) -> list[str]:
    """
    Normalize lexicon terms.

    - Lowercase
    - Strip whitespace
    - Drop null values
    - Remove duplicates
    """
    terms = (
        lexicon["term"]
        .dropna()
        .astype(str)
        .str.strip()
        .str.lower()
    )

    return sorted(set(terms))
