"""
The parameters in this file were taken from OpenKIM at
https://openkim.org/files/MO_959249795837_003/LennardJones612_UniversalShifted.params

 * Sigma parameters are set to (2^{-1/6})*r_0, where r_0 is the atomic
   covalent radius.  Covalent radii for elements 1--96 were taken from Wolfram
   Mathematica's `ElementData["CovalentRadius"]' command.  Covalent radii for
   elements 97--118 were taken from Fig. 3 of the article Pyykko, M. Atsumi,
   J. Chem. Eur. J. 15 (2009) 12770.

 * Epsilon parameters are set to the bond dissociation energy.  Bond
   dissociation energies for elements 1--55, 57--60, and 61--84 were taken
   from the CRC Handbook of Chemistry and Physics, 91st Edition,
   Ed. W.H. Haynes, 2010. (as posted here:
   http://staff.ustc.edu.cn/~luo971/2010-91-CRC-BDEs-Tables.pdf)

   The value (cohesive energy, in this case) for element 56 was obtained from
   p. 50 in Charles Kittel. Introduction to Solid State Physics, 8th
   edition. Hoboken, NJ: John Wiley & Sons, Inc, 2005.

   The bond dissociation energy value for element 61 was obtained from
   "Interpolation scheme for the cohesive energies for the lanthanides and
   actinides" Borje Johansson and Anders Rosengren, Phys. Rev. B 11, 1367
   (1975).

   The bond dissociation energies for elements 85--118 were not found in the
   literature.  Thus, the values used here are approximated by subtracting 10%
   from the value for the element in the same Group (column) and previous
   Period (row) of the periodic table.

 * Cutoff parameters are set to 4.0*sigma.  This corresponds to a cutoff
   energy of approximately epsilon/1024.

 * Lorentz-Berthelot mixing rules are used for interactions between unlike
   particles.  Each interaction potential is shifted to zero energy at its
   cutoff distance.
"""

LJ_PARAMS = {
    "H":       {"cutoff":    2.2094300,   "epsilon":    4.4778900,   "sigma":    0.5523570},
    "He":      {"cutoff":    1.9956100,   "epsilon":    0.0009421,   "sigma":    0.4989030},
    "Li":      {"cutoff":    9.1228000,   "epsilon":    1.0496900,   "sigma":    2.2807000},
    "Be":      {"cutoff":    6.8421000,   "epsilon":    0.5729420,   "sigma":    1.7105300},
    "B":       {"cutoff":    6.0581100,   "epsilon":    2.9670300 ,  "sigma":    1.5145300},
    "C":       {"cutoff":    5.4166600,   "epsilon":    6.3695300,   "sigma":    1.3541700},
    "N":       {"cutoff":    5.0603000,   "epsilon":    9.7537900,   "sigma":    1.2650800},
    "O":       {"cutoff":    4.7039500,   "epsilon":    5.1264700,   "sigma":    1.1759900},
    "F":       {"cutoff":    4.0625000,   "epsilon":    1.6059200,   "sigma":    1.0156200},
    "Ne":      {"cutoff":    4.1337700,   "epsilon":    0.0036471,   "sigma":    1.0334400},
    "Na":      {"cutoff":    11.8311000,  "epsilon":    0.7367450,   "sigma":    2.9577800},
    "Mg":      {"cutoff":    10.0493000,  "epsilon":    0.0785788,   "sigma":    2.5123300},
    "Al":      {"cutoff":    8.6239000,   "epsilon":    2.7006700,   "sigma":    2.1559700},
    "Si":      {"cutoff":    7.9111800,   "epsilon":    3.1743100,   "sigma":    1.9778000},
    "P":       {"cutoff":    7.6260900,   "epsilon":    5.0305000,   "sigma":    1.9065200},
    "S":       {"cutoff":    7.4835500,   "epsilon":    4.3692700,   "sigma":    1.8708900},
    "Cl":      {"cutoff":    7.2697300,   "epsilon":    4.4832800,   "sigma":    1.8174300},
    "Ar":      {"cutoff":    7.5548200,   "epsilon":    0.0123529,   "sigma":    1.8887100},
    "K":       {"cutoff":    14.4682000,  "epsilon":    0.5517990,   "sigma":    3.6170500},
    "Ca":      {"cutoff":    12.5439000,  "epsilon":    0.1326790,   "sigma":    3.1359600},
    "Sc":      {"cutoff":    12.1162000,  "epsilon":    1.6508000,   "sigma":    3.0290600},
    "Ti":      {"cutoff":    11.4035000,  "epsilon":    1.1802700,   "sigma":    2.8508800},
    "V":       {"cutoff":    10.9046000,  "epsilon":    2.7524900,   "sigma":    2.7261500},
    "Cr":      {"cutoff":    9.9067900,   "epsilon":    1.5367900,   "sigma":    2.4767000},
    "Mn":      {"cutoff":    9.9067900,   "epsilon":    0.5998880,   "sigma":    2.4767000},
    "Fe":      {"cutoff":    9.4078900,   "epsilon":    1.1844200,   "sigma":    2.3519700},
    "Co":      {"cutoff":    8.9802600,   "epsilon":    1.2776900,   "sigma":    2.2450600},
    "Ni":      {"cutoff":    8.8377200,   "epsilon":    2.0757200,   "sigma":    2.2094300},
    "Cu":      {"cutoff":    9.4078900,   "epsilon":    2.0446300,   "sigma":    2.3519700},
    "Zn":      {"cutoff":    8.6951700,   "epsilon":    0.1915460,   "sigma":    2.1737900},
    "Ga":      {"cutoff":    8.6951700,   "epsilon":    1.0642000,   "sigma":    2.1737900},
    "Ge":      {"cutoff":    8.5526300,   "epsilon":    2.7017100,   "sigma":    2.1381600},
    "As":      {"cutoff":    8.4813600,   "epsilon":    3.9599000,   "sigma":    2.1203400},
    "Se":      {"cutoff":    8.5526300,   "epsilon":    3.3867700,   "sigma":    2.1381600},
    "Br":      {"cutoff":    8.5526300,   "epsilon":    1.9706300,   "sigma":    2.1381600},
    "Kr":      {"cutoff":    8.2675400,   "epsilon":    0.0173276,   "sigma":    2.0668900},
    "Rb":      {"cutoff":    15.6798000,  "epsilon":    0.4682650,   "sigma":    3.9199500},
    "Sr":      {"cutoff":    13.8980000,  "epsilon":    0.1339230,   "sigma":    3.4745100},
    "Y":       {"cutoff":    13.5417000,  "epsilon":    2.7597500,   "sigma":    3.3854200},
    "Zr":      {"cutoff":    12.4726000,  "epsilon":    3.0520100,   "sigma":    3.1181500},
    "Nb":      {"cutoff":    11.6886000,  "epsilon":    5.2782000,   "sigma":    2.9221500},
    "Mo":      {"cutoff":    10.9759000,  "epsilon":    4.4749900,   "sigma":    2.7439700},
    "Tc":      {"cutoff":    10.4770000,  "epsilon":    3.3815900,   "sigma":    2.6192400},
    "Ru":      {"cutoff":    10.4057000,  "epsilon":    1.9617200,   "sigma":    2.6014200},
    "Rh":      {"cutoff":    10.1206000,  "epsilon":    2.4058200,   "sigma":    2.5301500},
    "Pd":      {"cutoff":    9.9067900,   "epsilon":    1.3709700,   "sigma":    2.4767000},
    "Ag":      {"cutoff":    10.3344000,  "epsilon":    1.6497600,   "sigma":    2.5836100},
    "Cd":      {"cutoff":    10.2632000,  "epsilon":    0.0377447,   "sigma":    2.5657900},
    "In":      {"cutoff":    10.1206000,  "epsilon":    0.8113140,   "sigma":    2.5301500},
    "Sn":      {"cutoff":    9.9067900,   "epsilon":    1.9005700,   "sigma":    2.4767000},
    "Sb":      {"cutoff":    9.9067900,   "epsilon":    3.0882800,   "sigma":    2.4767000},
    "Te":      {"cutoff":    9.8355200,   "epsilon":    2.6312300,   "sigma":    2.4588800},
    "I":       {"cutoff":    9.9067900,   "epsilon":    1.5393800,   "sigma":    2.4767000},
    "Xe":      {"cutoff":    9.9780700,   "epsilon":    0.0238880,   "sigma":    2.4945200},
    "Cs":      {"cutoff":    17.3903000,  "epsilon":    0.4166420,   "sigma":    4.3475900},
    "Ba":      {"cutoff":    15.3235000,  "epsilon":    1.9000000,   "sigma":    3.8308600},
    "La":      {"cutoff":    14.7533000,  "epsilon":    2.4996100,   "sigma":    3.6883200},
    "Ce":      {"cutoff":    14.5395000,  "epsilon":    2.5700800,   "sigma":    3.6348700},
    "Pr":      {"cutoff":    14.4682000,  "epsilon":    1.2994600,   "sigma":    3.6170500},
    "Nd":      {"cutoff":    14.3257000,  "epsilon":    0.8196050,   "sigma":    3.5814100},
    "Pm":      {"cutoff":    14.1831000,  "epsilon":    3.2413400,   "sigma":    3.5457800},
    "Sm":      {"cutoff":    14.1118000,  "epsilon":    0.5211220,   "sigma":    3.5279600},
    "Eu":      {"cutoff":    14.1118000,  "epsilon":    0.4299180,   "sigma":    3.5279600},
    "Gd":      {"cutoff":    13.9693000,  "epsilon":    2.0995600,   "sigma":    3.4923200},
    "Tb":      {"cutoff":    13.8267000,  "epsilon":    1.3999900,   "sigma":    3.4566900},
    "Dy":      {"cutoff":    13.6842000,  "epsilon":    0.6900550,   "sigma":    3.4210500},
    "Ho":      {"cutoff":    13.6842000,  "epsilon":    0.6900550,   "sigma":    3.4210500},
    "Er":      {"cutoff":    13.4704000,  "epsilon":    0.7387660,   "sigma":    3.3676000},
    "Tm":      {"cutoff":    13.5417000,  "epsilon":    0.5211220,   "sigma":    3.3854200},
    "Yb":      {"cutoff":    13.3278000,  "epsilon":    0.1303990,   "sigma":    3.3319600},
    "Lu":      {"cutoff":    13.3278000,  "epsilon":    1.4331500,   "sigma":    3.3319600},
    "Hf":      {"cutoff":    12.4726000,  "epsilon":    3.3608600,   "sigma":    3.1181500},
    "Ta":      {"cutoff":    12.1162000,  "epsilon":    4.0034300,   "sigma":    3.0290600},
    "W":       {"cutoff":    11.5460000,  "epsilon":    6.8638900,   "sigma":    2.8865100},
    "Re":      {"cutoff":    10.7621000,  "epsilon":    4.4387100,   "sigma":    2.6905100},
    "Os":      {"cutoff":    10.2632000,  "epsilon":    4.2625300,   "sigma":    2.5657900},
    "Ir":      {"cutoff":    10.0493000,  "epsilon":    3.7028700,   "sigma":    2.5123300},
    "Pt":      {"cutoff":    9.6929800,   "epsilon":    3.1401000,   "sigma":    2.4232400},
    "Au":      {"cutoff":    9.6929800,   "epsilon":    2.3058000,   "sigma":    2.4232400},
    "Hg":      {"cutoff":    9.4078900,   "epsilon":    0.0454140,   "sigma":    2.3519700},
    "Tl":      {"cutoff":    10.3344000,  "epsilon":    0.5770870,   "sigma":    2.5836100},
    "Pb":      {"cutoff":    10.4057000,  "epsilon":    0.8589880,   "sigma":    2.6014200},
    "Bi":      {"cutoff":    10.5482000,  "epsilon":    2.0798700,   "sigma":    2.6370600},
    "Po":      {"cutoff":    9.9780700 ,  "epsilon":    1.8995300,   "sigma":    2.4945200},
    "At":      {"cutoff":    10.6908000,  "epsilon":    1.3854420,   "sigma":    2.6727000},
    "Rn":      {"cutoff":    10.6908000,  "epsilon":    0.0214992,   "sigma":    2.6727000},
    "Fr":      {"cutoff":    18.5307000,  "epsilon":    0.3749778,   "sigma":    4.6326700},
    "Ra":      {"cutoff":    15.7511000,  "epsilon":    1.7100000,   "sigma":    3.9377700},
    "Ac":      {"cutoff":    15.3235000,  "epsilon":    2.2496490,   "sigma":    3.8308600},
    "Th":      {"cutoff":    14.6820000,  "epsilon":    2.3130720,   "sigma":    3.6705000},
    "Pa":      {"cutoff":    14.2544000,  "epsilon":    1.1695140,   "sigma":    3.5635900},
    "U":       {"cutoff":   13.9693000 ,  "epsilon":   0.7376445 ,   "sigma":   3.4923200},
    "Np":      {"cutoff":    13.5417000,  "epsilon":    2.9172060,   "sigma":    3.3854200},
    "Pu":      {"cutoff":    13.3278000,  "epsilon":    0.4690098,   "sigma":    3.3319600},
    "Am":      {"cutoff":    12.8289000,  "epsilon":    0.3869262,   "sigma":    3.2072400},
    "Cm":      {"cutoff":    12.0450000,  "epsilon":    1.8896040,   "sigma":    3.0112400},
    "Bk":      {"cutoff":    11.9737000,  "epsilon":    1.2599910,   "sigma":    2.9934200},
    "Cf":      {"cutoff":    11.9737000,  "epsilon":    0.6210495,   "sigma":    2.9934200},
    "Es":      {"cutoff":    11.7599000,  "epsilon":    0.6210495,   "sigma":    2.9399700},
    "Fm":      {"cutoff":    11.9024000,  "epsilon":    0.6648894,   "sigma":    2.9756000},
    "Md":      {"cutoff":    12.3300000,  "epsilon":    0.4690098,   "sigma":    3.0825100},
    "No":      {"cutoff":    12.5439000,  "epsilon":    0.1173591,   "sigma":    3.1359600},
    "Lr":      {"cutoff":    11.4748000,  "epsilon":    1.2898350,   "sigma":    2.8686900},
    "Rf":      {"cutoff":    11.1897000,  "epsilon":    3.0247740,   "sigma":    2.7974200},
    "Db":      {"cutoff":    10.6195000,  "epsilon":    3.6030870,   "sigma":    2.6548800},
    "Sg":      {"cutoff":    10.1919000,  "epsilon":    6.1775010,   "sigma":    2.5479700},
    "Bh":      {"cutoff":    10.0493000,  "epsilon":    3.9948390,   "sigma":    2.5123300},
    "Hs":      {"cutoff":    9.5504300 ,  "epsilon":    3.8362770,   "sigma":    2.3876100},
    "Mt":      {"cutoff":    9.1940700 ,  "epsilon":    3.3325830,   "sigma":    2.2985200},
    "Ds":      {"cutoff":    9.1228000 ,  "epsilon":    2.8260900,   "sigma":    2.2807000},
    "Rg":      {"cutoff":    8.6239000 ,  "epsilon":    2.0752200,   "sigma":    2.1559700},
    "Cn":      {"cutoff":    8.6951700 ,  "epsilon":    0.0408726,   "sigma":    2.1737900},
    "Nh":      {"cutoff":    9.6929800 ,  "epsilon":    0.5193783,   "sigma":    2.4232400},
    "Fl":      {"cutoff":    10.1919000,  "epsilon":    0.7730892,   "sigma":    2.5479700},
    "Mc":      {"cutoff":    11.5460000,  "epsilon":    1.8718830,   "sigma":    2.8865100},
    "Lv":      {"cutoff":    12.4726000,  "epsilon":    1.7095770,   "sigma":    3.1181500},
    "Ts":      {"cutoff":    11.7599000,  "epsilon":    1.2468978,   "sigma":    2.9399700},
    "Og":      {"cutoff":    11.1897000,  "epsilon":    0.0193493,   "sigma":    2.7974200},
}


ATOMIC_MASS = {
    'Ac': 227.0, 'Ag': 107.8682, 'Al': 26.9815386, 'Am': 243.0, 'Ar': 39.948, 'As': 74.9216, 'At': 210.0, 
    'Au': 196.966569, 'B': 10.811, 'Ba': 137.327, 'Be': 9.012182, 'Bi': 208.9804, 'Bk': 247.0, 'Br': 79.904, 
    'C': 12.0107, 'Ca': 40.078, 'Cd': 112.411, 'Ce': 140.116, 'Cf': 251.0, 'Cl': 35.453, 'Cm': 247.0, 
    'Co': 58.933195, 'Cr': 51.9961, 'Cs': 132.9054519, 'Cu': 63.546, 'Dy': 162.5, 'Er': 167.259, 'Es': 252.0, 
    'Eu': 151.964, 'F': 18.9984032, 'Fe': 55.845, 'Fm': 257.0, 'Fr': 223.0, 'Ga': 69.723, 'Gd': 157.25, 
    'Ge': 72.64, 'H': 1.00794, 'He': 4.002602, 'Hf': 178.49, 'Hg': 200.59, 'Ho': 164.93032, 'I': 126.90447, 
    'In': 114.818, 'Ir': 192.217, 'K': 39.0983, 'Kr': 83.798, 'La': 138.90547, 'Li': 6.941, 'Lr': 262.0, 
    'Lu': 174.967, 'Md': 258.0, 'Mg': 24.305, 'Mn': 54.938045, 'Mo': 95.94, 'N': 14.0067, 'Na': 22.98976928, 
    'Nb': 92.90638, 'Nd': 144.242, 'Ne': 20.1797, 'Ni': 58.6934, 'No': 259.0, 'Np': 237.0, 'O': 15.9994, 
    'Os': 190.23, 'P': 30.973762, 'Pa': 231.03588, 'Pb': 207.2, 'Pd': 106.42, 'Pm': 145.0, 'Po': 210.0, 
    'Pr': 140.90765, 'Pt': 195.084, 'Pu': 244.0, 'Ra': 226.0, 'Rb': 85.4678, 'Re': 186.207, 'Rh': 102.9055, 
    'Rn': 220.0, 'Ru': 101.07, 'S': 32.065, 'Sb': 121.76, 'Sc': 44.955912, 'Se': 78.96, 'Si': 28.0855, 
    'Sm': 150.36, 'Sn': 118.71, 'Sr': 87.62, 'Ta': 180.94788, 'Tb': 158.92535, 'Tc': 98.0, 'Te': 127.6, 
    'Th': 232.03806, 'Ti': 47.867, 'Tl': 204.3833, 'Tm': 168.93421, 'U': 238.02891, 'V': 50.9415, 
    'W': 183.84, 'Xe': 131.293, 'Y': 88.90585, 'Yb': 173.04, 'Zn': 65.409, 'Zr': 91.224, 'Rf': 267, 
    'Db': 268, 'Sg': 269, 'Bh': 270, 'Hs': 270, 'Mt': 278, 'Ds': 281, 'Rg': 282, 'Cn': 285, 'Nh': 286, 
    'Fl': 289, 'Mc': 290, 'Lv': 293, 'Ts': 294, 'Og': 294, 'D': 2.013553212712, 'T': 3.0155007134
    }


CRYSTAL_STRUCTURE = {
    'Au':    {'symmetry': 'fcc', 'lattice_param': 4.08},
    'Li':    {'symmetry': 'bcc', 'lattice_param': 3.44},
    'W':     {'symmetry': 'bcc', 'lattice_param': 3.165}, 
    }
