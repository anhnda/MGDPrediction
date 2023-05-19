#Gene2Drug
## Input-Output
- Input: A list of gens at ./data/gene_list.txt

- Output: Potentially associated drugs with each gen at ./wdir/Gene2Drugs.txt
## Running
### Training
```shell
    cd HyperAttentionDTI
    python HyperAttentionDTI_main.py
    cd ..
```
### Creating a dataset for prediction from a given gene list
```shell
   python main.py -c
```

### Prediction
```shell
    python main.py -p

```
