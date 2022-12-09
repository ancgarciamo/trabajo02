import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, RepeatedStratifiedKFold, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_curve, roc_auc_score, confusion_matrix, precision_recall_curve, auc
from sklearn.feature_selection import f_classif
from sklearn.pipeline import Pipeline
from sklearn.base import BaseEstimator, TransformerMixin
from scipy.stats import chi2_contingency
import lzma
import dill as pickle
import streamlit as st

ref_categories = ['mths_since_last_credit_pull_d:>75', 'mths_since_issue_d:>122', 'mths_since_earliest_cr_line:>434', 'total_rev_hi_lim:>79,780',
                  'total_rec_int:>7,260', 'total_pymnt:>25,000', 'out_prncp:>15,437', 'revol_util:>1.0', 'inq_last_6mths:>4', 'dti:>35.191',
                  'annual_inc:>150K', 'int_rate:>20.281', 'term:60', 'purpose:major_purch__car__home_impr', 'verification_status:Not Verified',
                  'home_ownership:MORTGAGE', 'grade:G']



@st.cache
def scores_guardados():
    with lzma.open('Scorecard.pkl', 'rb') as file:
        scores_saveg = pickle.load(file)
        return scores_saveg


scores_save = scores_guardados()
@st.cache
def woes_guardados():
    with lzma.open('WOE.pkl', 'rb') as file:
        woe_save_g = pickle.load(file)
        return woe_save_g

woe_save = woes_guardados()



def main():

    a,b,c,d,e,f,g=0,0,0,0,0,0,0
    v1,v2,v3=0,0,0
    h1,h2,h3,h4,h5=0,0,0,0,0
    p1,p2,p3,p4,p5=0,0,0,0,0
    p6,p7,p8,p9,p10=0,0,0,0,0
    p11,p12,p13,p14=0,0,0,0

    st.title("Formulario del scorecard")

    st.text("llene el formulario , y abajo podra ver su puntaje y su comparacion con la población")

    termino = st.radio("Escoja el termino del credito", (36, 60))
    tasa_int = st.number_input('Ingrese la tasa de interés del préstamo')

    texto_grado=st.text_input("Ingrese en mayusculas unicamente una letra entre A y G",value='C')

    num_anos_trabajando = st.slider("Ingrese el número de años que ha trabajado", 0, 10, 1)

    ingresos = st.number_input('Ingrese la cantidad de sus ingresos anuales',value=10000)
    st.text("Ingrese la verificacion asi")
    st.markdown('- Not Verified \n - Source Verified \n - Verified')
    status_de_verificacion = st.text_input("Ingrese el estado de verificacion:",value="Verified")
    st.text("")

    st.text("Ingrese el proposito del credito asi")
    st.markdown('- car \n - credit_card \n - debt_consolidation \n - educational \n - home_improvement \n - house \n - major_purchase \n - medical \n - moving \n - other \n - renewable_energy \n - small_business \n - vacation \n - wedding')

    status_de_proposito = st.text_input("Ingrese el proposito del credito",value="debt_consolidation")
    st.text("")
    st.text("Ingrese el estado de vivienda asi")
    st.markdown('- MORTGAGE \n - NONE \n - OTHER \n - OWN \n - RENT')

    status_de_casa = st.text_input("Ingrese el estado de su vivienda ",value="OWN")

    if texto_grado == 'A':
        a = 1
    elif texto_grado == 'B':
        b = 1
    elif texto_grado == 'C':
        c = 1
    elif texto_grado == 'D':
        d = 1
    elif texto_grado == 'E':
        e = 1
    elif texto_grado == 'F':
        f = 1
    elif texto_grado == 'G':
        g = 1


    if status_de_verificacion == 'Not Verified':
        v1 = 1
    elif status_de_verificacion == 'Fuente verificada':
        v2 = 1
    elif status_de_verificacion == 'Verificado':
        v3 = 1
    else:
        status_de_verificacion=""

    if status_de_casa == 'MORTGAGE':
        h1 = 1
    elif status_de_casa == 'NONE':
        h2 = 1
    elif status_de_casa == 'OTHER':
        h3 = 1
    elif status_de_casa == 'OWN':
        h4 = 1
    elif status_de_casa == 'RENT':
        h5 = 1
    else:
        status_de_casa=""

    if status_de_proposito == 'car':
        p1 = 'car'
    elif status_de_proposito == 'credit_card':
        p2 = 1
    elif status_de_proposito == 'debt_consolidation':
        p3 = 1
    elif status_de_proposito == 'educational':
        p4 = 1
    elif status_de_proposito == 'home_improvement':
        p5 = 1
    elif status_de_proposito == 'house':
        p6 = 1
    elif status_de_proposito == 'major_purchase':
        p7 = 1
    elif status_de_proposito == 'medical':
        p8 = 1
    elif status_de_proposito == 'moving':
        p9 = 1
    elif status_de_proposito == 'other':
        p10 = 1
    elif status_de_proposito == 'renewable_energy':
        p11 = 1
    elif status_de_proposito == 'small_business negocio':
        p12 = 1
    elif status_de_proposito == 'vacation':
        p13 = 1
    elif status_de_proposito == 'wedding':
        p14 = 1
    else:
        status_de_proposito=""

    a1 = st.number_input(
        "Ingrese su dti",value=1.6)
    a2 = st.number_input(
        "Ingrese el número de consultas en los últimos 6 meses",value=12)
    a3 = st.number_input(
        "Cantidad del crédito que el prestatario está utilizando en relación con todo el crédito giratorio disponible",
        value=7.1)
    a4 = st.number_input(
        "Ingrese el número total de líneas de crédito actualmente", value=12)
    a5 = st.number_input("Capital restante pendiente por el monto total financiado", value=1700)
    a6 = st.number_input("Ingrese el total de  pagos hasta la fecha", value=2500)
    a7 = st.number_input("Ingrese el total de los intereses hasta la fecha", value=520)
    a8 = st.number_input("Ingrese el último monto total de pago recibido", value=186)
    a9 = st.number_input("Ingrese su saldo actual total de todas las cuentas", value=4000)
    a10 = st.number_input("Límite total de crédito/crédito de alto aumento giratorio", value=26000)
    a11 = st.number_input("Número de meses desde que se abrió la línea de crédito más temprana del prestatario",
                               value=200)
    a12 = st.number_input("Número de meses desde que el préstamo fue hecho", value=50)
    a13 = st.number_input("Número de  meses desde efectuo su ultimo pago", value=50)
    a14 = st.number_input("Número de meses desde que la linea de credito obtuvo crédito por este préstamo", value=50)

    dataframe_ingresado = [{'term': termino,
                        'int_rate': tasa_int,
                        'grade': texto_grado,
                        'emp_length': num_anos_trabajando,
                        'home_ownership': status_de_casa,
                        'annual_inc': ingresos,
                        'verification_status': status_de_verificacion,
                        'purpose': status_de_proposito,
                        'dti': a1,
                        'inq_last_6mths': a2,
                        'revol_util': a3,
                        'total_acc': a4,
                        'out_prncp': a5,
                        'total_pymnt': a6,
                        'total_rec_int': a7,
                        'last_pymnt_amnt': a8,
                        'tot_cur_bal': a9,
                        'total_rev_hi_lim': a10,
                        'mths_since_earliest_cr_line': a11,
                        'mths_since_issue_d': a12,
                        'mths_since_last_pymnt_d': a13,
                        'mths_since_last_credit_pull_d': a14,
                        'grade:A': a,
                        'grade:B': b,
                        'grade:C': c,
                        'grade:D': d,
                        'grade:E': e,
                        'grade:F': f,
                        'grade:G': g,
                        'home_ownership:MORTGAGE': h1,
                        'home_ownership:NONE': h2,
                        'home_ownership:OTHER': h3,
                        'home_ownership:OWN': h4,
                        'home_ownership:RENT': h5,
                        'verification_status:Not Verified': v1,
                        'verification_status:Source Verified': v2,
                        'verification_status:Verified': v3,
                        'purpose:car': p1,
                        'purpose:credit_card': p2,
                        'purpose:debt_consolidation': p3,
                        'purpose:educational': p4,
                        'purpose:home_improvement': p5,
                        'purpose:house': p6,
                        'purpose:major_purchase': p7,
                        'purpose:medical': p8,
                        'purpose:moving': p9,
                        'purpose:other': p10,
                        'purpose:renewable_energy': p11,
                        'purpose:small_business': p12,
                        'purpose:vacation': p13,
                        'purpose:wedding': p14
                        }]
    dataframe_final = pd.DataFrame(dataframe_ingresado)
    X_test_woe_transformed = woe_save.fit_transform(dataframe_final)
    X_test_woe_transformed.insert(0, 'Intercept', 1)
    scorecard_scores = scores_save['Score - Final']
    X_test_woe_transformed = pd.concat(
        [X_test_woe_transformed, pd.DataFrame(dict.fromkeys(ref_categories, [0] * len(X_test_woe_transformed)),
                                              index=X_test_woe_transformed.index)], axis=1)

    scorecard_scores = scorecard_scores.values.reshape(102, 1)
    y_scores = X_test_woe_transformed.dot(scorecard_scores)

    st.title("Puntuacion")
    st.markdown("Su puntaje es : " + str(y_scores[0][0]))
    media = 549.198462
    st.markdown("El puntaje promedio en el Scorecard de la poblacion es:  " + str(media))
    if y_scores[0][0] >= media:
        st.markdown("Su puntaje es superior a la media de la poblacion")
    else:
        st.markdown("Su puntaje es inferior a la media de la poblacion")



if __name__=="__main__":
   main()