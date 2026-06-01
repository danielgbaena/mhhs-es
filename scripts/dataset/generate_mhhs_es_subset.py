"""
generate_mhhs_es_subset.py

Generate the MHHS-ES annotation subset from MentalRiskES.

This script:
- randomly samples subjects from each group,
- extracts all their messages,
- preserves chronological order,
- and exports a CSV file ready for Google Sheets annotation.
"""

import os
import json
import random
import pandas as pd

# =====================================================
# CONFIGURATION
# =====================================================

SEED = 42

# Root paths
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))

DATASET_PATH = os.path.join(
    PROJECT_ROOT, "data", "raw", "corpusMentalRiskES", "processed", "Depress"
)

GOLD_PATH = os.path.join(DATASET_PATH, "gold", "gold_label.csv")

DATA_PATH = os.path.join(DATASET_PATH, "data")

OUTPUT_PATH = os.path.join(PROJECT_ROOT, "data", "subsets")

OUTPUT_FILE = os.path.join(OUTPUT_PATH, "MHHS_ES_annotation_subset.csv")

SUBJECTS_FILE = os.path.join(OUTPUT_PATH, "selected_subjects.json")

random.seed(SEED)

# =====================================================
# CREATE OUTPUT DIRECTORY
# =====================================================

os.makedirs(OUTPUT_PATH, exist_ok=True)

# =====================================================
# LOAD GOLD LABELS
# =====================================================

print("Loading subject metadata...")

gold = pd.read_csv(GOLD_PATH, sep="\t")

# =====================================================
# BUILD SUBJECT GROUPS
# =====================================================

control_subjects = gold[gold["bc"] == 1]["nick"].tolist()

bsf_subjects = gold[gold["bsf"] == 1]["nick"].tolist()

bsa_subjects = gold[gold["bsa"] == 1]["nick"].tolist()

bso_subjects = gold[gold["bso"] == 1]["nick"].tolist()

# =====================================================
# RANDOM SUBJECT SAMPLING
# =====================================================

print("Sampling subjects...")

selected_control = random.sample(control_subjects, 25)

selected_bsf = random.sample(bsf_subjects, 25)

selected_bsa = random.sample(bsa_subjects, 25)

# IMPORTANT:
# only 13 BSO subjects exist
selected_bso = bso_subjects

# =====================================================
# STORE SUBJECT SELECTION
# =====================================================

selected_subjects = {
    "control": selected_control,
    "bsf": selected_bsf,
    "bsa": selected_bsa,
    "bso": selected_bso,
}

with open(SUBJECTS_FILE, "w", encoding="utf-8") as f:
    json.dump(selected_subjects, f, indent=4, ensure_ascii=False)

# =====================================================
# BUILD SUBJECT LIST
# =====================================================

subjects = []

for s in selected_control:
    subjects.append((s, "control"))

for s in selected_bsf:
    subjects.append((s, "bsf"))

for s in selected_bsa:
    subjects.append((s, "bsa"))

for s in selected_bso:
    subjects.append((s, "bso"))

# =====================================================
# EXTRACT ALL MESSAGES
# =====================================================

print("Extracting messages...")

rows = []

for subject_id, group in subjects:

    json_path = os.path.join(DATA_PATH, f"{subject_id}.json")

    with open(json_path, "r", encoding="utf-8") as f:
        messages = json.load(f)

    # chronological order
    messages = sorted(messages, key=lambda x: x["date"])

    for idx, msg in enumerate(messages):

        rows.append(
            {
                # ==================================
                # SUBJECT INFORMATION
                # ==================================
                "subject_id": subject_id,
                "group": group,
                # ==================================
                # MESSAGE INFORMATION
                # ==================================
                "message_order": idx + 1,
                "message_id": msg["id_message"],
                "date": msg["date"],
                "message": msg["message"],
                # ==================================
                # ANNOTATION COLUMNS
                # ==================================
                "annotator_1_label": "",
                "annotator_1_dimension": "",
                "annotator_2_label": "",
                "annotator_2_dimension": "",
                "annotator_3_label": "",
                "annotator_3_dimension": "",
                "final_label": "",
                "final_dimension": "",
                "notes": "",
            }
        )

# =====================================================
# BUILD DATAFRAME
# =====================================================

df = pd.DataFrame(rows)

# =====================================================
# SORT FOR CONTEXTUAL ANNOTATION
# =====================================================

df = df.sort_values(by=["subject_id", "message_order"])

# =====================================================
# EXPORT CSV
# =====================================================

print("Exporting CSV...")

df.to_csv(OUTPUT_FILE, index=False, encoding="utf-8-sig")

# =====================================================
# SUMMARY
# =====================================================

print("\n" + "=" * 60)
print("MHHS-ES annotation subset generated")
print("=" * 60)

print(f"\nTotal subjects: {len(subjects)}")
print(f"Total messages: {len(df)}")

print("\nSubjects per group:")
print(df.groupby("group")["subject_id"].nunique())

print("\nMessages per group:")
print(df.groupby("group").size())

print(f"\nCSV exported to:\n{OUTPUT_FILE}")

print(f"\nSubject selection saved to:\n{SUBJECTS_FILE}")

print("\nDone.")
