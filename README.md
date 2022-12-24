# ping

this system will alert you with telegram about offline servers.

## contents
1. [screenshots](https://github.com/cyberomanov/status-ping#screenshots)
2. [installation](https://github.com/cyberomanov/status-ping#installation)
3. [update](https://github.com/cyberomanov/status-ping#update)
4. [donations](https://github.com/cyberomanov/status-ping#donations)

### screenshots


<p align="center">
<img width="1000" alt="image" src="https://user-images.githubusercontent.com/41644451/209399231-e27f2a85-1f05-4583-bcd9-227e2fe800c0.png">
<br> <br>
<img width="600" alt="image" src="https://user-images.githubusercontent.com/41644451/209399270-1630eda4-deee-419a-9843-fa049a817e9e.png">
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
7. Edit `config.yaml` (recommend to set 1 offline/non-pingable server to check your alarms via telegram):
```
nano ~/ping/config.yaml
```
8. Open new tmux session:
```
tmux new -s ping  # to init a session
tmux attach -t ping  # to re-open the session
```
9. Run the `ping.py` to check you config settings:
```
python3 ping.py
```
10. If all seems okay, then edit your crontab with `crontab -e`:
```
# ping
*/5 * * * * /usr/bin/python3 /root/ping/ping.py
```
> check your logs in 5-10-15 minutes here: `~/ping/log/ping.log`
---------
### update

1. attach the tmux session and kill the process with `ctrl + c`:
```
tmux attach -t ping
```
2. backup your config:
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
4. print a new default config:
```
cat ~/ping/config.yaml
```
5. restore your previous config, **ONLY** if there is no breaking changes, else edit the new file:
```
mv ~/config_temp.yaml ~/ping/config.yaml
OR
nano ~/ping/config.yaml
```
6. Install requirements:
```
pip3 install -r ~/ping/requirements.txt
```
7. Run the `ping.py` to check you config settings:
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
