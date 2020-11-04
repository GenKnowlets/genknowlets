prefixes = """
@prefix dc: <http://purl.org/dc/terms/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix pav: <http://purl.org/pav/> .
@prefix np: <http://www.nanopub.org/nschema#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix this: <https://example.com/> .
@prefix sio: <http://semanticscience.org/resource/> .
@prefix ncbi-asb: <https://www.ncbi.nlm.nih.gov/assembly/> .
@prefix biol: <https://ontologi.es/biol/ns.html> .
"""

head = """
sub:Head {
  this: np:hasAssertion sub:assertion ;
    np:hasProvenance sub:provenance ;
    np:hasPublicationInfo sub:pubinfo ;
    a np:Nanopublication .
}
"""

assertion = """
sub:assertion {{
  ncbi-asb:{assembly_id} a sio:SIO_000984 ;
        sio:SIO_000628 [ a sio:SIO_010000 ;       
                         biol:hasTaxonomy <{taxonomy_link}> ;
                         dc:label  "{organism_name}" . ] .
}}
"""

provenance = """
sub:provenance {{
  sub:assertion prov:hadPrimarySource <{biosample_link}> ;
    prov:wasAttributedTo "{institution}" ;  
    prov:collectedDate "{collected_at}"^^xsd:dateTime ;
    sio:SIO_000772 <{publication_link}> ;
    dc:created "{submitted_at}"^^xsd:dateTime .
}}
"""

pubinfo = """
sub:pubinfo {{
  this: dc:created "{created_datetime}"^^xsd:dateTime ;
    pav:createdBy <{creator_id}> .
}}
"""