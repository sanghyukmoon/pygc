import numpy as np
from scipy.special import expn
"""
=======================================
Description | collection of SF theories
Author      | Sanghyuk Moon
=======================================
"""

def ftau(tauperp, tau=0):
    """plane-parallel ftau
    tauperp: Optical thickness of the FUV-emitting slab.
    tau    : Optical depth coordinate inside the slab (tau=0 for midplane).
             -tauperp/2 < tau < tauperp/2
    """
    return (1 - 0.5*expn(2,0.5*tauperp+tau) - 0.5*expn(2,0.5*tauperp-tau))\
            /tauperp 
def ftau_thin(tauperp):
    """ftau in optically thin limit"""
    return  0.5*(1.0-np.euler_gamma-np.log(0.5*tauperp))

def ftau_thick(tauperp):
    """ftau in optically thick limit"""
    return 1.0/tauperp

class theories(object):
    """ Global star formation theories
    """

    def __init__(self, ):
        pass

    def os11(self, surf, chi=0, fp=1., vsnr=1., epsstar=1., kap=1.):
        """ 
        Ostriker & Shetty 2011 turbulence-regulated star formation model
       
        INPUT
        ======================================================================
        surf    : gas surface density in units of M_sun pc^-2

        PARAMETERS
        ======================================================================
        chi     : stellar gravity parameter
        fp      : momentum injection efficiency (1~2)
        vsnr    : radial momentum per unit mass of stars formed (3000 km s^-1)
        epsstar : mass-to-radiation energy conversion efficiency in units of
                  6.2 x 10^-4
        kap     : IR opacity in units of 10 cm^2 g^-1

        RETURN
        ======================================================================
        sfrsurf : star formation rate surface density in units of
                  M_sun yr^-1 kpc^-2

        TODO
        ======================================================================
        When stellar gravity dominates (chi > 1), chi should not regarded as
        independent parameter, because it is proportional to the inverse of
        gas surface density. In this case, the star formation law would change
        to sfrsurf ~ surf instead of sfrsurf ~ surf**2.

        """
        print("chi={0}, fp={1}, vsnr={2}, epsstar={3}, kap={4}"
                .format(chi,fp,vsnr,epsstar,kap))
        taustar = 16.1*fp*vsnr/epsstar
        tau = 0.00209*kap*surf
        sfrsurf = 9.21e-6*(1.+chi)/(1.+tau/taustar)/fp/vsnr*(surf**2)
        return sfrsurf
