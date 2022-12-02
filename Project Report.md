
## Data generation
***

#### Theory.
In terms of the data generation we chose to rely on syntetic data to simulate the health of the patients. As the measurement of blood pressure is highly complex and requires both technological and medical expertise to gather and interpret the data. With the timeframe of this project this would not be attainable.
However, the data is based of actual medical records to ensure that the application is tested in a realistic enviroment[1].

Given that blood pressure oscillate it makes the modelling of the data more complex than it would be modelling stable data. In order to achieve realistic datasets we have incorporated the use of trigonometric functions as they have the ability to describe entities that fluctuate. 

## Results
In this case, a sine wave which grows psudo-randomly but are constructed in a way that it will only diverge from the average value when in range of realistic values for blood pressure. This way the data fluctuates as a blood pressure normally would and allows for a realistic model.

For improvements the generation methods could be optimized and refactored to a single module with the goal of generating, and a complementing module who focuses on generating patients. As it is now both generation of patients and data is done in the same module. But ultimatley the biggest improvment when it comes to the dataset of the application would be implementing actual sensors with actual real data from patients.