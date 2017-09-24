def print_models(unprinted_designs, completed_models):
    '''
    print models
    
    '''
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing model: " + current_design)
        completed_models.append(current_design)
        
def show_complete_models(complete_models):
    print("\nThe following models have been printed:")
    for complete_model in completed_models:
        print(complete_model)
        
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_complete_models(completed_models)
show_complete_models(unprinted_designs)
