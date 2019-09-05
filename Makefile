docker-image:
	@docker build -t lambda-builder .

zip:
	@docker run -i -t -v $(CURDIR):/code lambda-builder ./build-zip.sh
