# Welcome to Okra-Mission subsystem.

## Overview - UX

Okra-mission is a subsystem package included in Okra web platform suitable for all devices with a browser and internet connection. It's made with the idea of being separately downloaded and installed from a marketplace on any device.

The idea behind this software product is creating a web application which will store and manage information about users consumption, providing and assesment and analysis of it.

  * Mainly is intended to give a:
     - Sustainable approach to minimize carbon footprint supporting local vendors.
     - Sustainable approach to maximize human wellbeing.
     - Sustainable approach to minimize environmental impact.
  * To provide information such as:
     - Environmental, Social and Governance Key Performance Indicators for investors.
  * To become a ***goblal collaboration site*** educating people to behave in benefit of the evolution, **"The tomorrow".**

Include (User stories and Mockups and diagrams)

## Features

+ Existing features

  Feature 1: Changing eating habits mission.

    Feature 1.1: User X fill out a form with basic information: Age, height, weight, occupation and medical
    conditions. User X submit the information and the System stores it.

    Feature 1.2: User X fill out a new food diary form: Select one to many meals taken during last 24 hours and the foods and quantity intaken in these meals. For each food, User X will provide the brand of the food or generic, in case has not being manufactured. User X will indicate if executed any physical exercise during the day. User X submit the form and the System will store the information. Also, system will respond with the nutricional values of the foods intaken and a global assement (healthy/medium healthy/unhealthy diet).

    Feature 1.3: User X will accept to receive some advise about how to improve the diet. System will respond with advises.

    Feature 1.4: User X can delete any entry (food) previously inserted from the pre-filled food diary form. System will delete the food from the food diary.

    Feature 1.5: User X selects seeing situation of the local market. System  will respond showing bubble chart with information about brands consumed in the local area, clasified by conglomerates if possible. (Dimension: region, Brand Name, Conglomerate) (Metrics: Number of products).

    Feature 1.6: User X selects seeing situation of the global market. System  will respond showing bubble chart with information about brands consumed globally, clasified by conglomerates if possible. (Dimension: country, Brand Name, Conglomerate) (Metrics: Number of products).

    For features 1.2 to 1.4 it has been used FastSecret Platform REST API, to get nutricional values. ** http://platform.fatsecret.com **

  + Features left to implement.

    Feature 1: Changing fashion style.

    Feature 2: Changing hobbies.

      Mindfulness exercises


## Design and implementation.


## Knowlegde analysis

```
Concept: Get mission subsystem ideally would be a web/mobile application that users can download from a market store for free.
         It will retrieve information about user habits (via a questionary), process them, and return a table and buble chart diagram with information about the nutricional status of his/her body, his/her responsible consumist habits, his/her healthy hobbies and his/her contribution to the local/global market.

DOMAIN-KNOWLEDGE: Eating habits
    DOMAIN SCHEMA DESCRIPTION: concepts, relations and rules descripting user habits when eating. How many meals they took per day, their total intakes and nutritinal values. Rules definition to consider a healthy meal base on nutricional values of the food taken.
    On the other hand, user can input brands they use to prepare or buy their meals,statistic study of the local market (clustering by area) and global market.
    KNOWLEDGE BASE DESCRIPTION: Analytical tasks: clasification, assesment  and prediction
                                Synthetic tasks: configuring and asigning confinguration (giving solutions to improve diets)
END DOMAIN-KNOWLEDGE Eating habits

DOMAIN SCHEMA: Nutrition
    DOMAIN SCHEMA DEPENDENCIES: MEALCATEGORY{Breakfast, Lunch, Evening dinner, Snack, Drink},
                                BRAND{Sturbucks, Costa Coffee, Chiquitos, Nandos, Pizza Hut, Yo!, No brand(Generic), Nestle, Coca-cola,
                                Kraft, Dr. Oetker, Pepsi, Lays, BirdsEye, Iceland, The happy egg.co},
                                NUTRIENTS/FOOD {},
    CONCEPTS, RELATIONS, RULES: FOODS[List[nutrients,proportion]] o-> MEALS[List[food,portion]] [x] -> NUTRITIONSTATUS[List[meal,status]]
END DOMAIN SCHEMA: Nutrition


#########################################################################
CONCEPT: USER
#########################################################################
CONCEPT user:
   DESCRIPTION
    "User registered for Get Mission Application"
   ATTRIBUTES
    name: STRING
    nationality: STRING
    age: INT
    gender: STRING
   AXIOMS
    age >= 16
END CONCEPT user
#########################################################################
CONCEPT: REQUEST ASSESMENT
#########################################################################
CONCEPT request:
    DESCRIPTION
    "User request assesment for a healthy diet"
    ATTRIBUTES
       age: INT
       job-profile: {Administrative and clerical, Alternative therapies, Animals, plants and land, Arts, crafts and design, Catering services ,Construction,
       Education and training, Environmental sciences, Financial services, General and personal services, Information technology and information management,
       Legal services, Maintenance, service and repair, Management and planning, Manufacturing and engineering, Marketing, selling and advertising, Medical technology,
       Medicine and nursing, Performing arts, broadcast and media, Publishing and journalism, Retail sales and customer service, Science and research,
       Security and uniformed services, Social services, Sport, leisure and tourism, Storage, dispatching and delivery, Transport}
       weight: INT
       height: INT
       Known medical conditions: {Alcohol abuse and alcoholism, Allergies, Alopecia areata, Amputation, Anxiety disorders, Arthritis ,Asperger syndrome ,Asthma,
       Attention deficit hyperactivity disorder (ADHD), Autism and autism spectrum disorders, Bipolar disorder, Bleeding disorders, Blindness and low vision,
       Brain injury, Burn injury, Cancer, Celiac disease, Cerebral palsy, Charcot-Marie-Tooth disease, Chronic fatigue syndrome, Chronic illness, Cleft lip and palate
       Crohn's disease, Cystic fibrosis, Deafness and being hard of hearing, Depression, Diabetes, Down syndrome, Drug abuse and addiction, Dwarfism,
       Eating disorders, Endometriosis, Epilepsy, Eczema, Fetal alcohol syndrome, Fibromyalgia, GERD (Gastroesophageal Reflux Disease), Growth hormone deficiency,
       Heart diseases, HIV/AIDS, Huntington's disease, Inflammatory bowel disease, Intellectual disabilities (Formerly mental retardation), Juvenile rheumatoid ,
       Kidney disease, Lactose intolerance, Learning disabilities, Lupus, Migraine, Mental health, Mono(nucleosis), Multiple sclerosis, Muscular dystrophy,
       Narcolepsy, Obesity, Obsessive compulsive disorder (OCD), Polycystic ovary syndrome (PCOS), Post-traumatic stress disorder, Psoriasis, Scleroderma,
       Scoliosis, Sickle cell anemia, Speech and language disorders, Spina bifida, Spinal cord injury, Stroke, Thyroid disease, Tourette syndrome, Turner syndrome,
       Ulcerative colitis, Ulcers, Williams syndrome}
       HAS-PARTS: list_of_meals
END CONCEPT request
CONCEPT: activity
   DESCRIPTION: "Depending job profile, activity is classified"
   ATTRIBUTES:
      activity-level: {Lighly active, Moderately active, Active, Very active }
END CONCEPT activity
############################################################################
CONCEPT: MEAL
############################################################################
CONCEPT meal:
  DESCRIPTION "Possible different meals the user has taken"
  SUPERTYPE-OF: Meal Category
        ATTRIBUTES
           %calories : KJules/Kcal
           %proteins : int
           %carbs: int
           %fat: int
        HAS-PARTS: lists_of_foods
        AXIOMS:
    <12-20% Proteins, <50-55% carbs, <25-30% fat: need to do meals with nutrients contained in proteins, carbs and fat
          <12-20% Proteins, >50-55% carbs, <25-30% fat:
          <12-20% Proteins, <50-55% carbs, >25-30% fat:
          12-20% Proteins,  50-55% carbs,  25-30% fat:
          >12-20% Proteins, >50-55% carbs, >25-30% fat:
          >12-20% Proteins, <50-55% carbs, >25-30% fat:
          >12-20% Proteins, >50-55% carbs, <25-30% fat:
END CONCEPT meal
############################################################################
CONCEPT:FOOD
############################################################################
CONCEPT food:
  DESCRIPTION: "List of nutrients per intake"
        SUBTYPE-OF: meal
        ATRIBUTES
END CONCEPT food
############################################################################
CONCEPT: NUTRICION STATUS
############################################################################
CONCEPT nutricionStatus:
     DESCRIPTION
     "Nutricion status after assesment"
     ATTRIBUTES
     weight4age status: {standar, mild, moderate, sever, more sever}
     height4age: {normal, stunting, severe stunting}
     weight4height: {normal, wasting, severe wasting}
     index mass: {underweight, normal, overweight}
     activity:
     AXIOMS:
       12-20% Proteins, 50-55% carbs, 25-30% fat, weight4age status standar, height4age normal, index mass normal  = healthy
       <12-20% Proteins, < 50-55% carbs, < 25-30% fat, weight4age status standar, height4age normal, index mass normal  = medium healthy
       >12-20% Proteins, > 50-55% carbs, > 25-30% fat, weight4age status standar, height4age normal, index mass normal  = unhealthy
END CONCEPT
END DOMAIN SCHEMA Nutrition

```
## Technologies used

  Google analytics: to get the information about users connected to the application and usage.
  Fast secret: Foods knowledge base.
  Google charts: Javascript library to create dashboard with analytic data.


## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:

Different values for environment variables (Heroku Config Vars)?
Different configuration files?
Separate git branch?
In addition, if it is not obvious, you should also describe how to run your code locally.


## Run in development

 Use of Flask microframework as development runtime environment.

+ set FLASK_APP=run.py
+ set FLASK_ENV=development
+ flask


## Test Driven Design

Test Scenario and Test Cases


## Credits

## Content

+ The text for section Y was copied from the Wikipedia article Z

## Media

+ The photos used in this site were obtained from ...

## Acknowledges

+ Thanks to Laura Malo for understanding quickly the idea behind this project.
  She supported this work with her advises and knowledge in sustainability.




