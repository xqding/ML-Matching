__author__ = "Xinqiang Ding <xqding@umich.edu>"
__date__ = "2016/06/22 20:46:26"

import openbabel as ob

def LocalHydrogenTyper(atom):
    """
    LocalHydrogenTyper.py
    - The function assigns local atom types for hydrogen atoms based on its hybrization type, ring memebership, ring size, aromaticity.
    - atom: ob.OBAtom
    """
    ## check if the atom is a hydrogen atom
    if (atom.GetAtomicNum() != 1):
        raise ValueError("The argument for function LocalHydrogenTyper has to be an ob.OBAtom object")    

    ## assign types
    typeName = atom.GetType()
    return (typeName, atom.MemberOfRingSize())
    
    