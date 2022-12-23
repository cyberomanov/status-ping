# ping

this system will alert you with telegram about offline servers.

## contents
1. [screenshots](https://github.com/cyberomanov/status-ping#screenshots)
2. [installation](https://github.com/cyberomanov/status-ping#installation)
3. [update](https://github.com/cyberomanov/status-ping#update)
4. [donations](https://github.com/cyberomanov/status-ping#donations)

### screenshots

<p align="center">
<img width="600" alt="image" src="https://user-images.githubusercontent.com/41644451/208536945-12e91897-1cd7-4678-9636-8c7a2e95a901.png">
<br> <br>
<img width="600" alt="image" src="https://user-images.githubusercontent.com/41644451/208537089-63e58309-510a-4909-ab7b-8455d70168db.png">
</p>

### installation

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
### update

1. attach the tmux session and kill the process with `ctrl + c`:
```
tmux attach -t ping
```
2. backup your config
```
cp ~/ping/config.yaml ~/config_temp.yaml
```
3. pull changes from the repository:
```
cd ~/ping/ && \
git fetch && \
git reset --hard && \
git pull
```
4. check the latest tag and checkout it:
```
git checkout
```
5. print a new default config:
```
cat ~/ping/config.yaml
```
6. restore your previous config **ONLY** if there is no breaking changes, else edit the new file:
```
mv ~/config_temp.yaml ~/ping/config.yaml
OR
nano ~/ping/config.yaml
```
7. start ping.py:
```
python3 ping.py
```

### donations

```
SOL >>> 8UM1sHHShTgNa4vjQV6v1SEvi3BwDn4wG1pRRZnbFvRY
BTC >>> bc1qqpllwvwj3vrp6p5qq5t698j6fx2zaxlucrchru
DOT >>> 15rCbyqHZnS6oWon2ntp1JGPBZsTxt66EThMDMxdPxs67Y2K
ATOM >> cosmos1h359yz2xyy323ezd4dryxldkv98f2sc0cccjjw
TRC >>> TMZczdd7LZJSCp83WrLn245t6rSeEYeBTh
ETH >>>  0x81fb0dF0F16ABC3BE334aB619154C9b3736aB9c1
```
