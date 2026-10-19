# Innovation Diffusion Analysis: Apple AirPods Pro 3
**Course:** Marketing Analytics  
**Assignment:** Homework on Bass Model  
**Instructor:** Karen Hovhannisyan  
**Student:** Lusine Baghdasaryan

## Project Overview
This project models and predicts the market diffusion of the **Apple AirPods Pro 3** (featured on *TIME's Best Inventions 2025* list) using the **Bass Diffusion Model**. 

Because the AirPods Pro 3 is newly launched, parameter estimation cannot rely on its own sales history. We identify the original **Apple iPod (2001–2014)** as its historical single-product look-alike, estimate the behavioral coefficients of innovation ($p$) and imitation ($q$) from official SEC filings, and apply Fermi estimation to forecast global AirPods Pro 3 adoption over a 10-year horizon.

---

## Repository Directory Structure
```text
HW1/
├── README.md               # Main project documentation and overview
├── helper_functions.py     # Modular mathematical and estimation functions
├── script1.py              # Main execution script: loads data, runs model, outputs charts
├── data/
│   └── dataset1.csv        # Historical quarterly unit sales from Apple SEC 10-K filings
├── img/
│   ├── image1.png          # Historical Bass Model fit for Apple iPod
│   └── image2.png          # Forecasted annual and cumulative adoption for AirPods Pro 3
└── report/
    ├── report_source.md    # Full source markdown text of the report
    └── report.pdf          # Final compiled PDF report