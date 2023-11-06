<div align="center">
  
# ![icon of a cart](./cart.ico) AuctionBot

<br>

![GitHub](https://img.shields.io/github/license/wojtazk/allegro-auction-bot)
![GitHub top language](https://img.shields.io/github/languages/top/wojtazk/allegro-auction-bot?color=lightblue)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/wojtazk/allegro-auction-bot) 

![GitHub forks](https://img.shields.io/github/forks/wojtazk/allegro-auction-bot?logoColor=blue&style=social)
![GitHub Repo stars](https://img.shields.io/github/stars/wojtazk/allegro-auction-bot?style=social)

### Bot that wins auctions for you!!!

![image](https://github.com/wojtazk/allegro-auction-bot/assets/48928433/484e7a58-c176-4434-9e2b-2dd962696755)
![image](https://github.com/wojtazk/allegro-auction-bot/assets/48928433/77dea07b-b5b3-4551-9c96-72f0e938fefc)

</div>
<br>

> [!NOTE]
> It only works with [allegro lokalnie](https://allegrolokalnie.pl/) auctions
<br>

## How to run
> [!WARNING]
> You are using this software at your own risk

<br>

> [!IMPORTANT]
> You need to have [Firefox](https://www.mozilla.org/firefox/new/) web browser installed

### Windows

- Download AuctionBot_[version].exe from [releases](https://github.com/wojtazk/allegro-auction-bot/releases)
- run downloaded file
- click `More info`
  
  ![image](https://github.com/wojtazk/allegro-auction-bot/assets/48928433/8e09102e-a76f-4882-9776-599d6c2edbe4)
  
- then click `Run anyway`

    ![image](https://github.com/wojtazk/allegro-auction-bot/assets/48928433/dcf817d1-bc32-4390-8eef-3f5bc1d3fe8b)
 
<br>

### Linux
- Download AuctionBot_[version].run from [releases](https://github.com/wojtazk/allegro-auction-bot/releases)
- go to the directory where you downloaded the file
  ```shell
  cd [directory]
  ```
- run the executable
  ```shell
  ./AuctionBot_[version].run
  ```

![image](https://github.com/wojtazk/allegro-auction-bot/assets/48928433/0e9cb4ea-1427-4481-b18a-09f118612a04)

<br>

## Executable files
Download [here](https://github.com/wojtazk/allegro-auction-bot/releases)


### Generated with pyinstaller
> [!NOTE]
> AuctionBot icon -> link to the [img](https://iconduck.com/icons/249696/cart) (CC0)

<br>

Windows .exe file:  
```
pyinstaller --onefile --icon=cart.ico main.py --name AuctionBot_ver.exe
```
<br>

Linux .run file:  
```
pyinstaller --icon=cart.ico --onefile main.py --name AuctionBot_ver.run
```

<br>

## Project dependencies
`table generated with:` [pip-licenses](https://github.com/raimon49/pip-licenses)


```
pipenv run pip-licenses --from=classifier --with-urls --with-system --format=markdown
```

| Name                      | Version     | License                                                        | URL                                                      |
|---------------------------|-------------|----------------------------------------------------------------|----------------------------------------------------------|
| PySocks                   | 1.7.1       | UNKNOWN                                                        | https://github.com/Anorov/PySocks                        |
| altgraph                  | 0.17.4      | MIT License                                                    | https://altgraph.readthedocs.io                          |
| attrs                     | 23.1.0      | MIT License                                                    | https://www.attrs.org/en/stable/changelog.html           |
| certifi                   | 2023.7.22   | Mozilla Public License 2.0 (MPL 2.0)                           | https://github.com/certifi/python-certifi                |
| cffi                      | 1.16.0      | MIT License                                                    | http://cffi.readthedocs.org                              |
| h11                       | 0.14.0      | MIT License                                                    | https://github.com/python-hyper/h11                      |
| idna                      | 3.4         | BSD License                                                    | https://github.com/kjd/idna                              |
| outcome                   | 1.3.0.post0 | Apache Software License; MIT License                           | https://github.com/python-trio/outcome                   |
| packaging                 | 23.2        | Apache Software License; BSD License                           | https://github.com/pypa/packaging                        |
| pefile                    | 2023.2.7    | UNKNOWN                                                        | https://github.com/erocarrera/pefile                     |
| prettytable               | 3.9.0       | BSD License                                                    | https://github.com/jazzband/prettytable                  |
| pycparser                 | 2.21        | BSD License                                                    | https://github.com/eliben/pycparser                      |
| pyinstaller               | 6.1.0       | GNU General Public License v2 (GPLv2)                          | https://www.pyinstaller.org/                             |
| pyinstaller-hooks-contrib | 2023.10     | Apache Software License; GNU General Public License v2 (GPLv2) | https://github.com/pyinstaller/pyinstaller-hooks-contrib |
| pywin32-ctypes            | 0.2.2       | UNKNOWN                                                        | https://github.com/enthought/pywin32-ctypes              |
| selenium                  | 4.14.0      | Apache Software License                                        | https://www.selenium.dev                                 |
| setuptools                | 68.2.2      | MIT License                                                    | https://github.com/pypa/setuptools                       |
| sniffio                   | 1.3.0       | Apache Software License; MIT License                           | https://github.com/python-trio/sniffio                   |
| sortedcontainers          | 2.4.0       | Apache Software License                                        | http://www.grantjenks.com/docs/sortedcontainers/         |
| trio                      | 0.23.1      | Apache Software License; MIT License                           | https://github.com/python-trio/trio                      |
| trio-websocket            | 0.11.1      | MIT License                                                    | https://github.com/python-trio/trio-websocket            |
| urllib3                   | 2.0.7       | MIT License                                                    | https://github.com/urllib3/urllib3/blob/main/CHANGES.rst |
| wcwidth                   | 0.2.9       | MIT License                                                    | https://github.com/jquast/wcwidth                        |
| wsproto                   | 1.2.0       | MIT License                                                    | https://github.com/python-hyper/wsproto/                 |
