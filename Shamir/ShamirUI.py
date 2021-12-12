import streamlit as st
import Shamir.Services.ControlsService as CS
import Shamir.Services.MathService as MS
import Shamir.Services.ShamirMethodMathService as smms
import Shamir.Constants as cst

def ShamirUi():
    secret = 0
    rangeMaxValue = 0
    generatedSecret = 0
    sharesCount = 0
    sharesToRecover = ""
    sharesToRecoverCount = 0
    prime = 0
    si = []

    method = st.radio("Wybierz metodę:", ["trywialny", "shamir"])
    if method == "trywialny":

        rangeMaxValue = st.number_input("podaj zakres (k): ", min_value=0)
        if rangeMaxValue != 0:
            secret = st.number_input("podaj wartość sekretu(s):", max_value=rangeMaxValue - 1, min_value=0)
        if secret != 0:
            sharesCount = st.number_input("podaj ilość udziałów(n):", min_value=0)
        if st.button("generuj:"):
            shares = MS.GenerateShares(sharesCount, rangeMaxValue, secret)
            st.write("udziały:")
            for share in shares:
                st.write(share)
            generatedSecret = MS.GenerateSecret(shares, rangeMaxValue)
            print(generatedSecret)
            st.write("Wygenerowany sekret: ")
            st.write(generatedSecret)

    if method == "shamir":

        secret = st.number_input("podaj wartość sekretu(s):", min_value=0)
        if secret != 0:
            sharesCount = st.number_input("podaj ilość udziałów(n):", min_value=0)
        if sharesCount != 0:
            sharesToRecoverCount = st.number_input("podaj ilość udziałów do odtworzenia(t)", min_value=0)
        if sharesToRecoverCount != 0:
            prime = st.select_slider(options=[i for i in cst.primeNumbers if i > secret and i > sharesCount], label="wybierz liczbę pierwszą:")
        if st.button("generuj"):
            AValues = smms.GetRandomAs(sharesToRecoverCount)
            Si = smms.GetSi(sharesCount, secret, sharesToRecoverCount, prime, AValues)
            for item in Si:
                st.write(item)
            returnedSecret = smms.RecoverSecret("1,2,3,4,5,6", Si, prime)
            st.write(returnedSecret)

