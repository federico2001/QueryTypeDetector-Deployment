RUN IN PRODUCTION 

docker build --no-cache -t get_relevant_categories .

docker run -p 5000:5000 get_relevant_categories


