# PING

this system will alert you with telegram about offline servers.<br>
[donations are welcome](https://cyberomanov.tech/WTF_donate), if you find this tool helpful.

## Contents
1. [Screenshots](https://github.com/cyberomanov/status-ping#screenshots)
2. [Installation](https://github.com/cyberomanov/status-ping#installation)
3. [Update](https://github.com/cyberomanov/status-ping#update)

### Screenshots


<p align="center">
<img width="1000" alt="image" src="./assets/terminal.png">
<br> <br>
<img width="600" alt="image" src="./assets/telegram.png">
</p>

### Installation

1. Create telegram bot via `@BotFather`, customize it and get `bot_API_token` ([how_to](https://www.siteguarding.com/en/how-to-get-telegram-bot-api-token)).
2. Create at least 1 chat: `alarm`. Customize it, add your bot into this chat and get `chat_ID` ([how_to](https://stackoverflow.com/questions/32423837/telegram-bot-how-to-get-a-group-chat-id)).
3. Connect to your server where you plan to install ping-system.
4. Install `python3.10` or newer:
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
7. Edit `config.yaml`:
> recommend to set 1 offline/non-pingable server to check your alarms via telegram.
```
nano ~/ping/config.yaml
```
8. Run the `ping.py` to check you config settings:
```
python3 ping.py
```
9. If all seems okay, then edit your crontab with `crontab -e`:
> ping 10 servers takes about 2 minutes with 1 cpu x 1 ram vps.<br>
> so you have to edit your crontab rules with this knowledge.
```
# ping
*/5 * * * * cd /root/ping/ && /usr/bin/python3 ping.py
```
> check your logs in 5-10-15 minutes here: `~/ping/log/ping.log`
---------
### Update

1. backup your config:
```
cp ~/ping/config.yaml ~/config_temp.yaml
```
2. pull changes from the repository:
```
cd ~/ping/ && \
git fetch && \
git reset --hard && \
git pull
```
3. print a new default config:
```
cat ~/ping/config.yaml
```
4. restore your previous config, **ONLY** if there is no breaking changes, else edit the new file:
```
nano ~/ping/config.yaml

OR

mv ~/config_temp.yaml ~/ping/config.yaml
```
5. Install requirements:
```
pip3 install -r ~/ping/requirements.txt
```
6. Run the `ping.py` to check you config settings:
```
python3 ping.py
```
