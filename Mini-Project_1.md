## Mini-Project 1: Social Distance Detector

#### Video:

[![IMAGE ALT TEXT](http://img.youtube.com/vi/kme6VODgbt0/0.jpg)](http://www.youtube.com/watch?v=kme6VODgbt0)



#### Questions:

1. Was your social distance detector effective at detecting potential violations? Are you able to describe how the distance detector is applying its calculations of either being safe or noting a violation?

No, my social distance detector was not effective at detecting potential violations. I am not entirely certain how the calcualtions are applied but it appears that the program creates a rectangle around each person it identifies and then estimates the distance between rectangles.

2. Do you think this approach would be effective for estimating new infections in real time? How would you implement such an approach in response to the COVID-19 pandemic we are currently experiencing?

I think this approach could be effective at estimating new infections in real time with a few tweaks. It could be utilized in crowd settings, for example the NBA bubble, to estimate potential exposures to COVID so that people can quarntine faster. 

3. What limitations or improvements might you include in order to improve your proposed design?

I would like to experiment with the social distance detector's protocol for estimating distance and classifying people. One reason that the social distance detector may not have properly classified my video is that my roomate and myself got close enough that it classified us as one person. Additionally, it may be useful to incorperate multiple video angles, that way we can still classify people even if they fall out of view of one camera. 
