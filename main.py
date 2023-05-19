import params
from optparse import OptionParser


def parse_config(opts):
    params.GEN_SUFFIX = opts.s
    params.I_SEG = opts.sid
    params.DEVICE = opts.device

if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-d", "--device", dest="device", type='str', default='cuda:0', help="Device")

    parser.add_option("-s", "--suffix", dest="s", type='str', default='', help="Gene list type: '' for all, 'M' for male, 'F' for female")
    parser.add_option("-c", "--create", dest="c", action='store_true', help="Flag for creating a test file")
    parser.add_option("-p", "--predict", dest="p", action='store_true', help="Flag for predicting")
    parser.add_option("-i", "--sid", dest="sid", type='int', default=-1, help="Segment id")

    parser.add_option("-m", "--merge", dest="m", action='store_true', help="Merge prediction")

    parser.add_option("-x", "--export", dest="x", action='store_true', help="Flag for exporting scores")


    (options, args) = parser.parse_args()
    parse_config(options)
    if options.c:
        from exportSelectedGeneProteins import match
        from createNewTestFile import create_test
        match()
        create_test(params.N_SEG)
    elif options.p:
        from HyperAttentionDTI.predicting import run_predict
        print("Run prediction...")
        run_predict()
    elif options.m:
        from HyperAttentionDTI.predicting import merge
        print("Run merging...")
        merge()

    elif options.x:
        from exportSelectedGeneProteins import export_gene_drug
        print("Exporting gene-drug scores...")
        export_gene_drug()






