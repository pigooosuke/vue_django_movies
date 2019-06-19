build:
	docker build -t playground/movies --force-rm=true .

build-client:
	cd frontend && yarn run build && cd ..

collectstatic: build-client
	rm -f backend/templates/*.html
	rm -rf backend/static/css
	rm -rf backend/static/img
	rm -rf backend/static/js
	rm -rf backend/favicon.ico
	cp -r frontend/dist/static/* backend/static/
	cp frontend/dist/*.html backend/templates/

build-docker-image: collectstatic
	docker build -t playground/movies --force-rm=true .

build-docker-image-alone:
	docker build -t playground/movies --force-rm=true .

build-docker-image-clean: collectstatic
	docker build --no-cache -t playground/movies --force-rm=true .

clean:
	docker image rm playground/movies

data_setup:
	cd backend && \
	python3 manage.py load_dataset && \
	cd ..

run:
	docker run -it -p 8888:80 playground/movies
