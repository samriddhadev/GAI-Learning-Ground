
# Running OpenSearch in Docker Container
https://opensearch.org/docs/latest/install-and-configure/install-opensearch/docker/

docker build --tag=opensearch-custom-plugin .

## Create Certificates

openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout root-ca-key.pem -out root-ca.pem