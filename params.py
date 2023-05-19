import os

C_DIR = os.path.dirname(os.path.abspath(__file__))
W_DIR = "%s/wdir" % C_DIR
DATA_DIR = "%s/data" % C_DIR
DrugBankDrugGenePathO = "%s/data/DrugBankProteinGeneTarget.txt" % C_DIR
DrugBankDrugGenePath = "%s/data/DrugBankProteinGeneTargetNN.txt" % C_DIR


GENE_DRUG_JSON = "%s/GeneDrug.json" % W_DIR
DRUGBANK_PROTEINIDNOMATPPING_PATH = "%s/data/BENoUniProt_filter.txt" % C_DIR

UNIPORT_REVIEWED_PATH = "/home/gpux1/Data/UniProtReviewed/uniprot_sprot.dat"
GEN_SUFFIX = ""
DEVICE = "cuda:0"
N_SEG = 1
I_SEG = -1
FULL_PREDICTION = True
GENE_PATH = "%s/gene_list_females.txt" % DATA_DIR
if GEN_SUFFIX == "M":
    GENE_PATH = "%s/gene_list_male.txt" % DATA_DIR
elif GEN_SUFFIX == "":
    GENE_PATH = "%s/gene_list.txt" % DATA_DIR
