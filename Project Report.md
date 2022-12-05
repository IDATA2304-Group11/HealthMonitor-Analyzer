## Abstract
***
Statistics shows that over 26% of adults between 50 and 80 don't measure their blood pressure as often as they should. Hypertension, also known as blood pressure, increases the risk of heart disease and stroke, two leading causes of death in USA and Europe. As a result, we have developed a IoT device to make blood pressure tracking easier for exposed adults and elders. Healthmontor tracks blood pressure through a device such as a smart watch, and sends it to the patients doctor for reviewal. <b>This may help people slacking on their tracking</b>, and provide better quality of life. 

This report is written by four students at NTNU Ålesund; Mikkel Stavelie, Petter Edvardsen, Jørgen Finsveen and Ole-Kristian Dvergsdal.

## Introduction
***
In one of our courses here at NTNU Ålesund, we have been assigned a group project to create an application for the Internet of Things (IoT). The intention of the project is to apply the knowledge on networking in a broader context, by actively using our former knowledge on system development to create an application with social meaningful benefits. Considering this, the group has decided to create an application for doctors to monitor its patients. The application will mainly target adults and elders, but also people suffering from other diagnoses to help in case of emergencies.

Statistics from 2021 shows that more than half of adults between 50 and 80 have health conditions that put them on high risk if they don't keep their blood pressure under control. In all, 26% of all these adults in the range of 50 to 80 years of age, said they dont monitor their blood pressure as often as they should[1].

We want to make an application which makes it easier for all patients to monitor their blood pressure. By using devices such as smart watches, we could sense minutely, or hourly, the patients's blood pressure in constant time, and send the information to the doctor for monitoring. Our application will also have the social benefit to warn doctors about patients whose blood pressure is too high, or too low, depening on the situation the patient is located in.

## Theory and technology
***

As of web development, we use HTML5 and CSS for webdesign and decoration. HTML is a hypertext markup language for the web that defines the structure of web pages by creating html elements. Web pages are mostly structured by divisions, also called divs. These are containers that contain other html elements such as paragraphs, tables, text and buttons. In our webdesign, we have actively been using divisons to distribute responsibility of elements to make both html and css code more structured. 

CSS, cascading style sheets, is a programming language used to describe html elements with properties such as coloring,

In terms of the data generation we chose to rely on syntetic data to simulate the health of the patients. As the measurement of blood pressure is highly complex and requires both technological and medical expertise to gather and interpret the data. With the timeframe of this project this would not be attainable. However, the data is based of actual medical records to ensure that the application is tested in a realistic enviroment[2]. Given that blood pressure oscillate it makes the modelling of the data more complex than it would be modelling stable data. In order to achieve realistic datasets we have incorporated the use of trigonometric functions as they have the ability to describe entities that fluctuate. 

## Results
***

#### Web

At first we were unsure on whether to use text-based terminal gui, or create a webpage for visualization. However, we landed on creating a webpage due to its simplicity and ease of use. Some of the functionality we discussed before creating the website was:
* Patients visualization through table
* Patient search
* Diagrams for bloodpressure
* Choose patient and see data
and structuring by using HTML elements. HTML elements are the building blocks of a webpage, and are created by using tags and attributes.

Some of our goals when designing the website are good interaction between user and machine, such 

Currently we have limited the scope of the webpage to only show critial patients at the dashboard, as well as all patients under the patients tab in the sidebar. By using sidebars, we can easily expand the scope and implement new functionality by writing more HTML and CSS code.


#### Database

For the database we have chosen a relational data model to store our patients and users data. As there are only 2 relationships and 2 entity sets to model we chose the relational model for familiarity. The model is structured in a way that patients can have multiple diagnoses and multiple data entries. To ensure the integrity of the database there is applied a primary key to all relations and entity sets, this ensures that a patient can only have a realtion to a diagnosis once and only one data entry at a given time.

![database_ER|600](/img/database_ER.png)


#### Data generation

In this case, a sine wave which grows psudo-randomly but are constructed in a way that it will only diverge from the average value when in range of realistic values for blood pressure. This way the data fluctuates as a blood pressure normally would and allows for a realistic model.

For improvements the generation methods could be optimized and refactored to a single module with the goal of generating, and a complementing module who focuses on generating patients. As it is now both generation of patients and data is done in the same module. But ultimatley the biggest improvment when it comes to the dataset of the application would be implementing actual sensors with actual real data from patients.

#### <b>Wireframes</b>
<!-- Extension -->
![Statistics|600](/img/WIREFRAME1.png)

![Patient_list|600](/img/WIREFRAME2.png)


## <b>References</b>
[1] https://labblog.uofmhealth.org/rounds/many-at-risk-older-adults-arent-checking-blood-pressure-at-home-or-being-encouraged-to-do-so?fbclid=IwAR1x0WsrFR9vXrwJmKyf8ys5_aMfzVVqm3BcdKE6KTIKHlJt2L3r7m-GgYk

[2] National Health and Nutrition Examination Survey 2007-2010. JAMA. 2011;305(19):1971-1979