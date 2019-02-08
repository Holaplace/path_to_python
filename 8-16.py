import printing_functions
from printing_functions import print_models,show_completed_models
from printing_functions import  print_models as pm
import printing_functions as pf

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

printing_functions.print_models(unprinted_designs, completed_models)
printing_functions.show_completed_models(completed_models)

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

pm(unprinted_designs, completed_models)

pf.print_models(unprinted_designs, completed_models)
pf.show_completed_models(completed_models)