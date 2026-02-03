<div align="center">
  
# Maize ear sensing for on-farm yield predictions

<h3>
  <a href="https://www.cisdeli.dev/">Pedro Cisdeli</a>,
  <a href="https://gustavosantiago.shinyapps.io/WebResume/">Gustavo Santiago</a>,
  <a href="https://www.linkedin.com/in/gmandrini/">German Mandrini</a>,
  <a href="https://www.linkedin.com/in/ignaciociampitti/">Ignacio Ciampitti</a>.
</h3>

**Ciampitti Lab, Purdue University**

[![CVPR Workshop Vision for Agriculture 2025](https://img.shields.io/badge/CVPRWorkshop-VisionForAg%202025-green)](https://cvpr.thecvf.com/virtual/2025/35733)
[![IEEE Xplore](https://img.shields.io/badge/IEEE-Xplore-blue)](https://www.computer.org/csdl/proceedings-article/cvprw/2025/999400f402/2a1UOWVTYoE)
[![CVF Open Access](https://img.shields.io/badge/CVF-OpenAccess-orange)](https://openaccess.thecvf.com/content/CVPR2025W/V4A/papers/Cisdeli_Maize_ear_sensing_for_on-farm_yield_predictions_CVPRW_2025_paper.pdf)
[![Project Page](https://img.shields.io/badge/Project-Page-red)](https://ciampitti-lab.github.io/projects/maize-ear-sensing)

Nondestructive depth sensing that turns each captured husk-on maize ear into an instant, per-plant grain-yield estimate.

</div>

---

## Overview

This project provides a complete pipeline for predicting maize grain yield from single RGB + depth captures in the field. Using a depth camera, we can estimate ear morphology (length, width, volume) and predict final yield without any destructive sampling.

**Key Features:**
- Real-time field deployment (≈1 second per image)
- Non-destructive measurement
- High accuracy: 98.6% mAP@0.5 for segmentation, 28.9 ml RMSE for volume, 13.9 g RMSE for yield
- Works under challenging conditions (occlusion, variable lighting, noise)

---

## Pipeline

Our system processes images through four main stages:

1. **Segmentation** - YOLOv12n-seg model isolates maize ears from RGB images
2. **Point Cloud Processing** - Binary mask applied to depth maps to create cropped point clouds
3. **Morphology Extraction** - Length and width computed geometrically; volume predicted by EVNet (Ear Volume Network)
4. **Yield Prediction** - XGBoost model converts morphological traits to grain yield estimates

---

## Dataset

Available at: https://doi.org/10.5281/zenodo.18396680 

We provide the raw sensor data and ground truth measurements collected from Kansas field trials:

### Available Files

- **`.bag` files** - ROS bag files containing synchronized RGB + depth image streams from Intel RealSense camera
- **`read_bag.py`** - Python script to extract images from the bag files
- **`field_sample.csv`** - Ground truth measurements including:
```
Columns:
- id: Sample identifier
- length_cm: Ear length in centimeters
- width_mm: Ear width in millimeters
- weight_g: Fresh weight in grams
- volume_ml: Volume in milliliters
- dry_weight_g: Dry weight in grams
- moisture_percentage: Moisture content
- kernels_dry_weight_g: Kernel dry weight in grams
- kernels_count: Number of kernels
- stage: Growth stage (R4 or R6 = physiological maturity)
```

---

## Results

### Segmentation Performance
- **mAP@0.5**: 98.6%
- Robust to occlusion, variable lighting, and field noise

### Volume Prediction (EVNet)
- **RMSE**: 28.9 ml (ideal scenarios)
- Trained on cropped, filtered point clouds

### Yield Forecasting
- **Ideal scenario RMSE**: 13.9 g
- **Real field scenario RMSE**: 24.1 g
- Uses gradient-boosted decision trees with morphological features

---

## Code Release

The complete code for training and inference will be released following the publication of our multi-view dataset extension (coming soon).

Current release includes:
- Dataset (.bag files + ground truth)
- Data reading utilities

---

## License

This dataset is released under the [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-nc-sa/4.0/).

- Free for research and educational purposes
- Must provide attribution
- No commercial use
- Cannot be sold or used in commercial products

---

## Citation

If you use the methodology on the paper, please cite:

```bibtex
@INPROCEEDINGS {11147682,
author = { Cisdeli, Pedro and Santiago, Gustavo Nocera and Mandrini, German and Ciampitti, Ignacio },
booktitle = { 2025 IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshops (CVPRW) },
title = {{ Maize Ear Sensing for on-Farm Yield Predictions }},
year = {2025},
volume = {},
ISSN = {},
pages = {5402-5411},
abstract = { In maize (Zea mays L.), early yield prediction is a concept of great interest to breeders and agronomists. Limited studies have tried to leverage field-scale imaging data to perform such crop yield predictions. For this purpose, this study aims to provide a complete data pipeline that uses single-view depth and RGB image data to extract morphological traits of maize ears (length, width, and volume), to forecast yield in a non-destructive approach. A depth camera from a smartphone device was used to acquire imagery data, and those images were used to train the YOLOv12nseg model for segmenting the maize ears. The segmentation masks were then used to cut out the background from the point clouds. These point clouds then underwent a further filtering process to remove the remaining noise. The length and width of the ear were extracted using a geometric computational approach, while the volume was predicted using the deep learning model developed for this project, the Ear Volume Network (EVNet). Lastly, a yield prediction was obtained by using the ear morphological traits as input in the gradient-boosting decision trees. The segmentation task performed well under adverse environmental conditions such as occlusion, noise and variable lighting. The EVNet accurately predicted ear volumes under ideal scenarios ($RMSE =28.91 \text{ml}$). Likewise, the yield forecast step demonstrated high accuracy in both ideal ($R M S E=13.90 g)$ and real (RMSE $=24.12 ~\mathrm{g})$ scenarios. The results of this study highlight the potential of using new technologies to predict yield under field conditions. },
keywords = {Point cloud compression;Image segmentation;Accuracy;Computational modeling;Noise;Pipelines;Lighting;Ear;Feature extraction;Data mining},
doi = {10.1109/CVPRW67362.2025.00537},
url = {https://doi.ieeecomputersociety.org/10.1109/CVPRW67362.2025.00537},
publisher = {IEEE Computer Society},
address = {Los Alamitos, CA, USA},
month =Jun}
```

If you use the dataset, please cite:
```bibtex
@dataset{cisdeli_2026_18396680,
  author       = {Cisdeli, Pedro and
                  Ciampitti, Ignacio},
  title        = {Dataset - Maize Ear Sensing Dataset for On-Farm
                   Yield Predictions
                  },
  month        = jan,
  year         = 2026,
  publisher    = {Zenodo},
  version      = 1,
  doi          = {10.5281/zenodo.18396680},
  url          = {https://doi.org/10.5281/zenodo.18396680},
}
```
