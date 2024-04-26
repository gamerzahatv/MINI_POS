
# Tkinter POS with Devcontainer + Docker 
Why use devcontainer? Because docker can't run a GUI, but doing so is difficult. So I decided to implement devcontainer to make the project easier.




## Acknowledgements
 - [Docker](https://docs.docker.com/)
 - [Docker compose](https://docs.docker.com/compose/)
 - [Devcontainer](https://code.visualstudio.com/docs/devcontainers/containers)
 - [Tkinter](https://docs.python.org/3.8/library/tkinter.html)
 - [Mariadb](https://mariadb.com/kb/en/mariadb-1040-release-notes/)

 
 






## Run with Devcontainer

1.install Dev Containers Extension in vscode

2.use Ctrl + Shift + P in vscode  select 
Dev container : rebuild and reopen in container 

When connecting to devcontainer use this command

```bash
pip install -r requirements.txt
```
and run program

```bash
python main.py
``` 


## Database info

host: localhost

user: root  

password: root

database: app

port: 3306




## Screenshots

Home page

![App Screenshot](https://github.com/gamerzahatv/MINI_POS_TKINER/blob/main/Ex%20photo/home.PNG)

Stockpage

![App Screenshot](https://github.com/gamerzahatv/MINI_POS_TKINER/blob/main/Ex%20photo/stockpage.PNG)

Userpage

![App Screenshot](https://github.com/gamerzahatv/MINI_POS_TKINER/blob/main/Ex%20photo/UserPage.PNG)

Orderpage

![App Screenshot](https://github.com/gamerzahatv/MINI_POS_TKINER/blob/main/Ex%20photo/Orderpage.PNG)

Billpage

![App Screenshot](https://github.com/gamerzahatv/MINI_POS_TKINER/blob/main/Ex%20photo/Billpage.PNG)
