from diagrams import Diagram
from diagrams.azure.storage import DataLakeStorage
from diagrams.azure.analytics import Databricks
from diagrams.azure.storage import BlobStorage
from diagrams.azure.identity import AppRegistrations
from diagrams.saas.analytics import Snowflake
from diagrams.azure.compute import BatchAccounts

with Diagram("Azure diagram"):
    batch = BatchAccounts("batch for compute")
    adls = DataLakeStorage("new folder \nRaw/Level2")
    appreg = AppRegistrations("create new app reg for authentication")
    dbx = Databricks("databricks to transform raw")
    blob = BlobStorage("blob storage to store python modules")
    sf = Snowflake("snowflake as connector to Tableau")
    adls >> dbx >> sf
    blob >> batch
    appreg >> adls
