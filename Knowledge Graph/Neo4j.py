from neo4j import GraphDatabase

def get_driver():
    return GraphDatabase.driver(
        "bolt://localhost:7687",
        auth=("neo4j", "ommandhare1234")
    )

def run_query(query, params=None):
    driver = get_driver()
    with driver.session(database="conceptdictionary") as session:
        result = session.run(query, params or {})
        return [record.data() for record in result]

query="""
MATCH (r:Role {name: "Data Engineer"})
MATCH (r)-[:PREREQUISITE]->(s1:Skill)
MATCH (r)-[:MUST_HAVE]->(s2:Skill)
MATCH (r)-[:NICE_TO_HAVE]->(s3:Skill)
RETURN
  r.name as Role,
  collect(DISTINCT s1.Skill) as PREREQUISITE,
  collect(DISTINCT s2.Skill) as MUST_HAVE,
  collect(DISTINCT s3.Skill) as NICE_TO_HAVE

"""

result=run_query(query)

print(result)