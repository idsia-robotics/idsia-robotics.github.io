---
layout: splash
author_profile: false
classes: wide
title: Datasets
permalink: /datasets/

---

# Datasets

## Hazards&Robots - 2022
*Dario Mantegazza, Carlos Redondo, Fran Espada, Luca M. Gambardella, Alessandro Giusti and Jerome Guzzi*

We consider the problem of detecting, in the visual sensing data stream of an autonomous mobile robot, semantic  patterns that are unusual (i.e., anomalous) with respect to the robot’s previous experience in similar environments. These anomalies might indicate unforeseen hazards and, in scenarios where failure is costly, can be used to trigger an avoidance behavior
We contribute a novel image-based datasets acquired in robot exploration scenarios; the dataset is composed of more than 300k labeled frames, spanning various types of anomalies.

https://github.com/idsia-robotics/hazard-detection


  @ARTICLE{mantegazza2022outlier,
          author={Mantegazza, Dario and Giusti, Alessandro and Gambardella, Luca Maria and Guzzi, Jérôme}, 
          journal={IEEE Robotics and Automation Letters},
          title={An Outlier Exposure Approach to Improve Visual Anomaly Detection Performance for Mobile Robots.},
          year={2022}, 
          volume={7},
          number={4}, 
          pages={11354-11361}, 
          doi={10.1109/LRA.2022.3192794}
  }

<figure>
  <img src="assets/images/hazardsandrobots_dataset_examplev4.png" alt="RAL_paper_anomalies" style="background-color:white;"/>
  <p align = "center">Examples of samples of the <em>Corridors</em> scenario of the dataset </p>
</figure> 



## Swiss3DCities - 2020
*Gülcan Can, Dario Mantegazza, Gabriele Abbate, Sébastien Chappuis and Alessandro Giusti.*

We introduce a new outdoor urban 3D pointcloud dataset, covering a total area of 2.7 km2, sampled from three Swiss cities with different characteristics. The dataset is manually annotated for semantic segmentation with per-point labels, and is built using photogrammetry from images acquired by multirotors equipped with high-resolution cameras.  In contrast to datasets acquired with ground LiDAR sensors, the resulting point clouds are uniformly dense and complete, and are useful to disparate applications, including autonomous driving, gaming, smart city planning, and robotics.

https://zenodo.org/record/4390295

  @article{can2021swiss3dcities,
  title = {Semantic segmentation on Swiss3DCities: a benchmark study on aerial photogrammetric 3D pointcloud dataset},
  author = {Gülcan Can and Dario Mantegazza and Gabriele Abbate and Sébastien Chappuis and Alessandro Giusti},
  journal = {Pattern Recognition Letters},
  year = {2021},
  doi = {https://doi.org/10.1016/j.patrec.2021.06.004},
  url = {https://www.sciencedirect.com/science/article/pii/S0167865521001938},
  }

<figure>
  <img src="assets/images/swiss3dcities_example.png" alt="RAL_paper_anomalies" style="background-color:white;"/>
</figure> 

<!-- SUGGESTION FOR DATASET ADD
## DatasetName
Authors
Details
Site
Cite
ExampleImage -->