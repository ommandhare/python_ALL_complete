import mysql.connector
from neo4j import GraphDatabase
from pprint import pprint

# ============================================
# MYSQL CONNECTION
# ============================================

mysql_conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="0777",
    database="resume_analysis"
)

mysql_cursor = mysql_conn.cursor(dictionary=True)


# ============================================
# NEO4J CONNECTION
# ============================================

driver = GraphDatabase.driver(
    "bolt://localhost:7687",
    auth=("neo4j", "ommandhare1234")
)


# ============================================
# MYSQL QUERY
# ============================================

mysql_query = """
SELECT
c.candidate_id,
c.name,
GROUP_CONCAT(
DISTINCT we.role
) AS roles,

GROUP_CONCAT(
DISTINCT s.skill_name
) AS skills

FROM candidate c

LEFT JOIN work_experience we
ON c.candidate_id = we.candidate_id

LEFT JOIN candidate_skill cs
ON c.candidate_id = cs.candidate_id

LEFT JOIN skill s
ON cs.skill_id = s.skill_id

WHERE c.name="Om Mandhare"
GROUP BY
c.candidate_id,
c.name;
"""

mysql_cursor.execute(mysql_query)

roles = mysql_cursor.fetchall()


# ============================================
# NEO4J QUERY
# ============================================

neo_query = """
MATCH (r:Role {name:$role})

OPTIONAL MATCH (r)-[:PREREQUISITE]->(s1:Skill)
OPTIONAL MATCH (r)-[:MUST_HAVE]->(s2:Skill)
OPTIONAL MATCH (r)-[:NICE_TO_HAVE]->(s3:Skill)

RETURN
    r.name AS Role,
    collect(DISTINCT s1.Skill) AS PREREQUISITE,
    collect(DISTINCT s2.Skill) AS MUST_HAVE,
    collect(DISTINCT s3.Skill) AS NICE_TO_HAVE
"""


# ============================================
# RUN
# ============================================

with driver.session(database="conceptdictionary") as session:
    skillList=[]
    for row in roles:

        role = row["roles"]
        skill = row["skills"]

        print("=" * 70)
        print("Candidate ID :", row["candidate_id"])
        print("Role :", role)
        # print("Skill:", skill)
        # print(type(skill))
        skillList=skill.split(",")
        print("Skill Which user Already have............")
        pprint(skillList)

        result = session.run(
            neo_query,
            {
                "role": role,
                "skills":skill
            }
        )

        records = [record.data() for record in result]
        # print("records",records)
        if records:

            for record in records:
             # print(record)
             preq=[i.lower() for i in record["PREREQUISITE"]]
             must=[i.lower() for i in record["MUST_HAVE"]]
             nice=[i.lower() for i in record["NICE_TO_HAVE"]]
             # print(preq)
             # print(f"Prerequisite  ----- {record["PREREQUISITE"]}")
             # print(f"Must have  ----- {record["MUST_HAVE"]}")
             # print(f"Nice to have  ----- {record["NICE_TO_HAVE"]}")
        else:

             print("No Role Found in Neo4j")

have={}
nothave={}
# print(skillList)
preqHave = []
mustHave = []
niceHave = []
notHave = []
finalDict={}
for skill in skillList:
 skill=skill.lower()

 if skill in preq:
     preqHave.append(skill)
 elif skill in must:
     mustHave.append(skill)

 elif skill in nice:
     niceHave.append(skill)
 else:
     notHave.append(skill)
     nothave["EXTRA"]=notHave
#
# have["PREREQUISITE"]=preq - preqHave
finalDict["PREREQUISITE"]=[i for i in preq if i not in preqHave]
# have["MUST_HAVE"]= must - mustHave
finalDict["MUST_HAVE"]=[i for i in must if i not in mustHave]
# have["NICE_TO_HAVE"] = nice - niceHave
finalDict["NICE_TO_HAVE"]=[i for i in nice if i not in niceHave]
# print(result)
print("\n\n")
print("=" * 70)
print("Skills that User required for role",role)
pprint(finalDict,width=100)
print("\n\n")
print("Additional skills the user has")
print(nothave)



# ============================================
# CLOSE CONNECTIONS
# ============================================

mysql_cursor.close()
mysql_conn.close()
driver.close()