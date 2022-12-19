# ping

This system will alert you with telegram about offline servers.

## installation

1. Create telegram bot via `@BotFather`, customize it and `get bot API token` ([how_to](https://www.siteguarding.com/en/how-to-get-telegram-bot-api-token)).
2. Create at least 1 group: `alarm`. Customize it, add your bot into this chat and `get chat ID` ([how_to](https://stackoverflow.com/questions/32423837/telegram-bot-how-to-get-a-group-chat-id)).
3. Connect to your server where you plan to install ping-system.
4. Install `python3.10`:
```
# one-line-command
sudo apt-get update && \
sudo apt-get upgrade -y && \
sudo apt install software-properties-common tmux curl git -y && \
sudo add-apt-repository ppa:deadsnakes/ppa && \
sudo apt-get install python3.10 python3-pip -y && \
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 1; \
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.10 2; \
sudo update-alternatives --config python3 && \
sudo apt-get install python3-distutils && \
sudo apt-get install python3-apt && \
sudo apt install python3.10-distutils -y && \
curl -sS https://bootstrap.pypa.io/get-pip.py | python3.10 && \
sudo apt-get install python3.10-dev -y && \
pip3 install --ignore-installed PyYAML && \
python3 -V

>>> Python 3.10.9
```
5. Clone this repository:
```
cd ~/ && \
git clone https://github.com/cyberomanov/status-ping.git ping && \
cd ~/ping/
```
6. Install requirements:
```
pip3 install -r ~/ping/requirements.txt
```
7. Edit config.py (recommend to set 1 offline/non-pingable server to check your alarms via telegram):
```
nano ~/ping/config.py
```
8. Open new tmux session:
```
tmux new -s ping  # to init a session
tmux attach -t ping  # to re-open the session
```
9. Run the ping.py:
```
python3 ping.py

>>> 16:34:15 | INFO | [ax101] with [181.xx.xx.78] is online.
>>> 16:34:15 | INFO | [ax69] with [81.xx.xx.142] is online.
>>> 16:34:15 | INFO | [mevspace] with [89.xx.xx.146] is online.
>>> 16:35:05 | WARNING | [edgevana] with [12.xx.xx.114] is offline.
>>> 16:36:05 | INFO | [ax101] with [181.xx.xx.78] is online.
>>> 16:36:06 | INFO | [ax69] with [81.xx.xx.142] is online.
>>> 16:36:06 | INFO | [mevspace] with [89.xx.xx.146] is online.
>>> 16:36:56 | WARNING | [edgevana] with [12.xx.xx.114] is offline.
```

---------
## update

```
tmux attach -t ping  # ctrl + c to stop the process

cp ~/ping/config.py ~/config_temp.py  # backup your config

# hard update
cd ~/ping/ && \
git fetch && \
git reset --hard && \
git pull

git checkout v1.1  # check the latest release

cat ~/ping/config.py  # read new default config

mv ~/config_temp.py ~/ping/config.py  # restore your previous config ONLY if there is no breaking changes

python3 ping.py  # start ping
```

--------
## screenshots


<p align="center">
<img width="600" alt="image" src="https://user-images.githubusercontent.com/41644451/208536945-12e91897-1cd7-4678-9636-8c7a2e95a901.png">
<img width="600" alt="image" src="https://user-images.githubusercontent.com/41644451/208537089-63e58309-510a-4909-ab7b-8455d70168db.png">
</p>
