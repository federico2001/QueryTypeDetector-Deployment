# QueryTypeDetector-deployment
This repository contains a docker image with a deployment pipeline of a trained binary model and an API framework to service it.<br>
It recieves a string as an input and returns the predicted category and the confidence (in % terms) of such prediction.<br>
### Possible outcomes: 
 - 0 : 'retailer'
 - 1 ; 'brand'
 - 2 : 'category'

All specifications and context of this service can be found <a href="https://github.com/federico2001/QueryTypeDetector/tree/main">here</a>.
