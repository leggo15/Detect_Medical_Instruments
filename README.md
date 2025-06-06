# Deep Learning Examination – Instrument Segmentation

This repository contains the code, experiment notebooks, and report for our **PGR207 Deep Learning** examination at Kristiania University College. The project investigates how **image resolution**, **data augmentation**, and **training‑set size** influence a U‑Net model’s ability to segment surgical instruments in gastrointestinal endoscopy images ([Kvasir‑Instrument dataset](https://datasets.simula.no/kvasir-instrument/)).

## Repository layout

```
.
├── models/
│   ├── resolution_models/...
│   ├── augmentation_models/...
│   ├── data_size_test/...
│   ├── base_model.ipynb
│   └── run_all.py          # batch‑executes every notebook
├── requirements.txt
└── Deep_Learning_Examination_Report.pdf
```

## Use

Download the Kvasir‑Instrument dataset to 'Repo\data' by following the instructuons found on their webpage.

```
python -m venv env
pip install -r requirements.txt
python run_all.py      # executes every notebook in‑place
```

The notebooks can also be opened and run individually in JupyterLab.

## Experiments

| Experiment         | What changes                               | Key finding                                             |
| ------------------ | ------------------------------------------ | ------------------------------------------------------- |
| Image resolution   | Train on 32×32 → 2048×2048 + mixed‑res | 256‑576 px hits the sweet spot; extreme scaling hurts |
| Data augmentation  | Rotation, random crop, horizontal flip     | Minor gains alone                                       |
| Training‑set size | 25 % – 900 % of original via aug/res    | More data improves Dice/IoU with diminishing returns    |

See the PDF report for full metrics, graphs, and discussion.

## Dataset

[Kvasir‑Instrument](https://datasets.simula.no/kvasir-instrument/) – 590 annotated GI endoscopy images with binary masks. Only the metadata (paths) are version‑controlled; download the images separately and set `<span>KVASIR_ROOT</span>` in the notebooks.


## Acknowledgements

This repository was created for the PGR207 Deep Learning examination at Kristiania University College. We gratefully acknowledge the authors of the **Kvasir‑Instrument** dataset for making the data publicly available.
