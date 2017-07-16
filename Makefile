compile:
		python compile.py

deploy:
		rsync -crvz --exclude='.git' --delete-after --delete-excluded index.html adam@releasechecklist.com:/home/adam/projects/releasechecklist