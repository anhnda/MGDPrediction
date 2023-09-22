# Gene2Drug

## Input-Output
- Input: A list of gens at ./data/gene_list.txt
  - Format: Each line is a GeneName

- Output: Potentially associated drugs with each gen at ./wdir/Gene2Drugs.txt
  - Format: Each line contains predicted associated scores of drug with a gene: 
    - GeneName||drug1Id|score drug2Id|score...
## Running
### Training
```shell
    cd HyperAttentionDTI
    python HyperAttentionDTI_main.py
    cd ..
```
### Creating a dataset for prediction from a given gene list
```shell
   cd wdir
   unzip UniprotReviewedMapping2.zip
   cd ..
   python main.py -c
```

### Prediction
```shell
    python main.py -p

```
### Exporting predicted gene-drug scores
```shell
    python main.py -x

```
