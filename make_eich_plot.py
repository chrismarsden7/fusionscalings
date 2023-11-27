from uncertainties import ufloat
import matplotlib.pyplot as plt
import numpy as np

def process_result(result):

    if hasattr(result, '__len__'):
        result_nominal = np.asarray([val.nominal_value for val in result])
        result_err = np.asarray([val.std_dev for val in result])

    else:
        result_nominal = result.nominal_value
        result_err = result.std_dev

    result_min = result_nominal - result_err
    result_max = result_nominal + result_err

    return result_nominal, result_err, result_min, result_max, result

def Eich_15(Bpol):

    lq = ufloat(0.63,0.08) * Bpol**ufloat(-1.19,0.08)

    return process_result(lq)

if __name__ == '__main__':

    Bpol = np.linspace(0.1,0.6,100)
    lq_nominal, lq_err, lq_min, lq_max, lq = Eich_15(Bpol)

    fig, ax = plt.subplots()
    ax.plot(Bpol,lq_nominal,'r')
    ax.plot(Bpol,lq_min,'k--')
    ax.plot(Bpol,lq_max,'k--')
    ax.set_xlabel(r'$B_{\theta}$ (T)')
    ax.set_ylabel(r'$\lambda_{q}$ (mm)')
    plt.grid(color='k',linestyle='--',alpha=0.25)
    plt.show()