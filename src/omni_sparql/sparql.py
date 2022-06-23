
# Instructions to add new queries: 
# Create new function, document correctly its parameter(s), replace the parameter name(s) as ##INPUT[I]## in the sparql query. 
from .utils import replace_input

class getSparqlQuery: 
    """
    Available SPARQL queries. One or multiple input to define when called. 
    
    Returns: 
        A string which contains a SPARQL command to use with `query_from_sparql`.
    """

    def all_triples(order_by = "s", n = 10): 
        """
        Shows all triples. 

        Args: 
            order_by (str): how to order the output. "s", "p", or "o". 
            n (int): how many triples to show.
        
        """
        query = """
        SELECT *
        WHERE {
            ?s ?p ?o
        }
        ORDER BY ?##INPUT0##
        LIMIT ##INPUT1##
        """
        replace_by = [order_by, str(n)]
        query = replace_input(query, replace_by)
        return(query)
    

    def datasets_from_project(project_name): 
        """
        Retrieves datasets associated to a project, also showing original project or imported/modified

        Args: 
            project_name (str): A project name, e.g. "omni_batch_processed".
        
        """

        query = """
        # 
        PREFIX prov: <http://www.w3.org/ns/prov#>
        PREFIX renku: <https://swissdatasciencecenter.github.io/renku-ontology#>
        PREFIX schema: <http://schema.org/>

        SELECT DISTINCT ?projectName ?dsName ?dsIdentifier ?originalDsId ?previousVersionDsId ?orignalProjectName ?orignalProjectId
        WHERE {
        ?projectId a schema:Project;
                    schema:name ##INPUT0##';
                    schema:name ?projectName;
                    renku:hasDataset ?dsId.  
                    ## all hadDataset IDs related to project
        ?dsId schema:name ?dsName;
                schema:identifier ?dsIdentifier. 
                ## identifier from triples where hadDataset IDs are the subject
        OPTIONAL { ?dsId prov:wasDerivedFrom/schema:url ?previousVersionDsId } ## <-- for old datasets that were reused
        OPTIONAL { 
            ?dsId schema:sameAs/schema:url ?originalDsId ## <-- original ID od dataset
        }
        }
        order by (?dsName)
        """
        query = replace_input(query, project_name)
        return(query)
   

