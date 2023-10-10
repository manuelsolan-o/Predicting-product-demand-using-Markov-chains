# Predicting product demand using Markov chains

<p align="center">
<img src="images/medicom.png" alt="medicom" width="250" height="170">
</p>

<p align="center">
  <em> This project was developed in collaboration with Medicom, a business unit of Grupo PISA. </em>
</p>

__Authors__: [Alejandra Velaco](https://github.com/Aleevz), [Manuel Solano](https://github.com/manuelsolan-o), [José Carlos Yamuni](https://github.com/josecyamuni), [Antonio Juaréz](https://github.com/JAJP2203), [Mayra de Luna](https://github.com/mayradlu)

## General Information

[Grupo PiSA](https://www.pisa.com.mx/) is a 100% Mexican company founded in 1946, dedicated to developing comprehensive products and services for the public and private healthcare sectors in Mexico, the United States, Latin America, and the Caribbean. The growth of PiSA Pharmaceutical has been consistent over the years, and they are recognized for their extensive production capacity and vast experience in the market, allowing them to set the standard for their growth and international expansion. One of the business units within the PiSA group, catering to the most fragmented segment of the market, is Medicom. Medicom specializes in selling medicines and healthcare products to hospitals (clinics), pharmacies, and distributors. The behaviors of the three sales profiles at Medicom are as follows:

* Hospitals (clinics): Products for patient care are sold, and purchases are recurrent but in smaller quantities, resulting in less competition.

* Pharmacies: Products sold are for home use, leading to recurrent purchases in smaller quantities and higher competition.

* Distributors: Products are supplied to clinics and pharmacies, resulting in less recurrent but larger quantity purchases.

The top 20% of Medicom's customers represent 80% of the market consumption, and they have over 4,000 customers nationwide. Due to Medicom's significant impact within PiSA, there is a need to analyze the supply and demand behavior of PiSA's products to understand the probability of product activation and deactivation.

## Objective

The objective of this project is to analyze the probability of each customer discontinuing the purchase of each product and, in the event that the products are deactivated, to understand the probability of customers repurchasing these products. Furthermore, the aim is to analyze the data in order to formulate various hypotheses and thereby gain insights into different customer patterns and behaviors.

## Instalation
### Step 1)

To install the libraries needed to run the app, we need to write the following in the terminal:
pip install -r requirements.txt
OR
pip3 install -r requirements.txt

### Step 2)
Run the app.py file from the directory where the app has been downloaded

    streamlit run app.py
