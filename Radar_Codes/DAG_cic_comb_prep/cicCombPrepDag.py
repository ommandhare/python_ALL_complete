"""
Name: cicCombPrepDag.py
Description: This is script to create clean description for cic combination.
Author: kiran Biradar
Creation Date:  2024-12-5
Revised Date:   REVISED BY:
"""
# ------------------- air flow imports ----------------- #
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'prep_comb_code'))

from distutils.util import execute
from http import client
from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.python_operator import PythonOperator
from airflow.operators.python import BranchPythonOperator
from airflow.operators.dummy import DummyOperator
from google.cloud import bigquery
from airflow.models import Variable
from google.cloud.exceptions import NotFound
#from airflow.contrib.operators.bigquery_operator import BigQueryOperator
from airflow.providers.google.cloud.operators.bigquery import BigQueryInsertJobOperator
from airflow.exceptions import AirflowFailException
#from airflow.models import taskinstance
from google.cloud import storage
import time
from datetime import datetime, timedelta
# ------------------ prep_comb imports --------------------------- #
import prep_wordCnt as pwc
import prep_baseWordFinder as pbw
import prep_merge_synonym_files as msf
import compositCombination as cc
import combPruning as cp
import compositWordReplace as cr
import des_synonym_replace as dsr
import prepItemAttrib as pia

# ------------ calling compositeWordPrg iteratively ------------------ #
def compositeWordFun(**kwarg):
    for r in range(2,6):
        cc.compositWordPrg(r,params=kwarg["params"])

# -------------------- Config variables ----------------- #
BQ_CONN_ID = os.environ['bq_conn_id']
INSTANCE = os.environ['instance']
envParamsDict = {"env": INSTANCE}
# --------------------- Define DAG ---------------------- #
defaultArg = {'owner': 'airflow', 'start_date': datetime(2025, 1, 15, 0, 0, 0)}

dag = DAG(
    'cic_comb_prep_DAG',
    default_args=defaultArg,
    description='This DAG creates clean dsc for comb',
    schedule_interval=None,
    template_searchpath=['/home/airflow/gcs/dags/'],
    catchup=False
)

# ----------------------TASK DEFINE------------------------ #

# ------------------ Create a DummyOperator task ---------- #
start_task = DummyOperator(task_id='start_task', dag=dag)
finish_task = DummyOperator(task_id='finish_task', dag=dag)

# ----------------- Create wordCnt task ------------------- #
wordCnt_task = PythonOperator(
     task_id = 'wordCnt_task',
     python_callable = pwc.wordCnt,
     provide_context = True,
     op_args = [],
     params = envParamsDict,
     dag = dag,
)
# ----------------- Create synonymFinder task ------------------- #
synonymFinder_task = PythonOperator(
     task_id = 'synonymFinder_task',
     python_callable =pbw.synonymFinderPrg,
     provide_context = True,
     op_args = [],
     params = envParamsDict,
     dag = dag,
)
# ----------------- Create mergeSynonym task ------------------- #
mergeSynonym_task = PythonOperator(
     task_id = 'mergeSynonym_task',
     python_callable =msf.merge_synonym_prg,
     provide_context = True,
     op_args = [],
     params = envParamsDict,
     dag = dag,
)
# ----------------- Create compositWrd task ------------------- #
compositWrd_task = PythonOperator(
     task_id = 'compositWrd_task',
     python_callable = compositeWordFun,
     provide_context = True,
     op_args = [],
     params = envParamsDict,
     dag = dag,
)
# ----------------- Create compositWrdPr task ------------------- #
compositWrdPr_task = PythonOperator(
     task_id = 'compositWrdPr_task',
     python_callable = cp.combPruningPrg,
     provide_context = True,
     op_args = [],
     params = envParamsDict,
     dag = dag,
)
# ----------------- Create compositWrdRep task ------------------- #
compositWrdRep_task = PythonOperator(
     task_id = 'compositWrdRep_task',
     python_callable = cr.compositWdRepPrg,
     provide_context = True,
     op_args = [],
     params = envParamsDict,
     dag = dag,
)
# ----------------- Create synonymWrdRep task ------------------- #
synonymWrdRep_task = PythonOperator(
     task_id = 'synonymWrdRep_task',
     python_callable = dsr.dscSynonymPrg,
     provide_context = True,
     op_args = [],
     params = envParamsDict,
     dag = dag,
)
# ----------------- Create prepItemIngDsc task ------------------- #
prepItemIngDsc_task = PythonOperator(
     task_id = 'prepItemIngDsc_task',
     python_callable = pia.prepItemAttribPrg,
     provide_context = True,
     op_args = [],
     params = envParamsDict,
     dag = dag,
)

# ------------ Define task dependencies -----------------------------#
start_task >> wordCnt_task >> synonymFinder_task >> mergeSynonym_task >> compositWrd_task >> compositWrdPr_task >>compositWrdRep_task >>synonymWrdRep_task >> prepItemIngDsc_task >> finish_task
# -------------------------- code flow ----------------------------------------- #
# step 1 cic_cmb_wordCnt.py
#pwc.wordCnt()

# step 2 prep_baseWordFinder.py
#pbw.synonymFinderPrg()

# step 3 prep_merge_synonym_files.py
#msf.merge_synonym_prg()

# step 4 compositCombination.py
#for r in range(2,6):
    #cc.compositWordPrg(r)

# step 5 combPruning.py
#cp.combPruningPrg()

# step 6 compositWordReplace.py
#cr.compositWdRepPrg()

# step 7 des_synonym_replace.py
#dsr.dscSynonymPrg()

# step 8 prepItemAttrib.py
#pia.prepItemAttribPrg()
