import pandas as pd

def load_lexicon(path):
    return pd.read_csv(path)

def load_notes(path):
    return pd.read_csv(path)

def predict_label(text, terms):
    text = str(text).lower()
    hits = sum(1 for t in terms if t and t in text)

    if hits >= 2:
        return "high"
    elif hits == 1:
        return "intermediate"
    else:
        return "low"

def run(lexicon_path, notes_path, output_path):
    lexicon = load_lexicon(lexicon_path)
    notes = load_notes(notes_path)

    terms = [str(t).lower() for t in lexicon["term"].tolist()]

    notes["predicted_label"] = notes["text"].apply(
        lambda x: predict_label(x, terms)
    )

    notes[["id", "text", "entity", "predicted_label"]].to_csv(
        output_path,
        index=False
    )

    print(f"Saved {output_path}")

if __name__ == "__main__":
    run(
        "../data/lexicon_redflags.csv",
        "../data/notes_synthetic.csv",
        "../outputs/predictions.csv"
    )
