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
    
    return(ret.values())










