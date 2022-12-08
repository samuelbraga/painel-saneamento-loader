docker-compose run --rm generator python run.py
# files=$(ls artifacts)
# for file in $files
# do
#     docker-compose run --rm pg_client -f /opt/${file} -q 
# done