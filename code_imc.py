import streamlit as st

st.title(u"Programme qui calcule l'indice de la masse corporelle (IMC)")

st.write("===============================================")
st.header(u"Saisi des informations pour le calcul de l'IMC")
st.write("------------------------------------------------")
nom = st.text_input(u"Saisir votre nom :")
age = st.number_input(u"Saisir votre âge")
poids = st.number_input(u"Saisir votre poids en kilogramme (KG)")
taille =  st.number_input(u"Saisir votre taille en mètre (M)")

st.write("------------------------------------------------")

# Calcul de l'IMC
button = st.button(u"Calculer votre IMC")

if button :
    if (nom !="" and age != 0 and poids !="" and taille !=0) :
        imc = poids/(taille**2)
        if imc < 16:
            st.write("L'IMC de {} est :".format(nom))
            st.success(imc)
            st.text(u"Selon l'OMS, dans votre cas on parle d'anorexie ou de dénutrition")
            st.write("------------------------------------------------")
            if age>=19 and age<24:
                st.text(u"Selon l'OMS et votre âge, votre IMC doit être entre 19 et 24")
            elif age >=24 and age<=34 :
                st.text(u"Selon l'OMS et votre âge, votre IMC doit être entre 20 et 25")
            elif age >=35 and age<=44 :
                st.text(u"Selon l'OMS et votre âge, votre IMC doit être entre 21 et 26")
            elif age >=45 and age<54 :
                st.text(u"Selon l'OMS et votre âge, votre IMC doit être entre 22 et 27")
            elif age >=55 and age<64 :
                st.text(u"Selon l'OMS et votre âge, votre IMC doit être entre 23 et 28")
            else :
                st.text(u"Votre age n'est pas catégorisé")

        elif imc>=16.50 and imc<18.50 :
            st.write("L'IMC de {} est :".format(nom))
            st.success(imc)
            st.text(u"Selon l'OMS, vous êtes en Ã©tat de maigreur ")
            st.write("------------------------------------------------")
            if age>=19 and age<24:
                st.text(u"Selon l'OMS et votre âge, votre IMC doit être entre 19 et 24")
            elif age >=24 and age<=34 :
                st.text(u"Selon l'OMS et votre âge, votre IMC doit être entre 20 et 25")
            elif age >=35 and age<=44 :
                st.text(u"Selon l'OMS et votre âge, votre IMC doit être entre 21 et 26")
            elif age >=45 and age<54 :
                st.text(u"Selon l'OMS et votre âge, votre IMC doit être entre 22 et 27")
            elif age >=55 and age<64 :
                st.text(u"Selon l'OMS et votre âge, votre IMC doit être entre 23 et 28")
            else :
                st.text(u"Votre age n'est pas catégorisé")

        elif imc>=18.50 and imc<=25 :
            st.write(u"L'IMC de {} est :".format(nom))
            st.success(imc)
            st.text(u"Selon l'OMS, vous avez une corpulence normale")
            st.write("------------------------------------------------")
            if age>=19 and age<24:
                st.text(u"Selon l'OMS et votre âge, votre IMC doit être entre 19 et 24")
            elif age >=24 and age<=34 :
                st.text(u"Selon l'OMS et votre âge, votre IMC doit être entre 20 et 25")
            elif age >=35 and age<=44 :
                st.text(u"Selon l'OMS et votre âge, votre IMC doit être entre 21 et 26")
            elif age >=45 and age<54 :
                st.text(u"Selon l'OMS et votre âge, votre IMC doit être entre 22 et 27")
            elif age >=55 and age<64 :
                st.text(u"Selon l'OMS et votre âge, votre IMC doit être entre 23 et 28")
            else :
                st.text(u"Votre age n'est pas catégorisé")


        elif imc>25 and imc<=30 :
            st.write(u"L'IMC de {} est :".format(nom))
            st.success(imc)
            st.text(u"Selon l'OMS, vous êtes en surpoids")
            st.write("------------------------------------------------")
            if age>=19 and age<24:
                st.text(u"Selon l'OMS et votre âge, votre IMC doit être entre 19 et 24")
            elif age >=24 and age<=34 :
                st.text(u"Selon l'OMS et votre âge, votre IMC doit être entre 20 et 25")
            elif age >=35 and age<=44 :
                st.text(u"Selon l'OMS et votre âge, votre IMC doit être entre 21 et 26")
            elif age >=45 and age<54 :
                st.text(u"Selon l'OMS et votre âge, votre IMC doit être entre 22 et 27")
            elif age >=55 and age<64 :
                st.text(u"Selon l'OMS et votre âge, votre IMC doit être entre 23 et 28")
            else :
                st.text(u"Votre age n'est pas catégorisé")


        elif imc > 30 and imc <= 35:
            st.write(u"L'IMC de {} est :".format(nom))
            st.success(imc)
            st.text(u"Selon l'OMS, vous êtes en obésité modérée de classe 1")
            st.write("------------------------------------------------")
            if age>=19 and age<24:
                st.text(u"Selon l'OMS et votre âge, votre IMC doit être entre 19 et 24")
            elif age >=24 and age<=34 :
                st.text(u"Selon l'OMS et votre âge, votre IMC doit être entre 20 et 25")
            elif age >=35 and age<=44 :
                st.text(u"Selon l'OMS et votre âge, votre IMC doit être entre 21 et 26")
            elif age >=45 and age<54 :
                st.text(u"Selon l'OMS et votre âge, votre IMC doit être entre 22 et 27")
            elif age >=55 and age<64 :
                st.text(u"Selon l'OMS et votre âge, votre IMC doit être entre 23 et 28")
            else :
                st.text(u"Votre age n'est pas catégorisé")


        elif imc > 35 and imc <= 40:
            st.write(u"L'IMC de {} est :".format(nom))
            st.success(imc)
            st.text(u"Selon l'OMS, vous êtes en obésité élevée de classe 2")
            st.write("------------------------------------------------")
            if age>=19 and age<24:
                st.text(u"Selon l'OMS et votre âge, votre IMC doit être entre 19 et 24")
            elif age >=24 and age<=34 :
                st.text(u"Selon l'OMS et votre âge, votre IMC doit être entre 20 et 25")
            elif age >=35 and age<=44 :
                st.text(u"Selon l'OMS et votre âge, votre IMC doit être entre 21 et 26")
            elif age >=45 and age<54 :
                st.text(u"Selon l'OMS et votre âge, votre IMC doit être entre 22 et 27")
            elif age >=55 and age<64 :
                st.text(u"Selon l'OMS et votre âge, votre IMC doit être entre 23 et 28")
            else :
                st.text(u"Votre âge n'est pas catégorisé")


        else :
            st.write(u"L'IMC de {} est :".format(nom))
            st.success(imc)
            st.text(u"Selon l'OMS, vous êtes en obésité morbide ou massive ")
            st.write("------------------------------------------------")
            if age>=19 and age<24:
                st.text(u"Selon l'OMS et votre âge, vous IMC doit être entre 19 et 24")
            elif age >=24 and age<=34 :
                st.text(u"Selon l'OMS et votre âge, votre IMC doit être entre 20 et 25")
            elif age >=35 and age<=44 :
                st.text(u"Selon l'OMS et votre âge, votre IMC doit être entre 21 et 26")
            elif age >=45 and age<54 :
                st.text(u"Selon l'OMS et votre âge, votre IMC doit être entre 22 et 27")
            elif age >=55 and age<64 :
                st.text(u"Selon l'OMS et votre âge, votre IMC doit être entre 23 et 28")
            else :
                st.text(u"Votre age n'est pas catÃ©gorisÃ©")


    else : st.error(u"Vérifier la saisie des informations!")

