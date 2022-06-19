FROM python:3.9-slim AS base-image

# Setup.
RUN mkdir /opt/thepeak-spotify
WORKDIR /opt/thepeak-spotify
RUN cp /usr/share/zoneinfo/America/Vancouver /etc/localtime
RUN echo "America/Vancouver" > /etc/timezone

# Install dependencies.
COPY ./requirements.txt /opt/thepeak-spotify
RUN pip --disable-pip-version-check install -r requirements.txt
COPY ./tests /opt/thepeak-spotify

# Env.
ENV SPOTIFY_CLIENT_ID=${SPOTIFY_CLIENT_ID}
ENV SPOTIFY_CLIENT_SECRET=${SPOTIFY_CLIENT_SECRET}
ENV SPOTIFY_REDIRECT_URI=${SPOTIFY_REDIRECT_URI}
ENV SPOTIFY_PLAYLIST_ID=${SPOTIFY_PLAYLIST_ID}

# Entrypoint.
CMD ["python", "spotify_playlist.py"]
