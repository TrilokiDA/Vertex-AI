from scipy import optimize
import numpy as np
import time

########## Alternate Formulation
# Constraint function returns a positive number on being satisfied
def constraint_townsend(x):
    y = x[1]
    x = x[0]

    t = np.arctan2(x, y)
    #t = np.arctan(x/y)

    lhs = np.square(x) + np.square(y)
    rhs = np.square((2*np.cos(t)) -(.5*np.cos(2*t)) -(.25*np.cos(3*t)) -(.125*np.cos(4*t))) + np.square(2*np.sin(t))
    #rhs = ((2*np.cos(t)) -(.5*np.cos(2*t)) -(.25*np.cos(3*t)) -(.125*np.cos(4*t))) + 2*np.sin(t)
    violation  =  lhs-rhs

    if violation > 0:
        violation =np.log(1 + violation)
    else:
        violation= 0
    return violation
def townsend(x):   
    y = x[1]
    x = x[0]

    first_term = -np.square(np.cos((x-.1)*y))
    second_term = -x*np.sin((3*x)+y)
    func = first_term+second_term
    return func
def document_constraint_townsend(x):
    y = x[1]
    x = x[0]

    t = np.arctan2(x, y)
    #t = np.arctan(x/y)

    lhs = np.square(x) + np.square(y)
    rhs = np.square((2*np.cos(t)) -(.5*np.cos(2*t)) -(.25*np.cos(3*t)) -(.125*np.cos(4*t))) + np.square(2*np.sin(t))
    #rhs = ((2*np.cos(t)) -(.5*np.cos(2*t)) -(.25*np.cos(3*t)) -(.125*np.cos(4*t))) + 2*np.sin(t)
    violation  =  lhs-rhs

    if violation > 0:
        violation =np.abs(violation)
    else:
        violation= 0
    return violation


def opt(req):

    lb = [-2.25, -2.5]
    ub = [2.5, 1.75]

    # Scipy nonlinear constraint
    constr = optimize.NonlinearConstraint(constraint_townsend, -np.inf, 0)
    constraints = [constr, {'type': 'ineq', 'fun': constraint_townsend}]
    
    n_init = req['instances'][0]['n_init']
    x_results = []
    y_results = []
    cv_trust = []
    init = np.random.uniform(low = lb, high = ub, size = (n_init, 2))


    init_time = time.time()
    for initial in init:
        results = optimize.minimize(fun=townsend, x0=initial, method = 'trust-constr', bounds = list(zip(lb, ub)), 
                       options={'disp': None,  
                                 'maxiter': 2000}, constraints = constraints)
        x_results.append(results.x)
        y_results.append(results.fun)
        cv_trust.append(document_constraint_townsend(results.x))

    y_best_trust = townsend(np.array(x_results)[np.argmin(y_results)])
    cons_best_trust = document_constraint_townsend(np.array(x_results)[np.argmin(y_results)])

    final_time = time.time()
    trust_time = final_time - init_time
    print(f'Time taken for 1000 Fresh Runs: {trust_time}')

    return trust_time
