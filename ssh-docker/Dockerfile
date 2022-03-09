FROM debian:stretch-slim

RUN apt-get update && apt-get install -y --no-install-recommends openssh-server

ARG USER=user
ENV USER $USER
RUN useradd --shell /bin/bash --create-home $USER
RUN echo "$USER:secret" | chpasswd
RUN echo "root:mypassword" | chpasswd

RUN ssh-keygen -t rsa -f /etc/ssh/ca_key -P "" -C ca_key
RUN chmod 644 /etc/ssh/ca_key.pub
RUN echo TrustedUserCAKeys /etc/ssh/ca_key.pub >> /etc/ssh/sshd_config

RUN ssh-keygen -f /home/user/user_key
RUN ssh-keygen -s /etc/ssh/ca_key -I viper -n user /home/user/user_key.pub

RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd
RUN mkdir /var/run/sshd
EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]
