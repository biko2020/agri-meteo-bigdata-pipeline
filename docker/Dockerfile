FROM apache/spark:3.4.1

USER root


# Installer Python et pip
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Créer un lien symbolique pour python
RUN ln -s /usr/bin/python3 /usr/bin/python

# Copier et installer les dépendances
COPY requirements.txt /tmp/requirements.txt
RUN pip3 install --no-cache-dir -r /tmp/requirements.txt

WORKDIR /app

# Revenir à l'utilisateur spark
USER spark