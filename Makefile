
image:
	@docker build -t notapigateway -f Dockerfile.dev .

.PHONY: image
