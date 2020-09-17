# pixel-based-land-cover-analysis
Urban Analytics Dissertation code

This repository holds the code used for the M.Sc. Urban Analytics dissertation at the University of Glasgow. The title of the dissertation is 'Analysing vacant and derelict land in Glasgow using pixel-level land cover classification'.


# Abstract 

The aim of this study is to provide a detailed analysis of vacant and derelict land in Glasgow, Scotland. The city’s deindustrialisation left many areas abandoned for decades, causing various socioeconomic and health problems in the neighbouring areas. The analysis contributes to the existing literature by helping to understand the current state and land cover of vacant and derelict land. This is done through a pixel-based land cover analysis with gradient boosting, which classifies each pixel in very high resolution (1m x 1m) aerial photography. The studied area covers 76.67 km2 of Glasgow and the satellite images are from 2018. The accuracy of the classifier is 83.9%, which is similar to other land cover classifiers in the literature. The predictions of the classifier reveal that today vegetation is the most common land cover type on both derelict and vacant sites, followed by bare soil. The temporal findings show that the longer an area is abandoned, the higher the vegetation percentage, which leads to information loss and higher development costs. These findings imply that authorities need to focus on prevention and address already existing vacant and derelict land through various policy instruments.

# Notebooks

**1: Creating mask:**: This notebook creates randomly coloured masks for the polygons in an area. The inputs are the image and the corresponding shapefile, while the output is a png with the coloured polygons.

**2. Classification workflow**: This notebook creates the masks for the sample area and saves the classified pixels with the corresponding classes in a dataset.

**3.Classifiers-aerial-image-pixels**: This notebook trains tha different classifiers for the dataset. Random Forest and XGBoost are the two classifiers tried and the best models are saved to predict on the entire aerial image of Glasgow.

**4. Prediction_on_satellite_image**: This script useses the trained XGBoost model and predicts the pixels of the entire Glasgow image.

**5. View_predictions_v1**: This notebook looks at the predictions for both the sample area and the entire city of Glasgow. It also has some basic analysis and plotting. 

**6. Polygon_dataframe**: This notebook merges the pixel-based predictions with the shapefile's dataset. 

**7. Outcome_data_analysis**: The land cover predictions are analysed in this notebook with most figures. 




