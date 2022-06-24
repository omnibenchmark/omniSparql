# omni-SPARQL

Python package to query triples from the OMNIBENCHMARK triplestore. 

## Usage

Let's start by getting a query. Several SPARQL queries are available in the **`getSparqlQuery`** class. If you are not sure which one you want, have a look at the class:  

```python
import omni_sparql as omni
help(omni.getSparqlQuery)
```

```
Help on class getSparqlQuery in module omni_sparql.sparql:

class getSparqlQuery(builtins.object)
 |  Available SPARQL queries. One or multiple input to define when called. 
 |  
 |  Returns: 
 |      A string which contains a SPARQL command to use with `query_from_sparql`.
 |  
 |  Methods defined here:
 |  
 |  all_triples(order_by='s', n=10)
 |      Shows all triples. 
 |      
 |      Args: 
 |          order_by (str): how to order the output. "s", "p", or "o". 
 |          n (int): how many triples to show.
 ...
```

You can then select a query, for instance `all_triples` and store it for the next step. Beware that, unlike this example, most queries do have arguments that you will have to specify (e.g. file or project to query on).

```python
q = omni.getSparqlQuery.all_triples()
q
```
```
'\n        SELECT *\n        WHERE {\n            ?s ?p ?o\n        }\n        ORDER BY ?s\n        LIMIT 10\n        '
```

The output is a SPARQL query that can readily be used to query our triplestore with the **`query_from_sparql`** function: 

```python
omni.query_from_sparql(q)
```

```
dict_values([{'vars': ['s', 'p', 'o']}, {'bindings': [{'s': {'type': 'uri', 'value': 'https://github.com/swissdatasciencecenter/renku-python/tree/v0.14.1'}, ...
```

