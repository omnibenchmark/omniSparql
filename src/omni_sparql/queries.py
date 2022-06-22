from SPARQLWrapper import SPARQLWrapper, JSON


def show_triple(n_to_show):
    URL = "http://imlspenticton.uzh.ch/sparql"

    sparql = SPARQLWrapper(URL)
    sparql.setReturnFormat(JSON)

    sparql.setQuery("""

        SELECT *
        WHERE {
            ?s ?p ?o
        }
        ORDER BY ?s
        LIMIT 3
        """
    )
    ret = sparql.queryAndConvert()
    print("Updated")
    return(ret.values())


def datasets_from_project():
    URL = "http://imlspenticton.uzh.ch/sparql"

    sparql = SPARQLWrapper(URL)
    sparql.setReturnFormat(JSON)

    sparql.setQuery("""

        # retrieve datasets associated to a project, also showing original project or imported/modified
        PREFIX prov: <http://www.w3.org/ns/prov#>
        PREFIX renku: <https://swissdatasciencecenter.github.io/renku-ontology#>
        PREFIX schema: <http://schema.org/>

        SELECT DISTINCT ?projectName ?dsName ?dsIdentifier ?originalDsId ?previousVersionDsId ?orignalProjectName ?orignalProjectId
        WHERE {
        ?projectId a schema:Project;
                    schema:name 'omni_batch_processed';
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
    )
    ret = sparql.queryAndConvert()
    
    return(ret.values())







