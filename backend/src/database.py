connectionstring = "postgres://uofthax8hack@free-tier.gcp-us-central1.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full&sslrootcert=<your_certs_directory>/cc-ca.crt&options=--cluster=mature-otter-855"

username = "uofthax8hack"

host = "free-tier.gcp-us-central1.cockroachlabs.cloud"

port = 26257

database_co = "mature-otter-855.defaultdb"

password = "UofTHacks2021"

import psycopg2

conn = psycopg2.connect(
    database=database_co,
    user='username',
    password=password,
    sslmode='verify-full',
    sslrootcert='cc-ca.crt',
    port=26257,
    host='free-tier.gcp-us-central1.cockroachlabs.cloud',
    options="--cluster=mature-otter-855"
)



