# CNN-hand-classification
EME internship graduation project.

## Overview
This is a Computer vision project. A hand guesture classification CNN that detects and classifies different hand guestures.

## Part I: YOLOv8 Retrained Model
In this part We -as a team of 3- gathered and labeled data to train YOLOv8 to detect hands in different position and from different individuals.
This has created enough variance for the model to detect hands of people outside of our team.
Each individual in the team took 300 pictures while doing different hand guestures in different positions in the screen.
We used [Roboflow](https://roboflow.com/) to label our data.
This helped prepare the data for YOLOv8 to train.
We used [Google Colab](https://colab.research.google.com/) TPU feature to train our model using GPU.
This helped alot in the train time.
The output from this part with get cropped and passed to Part II.

## Part II: CNN classification model
In this part we did some research and concluded that with a different variance of [ALEXnet](https://proceedings.neurips.cc/paper_files/paper/2012/file/c399862d3b9d6b76c8436e924a68c45b-Paper.pdf) Architecture, it would suit our application best.
The choice of ALEXnet architecture is due to it being a relatively small model, deep enough but not too deep and can be deployed later on embedded systems easily or any low power systems.
We tweaked some design decisions to best fit our application.
What really mattered in our design was preprocessing all images to make the model focus on only the important features of the images thus isolating the background and colors.
This should result a thresholded image that only has the hand with the outlines of the hand clear to make the classification process more efficient and to remove any bias from the training data.

## Part III: arduino Demo
In this part, we made a simple arduino sketch that would take that predicted output from the two previous parts and apply pwm to control the speed levels of a dc motor as a demo.
This can be using for more than just a DC motor but it is only made as an explanation of the uses of this model.
Each level represents 20% power of the maximum power of the motor.

## Dependencies
1. pyserial
2. Tensorflow
3. opencv
4. keras
5. supervision
6. numpy
7. unltralytics

## Resources
1. https://www.tensorflow.org/api_docs
2. https://opencv.org/get-started/
3. https://roboflow.com/
4. https://proceedings.neurips.cc/paper_files/paper/2012/file/c399862d3b9d6b76c8436e924a68c45b-Paper.pdf

## Colaborators
This section only includes the team members who worked on this Project
1. Abdullah M. El-Sayed
2. Mohamed El-Sayed Atallah
3. Ali Mahmoud Sobhy

