Hi So This is my solution regarding model Prunning:
I use tensorflow (because i dont like pytorch that much!)

So  in the adjoinging jupyter notebook  you can find what have done.
I trained a Model for disease detection in plants.
It is trained on 70,000 plant images belonging to 38 different classes.
(I might have used MNIST but it would have been no fun !!)


I used tensorflow-model_optimization to do weight pruning.
As in a nerual net its not necessary that a pathways are used ie all weight have
a non zero value.  we can remove whose wiehgts that have a zero value.
There by reducing model size and improving its performance.

unlike the example on googles tensorflow I only managaed to 
acheive only 30 % reduction in model size and approx 10 second improvement
on validation set. 

you can always check this note here :
https://www.kaggle.com/vanvalkenberg/cnn-for-plant-disease-detection-92-val-accuracy