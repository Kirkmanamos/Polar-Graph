push:
	git add .
	git commit -m "$(or $(m),Update project)"
	git push