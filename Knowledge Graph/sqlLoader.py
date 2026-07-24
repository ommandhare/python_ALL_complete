import json
import mysql.connector
import re


# ======================================
# MYSQL CONNECTION
# ======================================

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="0777",
    database="resume_analysis"
)

cursor = conn.cursor()


# ======================================
# HELPERS
# ======================================

def safe_text(value, limit=None):

    if value is None:
        return ""

    value = str(value).strip()

    if limit:
        return value[:limit]

    return value


def extract_dates(timeline):

    if not timeline:
        return "", ""


    # Only take first line
    timeline = timeline.split("\n")[0].strip()


    parts = re.split(
        r'\s*(?:-|–|to)\s*',
        timeline,
        flags=re.I
    )


    if len(parts) == 2:

        return (
            parts[0].strip(),
            parts[1].strip()
        )


    return timeline, ""



# ======================================
# LOAD JSON
# ======================================


with open(
    "Resume.json",
    "r",
    encoding="utf-8"
) as f:

    resume = json.load(f)



with open(
    "SplitWork.json",
    "r",
    encoding="utf-8"
) as f:

    split_json = json.load(f)



work_data = split_json.get(
    "Work Experience",
    []
)


print(
    "Total Projects:",
    len(work_data)
)



try:


    # ======================================
    # INSERT CANDIDATE
    # ======================================


    cursor.execute(
    """
    INSERT INTO candidate
    (
    name,
    email,
    phone,
    professional_summary
    )

    VALUES(%s,%s,%s,%s)

    """,
    (
        safe_text(resume.get("Name")),
        safe_text(resume.get("Email")),
        safe_text(resume.get("Phone")),
        safe_text(resume.get("Professional Summary"))
    )

    )


    candidate_id = cursor.lastrowid



    print(
        "Candidate ID:",
        candidate_id
    )



    # ======================================
    # SKILLS
    # ======================================


    skills = resume.get(
        "Technical Skills",
        {}
    )


    for category, skill_list in skills.items():


        if not skill_list:
            continue


        cursor.execute(
        """
        INSERT INTO skill_category
        (category_name)

        VALUES(%s)

        """,
        (
            category,
        )
        )


        category_id = cursor.lastrowid



        for skill in skill_list:


            cursor.execute(
            """
            INSERT INTO skill
            (
            category_id,
            skill_name
            )

            VALUES(%s,%s)

            """,
            (
                category_id,
                skill
            )
            )


            skill_id = cursor.lastrowid



            cursor.execute(
            """
            INSERT INTO candidate_skill
            (
            candidate_id,
            skill_id
            )

            VALUES(%s,%s)

            """,
            (
                candidate_id,
                skill_id
            )
            )



    # ======================================
    # WORK EXPERIENCE
    # ======================================


    for work in work_data:


        print(
            "\nLoading:",
            work.get("Project")
        )


        start_date,end_date = extract_dates(
            work.get("Timeline")
        )


        print(
            "START:",
            start_date,
            "END:",
            end_date
        )


        cursor.execute(
        """

        INSERT INTO work_experience
        (
        candidate_id,
        project_name,
        role,
        company,
        client,
        start_date,
        end_date,
        work_summary
        )


        VALUES
        (%s,%s,%s,%s,%s,%s,%s,%s)

        """,
        (
            candidate_id,

            safe_text(work.get("Project")),

            safe_text(work.get("Role")),

            safe_text(work.get("Company")),

            safe_text(work.get("Client")),

            safe_text(start_date),

            safe_text(end_date),

            safe_text(work.get("Work Summary"))

        )

        )


        experience_id = cursor.lastrowid



        # ======================================
        # TECHNOLOGY
        # ======================================


        technologies = work.get(
            "Technology Used",
            ""
        )


        if isinstance(technologies,str):

            technologies = technologies.split(",")



        for tech in technologies:


            tech = tech.strip()


            if not tech:
                continue



            cursor.execute(
            """
            INSERT INTO technology
            (
            technology_name
            )

            VALUES(%s)

            """,
            (
                tech,
            )
            )


            technology_id = cursor.lastrowid



            cursor.execute(
            """
            INSERT INTO experience_technology
            (
            experience_id,
            technology_id
            )

            VALUES(%s,%s)

            """,
            (
                experience_id,
                technology_id
            )
            )



        # ======================================
        # RESPONSIBILITY
        # ======================================


        summary = work.get(
            "Work Summary",
            ""
        )


        if isinstance(summary,str):

            points = summary.split("\n")

        else:

            points = []



        for point in points:


            point = point.strip()


            if point:


                cursor.execute(
                """
                INSERT INTO responsibility
                (
                experience_id,
                description
                )

                VALUES(%s,%s)

                """,
                (
                    experience_id,
                    point
                )
                )



    # ======================================
    # EDUCATION
    # ======================================


    education = safe_text(
        resume.get("Education")
    )


    cursor.execute(
    """
    INSERT INTO education
    (
    candidate_id,
    degree,
    university,
    institute
    )

    VALUES(%s,%s,%s,%s)

    """,
    (
        candidate_id,
        education,
        "",
        ""
    )
    )



    # ======================================
    # LANGUAGE
    # ======================================


    languages = resume.get(
        "Languages",
        ""
    )


    if isinstance(languages,str):

        languages = languages.split(",")



    for lang in languages:


        lang = lang.strip()


        if lang:


            cursor.execute(
            """
            INSERT INTO language
            (
            candidate_id,
            language_name
            )

            VALUES(%s,%s)

            """,
            (
                candidate_id,
                lang
            )
            )



    conn.commit()



    print(
    "========== Resume Loaded Successfully =========="
    )


except Exception as e:


    conn.rollback()

    print(
        "ERROR:",
        e
    )



finally:

    cursor.close()

    conn.close()