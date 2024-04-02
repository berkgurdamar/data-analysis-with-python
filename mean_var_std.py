import numpy as np

def calculate(list):

    if len(list) == 9:
        tmp_array = np.array(list).reshape(3,3)

        calculations = {"mean" : [np.mean(tmp_array, 0).tolist(),
                                  np.mean(tmp_array, 1).tolist(),
                                  np.mean(np.array(list))],
                        "variance" : [np.var(tmp_array, 0).tolist(),
                                      np.var(tmp_array, 1).tolist(),
                                      np.var(np.array(list))],
                        "standard deviation" : [np.std(tmp_array, 0).tolist(),
                                                np.std(tmp_array, 1).tolist(),
                                                np.std(np.array(list))],
                        "max" : [np.max(tmp_array, 0).tolist(),
                                 np.max(tmp_array, 1).tolist(),
                                 np.max(np.array(list))],
                        "min" : [np.min(tmp_array, 0).tolist(),
                                 np.min(tmp_array, 1).tolist(),
                                 np.min(np.array(list))],
                        "sum" : [np.sum(tmp_array, 0).tolist(),
                                 np.sum(tmp_array, 1).tolist(),
                                 np.sum(np.array(list))],}

    else:
        raise ValueError("List must contain nine numbers.")
    return calculations
