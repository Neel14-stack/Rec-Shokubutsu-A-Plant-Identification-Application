from fastapi import FastAPI,File, UploadFile
from io import BytesIO
from PIL import Image
import tensorflow as tf
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
import socket
import numpy as np
#socket.getaddrinfo('127.0.0.1', 8080)

app = FastAPI()

MODEL = tf.keras.models.load_model("D:/Uzumaki/GitHub/Plant_disease/plant.h5")
CLASS_NAMES = ['abies_concolor',
 'abies_nordmanniana',
 'acer_campestre',
 'acer_ginnala',
 'acer_griseum',
 'acer_negundo',
 'acer_palmatum',
 'acer_pensylvanicum',
 'acer_platanoides',
 'acer_pseudoplatanus',
 'acer_rubrum',
 'acer_saccharinum',
 'acer_saccharum',
 'aesculus_flava',
 'aesculus_glabra',
 'aesculus_hippocastamon',
 'aesculus_pavi',
 'ailanthus_altissima',
 'albizia_julibrissin',
 'amelanchier_arborea',
 'amelanchier_canadensis',
 'amelanchier_laevis',
 'asimina_triloba',
 'betula_alleghaniensis',
 'betula_jacqemontii',
 'betula_lenta',
 'betula_nigra',
 'betula_populifolia',
 'broussonettia_papyrifera',
 'carpinus_betulus',
 'carpinus_caroliniana',
 'carya_cordiformis',
 'carya_glabra',
 'carya_ovata',
 'carya_tomentosa',
 'castanea_dentata',
 'catalpa_bignonioides',
 'catalpa_speciosa',
 'cedrus_atlantica',
 'cedrus_deodara',
 'cedrus_libani',
 'celtis_occidentalis',
 'celtis_tenuifolia',
 'cercidiphyllum_japonicum',
 'cercis_canadensis',
 'chamaecyparis_pisifera',
 'chamaecyparis_thyoides',
 'chionanthus_retusus',
 'chionanthus_virginicus',
 'cladrastis_lutea',
 'cornus_florida',
 'cornus_kousa',
 'cornus_mas',
 'corylus_colurna',
 'crataegus_crus-galli',
 'crataegus_laevigata',
 'crataegus_phaenopyrum',
 'crataegus_pruinosa',
 'crataegus_viridis',
 'cryptomeria_japonica',
 'diospyros_virginiana',
 'eucommia_ulmoides',
 'evodia_daniellii',
 'fagus_grandifolia',
 'ficus_carica',
 'fraxinus_americana',
 'fraxinus_nigra',
 'fraxinus_pennsylvanica',
 'ginkgo_biloba',
 'gleditsia_triacanthos',
 'gymnocladus_dioicus',
 'halesia_tetraptera',
 'ilex_opaca',
 'juglans_cinerea',
 'juglans_nigra',
 'juniperus_virginiana',
 'koelreuteria_paniculata',
 'larix_decidua',
 'liquidambar_styraciflua',
 'liriodendron_tulipifera',
 'maclura_pomifera',
 'magnolia_acuminata',
 'magnolia_denudata',
 'magnolia_grandiflora',
 'magnolia_macrophylla',
 'magnolia_soulangiana',
 'magnolia_stellata',
 'magnolia_tripetala',
 'magnolia_virginiana',
 'malus_angustifolia',
 'malus_baccata',
 'malus_coronaria',
 'malus_floribunda',
 'malus_hupehensis',
 'malus_pumila',
 'metasequoia_glyptostroboides',
 'morus_alba',
 'morus_rubra',
 'nyssa_sylvatica',
 'ostrya_virginiana',
 'oxydendrum_arboreum',
 'paulownia_tomentosa',
 'phellodendron_amurense',
 'picea_abies',
 'picea_orientalis',
 'picea_pungens',
 'pinus_bungeana',
 'pinus_cembra',
 'pinus_densiflora',
 'pinus_echinata',
 'pinus_flexilis',
 'pinus_koraiensis',
 'pinus_nigra',
 'pinus_parviflora',
 'pinus_peucea',
 'pinus_pungens',
 'pinus_resinosa',
 'pinus_rigida',
 'pinus_strobus',
 'pinus_sylvestris',
 'pinus_taeda',
 'pinus_thunbergii',
 'pinus_virginiana',
 'pinus_wallichiana',
 'platanus_acerifolia',
 'platanus_occidentalis',
 'populus_deltoides',
 'populus_grandidentata',
 'populus_tremuloides',
 'prunus_pensylvanica',
 'prunus_sargentii',
 'prunus_serotina',
 'prunus_serrulata',
 'prunus_subhirtella',
 'prunus_virginiana',
 'prunus_yedoensis',
 'pseudolarix_amabilis',
 'ptelea_trifoliata',
 'pyrus_calleryana',
 'quercus_acutissima',
 'quercus_alba',
 'quercus_bicolor',
 'quercus_cerris',
 'quercus_coccinea',
 'quercus_falcata',
 'quercus_imbricaria',
 'quercus_macrocarpa',
 'quercus_marilandica',
 'quercus_michauxii',
 'quercus_montana',
 'quercus_muehlenbergii',
 'quercus_nigra',
 'quercus_palustris',
 'quercus_phellos',
 'quercus_robur',
 'quercus_rubra',
 'quercus_shumardii',
 'quercus_stellata',
 'quercus_velutina',
 'quercus_virginiana',
 'robinia_pseudo-acacia',
 'salix_babylonica',
 'salix_caroliniana',
 'salix_matsudana',
 'salix_nigra',
 'sassafras_albidum',
 'staphylea_trifolia',
 'stewartia_pseudocamellia',
 'styrax_japonica',
 'styrax_obassia',
 'syringa_reticulata',
 'taxodium_distichum',
 'tilia_americana',
 'tilia_cordata',
 'tilia_europaea',
 'tilia_tomentosa',
 'toona_sinensis',
 'tsuga_canadensis',
 'ulmus_americana',
 'ulmus_glabra',
 'ulmus_parvifolia',
 'ulmus_pumila',
 'ulmus_rubra',
 'zelkova_serrata']


origins = [
    "http://localhost",
    "http://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/ping")
async def ping():
    return "Hello I'm alive server"

def read_file_as_image(data) -> np.ndarray:
    image = np.array(Image.open(BytesIO(data)))
    return image

@app.post("/predict")
async def predict(
    file: UploadFile = File(...)

):
    image = read_file_as_image(await file.read())
    img_batch = np.expand_dims(image,0)
    
    prediction = MODEL.predict(img_batch)

    predicted_class = CLASS_NAMES[np.argmax(prediction[0])]
    confidence = np.max(prediction[0])
    return {
        'class': predicted_class,
        'confidence': float(confidence)
    }
    pass

if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1',port = 8080)