from django.shortcuts import render
from .forms import PatientPredictionForm
import joblib

model1 = joblib.load('./model/PatientMiseInva81.joblib')
model2 = joblib.load('./model/Repos93model.joblib')
model3 = joblib.load('./model/reprise.joblib')
# Create your views here.
def predict(request):
    Repos = None
    MiseInv = None
    reprise = None
    form=PatientPredictionForm()
    if request.method == "POST":
        form=PatientPredictionForm(request.POST)
        if form.is_valid():
            Type_ACT_MLD = form.cleaned_data['Type_ACT_MLD']
            mode_début = form.cleaned_data['mode_début']
            lombalgies= form.cleaned_data['lombalgies']
            sciatalgie= form.cleaned_data['sciatalgie']
            diabète= form.cleaned_data['diabète']
            HTA=form.cleaned_data['HTA']
            respiratoire=form.cleaned_data['respiratoire']
            Autre_1=form.cleaned_data['Autre_1']
            mariage=form.cleaned_data['mariage']
            nombre_enfants=form.cleaned_data['nombre_enfants']
            rééducation=form.cleaned_data['rééducation']
            age=form.cleaned_data['age']
            état_général=form.cleaned_data['état_général']
            coopérant=form.cleaned_data['coopérant']
            poids=form.cleaned_data['poids']
            taille=form.cleaned_data['taille']
            IMC=form.cleaned_data['IMC']
            corpulence=form.cleaned_data['corpulence']
            ceinture_de_soutien=form.cleaned_data['ceinture_de_soutien']
            boiterie=form.cleaned_data['boiterie']
            déroulement_du_pas=form.cleaned_data['déroulement_du_pas']
            droit=form.cleaned_data['droit']
            gauche=form.cleaned_data['gauche']
            sur_les_talons=form.cleaned_data['sur_les_talons']
            sur_les_pointes_des_pieds=form.cleaned_data['sur_les_pointes_des_pieds']
            mode=form.cleaned_data['mode']
            stabilité=form.cleaned_data['stabilité']
            cicatrice=form.cleaned_data['cicatrice']
            ROT=form.cleaned_data['ROT']
            
            
            Repos = model1.predict([[Type_ACT_MLD,
            mode_début,
            lombalgies,
            sciatalgie,
            diabète,
            HTA,
            respiratoire,
            Autre_1,
            mariage,
            nombre_enfants,
            rééducation,
            age,
            état_général,
            coopérant,
            poids,
            taille,
            IMC,
            corpulence,
            ceinture_de_soutien,
            boiterie,
            déroulement_du_pas,
            droit,
            gauche,
            sur_les_talons,
            sur_les_pointes_des_pieds,
            mode,
            stabilité,
            cicatrice,
            ROT]])
            MiseInv = model2.predict([[
            Type_ACT_MLD,
            mode_début,
            lombalgies,
            sciatalgie,
            diabète,
            HTA,
            respiratoire,
            Autre_1,
            mariage,
            nombre_enfants,
            rééducation,
            age,
            état_général,
            coopérant,
            poids,
            taille,
            IMC,
            corpulence,
            ceinture_de_soutien,
            boiterie,
            déroulement_du_pas,
            droit,
            gauche,
            sur_les_talons,
            sur_les_pointes_des_pieds,
            mode,
            stabilité,
            cicatrice,
            ROT
            ]])
            
            reprise = model3.predict([[
            Type_ACT_MLD,
            mode_début,
            lombalgies,
            sciatalgie,
            diabète,
            HTA,
            respiratoire,
            Autre_1,
            mariage,
            nombre_enfants,
            rééducation,
            age,
            état_général,
            coopérant,
            poids,
            taille,
            IMC,
            corpulence,
            ceinture_de_soutien,
            boiterie,
            déroulement_du_pas,
            droit,
            gauche,
            sur_les_talons,
            sur_les_pointes_des_pieds,
            mode,
            stabilité,
            cicatrice,
            ROT
            ]])
            
            if Repos == 1:
                Repos = "Justifié"
            else:
                Repos ="Non justifié"
            if MiseInv == 1:
                MiseInv = "Oui"
            else:
                MiseInv = "Non"
            if reprise == 1:
                reprise = "Oui"
            else:
                reprise = "Non"

            
    context = {
        "form":form,
        "Repos":Repos,
        "MiseInv":MiseInv,
        "reprise":reprise
    }
    return render(request, 'form.html',context)
