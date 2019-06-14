build:
	docker build -t playground/movies --force-rm=true .

run:
	docker run -it -p 8888:80 playground/movies /bin/bash