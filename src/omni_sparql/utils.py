
def replace_input(sparql_command, inputs): 
    for i in range(len(inputs)): 
        sparql_command = sparql_command.replace("##INPUT".__add__(str(i)).__add__("##"), inputs[i] )
    return(sparql_command)
