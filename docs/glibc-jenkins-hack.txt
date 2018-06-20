# jenkins-docker-sidecar-test


Insane method to get glibc in jenkins image for docker-compose to work:
TODO: Clean this up and build a new jenkins dockerfile


docker run -u root --rm -d -p 8080:8080 -p 50000:50000 -v /home/theo/jenkins/:/var/jenkins_home -v /var/run/docker.sock:/var/run/docker.sock jenkinsci/blueocean



export GLIBC="2.27-r0"
export DOCKERBINS_SHA="1270dce1bd7e1838d62ae21d2505d87f16efc1d9074645571daaefdfd0c14054"

apk update && apk add --no-cache openssl ca-certificates curl libgcc && curl -fsSL -o /etc/apk/keys/sgerrand.rsa.pub https://raw.githubusercontent.com/sgerrand/alpine-pkg-glibc/master/sgerrand.rsa.pub && curl -fsSL -o glibc-$GLIBC.apk https://github.com/sgerrand/alpine-pkg-glibc/releases/download/$GLIBC/glibc-$GLIBC.apk && apk add --no-cache glibc-$GLIBC.apk && ln -s /lib/libz.so.1 /usr/glibc-compat/lib/ && ln -s /lib/libc.musl-x86_64.so.1 /usr/glibc-compat/lib && ln -s /usr/lib/libgcc_s.so.1 /usr/glibc-compat/lib && curl -fsSL -o dockerbins.tgz "https://download.docker.com/linux/static/stable/x86_64/docker-17.12.1-ce.tgz" && echo "${DOCKERBINS_SHA}  dockerbins.tgz" | sha256sum -c - && tar xvf dockerbins.tgz docker/docker --strip-components 1 && mv docker /usr/local/bin/docker && chmod +x /usr/local/bin/docker && rm dockerbins.tgz /etc/apk/keys/sgerrand.rsa.pub glibc-$GLIBC.apk && apk del curl

  31  apk add curl
   32  curl -L https://github.com/docker/compose/releases/download/1.21.2/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose
   33  chmod +x /usr/local/bin/docker-compose 
   34  /usr/local/bin/docker-compose 

