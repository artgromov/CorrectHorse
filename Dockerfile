FROM python
COPY . /src
WORKDIR "/src"
CMD ["python", "correcthorse.py"]

#
# build: 'docker build -t <container_name> <path_to_dir_with_dockerfile>'
# usage: 'docker run -t -i --rm <container_name>'
#
