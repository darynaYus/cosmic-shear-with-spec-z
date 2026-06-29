import treecorr
import numpy as np

def get_catalog_columns(catalog_file):
    return (
        catalog_file['TARGET_RA'],
        catalog_file['TARGET_DEC'],
        catalog_file['e1'],
        catalog_file['e2'],
        catalog_file['Z_BEST'])


def get_shear_correlation(ra, dec, g1, g2, min_sep=1.0, max_sep=100.0, nbins=20, sep_units='arcmin'):
    """
    Calculates treecorr GGCorrelation for a given set of galaxy coordinates and shears.
    """
    # Create catalog
    cat = treecorr.Catalog(
        ra=ra, dec=dec, g1=g1, g2=g2, 
        ra_units='degrees', dec_units='degrees'
    )
    
    # Initialize and process correlation
    gg = treecorr.GGCorrelation(min_sep=min_sep, max_sep=max_sep, nbins=nbins, sep_units=sep_units)
    gg.process(cat)
    
    # Return results as a dictionary
    return {
        'cat': cat,
        'gg': gg,
        'r': np.exp(gg.meanlogr),
        'xip': gg.xip,
        'xim': gg.xim,
        'sig_xip': np.sqrt(gg.varxip),
        'sig_xim': np.sqrt(gg.varxim)
    }