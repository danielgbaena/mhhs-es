# MHHS-ES

Mental Health Hope Speech for Spanish: A Recovery-Oriented Framework for Adaptive Coping Discourse in Depression-Related Social Media

## Overview

MHHS-ES is a research project focused on the computational modeling of **Mental Health Hope Speech (MH-HS)**, a novel discourse framework for identifying adaptive coping and recovery-oriented communication in mental health-related social media environments.

Unlike traditional Hope Speech (HS) approaches centered on Equality, Diversity, and Inclusion (EDI) contexts, MH-HS focuses on linguistic expressions associated with:
- adaptive coping,
- emotional resilience,
- recovery orientation,
- interpersonal support,
- and future-directed self-efficacy
in contexts of emotional distress and depression-related communication.

This repository contains:
- annotation resources,
- MH-HS guidelines,
- experimental scripts,
- computational models,
- and analysis tools
for the creation and validation of the first Spanish-language MH-HS dataset.

---

## Research Goals

The main objectives of this project are:

1. Define a theoretically grounded MH-HS framework for computational mental health.
2. Develop annotation guidelines for recovery-oriented discourse.
3. Create a manually annotated Spanish MH-HS corpus.
4. Validate the consistency and operationalizability of MH-HS annotations.
5. Explore computational approaches for MH-HS detection.

---

## Dataset

This project uses the MentalRiskES corpus:

> Mármol-Romero et al. (2024). *MentalRiskES: A New Corpus for Early Detection of Mental Disorders in Spanish.*

The MHHS-ES subset is constructed from depression-related communities and includes balanced subject sampling across:
- control,
- bsf,
- bsa,
- and bso
profiles.

---

## Project Structure

```text
mhhs-es/
├── data/
├── guidelines/
├── scripts/
├── notebooks/
├── models/
├── results/
├── paper/
└── prompts/
```

---

## Annotation Framework

MH-HS annotations are performed at the message level while preserving conversational and subject-level context.

The current annotation schema includes:
- Binary MH-HS labels
- Optional discourse dimensions:
  - Agency-oriented discourse
  - Recovery-oriented discourse
  - Emotional resilience
  - Interpersonal supportive discourse
  - Adaptive reframing

---

## Computational Validation

The project explores several computational approaches for MH-HS detection:
- TF-IDF + SVM baselines
- Transformer-based models
- Zero-shot Large Language Models (LLMs)

The goal is not to optimize benchmark performance, but to evaluate whether MH-HS constitutes a computationally learnable discourse construct.

---

## Current Status

Project stage:
- [x] Theoretical framework design
- [x] Annotation guideline drafting
- [x] Subset generation pipeline
- [ ] Manual annotation
- [ ] Agreement analysis
- [ ] Computational experiments
- [ ] Paper submission

---

## Citation

Citation information will be added after publication.

---

## License

This repository is intended exclusively for research purposes.

Please respect the original access conditions and ethical considerations associated with the MentalRiskES corpus.

---

## Contact

Daniel García-Baena  
SINAI Research Group  
University of Jaén  
Spain
