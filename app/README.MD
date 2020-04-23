source env/bin/activate

test on localhost first! then you can 
docker build -f Dockerfile -t tagoose:latest .
docker run -p 5001:5000 tagoose

